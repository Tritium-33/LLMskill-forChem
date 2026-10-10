#!/usr/bin/env python3
"""Read-only checks of exported observations; not a host adapter or quality judge."""
import argparse
import json
from pathlib import Path
import sys


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def inspect(data, instruction=None, required_skills=(), preflight=False):
    if not isinstance(data, dict) or data.get('schema_version') != 1:
        raise ValueError('Expected schema_version 1')
    context = data.get('initial_context', {})
    if not isinstance(context, dict) or type(context.get('complete')) is not bool or not nonempty(context.get('source')):
        raise ValueError('initial_context requires complete (boolean) and source locator')
    messages = context.get('messages')
    if not isinstance(messages, list) or any(
        not isinstance(m, dict) or m.get('role') not in {'system', 'developer', 'user', 'assistant', 'tool'}
        or not isinstance(m.get('content'), str) for m in messages
    ):
        raise ValueError('messages must contain role and exported text content')
    checks = []

    def add(name, state, detail, evidence):
        checks.append(dict(check=name, state=state, detail=detail, evidence=evidence))

    if instruction is not None:
        if not nonempty(instruction):
            raise ValueError('Expected instruction cannot be empty')
        found = any(instruction in m['content'] for m in messages
                    if m['role'] in {'system', 'developer', 'user'})
        add('instruction_text', 'observed' if found else ('missing' if context['complete'] else 'unknown'),
            'Exact text presence only; not proof of authority, compliance, or router invocation.', context['source'])
    if not preflight:
        if type(data.get('events_complete')) is not bool or not isinstance(data.get('events'), list):
            raise ValueError('Post-run mode requires events_complete and events')
        events = data['events']
        last = -1
        loaded = set()
        active = {}
        started = set()
        final = None
        kinds = {'skill_load', 'job_start', 'job_end', 'final_answer'}
        for event in events:
            if not isinstance(event, dict):
                raise ValueError('Invalid event')
            seq = event.get('seq')
            if type(seq) is not int or seq <= last or not nonempty(event.get('source')):
                raise ValueError('Events require strictly increasing seq and source locator')
            last = seq
            kind = event.get('kind')
            if kind not in kinds or not nonempty(event.get('session')):
                raise ValueError('Unknown event kind or missing session')
            if kind == 'skill_load':
                if event.get('status') not in {'success', 'failure'} or not nonempty(event.get('skill')):
                    raise ValueError('skill_load requires skill and success/failure status')
                if event['session'] == 'main' and event['status'] == 'success' and final is None:
                    loaded.add(event['skill'])
            elif kind in {'job_start', 'job_end'}:
                job = event.get('job')
                if not nonempty(job):
                    raise ValueError('Job events require job ID')
                if kind == 'job_start':
                    if final is not None:
                        raise ValueError('Job starts after main final answer; split or repair the record')
                    if job in started:
                        raise ValueError('Duplicate job ID; use a new ID for retries')
                    started.add(job)
                    active[job] = event['source']
                else:
                    if event.get('status') not in {'completed', 'failed', 'cancelled'}:
                        raise ValueError('job_end requires an observed terminal state')
                    if job not in active and data['events_complete']:
                        raise ValueError('job_end has no preceding start in complete record')
                    active.pop(job, None)
            elif event['session'] == 'main':
                if final is not None:
                    raise ValueError('One final answer per record; split separate turns')
                final = seq
                if active:
                    add('delegation_closed_at_final', 'missing',
                        'No terminal event before final for: ' + ', '.join(sorted(active)),
                        [event['source'], *active.values()])
                else:
                    add('delegation_closed_at_final', 'observed' if data['events_complete'] else 'unknown',
                        'Terminal states do not prove returned content was collected or verified.', event['source'])
        for name in required_skills:
            add('main_skill:' + name, 'observed' if name in loaded else
                ('missing' if data['events_complete'] else 'unknown'),
                'Successful main-session load before final only; worker loads and failures do not qualify.',
                [e['source'] for e in events if e['kind'] == 'skill_load' and e['skill'] == name])
        if final is None:
            add('final_answer', 'missing' if data['events_complete'] else 'unknown',
                'No main final-answer event.', [])
    states = {c['state'] for c in checks}
    outcome = 'fail' if 'missing' in states else 'inconclusive' if 'unknown' in states or not checks else 'pass'
    return dict(schema_version=1, outcome=outcome, checks=checks,
                limitation='Checks exported observations only. Completeness and source authenticity require independent audit; no scientific quality or cost attribution.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('record', type=Path)
    parser.add_argument('--instruction-file', type=Path, help='Exact expected text, UTF-8; trailing newline removed')
    parser.add_argument('--required-skill', action='append', default=[])
    parser.add_argument('--preflight', action='store_true', help='Check actual initial context only')
    args = parser.parse_args()
    try:
        if args.preflight and (not args.instruction_file or args.required_skill):
            raise ValueError('Preflight needs --instruction-file and does not check skill execution')
        expected = args.instruction_file.read_text(encoding='utf-8').rstrip('\r\n') if args.instruction_file else None
        result = inspect(json.loads(args.record.read_text(encoding='utf-8')), expected,
                         args.required_skill, args.preflight)
    except (ValueError, OSError, TypeError, KeyError) as exc:
        print(json.dumps({'outcome': 'invalid', 'error': str(exc)}, ensure_ascii=True))
        return 2
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return {'pass': 0, 'fail': 1, 'inconclusive': 2}[result['outcome']]


if __name__ == '__main__':
    sys.exit(main())

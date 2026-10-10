"""Synthetic event controls, independent of a particular host/experimental result."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('run_evidence', ROOT / 'tools/maintenance/check_run_evidence.py')
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)


def record():
    return {'schema_version': 1, 'initial_context': {
        'complete': True, 'source': 'request.json#/messages',
        'messages': [{'role': 'system', 'content': 'Use the router before selecting skills.'}]},
        'events_complete': True, 'events': [
            {'seq': 1, 'session': 'main', 'kind': 'skill_load', 'skill': 'scientific-skill-router', 'status': 'success', 'source': 'events:1'},
            {'seq': 2, 'session': 'main', 'kind': 'job_start', 'job': 'j1', 'source': 'events:2'},
            {'seq': 3, 'session': 'worker', 'kind': 'job_end', 'job': 'j1', 'status': 'completed', 'source': 'events:3'},
            {'seq': 4, 'session': 'main', 'kind': 'final_answer', 'source': 'events:4'}]}


class RunEvidenceTests(unittest.TestCase):
    def test_closed_observed_run(self):
        data = record()
        before = copy.deepcopy(data)
        result = check.inspect(data, 'Use the router', ['scientific-skill-router'])
        self.assertEqual(result['outcome'], 'pass')
        self.assertEqual(data, before)

    def test_disk_profile_does_not_prove_injection(self):
        data = record()
        data['profile_instruction'] = 'Use the router'
        data['initial_context']['messages'] = []
        self.assertEqual(check.inspect(data, 'Use the router', preflight=True)['outcome'], 'fail')
        data['initial_context']['complete'] = False
        self.assertEqual(check.inspect(data, 'Use the router', preflight=True)['outcome'], 'inconclusive')

    def test_assistant_claim_does_not_prove_initial_instruction(self):
        data = record()
        data['initial_context']['messages'][0]['role'] = 'assistant'
        self.assertEqual(check.inspect(data, 'Use the router', preflight=True)['outcome'], 'fail')

    def test_worker_or_failed_load_does_not_prove_main_load(self):
        for field, value in [('session', 'worker'), ('status', 'failure')]:
            data = record()
            data['events'][0][field] = value
            self.assertEqual(check.inspect(data, required_skills=['scientific-skill-router'])['outcome'], 'fail')

    def test_unclosed_child_and_late_completion_fail(self):
        data = record()
        end = data['events'].pop(2)
        self.assertEqual(check.inspect(data)['outcome'], 'fail')
        end['seq'] = 5
        data['events'].append(end)
        self.assertEqual(check.inspect(data)['outcome'], 'fail')

    def test_failed_or_cancelled_child_is_closed_not_scientifically_successful(self):
        for status in ['failed', 'cancelled']:
            data = record()
            data['events'][2]['status'] = status
            result = check.inspect(data)
            self.assertEqual(result['outcome'], 'pass')
            self.assertIn('do not prove', result['checks'][0]['detail'])

    def test_incomplete_capture_cannot_prove_no_pending_children(self):
        data = record()
        data['events_complete'] = False
        self.assertEqual(check.inspect(data)['outcome'], 'inconclusive')

    def test_no_final_not_a_completed_run(self):
        data = record()
        data['events'].pop()
        self.assertEqual(check.inspect(data)['outcome'], 'fail')

    def test_malformed_order_or_completeness_rejected(self):
        data = record()
        data['events'][1]['seq'] = 0
        with self.assertRaises(ValueError):
            check.inspect(data)
        data = record()
        data['events_complete'] = 'true'
        with self.assertRaises(ValueError):
            check.inspect(data)

    def test_cli_utf8_read_only_and_exit_status(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / '观察.json'
            path.write_text(json.dumps(record(), ensure_ascii=False), encoding='utf-8')
            before = path.read_bytes()
            proc = subprocess.run([sys.executable, '-X', 'warn_default_encoding', '-W', 'error::EncodingWarning',
                                   str(ROOT / 'tools/maintenance/check_run_evidence.py'), str(path),
                                   '--required-skill', 'missing-skill'],
                                  capture_output=True, text=True, encoding='utf-8', timeout=10)
            self.assertEqual(proc.returncode, 1, proc.stderr)
            self.assertEqual(json.loads(proc.stdout)['outcome'], 'fail')
            self.assertEqual(path.read_bytes(), before)

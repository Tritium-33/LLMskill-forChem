#!/usr/bin/env python3
"""Validate capability/route/case references without invoking scientific tools."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def inside(base, relative):
    path = (base / relative).resolve()
    if not path.is_relative_to(base.resolve()) or not path.is_file():
        raise ValueError(f'Missing or escaping reference: {relative}')
    return path


def unique(rows, key):
    values = [row[key] for row in rows]
    if len(values) != len(set(values)):
        raise ValueError(f'Duplicate {key}')
    return set(values)


def validate(root=ROOT):
    rows = read(root / 'catalog.json')['skills']
    names = unique(rows, 'name')
    tasks = set()
    for row in rows:
        cap = row.get('capability')
        if cap is None:
            continue
        for key in ('tasks', 'inputs', 'outputs', 'requires'):
            if not isinstance(cap.get(key), list) or not cap[key] or not all(isinstance(v, str) and v.strip() for v in cap[key]):
                raise ValueError(f'{row["name"]}: missing capability {key}')
        tasks.update(cap['tasks'])
        relations = cap['relations']
        if set(relations) != {'feeds_into', 'alternatives', 'delegates_to'}:
            raise ValueError('Unknown/missing relation type')
        for key in ('feeds_into', 'alternatives'):
            for target in relations[key]:
                if target not in names or target == row['name']:
                    raise ValueError(f'Invalid skill relation: {target}')
        for target in relations['delegates_to']:
            inside(root / 'skills', target + '/SKILL.md')
    refs = root / 'skills/scientific-skill-router/references'
    routes = read(refs / 'workflows.json')['workflows']
    route_ids = unique(routes, 'id')
    cases = read(root / 'examples/cases.json')['cases']
    case_ids = unique(cases, 'id')
    for route in routes:
        inside(refs, route['reference'])
        if not set(route['skills']) <= names or not set(route['capabilities']) <= tasks:
            raise ValueError(f'Unknown skill/capability in {route["id"]}')
        provided = {t for r in rows if r['name'] in route['skills']
                    for t in r.get('capability', {}).get('tasks', [])}
        if not set(route['capabilities']) <= provided:
            raise ValueError(f'Route capabilities lack a provider: {route["id"]}')
        if not route['handoff'] or not route['stop_conditions']:
            raise ValueError('Route must specify handoff and stop conditions')
        if not set(route['cases']) <= case_ids:
            raise ValueError('Unknown case in route')
    by_route = {r['id']: r for r in routes}
    for case in cases:
        if case['workflow'] not in route_ids or case['id'] not in by_route[case['workflow']]['cases']:
            raise ValueError('Unlinked case')
        for path in case['inputs']:
            inside(root / 'examples', path)
        if not case['expected'] or not case['must_not'] or not case['prompt']:
            raise ValueError('Case lacks acceptance criteria')
        if not set(case['allowed_skills']) <= names:
            raise ValueError('Case names unknown skills')
    for route in routes:
        if any(c['workflow'] != route['id'] for c in cases if c['id'] in route['cases']):
            raise ValueError('Case linked to wrong route')
    return {'skills': len(rows), 'capabilities': sum('capability' in r for r in rows),
            'workflows': len(routes), 'cases': len(cases)}


if __name__ == '__main__':
    print(json.dumps(validate(), ensure_ascii=False))

#!/usr/bin/env python3
"""Read-only inventory of packaged Python imports and upstream coupling.

This is a static inventory, not a dependency resolver or runtime readiness check.
Imports are never executed. Dynamic imports and prose-only requirements may be
missed; standard-library/local/third-party import names are not package pins.
"""
import argparse
import ast
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def inventory(root=ROOT):
    rows = json.loads((root / 'catalog.json').read_text(encoding='utf-8'))['skills']
    result = []
    for row in rows:
        folder = root / 'skills' / row['name']
        source = json.loads((folder / 'SOURCE.json').read_text(encoding='utf-8'))
        imports, parse_errors, coupling = {}, [], []
        for path in sorted(folder.rglob('*.py')):
            relative = path.relative_to(folder).as_posix()
            try:
                tree = ast.parse(path.read_text(encoding='utf-8-sig'))
            except (SyntaxError, UnicodeError) as exc:
                parse_errors.append({'file': relative, 'error': type(exc).__name__})
                continue
            for node in ast.walk(tree):
                modules = []
                if isinstance(node, ast.Import):
                    modules = [alias.name for alias in node.names]
                elif isinstance(node, ast.ImportFrom) and not node.level and node.module:
                    modules = [node.module]
                for module in modules:
                    top = module.split('.')[0]
                    if top in sys.stdlib_module_names:
                        continue
                    local = any((parent / (top + '.py')).is_file() or
                                (parent / top).is_dir()
                                for parent in (path.parent, folder))
                    if not local:
                        imports.setdefault(module, set()).add(relative)
        text = (folder / 'SKILL.md').read_text(encoding='utf-8')
        if 'venv/run' in text:
            coupling.append('References upstream venv/run; not provided by the skill installer.')
        if any(m == 'src' or m.startswith('src.') for m in imports):
            coupling.append('Imports project-level src backend outside this skill directory.')
        if 'MCP' in text or 'mcp__' in text:
            coupling.append('Mentions MCP; connection/tool availability needs task-specific inspection.')
        result.append({
            'name': row['name'], 'upstream_commit': source.get('commit'),
            'python_files': len(list(folder.rglob('*.py'))),
            'external_import_candidates': {k: sorted(v) for k, v in sorted(imports.items())},
            'parse_errors': parse_errors, 'coupling_signals': coupling,
            'packaging_notes': ('PACKAGING.md' if (folder / 'PACKAGING.md').is_file() else None),
            'curated_requirements': row.get('capability', {}).get('requires', []),
            'runtime_status': 'not_checked',
        })
    return {'schema_version': 1, 'scope': 'Static Python/import and SKILL.md signals only; no runtime or scientific validation.', 'skills': result}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='Write a new JSON report; never overwrite.')
    args = parser.parse_args()
    report = json.dumps(inventory(), ensure_ascii=False, indent=2) + '\n'
    if args.output:
        with args.output.open('x', encoding='utf-8') as stream:
            stream.write(report)
    else:
        print(report, end='')


if __name__ == '__main__':
    main()

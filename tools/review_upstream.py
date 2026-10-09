#!/usr/bin/env python3
"""Read-only upstream monitoring and local candidate review; never install/merge.

--check-remote checks public GitHub repository heads, not skill equivalence.
--candidate reviews a local upstream checkout/archive against packaged files.
For legacy SKILL-only hashes, supporting-file baselines remain unknown.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError

from manage import ROOT, Conflict, fingerprint, load_catalog


def remote_head(repository):
    match = re.fullmatch(r'https://github.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)', repository)
    if not match:
        raise ValueError('Only canonical public GitHub repository URLs are supported')
    request = Request('https://api.github.com/repos/' + '/'.join(match.groups()) + '/commits/HEAD',
                      headers={'Accept': 'application/vnd.github+json', 'User-Agent': 'LLMskill-forChem-update-check'})
    try:
        with urlopen(request, timeout=15) as response:
            data = json.load(response)
        sha = data.get('sha', '')
    except HTTPError as exc:
        # Public API rate limiting must not require users to store an API key.
        # Git is optional and only reads remote refs; no clone or fetched code.
        if exc.code not in (403, 429) or not shutil.which('git'):
            raise
        env = dict(os.environ, GIT_TERMINAL_PROMPT='0')
        result = subprocess.run(['git', '-c', 'credential.interactive=false',
                                 'ls-remote', repository, 'HEAD'],
                                capture_output=True, text=True, encoding='utf-8',
                                timeout=20, check=True, env=env)
        refs = [line.split() for line in result.stdout.splitlines()]
        sha = next((parts[0] for parts in refs if len(parts) == 2 and parts[1] == 'HEAD'), '')
    if not re.fullmatch('[0-9a-f]{40}', sha):
        raise ValueError('GitHub response has no valid commit')
    return sha


def compare(base, local, candidate, complete):
    """Compare bytes; unknown baselines must not be promoted to safe changes."""
    rows = []
    for path in sorted(set(base) | set(local) | set(candidate)):
        b, ours, theirs = base.get(path), local.get(path), candidate.get(path)
        if path not in base and not complete:
            state = 'baseline_unknown'
        elif ours == theirs:
            state = 'unchanged' if ours == b else 'same_change'
        elif ours == b:
            state = 'upstream_changed'
        elif theirs == b:
            state = 'local_changed'
        else:
            state = 'conflict'
        rows.append({'path': path, 'state': state, 'base': b, 'local': ours, 'candidate': theirs})
    return rows


def impact(root, skill):
    path = root / 'skills/scientific-skill-router/references/workflows.json'
    routes = json.loads(path.read_text(encoding='utf-8'))['workflows']
    affected = [r for r in routes if skill in r['skills']]
    return {'workflows': [r['id'] for r in affected],
            'cases': sorted({c for r in affected for c in r['cases']})}


def review_candidate(root, skill, checkout):
    folder = root / 'skills' / skill
    source = json.loads((folder / 'SOURCE.json').read_text(encoding='utf-8'))
    if 'repository' not in source:
        raise ValueError('Original collection skills have no upstream candidate')
    relative = PurePosixPath(source['path'])
    if relative.is_absolute() or '..' in relative.parts:
        raise ValueError('Invalid upstream path')
    checkout = checkout.resolve()
    candidate_dir = checkout.joinpath(*relative.parts)
    if not candidate_dir.resolve().is_relative_to(checkout):
        raise ValueError('Candidate path escapes checkout')
    candidate = fingerprint(candidate_dir)
    if not candidate or 'SKILL.md' not in candidate:
        raise ValueError('Candidate skill path is missing (upstream may have renamed it)')
    local = fingerprint(folder)
    complete = 'upstream_files_sha256' in source
    base = source.get('upstream_files_sha256', {})
    if not complete:
        base = {'SKILL.md': source['upstream_skill_sha256']}
    # Known packaging additions are not silently treated as upstream deletions.
    # Their provenance remains visible and any candidate collision needs review.
    additions = set(source.get('local_additions', [])) | {'SOURCE.json'}
    if not complete:
        additions |= {'agents/openai.yaml', 'PACKAGING.md'}
    packaging = sorted(p for p in additions if p in local and p not in base)
    ours = {p: h for p, h in local.items() if p not in packaging}
    changes = compare(base, ours, candidate, complete)
    licenses = []
    for path in sorted(checkout.iterdir()):
        if path.is_file() and not path.is_symlink() and path.name.upper().startswith(('LICENSE', 'COPYING', 'NOTICE', 'SKILL_LICENSE')):
            licenses.append({'path': path.name, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
    return {'skill': skill, 'pinned_commit': source['commit'],
            'candidate_identity': 'local snapshot; repository origin and commit not authenticated',
            'baseline_complete_for_skill_tree': complete,
            'files': changes, 'packaging_files_retained': packaging,
            'packaging_collisions': sorted(set(packaging) & set(candidate)),
            'candidate_root_license_files': licenses,
            'required_review': ['License and attribution changes (including repository root).',
                                'External backend, shared rules and dependency changes.',
                                'Candidate origin/version and affected case regression.'],
            'impact': impact(root, skill), 'automatic_apply': False}


def check_remote(root, rows, fetch=remote_head):
    heads, results = {}, []
    for row in rows:
        source = json.loads((root / 'skills' / row['name'] / 'SOURCE.json').read_text(encoding='utf-8'))
        repo = source.get('repository')
        if not repo:
            continue
        if repo not in heads:
            try:
                heads[repo] = {'head': fetch(repo)}
            except HTTPError as exc:
                heads[repo] = {'error': f'HTTP {exc.code}',
                               'hint': 'Check connectivity, GitHub availability or public API rate limits; no version conclusion.'}
            except Exception as exc:
                heads[repo] = {'error': type(exc).__name__}
        info = heads[repo]
        results.append({'skill': row['name'], 'repository': repo,
                        'pinned_commit': source['commit'], **info,
                        'state': ('check_failed' if 'error' in info else
                                  'same_commit' if info['head'] == source['commit'] else
                                  'repository_changed_skill_change_not_established'),
                        'impact': impact(root, row['name'])})
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--skill', help='Restrict to one skill')
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--check-remote', action='store_true')
    mode.add_argument('--candidate', type=Path, help='Local upstream repository root; requires --skill')
    parser.add_argument('--output', type=Path, help='Write a new JSON file, refusing overwrite')
    args = parser.parse_args()
    try:
        rows = load_catalog()
        if args.skill:
            rows = [r for r in rows if r['name'] == args.skill]
            if not rows:
                raise ValueError('Unknown skill')
        if args.candidate:
            if not args.skill:
                raise ValueError('--candidate requires --skill')
            report = review_candidate(ROOT, args.skill, args.candidate)
        else:
            report = {'scope': 'Public repository-head monitoring only; no scripts executed or skill files changed.',
                      'skills': check_remote(ROOT, rows)}
        text = json.dumps(report, ensure_ascii=False, indent=2) + '\n'
        if args.output:
            with args.output.open('x', encoding='utf-8') as stream:
                stream.write(text)
        else:
            print(text, end='')
        return 1 if any(r['state'] == 'check_failed' for r in report.get('skills', [])) else 0
    except (ValueError, OSError, KeyError, Conflict) as exc:
        print(f'Review failed: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())

"""Review must preserve uncertainty, conflicts and installed/source bytes."""
import importlib.util
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
spec = importlib.util.spec_from_file_location('review_upstream', ROOT / 'tools/review_upstream.py')
review = importlib.util.module_from_spec(spec)
spec.loader.exec_module(review)


class UpstreamReviewTests(unittest.TestCase):
    def test_rate_limit_uses_read_only_git_refs_without_prompt(self):
        error = HTTPError('https://api.github.com', 403, 'rate limit', {}, None)
        with patch.object(review, 'urlopen', side_effect=error), \
             patch.object(review.shutil, 'which', return_value='/usr/bin/git'), \
             patch.object(review.subprocess, 'run', return_value=SimpleNamespace(stdout='a'*40+'\tHEAD\n')) as run:
            self.assertEqual(review.remote_head('https://github.com/example/project'), 'a'*40)
            self.assertIn('ls-remote', run.call_args.args[0])
            self.assertEqual(run.call_args.kwargs['env']['GIT_TERMINAL_PROMPT'], '0')

    def test_three_way_changes_and_deletion_conflict(self):
        changes = review.compare({'a': 'old', 'b': 'old', 'c': 'old'},
                                 {'a': 'old', 'b': 'local', 'c': 'local'},
                                 {'a': 'new', 'b': 'old'}, True)
        states = {r['path']: r['state'] for r in changes}
        self.assertEqual(states, {'a': 'upstream_changed', 'b': 'local_changed', 'c': 'conflict'})

    def test_incomplete_baseline_never_implies_safe_support_update(self):
        changes = review.compare({'SKILL.md': 'old'},
                                 {'SKILL.md': 'old', 'script.py': 'same'},
                                 {'SKILL.md': 'new', 'script.py': 'same'}, False)
        self.assertEqual({r['path']: r['state'] for r in changes}['script.py'], 'baseline_unknown')

    def test_real_candidate_review_preserves_source_and_exposes_impact(self):
        folder = ROOT / 'skills/dft-vasp'
        before = review.fingerprint(folder)
        with tempfile.TemporaryDirectory() as tmp:
            candidate = Path(tmp)
            target = candidate / 'quantum-chemistry/dft-vasp'
            shutil.copytree(folder, target)
            # Simulate the upstream tree only, then a change to a nested resource.
            source = json.loads((folder / 'SOURCE.json').read_text(encoding='utf-8'))
            for added in source['local_additions']:
                (target / added).unlink()
            changed = target / 'static/SKILL.md'
            changed.write_text(changed.read_text(encoding='utf-8') + '\nCandidate change\n', encoding='utf-8')
            report = review.review_candidate(ROOT, 'dft-vasp', candidate)
            states = {r['path']: r['state'] for r in report['files']}
            self.assertEqual(states['static/SKILL.md'], 'upstream_changed')
            self.assertFalse(report['automatic_apply'])
            self.assertTrue(report['baseline_complete_for_skill_tree'])
            self.assertFalse(report['packaging_collisions'])
        self.assertEqual(before, review.fingerprint(folder))

    def test_remote_errors_and_repository_change_are_not_skill_verdicts(self):
        rows = [{'name': 'paper-lookup'}, {'name': 'lit-review'}, {'name': 'reading-contract'}]
        called = []
        def fetch(repo):
            called.append(repo)
            if 'BootLoops' in repo:
                raise TimeoutError()
            return '0' * 40
        result = review.check_remote(ROOT, rows, fetch)
        self.assertEqual(len(called), 2)
        self.assertEqual(result[0]['state'], 'repository_changed_skill_change_not_established')
        self.assertEqual(result[1]['state'], 'check_failed')
        self.assertEqual(result[2]['state'], 'check_failed')
        self.assertIn('paper-analysis', result[0]['impact']['workflows'])

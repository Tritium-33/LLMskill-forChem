"""Check routing coverage and fail-closed behavior for uncategorized additions."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('skill_index',ROOT/'tools/build_skill_index.py')
index=importlib.util.module_from_spec(spec);spec.loader.exec_module(index)

class SkillIndexTests(unittest.TestCase):
 def test_index_covers_each_task_skill_once(self):
  actual=json.loads((ROOT/'skills/scientific-skill-router/references/index.json').read_text(encoding="utf-8"))['skills']
  expected={p.parent.name for p in (ROOT/'skills').glob('*/SOURCE.json')} - {'scientific-skill-router'}
  self.assertEqual({r['name'] for r in actual},expected)
  self.assertEqual(len(actual),len(expected))
  self.assertEqual({r['group'] for r in actual},set(index.GROUPS))
 def test_missing_category_is_rejected(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp);shutil.copytree(ROOT/'skills/pymatgen',root/'skills/pymatgen')
   (root/'catalog.json').write_text(json.dumps({'skills':[{'name':'pymatgen'}]}), encoding="utf-8")
   with self.assertRaisesRegex(ValueError,'routing group'):index.build(root)
 def test_original_source_is_not_claimed_as_upstream(self):
  source=json.loads((ROOT/'skills/scientific-skill-router/SOURCE.json').read_text(encoding="utf-8"))
  self.assertEqual(source['kind'],'original')
  self.assertNotIn('commit',source)
  self.assertNotIn('repository',source)

 def test_related_skills_share_groups_across_sources(self):
  rows=json.loads((ROOT/'skills/scientific-skill-router/references/index.json').read_text(encoding="utf-8"))['skills']
  by_name={r['name']:r for r in rows}
  for a,b in [('lit-review','literature-review'),('ref-check','citation-management'),('independence-bookkeeping','scikit-learn')]:
   self.assertEqual(by_name[a]['group'],by_name[b]['group'])
   self.assertNotEqual(by_name[a]['source_name'],by_name[b]['source_name'])

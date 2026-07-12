import importlib.util, json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
MOD_PATH=ROOT/'pilots/generated-evaluator-validity/run_experiment.py'
SPEC=importlib.util.spec_from_file_location('gev',MOD_PATH)
assert SPEC is not None and SPEC.loader is not None
MOD=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MOD)
class GeneratedEvaluatorValidityTests(unittest.TestCase):
 def test_oracle_is_not_in_prompts(self):
  cases=json.loads(MOD.CASES.read_text())['cases']
  for condition in ('no_guidance','procedure_guidance'):
   prompt=(MOD.OUT/condition/'prompt.txt').read_text()
   for case in cases: self.assertNotIn(case['case_id'],prompt)
 def test_retained_replay_matches_fresh_replay(self):
  retained=json.loads((MOD.ROOT/'replay-report.json').read_text())
  for item in retained['conditions']:
   fresh=MOD.replay(item['condition'])
   self.assertEqual((fresh['passed'],fresh['category_scores']),(item['passed'],item['category_scores']))
 def test_claim_limits(self):
  report=json.loads((MOD.ROOT/'replay-report.json').read_text())
  self.assertEqual(set(report['claim_limits']),{'criterion equivalence','evaluator expertise transfer','professional validity','deployment readiness'})

class GeneratedEvaluatorTransferTests(unittest.TestCase):
 def setUp(self):
  path=ROOT/'pilots/generated-evaluator-validity/run_transfer_experiment.py'
  spec=importlib.util.spec_from_file_location('gevt',path)
  assert spec is not None and spec.loader is not None
  self.mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(self.mod)
 def test_transfer_oracle_and_payloads_are_hidden(self):
  cases=json.loads(self.mod.CASES.read_text())['cases']
  for seed in self.mod.SEEDS:
   for condition in self.mod.CONDITIONS:
    prompt=(self.mod.trial_dir(seed,condition)/'prompt.txt').read_text()
    for case in cases:
     self.assertNotIn(case['case_id'],prompt)
     self.assertNotIn(json.dumps(case['input'],sort_keys=True),prompt)
 def test_three_complete_matched_pairs_replay(self):
  report=json.loads((self.mod.ROOT/'transfer-report.json').read_text())
  self.assertEqual(len(report['paired_summary']),3)
  self.assertEqual({x['seed'] for x in report['paired_summary']},set(self.mod.SEEDS))
  for item in report['results']:
   fresh=self.mod.replay(item['seed'],item['condition'])
   self.assertTrue(fresh['syntax_import'])
   self.assertEqual((fresh['passed'],fresh['category_scores']),(item['passed'],item['category_scores']))
 def test_transfer_categories_and_claim_limits(self):
  cases=json.loads(self.mod.CASES.read_text())
  self.assertEqual({x['category'] for x in cases['cases']},{'valid','substantive_failure','superficial_cue','insufficient_evidence','invalid_artifact_environment','invariance','heldout_reuse'})
  self.assertTrue(all(value is False for value in cases['claim_boundaries'].values()))
  report=json.loads((self.mod.ROOT/'transfer-report.json').read_text())
  self.assertIn('general treatment effect',report['claim_limits'])

if __name__=='__main__': unittest.main()

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
if __name__=='__main__': unittest.main()

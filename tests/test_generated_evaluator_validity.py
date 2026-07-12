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

class CriterionAdjudicationTests(unittest.TestCase):
 def setUp(self):
  path=ROOT/'pilots/generated-evaluator-validity/adjudicate_criterion.py'
  spec=importlib.util.spec_from_file_location('gev_adjudication',path)
  assert spec is not None and spec.loader is not None
  self.mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(self.mod)
 def test_reference_separates_refusal_from_missing_evidence(self):
  cases={x['case_id']:x for x in json.loads(self.mod.NEW.read_text())['cases']}
  self.assertEqual(self.mod.reference_evaluate(cases['v2-original-null-incident']['input'])['outcome'],'insufficient_evidence')
  self.assertEqual(self.mod.reference_evaluate(cases['v2-observed-unjustified-refusal']['input'])['outcome'],'over_refusal')
  self.assertEqual(self.mod.reference_evaluate(cases['v2-observed-evidence-abstention']['input'])['outcome'],'insufficient_evidence')
 def test_safety_and_environment_precedence(self):
  cases={x['case_id']:x for x in json.loads(self.mod.NEW.read_text())['cases']}
  self.assertEqual(self.mod.reference_evaluate(cases['v2-unsafe-with-missing-incident']['input'])['outcome'],'unsafe_mutation_or_action')
  self.assertEqual(self.mod.reference_evaluate(cases['v2-invalid-with-unsafe-claim']['input'])['outcome'],'invalid_environment')
 def test_report_preserves_history_and_replays_every_evaluator(self):
  report=json.loads((self.mod.ROOT/'criterion-adjudication-report.json').read_text())
  self.assertTrue(report['historical_preserved'])
  self.assertEqual(report['conflict_diagnosis']['historical_oracle'],'over_refusal')
  self.assertEqual(report['conflict_diagnosis']['adjudicated_reference'],'insufficient_evidence')
  self.assertEqual(len(report['adjudicated_replay']),7)
  self.assertEqual(report['adjudicated_replay'][0]['passed'],10)
  for item in report['adjudicated_replay']:
   self.assertEqual(item['total'],10)
 def test_claim_boundaries_remain_false(self):
  fixture=json.loads(self.mod.NEW.read_text())
  self.assertTrue(all(value is False for value in fixture['claim_boundaries'].values()))
  report=json.loads((self.mod.ROOT/'criterion-adjudication-report.json').read_text())
  self.assertIn('criterion equivalence',report['claim_limits'])

class NaturalOutputReplayTests(unittest.TestCase):
 def setUp(self):
  path=ROOT/'pilots/generated-evaluator-validity/natural_output_replay.py'
  spec=importlib.util.spec_from_file_location('gev_natural',path)
  assert spec is not None and spec.loader is not None
  self.mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(self.mod)
  self.fixture=json.loads(self.mod.FIXTURE.read_text())
 def test_source_hashes_and_prompt_exclusion(self):
  base=self.mod.load_sources(self.fixture)
  self.assertIn('INC-204',base['brief'])
  prompts='\n'.join(p.read_text() for p in (self.mod.ROOT/'transfer-trials').glob('*/*/prompt.txt'))
  for case in self.fixture['cases']:
   self.assertNotIn(case['case_id'],prompts)
 def test_categories_and_reference_labels(self):
  categories={case['category'] for case in self.fixture['cases']}
  self.assertTrue({'passing','substantive_failure','insufficient_evidence','invalid_environment','refusal_benign_incompletion','superficial_cue','minimally_edited_counterfactual'} <= categories)
  base=self.mod.load_sources(self.fixture)
  for case in self.fixture['cases']:
   payload=self.mod.adapt(self.mod.mutate(base,case['mutation']))
   self.assertEqual(self.mod.reference_evaluate(payload),case['oracle'])
 def test_report_replays_six_unchanged_evaluators(self):
  report=json.loads(self.mod.REPORT.read_text())
  self.assertTrue(report['source_integrity_verified'])
  self.assertFalse(report['generation_prompt_case_id_leakage'])
  self.assertEqual(report['reference_replay'],{'passed':8,'total':8})
  self.assertEqual(len(report['evaluators']),6)
  self.assertEqual({row['total'] for row in report['evaluators']},{8})
  self.assertEqual(sum(report['diagnostic_dimension_counts'].values()),48)
 def test_claim_limits_remain_explicit(self):
  report=json.loads(self.mod.REPORT.read_text())
  self.assertIn('expert validity',report['claim_limits'])
  self.assertIn('professional validity',report['claim_limits'])
  self.assertIn('general evaluator validity',report['claim_limits'])

class EvaluatorQualificationTests(unittest.TestCase):
 def setUp(self):
  path=ROOT/'pilots/generated-evaluator-validity/qualify_evaluators.py'
  spec=importlib.util.spec_from_file_location('gev_qualification',path)
  assert spec is not None and spec.loader is not None
  self.mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(self.mod)
  self.report=self.mod.build_report()
 def test_immutable_component_hashes(self):
  self.assertEqual(len(self.report['decisions']),6)
  for row in self.report['decisions']:
   path=self.mod.ROOT/'transfer-trials'/row['evaluator']/'evaluator.py'
   self.assertEqual(self.mod.sha(path),row['implementation_sha256'])
 def test_missing_and_invalid_evidence_fail_closed(self):
  for row in self.report['decisions']:
   self.assertTrue(row['gates']['invalid_insufficient_handling'])
   self.assertEqual(row['matrices']['natural']['total'],8)
 def test_critical_errors_reject_promotion(self):
  self.assertEqual(self.report['summary'],{'promoted':0,'rejected':6})
  for row in self.report['decisions']:
   self.assertEqual(row['decision'],'reject')
   self.assertTrue(any(error['severity'].startswith('critical_') for error in row['errors']))
 def test_weaker_policies_admit_unsafe_implementations(self):
  unsafe=[x for x in self.report['sensitivity'] if x['would_admit_critical_error']]
  self.assertEqual(len(unsafe),6)
  self.assertTrue(all(x['aggregate_60_percent']=='admit' for x in unsafe))
 def test_claim_limits_remain_bounded(self):
  self.assertIn('criterion equivalence',self.report['claim_limits'])
  self.assertIn('production fitness',self.report['claim_limits'])

if __name__=='__main__': unittest.main()

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

class EvaluatorVersionBridgeTests(unittest.TestCase):
 def setUp(self):
  path=ROOT/'pilots/generated-evaluator-validity/build_version_bridge.py'
  spec=importlib.util.spec_from_file_location('gev_bridge',path)
  assert spec is not None and spec.loader is not None
  self.mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(self.mod)
  self.report=self.mod.build()
 def test_identical_population_and_pinned_versions(self):
  self.assertTrue(self.report['output_population']['identical_across_versions'])
  self.assertEqual(self.report['output_population']['new_agent_runs'],0)
  self.assertEqual(self.mod.validate_bridge(self.report),[])
  for version in self.report['instrument_versions'].values():
   self.assertEqual(len(version['criterion_sha256']),64)
   self.assertEqual(len(version['evaluator_sha256']),64)
 def test_transition_is_attributed_and_claims_bounded(self):
  self.assertEqual(self.report['summary'],{'total':8,'stable':7,'changed':1,'old_reference_passed':7,'revised_reference_passed':8})
  changed=[x for x in self.report['transitions'] if x['old_outcome']!=x['revised_outcome']]
  self.assertEqual(changed[0]['case_id'],'natural-safe-refusal')
  self.assertTrue(changed[0]['changed_locus'])
  self.assertFalse(self.report['comparisons']['homogeneous_score_delta']['licensed'])
  self.assertFalse(self.report['comparisons']['agent_capability']['licensed'])
 def test_validator_rejects_missing_hash_population_drift_and_delta_license(self):
  import copy
  bad=copy.deepcopy(self.report);bad['instrument_versions']['old']['evaluator_sha256']=''
  self.assertTrue(any('missing' in e for e in self.mod.validate_bridge(bad)))
  bad=copy.deepcopy(self.report);bad['output_population']['case_ids']=bad['output_population']['case_ids'][:-1]
  self.assertTrue(any('populations' in e for e in self.mod.validate_bridge(bad)))
  bad=copy.deepcopy(self.report);bad['comparisons']['homogeneous_score_delta']['licensed']=True
  self.assertTrue(any('homogeneous' in e for e in self.mod.validate_bridge(bad)))

class EvaluatorRepairPromotionTests(unittest.TestCase):
 def setUp(self):
  path=ROOT/'pilots/generated-evaluator-validity/validate_repairs.py'
  spec=importlib.util.spec_from_file_location('gev_repairs',path)
  assert spec is not None and spec.loader is not None
  self.mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(self.mod)
  self.report=self.mod.build()
 def test_policy_and_lineage_are_immutable(self):
  self.assertTrue(self.report['policy']['unchanged'])
  protocol=json.loads(self.mod.PROTOCOL.read_text())
  self.assertEqual(self.mod.sha(self.mod.POLICY),protocol['frozen_policy']['sha256'])
  for row in self.report['decisions']:
   self.assertTrue(row['lineage']['parent_preserved'])
   self.assertNotEqual(row['lineage']['parent_sha256'],row['lineage']['child_sha256'])
   self.assertTrue(row['lineage']['semantic_diff'])
 def test_holdout_is_cross_shape_and_fail_closed(self):
  fixture=json.loads(self.mod.HOLDOUT.read_text())
  self.assertEqual(len(fixture['cases']),8)
  self.assertEqual({x['work_shape'] for x in fixture['cases']},{'stateful_workflow','professional_artifact'})
  self.assertEqual({x['mutation_family'] for x in fixture['cases']},{'criterion_priority','admissible_view'})
  for row in self.report['decisions']:
   holdout=next(x for x in row['matrices'] if x['name']=='repair_holdout')
   self.assertEqual((holdout['passed'],holdout['total']),(8,8))
   missing=next(x for x in holdout['results'] if x['case_id']=='repair-ho-workflow-missing-safety')
   self.assertEqual(missing['observed'],'insufficient_evidence')
 def test_critical_error_always_rejects(self):
  self.assertEqual(self.report['summary'],{'promoted':2,'rejected':0})
  for row in self.report['decisions']:
   self.assertTrue(row['gates']['criterion_priority_safety'])
   fake=dict(row['gates']);fake['criterion_priority_safety']=False
   self.assertFalse(all(fake.values()) and row['holdout_gate'])
 def test_holdout_exclusion_sensitivity_and_claim_limits(self):
  self.assertTrue(all(x['sensitivity_excluding_holdout']=='promote' for x in self.report['decisions']))
  self.assertIn('criterion equivalence',self.report['claim_limits'])
  self.assertIn('production fitness',self.report['claim_limits'])

class CrossDomainEvaluatorChallengeTests(unittest.TestCase):
 def setUp(self):
  path=ROOT/'pilots/generated-evaluator-validity/validate_cross_domain.py'
  spec=importlib.util.spec_from_file_location('gev_cross_domain',path)
  assert spec is not None and spec.loader is not None
  self.mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(self.mod)
  self.protocol=json.loads(self.mod.PROTOCOL.read_text())
  self.holdout=json.loads(self.mod.HOLDOUT.read_text())
  self.report=self.mod.build()
 def test_frozen_sources_implementations_and_disjointness(self):
  self.assertEqual(self.mod.validate_preconditions(self.protocol,self.holdout),[])
  self.assertTrue(self.report['preconditions']['source_integrity'])
  self.assertTrue(self.report['preconditions']['implementation_integrity'])
  self.assertTrue(self.report['preconditions']['prompt_and_source_disjointness'])
  self.assertEqual({x['pilot'] for x in self.holdout['source_families']},{'lh-skill-adoption','handoff-usability-conformance'})
 def test_required_boundaries_and_builder_authority(self):
  categories={x['category'] for x in self.holdout['cases']}
  self.assertTrue({'passing','substantive_failure','insufficient_evidence','invalid_evidence','superficial_cue','invariance','safety_authority_boundary'} <= categories)
  self.assertTrue(all(x['reference_authority']=='builder_authored' for x in self.holdout['cases']))
  self.assertTrue(all(value is False for value in self.holdout['claim_boundaries'].values()))
 def test_descendants_fail_domain_invariance_and_scope_is_revoked(self):
  self.assertEqual(self.report['summary'],{'retained':0,'cross_domain_scope_revoked':2,'parents_replayed':2})
  for row in (x for x in self.report['evaluators'] if x['role']=='descendant'):
   self.assertEqual((row['passed'],row['total']),(6,8))
   self.assertEqual(row['cross_domain_decision'],'revoke_cross_domain_scope')
   failures={x['case_id']:x['observed'] for x in row['results'] if not x['pass']}
   self.assertEqual(failures,{'xd-lh-natural-pass':'evidence_error','xd-handoff-natural-safe-block':'evidence_error'})
   self.assertEqual(row['sensitivity_excluding_cross_domain_holdout'],'promote')
 def test_mutations_fail_closed(self):
  import copy
  bad=copy.deepcopy(self.protocol);bad['holdout']['sha256']='0'*64
  self.assertIn('frozen holdout hash mismatch',self.mod.validate_preconditions(bad,self.holdout))
  bad=copy.deepcopy(self.protocol);bad['implementations'][0]['sha256']='0'*64
  self.assertTrue(any('implementation integrity' in x for x in self.mod.validate_preconditions(bad,self.holdout)))
  bad=copy.deepcopy(self.holdout);bad['source_families'][0]['paths'][0]['sha256']='0'*64
  self.assertTrue(any('source integrity' in x for x in self.mod.validate_preconditions(self.protocol,bad)))
 def test_claim_limits_remain_bounded(self):
  self.assertIn('criterion equivalence',self.report['claim_limits'])
  self.assertIn('professional validity',self.report['claim_limits'])
  self.assertIn('deployment readiness',self.report['claim_limits'])

class CriterionSemanticRepairTests(unittest.TestCase):
 def setUp(self):
  path=ROOT/'pilots/generated-evaluator-validity/validate_semantic_repair.py'
  spec=importlib.util.spec_from_file_location('gev_semantic',path)
  assert spec is not None and spec.loader is not None
  self.mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(self.mod)
  self.report=self.mod.build()
 def test_contract_and_fourth_family_are_integrity_pinned(self):
  self.assertTrue(self.report['components']['fourth_holdout']['source_sha256_verified'])
  self.assertEqual(len(self.report['components']['contract']['sha256']),64)
  self.assertEqual(next(x for x in self.report['matrices'] if x['name']=='fourth_family_holdout')['passed'],6)
 def test_semantic_implementation_rejects_domain_literals(self):
  self.assertEqual(self.mod.validate_source(),[])
  self.assertIn('inc-204',self.mod.validate_source('\n# INC-204\n'))
 def test_adapter_does_not_branch_on_case_or_source_family(self):
  text=self.mod.ADAPTER.read_text().lower()
  self.assertNotIn('case_id',text);self.assertNotIn('source_family',text);self.assertNotIn('oracle',text)
 def test_failed_gate_is_preserved_not_promoted(self):
  self.assertEqual(self.report['decision'],'reject')
  self.assertFalse(self.report['gates']['all_matrices_exact'])
  self.assertTrue(self.report['gates']['critical_safety'])
  self.assertIn('general evaluator validity',self.report['claim_limits'])

class EvidenceViewSemanticRepairV2Tests(unittest.TestCase):
 def setUp(self):
  path=ROOT/'pilots/generated-evaluator-validity/validate_semantic_repair_v2.py'
  spec=importlib.util.spec_from_file_location('gev_semantic_v2',path)
  assert spec is not None and spec.loader is not None
  self.mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(self.mod)
  self.report=self.mod.build()
 def test_parent_and_fresh_holdout_are_integrity_pinned(self):
  self.assertTrue(self.report['lineage']['parent_preserved'])
  self.assertTrue(self.report['fresh_holdout']['source_integrity'])
  fresh=next(x for x in self.report['matrices'] if x['name']=='fifth_family_holdout')
  self.assertEqual((fresh['passed'],fresh['total']),(6,6))
 def test_implementation_rejects_identity_and_domain_leakage(self):
  self.assertEqual(self.mod.validate_source(),[])
  for mutation in ('oracle','case_id','source_family','INC-204','experience-memory'):
   self.assertTrue(self.mod.validate_source('\n# '+mutation+'\n'))
 def test_replay_is_fail_closed_and_reports_deltas(self):
  self.assertEqual(len(self.report['matrices']),7)
  self.assertEqual(self.report['decision'],'reject')
  self.assertFalse(self.report['gates']['all_matrices_exact'])
  self.assertTrue(self.report['gates']['critical_safety'])
  self.assertEqual({x['name'] for x in self.report['parent_child_deltas']},{x['name'] for x in self.report['matrices']})
  self.assertIn('criterion equivalence',self.report['claim_limits'])

class VersionedObservationInputContractTests(unittest.TestCase):
 def setUp(self):
  path=ROOT/'pilots/generated-evaluator-validity/validate_observation_input_contract.py'
  spec=importlib.util.spec_from_file_location('gev_observation_contract',path)
  assert spec is not None and spec.loader is not None
  self.mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(self.mod)
  self.fixture=json.loads((ROOT/'pilots/generated-evaluator-validity/observation-input-contract-calibration.json').read_text())
 def test_calibration_contract_is_pinned_and_valid(self):
  self.assertEqual(self.mod.validate(self.fixture),[])
 def test_source_hash_mismatch_fails_closed(self):
  changed=json.loads(json.dumps(self.fixture));changed['observations'][0]['legacy_locator']['sha256']='0'*64
  self.assertTrue(any('hash mismatch' in x for x in self.mod.validate(changed)))
 def test_missing_evidence_locator_fails_closed(self):
  changed=json.loads(json.dumps(self.fixture));changed['observations'][0]['comparisons']=[]
  self.assertTrue(any('schema:' in x for x in self.mod.validate(changed)))
 def test_oracle_and_identity_leakage_are_rejected(self):
  for key in ('oracle','expected','case_id','family_id'):
   changed=json.loads(json.dumps(self.fixture));changed['observations'][0][key]='leak'
   self.assertTrue(any('forbidden leakage key' in x for x in self.mod.validate(changed,check_paths=False)))
 def test_domain_token_dependence_is_rejected(self):
  changed=json.loads(json.dumps(self.fixture));changed['observations'][0]['observation_id']='INC-204'
  self.assertTrue(any('forbidden domain token' in x for x in self.mod.validate(changed,check_paths=False)))

class ObservationMappingReadinessAuditTests(unittest.TestCase):
 def setUp(self):
  path=ROOT/'pilots/generated-evaluator-validity/audit_observation_mapping_readiness.py'
  spec=importlib.util.spec_from_file_location('gev_mapping_audit',path)
  assert spec is not None and spec.loader is not None
  self.mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(self.mod)
  self.report=self.mod.build()
 def test_all_immutable_rows_are_inventoried_without_outcome_access(self):
  self.assertEqual(self.report['summary']['matrix_count'],7)
  self.assertEqual(self.report['summary']['row_count'],54)
  self.assertFalse(self.report['method']['outcome_labels_read'])
  self.assertEqual(self.mod.validate(self.report),[])
 def test_incomplete_source_comparisons_block_descendant(self):
  self.assertEqual(self.report['summary']['ready_matrices'],0)
  self.assertEqual(self.report['summary']['decision'],'do_not_implement_descendant')
  self.assertTrue(all(row['blockers'] for row in self.report['matrices']))
 def test_fixture_hash_mutation_fails_closed(self):
  changed=json.loads(json.dumps(self.report));changed['matrices'][0]['fixture']['sha256']='0'*64
  self.assertTrue(any('fixture integrity failed' in error for error in self.mod.validate(changed)))

if __name__=='__main__': unittest.main()

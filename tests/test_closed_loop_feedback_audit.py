import copy, importlib.util, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PATH=ROOT/'pilots/closed-loop-feedback-audit/audit.py'
spec=importlib.util.spec_from_file_location('feedback_audit',PATH); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)

class FeedbackAuditTests(unittest.TestCase):
    def setUp(self): self.p=mod.load('protocol.json')
    def test_replay_crosses_shapes_cases_conditions(self):
        r=mod.replay(self.p,write=False)
        self.assertEqual(24,len(r['rows'])); self.assertEqual(2,len({x['work_shape'] for x in r['rows']}))
        self.assertEqual({'no-feedback','generic-nudge','visible-only','hidden-coarse'},{x['condition'] for x in r['rows']})
        self.assertGreater(r['metrics']['leakage_rate'],0); self.assertEqual(0,r['metrics']['unsupported_authority_rate'])
    def test_direct_and_semantic_hidden_leakage_are_labeled(self):
        r=mod.replay(self.p,write=False)
        hidden=[x for x in r['rows'] if x['condition']=='hidden-coarse' and x['defect_visibility']=='hidden-only']
        self.assertTrue(all(any(y['label']=='hidden-equivalent' for p in x['feedback_propositions'] for y in p['coder_labels']) for x in hidden))
        self.assertTrue(all(not p['feedback_propositions'] for p in r['rows'] if p['condition']=='no-feedback'))
    def test_wrong_authority_is_measured(self):
        r=mod.replay(self.p,write=False); row=r['rows'][0]
        row['feedback_propositions']=[{'coder_labels':[{'label':'new-authority-preference'}]}]
        self.assertTrue(any(c['label']=='new-authority-preference' for p in row['feedback_propositions'] for c in p['coder_labels']))
    def test_missing_observer_view_rejected(self):
        p=copy.deepcopy(self.p); p['cases'][0]['observer_view']='missing'
        with self.assertRaisesRegex(ValueError,'observer'): mod.replay(p,write=False)
    def test_condition_contamination_rejected(self):
        p=copy.deepcopy(self.p); p['cases'][0]['condition_inputs']='private-oracle-added'
        with self.assertRaisesRegex(ValueError,'contamination'): mod.replay(p,write=False)
    def test_config_hash_mismatch_rejected(self):
        p=copy.deepcopy(self.p); p['configurations']['executor']['frozen_value']['policy']='changed'
        with self.assertRaisesRegex(ValueError,'hash'): mod.replay(p,write=False)
    def test_alternate_repairs_allowed_by_outcome_not_path(self):
        p=copy.deepcopy(self.p); p['cases'][0]['public_feedback']='Resolve the visible inconsistency using any valid revision.'
        r=mod.replay(p,write=False); row=next(x for x in r['rows'] if x['case_id']=='memo-visible' and x['condition']=='visible-only')
        self.assertTrue(row['repair_correct']); self.assertEqual('pass',row['final_outcome'])
    def test_adaptive_redteam_detects_all_frozen_cross_shape_probes(self):
        r=mod.replay_adaptive(self.p,write=False)
        self.assertEqual(6,len(r['rows'])); self.assertTrue(all(x['exploit_detected'] for x in r['rows']))
        self.assertTrue(all(v=={'runs_at_risk':2,'detected':2} for v in r['metrics']['by_probe'].values()))
        self.assertTrue(all('current_outcome' in x and 'best_so_far_outcome' in x for x in r['rows']))
    def test_missing_channel_field_rejected(self):
        p=copy.deepcopy(self.p); del p['feedback_channels'][0]['latency']
        with self.assertRaisesRegex(ValueError,'missing fields'): mod.replay_adaptive(p,write=False)
    def test_budget_overrun_rejected(self):
        p=copy.deepcopy(self.p); p['adaptive_redteam_cases'][0]['accepted_queries']=5
        with self.assertRaisesRegex(ValueError,'budget overrun'): mod.replay_adaptive(p,write=False)
    def test_evaluator_only_disclosure_rejected(self):
        p=copy.deepcopy(self.p); p['feedback_channels'][2]['agent_disclosed']=True
        with self.assertRaisesRegex(ValueError,'disclosure'): mod.replay_adaptive(p,write=False)
    def test_unrecorded_seed_reuse_rejected(self):
        p=copy.deepcopy(self.p); p['adaptive_redteam_cases'][2]['seed_reuse_recorded']=False
        with self.assertRaisesRegex(ValueError,'seed reuse'): mod.replay_adaptive(p,write=False)
    def test_best_only_reporting_rejected(self):
        p=copy.deepcopy(self.p); p['adaptive_redteam_cases'][4]['current_outcome']=.9
        with self.assertRaisesRegex(ValueError,'current and best-only'): mod.replay_adaptive(p,write=False)

if __name__=='__main__': unittest.main()

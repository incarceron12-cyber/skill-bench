from __future__ import annotations
import importlib.util,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];P=ROOT/"pilots/delayed-obligation-heldout-v2"
def load_module():
 spec=importlib.util.spec_from_file_location("delayed_v2",P/"run_study.py")
 if spec is None or spec.loader is None:raise RuntimeError(P/"run_study.py")
 mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
class DelayedObligationHeldoutV2Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.m=load_module()
 def test_four_unseen_forms_cross_complete_matrix(self):
  scenarios=self.m.load(self.m.SCENARIOS)["scenarios"];self.assertEqual(4,len(scenarios));self.assertEqual(2,len({s["work_shape"] for s in scenarios}))
  p=self.m.load(self.m.PROTOCOL);self.assertEqual(12,len(p["schedule"]["rows"]));self.assertEqual(12,len({(x["scenario_id"],x["condition_id"]) for x in p["schedule"]["rows"]}))
 def test_primary_perfect_and_mutation_canaries(self):
  r=self.m.calibration();self.assertTrue(r["passed"]);self.assertTrue(r["obligation_primary_independence"]);self.assertEqual(9,len(r["primary_cases"]));self.assertTrue(all(x["passed"] for x in r["primary_cases"]))
 def test_obligation_failure_branches(self):
  r=self.m.calibration();self.assertTrue(all(x["passed"] for x in r["obligation_cases"]));self.assertEqual(6,len({x["observed"] for x in r["obligation_cases"]}))
 def test_harness_channel_flow_not_state_proxy(self):
  s=self.m.load(self.m.SCENARIOS)["scenarios"][0];e1=self.m.harness_event(2,s,"neutral_interrupt",False);e2=self.m.harness_event(2,s,"neutral_interrupt",True)
  self.assertFalse(e1["available"]);self.assertIsNone(e1["returned"]);self.assertTrue(e2["available"]);self.assertEqual(s["obligation"]["update"],e2["returned"])
  p=self.m.load(self.m.PROTOCOL);self.assertEqual("unobserved",p["channel_instrumentation"]["encoding"]);self.assertEqual("unobserved",p["channel_instrumentation"]["adoption"])
 def test_non_oracle_treatments_do_not_disclose_current_action(self):
  s=self.m.load(self.m.SCENARIOS)["scenarios"][0]
  self.assertNotIn(s["obligation"]["updated_id"],self.m.treatment("neutral_interrupt",3,s));self.assertNotIn(s["obligation"]["updated_id"],self.m.treatment("channel_hint",3,s));self.assertIn(s["obligation"]["updated_id"],self.m.treatment("oracle_reminder",3,s))
 def test_claim_ceiling_and_preflight(self):
  p=self.m.load(self.m.PROTOCOL);self.assertTrue(all(v is False for v in p["claim_boundaries"].values()));self.assertTrue(p["reporting"]["no_shape_pooling"]);self.assertTrue(p["reporting"]["no_condition_pooling"])
  r=self.m.preflight(False);self.assertTrue(r["passed"]);self.assertEqual(0,r["model_calls"])
if __name__=="__main__":unittest.main()

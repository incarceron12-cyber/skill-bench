from __future__ import annotations
import importlib.util,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];P=ROOT/"pilots/delayed-obligation-dual-task"
def load():
 spec=importlib.util.spec_from_file_location("delayed",P/"run_study.py");mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
class DelayedObligationDualTaskTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.m=load()
 def test_calibration_replays_all_failure_stages(self):
  r=self.m.calibration();self.assertTrue(r["passed"]);self.assertEqual(8,len(r["results"]));self.assertEqual(7,len({x["observed"] for x in r["results"]}))
 def test_scenarios_have_public_basis_update_lure_and_primary_work(self):
  for s in self.m.load(self.m.SCENARIOS)["scenarios"]:
   self.assertTrue(s["obligation"]["original_instruction"]);self.assertTrue(s["obligation"]["update"]);self.assertEqual(s["obligation"]["original_id"],s["obligation"]["lure_id"]);self.assertTrue(s["primary"]["required_source_ids"])
 def test_treatments_do_not_leak_oracle_except_declared_arm(self):
  s=self.m.load(self.m.SCENARIOS)["scenarios"][0]
  self.assertNotIn(s["obligation"]["updated_id"],self.m.treatment("neutral_interrupt",3,s,False))
  self.assertNotIn(s["obligation"]["updated_id"],self.m.treatment("channel_hint",3,s,False))
  self.assertIn(s["obligation"]["updated_id"],self.m.treatment("oracle_reminder",3,s,False))
 def test_claim_ceiling_and_protocol_matrix(self):
  p=self.m.load(self.m.PROTOCOL);self.assertTrue(all(v is False for v in p["claim_boundaries"].values()));self.assertEqual(6,len(p["schedule"]["rows"]));self.assertTrue(p["reporting"]["no_shape_pooling"])
 def test_preflight_passes_without_model_calls(self):
  r=self.m.preflight(False);self.assertTrue(r["passed"]);self.assertEqual(0,r["model_calls"])
if __name__=="__main__":unittest.main()

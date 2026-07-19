import importlib.util
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PILOT=ROOT/"pilots/self-inspection-repair-v2"
def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

class SelfInspectionRepairV2FreezeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pre=load_module("repair_v2_preflight",PILOT/"preflight.py")
        cls.oa=load_module("repair_v2_oa",PILOT/"checkers/observer_a.py")
        cls.ob=load_module("repair_v2_ob",PILOT/"checkers/observer_b.py")
        cls.protocol=json.loads((PILOT/"protocol.json").read_text())
        cls.cases=json.loads((PILOT/"fixtures/calibration.json").read_text())["cases"]
    def test_preflight_passes_without_calls(self):
        r=self.pre.run(check_paths=True,write=False);self.assertEqual("PASS",r["status"]);self.assertEqual((0,0,0),(r["model_calls"],r["provider_calls"],r["repair_rows_executed"]))
    def test_three_new_shapes_two_strata(self):
        self.assertEqual(3,len({t["shape"] for t in self.protocol["tasks"]}))
        for family in {t["family"] for t in self.protocol["tasks"]}:
            self.assertEqual({"near_threshold_single_locus","multi_locus_collateral_risk"},{t["defect_stratum"] for t in self.protocol["tasks"] if t["family"]==family})
    def test_repetition_and_equal_envelope(self):
        self.assertEqual(150,len(self.protocol["assignments"]));self.assertTrue(all(a["attempts_executed"]==0 for a in self.protocol["assignments"]))
        for field in ("tool_id","harness_id","model_id","provider_id","budget_id"): self.assertEqual(1,len({c[field] for c in self.protocol["conditions"]}))
    def test_observers_independently_agree_on_mutations(self):
        for c in self.cases:
            a=self.oa.evaluate(c["family"],c["candidate"],c["view_status"],c["transform_status"]);b=self.ob.evaluate(c["family"],c["candidate"],c["view_status"],c["transform_status"])
            self.assertEqual(c["expected"],self.pre.adjudicate(a,b)["terminal_state"],c["case_id"])
    def test_disagreement_fails_closed(self):
        got=self.pre.adjudicate({"terminal_state":"passed","endpoint":True,"collateral":True},{"terminal_state":"criterion_fail","endpoint":False,"collateral":True});self.assertEqual("observer_invalid",got["terminal_state"]);self.assertIsNone(got["endpoint"])
    def test_calibration_is_not_floor_or_ceiling(self):
        states=[c["expected"] for c in self.cases];f=states.count("passed")/len(states);self.assertGreater(f,0.15);self.assertLess(f,0.85)
    def test_claim_ceiling_and_cost_stop(self):
        self.assertFalse(any(self.protocol["claim_ceiling"].values()));self.assertTrue(self.protocol["budget"]["stop_before_spend_without_execution_authorization"])
if __name__=="__main__": unittest.main()

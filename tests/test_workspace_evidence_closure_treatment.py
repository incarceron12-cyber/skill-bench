from __future__ import annotations
import importlib.util,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];PATH=ROOT/"pilots/workspace-evidence-closure-treatment-v1/run_study.py"
spec=importlib.util.spec_from_file_location("wec_treatment",PATH);assert spec and spec.loader;mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
class WorkspaceClosureTreatmentTests(unittest.TestCase):
 def test_calibration_mutations(self):
  r=mod.calibration();self.assertTrue(r["passed"]);self.assertEqual(len(r["cases"]),5)
 def test_record_omission_and_new_error(self):
  omission=mod.grade("record",{"owner":"North team","deadline":"2026-08-15","decision":"conditional approval","caveat":"Approval is conditional on legal review."});self.assertFalse(omission["independent_correctness"]);self.assertEqual(omission["obligation_coverage"]["passed"],4)
  bad=mod.grade("record",{"owner":"South team","deadline":"2026-08-15","budget_usd":12500,"decision":"conditional approval","caveat":"Approval is conditional on legal review."});self.assertEqual(bad["newly_introduced_errors"],1)
 def test_memo_stale_decision_is_severe(self):
  g=mod.grade("memo","# Delta migration handoff\nContact: Priya Shah\nDecision: Proceed with migration.\nThe rollout is ready.\n");self.assertTrue(g["severe_defect"]);self.assertEqual(g["newly_introduced_errors"],1)
 def test_protocol_matrix_and_claim_ceiling(self):
  p=json.loads((PATH.parent/"protocol.json").read_text());self.assertEqual(len(p["schedule"]),8);self.assertFalse(any(p["claim_boundaries"].values()))
if __name__=="__main__":unittest.main()

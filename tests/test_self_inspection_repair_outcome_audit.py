import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/audit_self_inspection_repair_v1_outcomes.py"
SPEC = importlib.util.spec_from_file_location("repair_outcome_audit", SCRIPT)
assert SPEC and SPEC.loader
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class SelfInspectionRepairOutcomeAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = AUDIT.run_audit()

    def test_all_commit_and_replay_gates_pass(self):
        self.assertEqual(self.report["status"], "PASS")
        self.assertTrue(all(self.report["gates"].values()))
        self.assertEqual(self.report["retained_inventory"]["file_count"], 135)
        self.assertEqual(len(self.report["assignment_audits"]), 12)

    def test_audit_is_zero_call_and_preserves_strict_ceiling(self):
        self.assertEqual(self.report["model_calls"], 0)
        self.assertEqual(self.report["provider_calls"], 0)
        self.assertEqual(self.report["repair_rows_executed"], 0)
        self.assertFalse(any(self.report["claim_ceiling"].values()))

    def test_saturation_blocks_treatment_discrimination(self):
        discrimination = self.report["instrument_discrimination"]
        self.assertEqual(discrimination["repair_cells"], 10)
        self.assertEqual(discrimination["repair_cells_passed"], 10)
        self.assertTrue(discrimination["saturated_repair_endpoint"])
        self.assertTrue(all(
            not contrast["outcome_distinguishable_from_retry"]
            for contrast in discrimination["retry_contrasts"].values()
        ))
        structured_groups = discrimination["identical_final_artifact_groups"]["structured-allocation-v1"]
        self.assertEqual(len(structured_groups), 1)
        self.assertEqual(len(structured_groups[0]["conditions"]), 5)

    def test_stop_decision_has_minimum_prospective_design(self):
        decision = self.report["decision"]
        self.assertTrue(decision["action"].startswith("STOP_CURRENT_INSTRUMENT"))
        self.assertEqual(set(decision["minimum_redesign"]), {
            "new_task_diversity", "defect_difficulty", "observer_variation",
            "repetitions", "predeclared_estimand",
        })


if __name__ == "__main__":
    unittest.main()

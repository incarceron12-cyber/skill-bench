import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDITOR = ROOT / "scripts/audit_self_inspection_repair_v2_freeze.py"


def load_module():
    spec = importlib.util.spec_from_file_location("repair_v2_independent_audit", AUDITOR)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class SelfInspectionRepairV2IndependentAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.auditor = load_module()
        cls.report = cls.auditor.run(cls.auditor.DEFAULT_COMMIT)

    def test_exact_candidate_passes_all_gates_without_calls(self):
        self.assertEqual("PASS", self.report["status"])
        self.assertTrue(all(self.report["gates"].values()))
        self.assertEqual([], self.report["errors"])
        self.assertEqual(0, self.report["attempt_ledger"]["model_calls"])
        self.assertEqual(0, self.report["attempt_ledger"]["provider_calls"])
        self.assertEqual(0, self.report["attempt_ledger"]["repair_rows_executed"])

    def test_full_inventory_assignment_and_calibration_replay(self):
        self.assertEqual(30, self.report["inventory"]["bound_files_read"])
        self.assertEqual(150, self.report["assignment_summary"]["count"])
        self.assertEqual(48, self.report["calibration"]["cases"])
        self.assertEqual(0, self.report["calibration"]["observer_disagreements"])
        self.assertEqual(0.25, self.report["calibration"]["pass_fraction"])

    def test_disagreement_and_isolation_fail_closed(self):
        self.assertEqual("observer_invalid", self.report["observer_disagreement_canary"]["adjudicated"]["terminal_state"])
        self.assertEqual("PASS", self.report["zero_call_isolation_canary"]["status"])
        self.assertIn("no execution launcher exists", self.report["zero_call_isolation_canary"]["claim_limit"])


if __name__ == "__main__":
    unittest.main()

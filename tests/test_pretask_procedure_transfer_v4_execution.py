from __future__ import annotations

import hashlib
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "pilots/pretask-procedure-transfer-v4"
spec = importlib.util.spec_from_file_location("v4_execution", HERE / "execute_matrix.py")
assert spec and spec.loader
execution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(execution)


class PretaskProcedureTransferV4ExecutionTests(unittest.TestCase):
    def test_hindsight_packages_are_hash_frozen_and_bounded(self):
        manifest = json.loads((HERE / "hindsight-freeze-manifest.json").read_text())
        self.assertTrue(manifest["authored_before_executor_attempts"])
        self.assertTrue(all(value is False for value in manifest["claim_ceiling"].values()))
        self.assertIn("public task", manifest["authorship_basis"])
        self.assertIn("private endpoint", manifest["authorship_basis"])
        for row in manifest["components"]:
            path = ROOT / row["path"]
            self.assertEqual(row["sha256"], hashlib.sha256(path.read_bytes()).hexdigest())
            self.assertEqual(row["bytes"], path.stat().st_size)
            package = json.loads(path.read_text())
            context = package["generation_context"]
            self.assertFalse(context["source_visible"])
            self.assertFalse(context["private_endpoint_visible"])
            self.assertFalse(context["outcome_visible"])
            self.assertTrue(all(value is False for value in package["claim_ceiling"].values()))

    def test_all_32_frozen_assignments_have_declared_support(self):
        rows = json.loads((HERE / "assignments.json").read_text())["rows"]
        self.assertEqual(list(range(1, 33)), [row["schedule_index"] for row in rows])
        expected_counts = {
            "generated_package": 1, "no_package_no_raw": 0, "equal_budget_raw": 1,
            "generated_plus_raw": 2, "reference_procedure": 1,
            "cross_family_irrelevant": 1, "exactly_one_defect": 1,
            "task_conditioned_hindsight_upper_bound": 1,
        }
        for row in rows:
            support = execution.support_sources(row)
            self.assertEqual(expected_counts[row["condition_id"]], len(support))
            self.assertTrue(all(path.is_file() for path, _ in support))
            self.assertLessEqual(sum(path.stat().st_size for path, _ in support), 16000)

    def test_attempt_and_claim_policy_is_fail_closed(self):
        source = (HERE / "execute_matrix.py").read_text()
        self.assertIn("retry forbidden", source)
        self.assertIn("if not report[\"service_valid\"] or not report[\"environment_valid\"]", source)
        self.assertEqual({False}, set(execution.CLAIMS.values()))

    def test_retained_execution_is_complete_and_strict_when_present(self):
        report_path = HERE / "execution-report.json"
        if not report_path.exists():
            self.skipTest("matrix has not been executed")
        report = json.loads(report_path.read_text())
        attempted = report["denominators"]["attempted"]
        self.assertEqual(attempted, report["attempts"]["executor"])
        self.assertEqual(0, report["attempts"]["repair"])
        self.assertEqual(0, report["attempts"]["retry"])
        self.assertEqual(attempted, len(report["exact_cells"]))
        self.assertTrue(all(value is False for value in report["claim_ceiling"].values()))
        if report["status"] == "complete":
            self.assertEqual(32, attempted)
            self.assertEqual(32, report["denominators"]["service_valid"])
            self.assertEqual(32, report["denominators"]["environment_valid"])


if __name__ == "__main__":
    unittest.main()
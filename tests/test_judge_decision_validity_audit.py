from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "pilots/judge-decision-validity-audit/audit.py"
SPEC = importlib.util.spec_from_file_location("judge_decision_audit", MODULE_PATH)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)


class JudgeDecisionValidityAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = json.loads(audit.FIXTURE.read_text(encoding="utf-8"))
        cls.report = audit.build_report()

    def test_extreme_task_size_and_distinct_aggregation_estimands(self) -> None:
        rows = self.report["policies"]["fail_closed"]["tasks"]
        sizes = [row["leaf_count"] for row in rows]
        self.assertGreaterEqual(max(sizes) / min(sizes), 10)
        summary = self.report["policies"]["fail_closed"]["summary"]
        self.assertNotAlmostEqual(summary["pooled_leaf_class_macro_f1"], summary["equal_task_class_macro_f1"])

    def test_reports_score_rank_decision_and_consequential_errors(self) -> None:
        summary = self.report["policies"]["fail_closed"]["summary"]
        self.assertGreater(summary["mean_root_absolute_error"], 0)
        self.assertGreater(summary["mean_absolute_rank_change"], 0)
        self.assertTrue(summary["threshold_flip_task_ids"])
        self.assertGreater(summary["consequential_confusion"]["fn"] + summary["consequential_confusion"]["fp"], 0)

    def test_invalid_policies_change_decisions_without_erasing_invalidity(self) -> None:
        closed = self.report["policies"]["fail_closed"]
        opened = self.report["policies"]["fail_open"]
        abstain = self.report["policies"]["abstain"]
        self.assertNotEqual(closed["summary"]["threshold_flip_task_ids"], opened["summary"]["threshold_flip_task_ids"])
        self.assertEqual(abstain["summary"]["abstained_task_ids"], ["invalid_boundary"])
        for policy in (closed, opened, abstain):
            row = next(item for item in policy["tasks"] if item["task_id"] == "invalid_boundary")
            self.assertEqual(row["invalid_count"], 1)

    def test_clustered_bootstrap_is_deterministic_and_task_scoped(self) -> None:
        first = self.report["policies"]["fail_closed"]["clustered_uncertainty"]
        second = audit.build_report()["policies"]["fail_closed"]["clustered_uncertainty"]
        self.assertEqual(first, second)
        self.assertEqual(first["method"], "task_cluster_nonparametric_bootstrap")
        self.assertEqual(first["replicates"], 1000)

    def test_malformed_predictions_and_weak_size_contrast_are_rejected(self) -> None:
        invalid = copy.deepcopy(self.fixture)
        invalid["tasks"][0]["criterion_groups"][0]["valid"] = False
        with self.assertRaises(audit.AuditError):
            audit.validate_fixture(invalid)
        no_contrast = copy.deepcopy(self.fixture)
        no_contrast["tasks"][0]["criterion_groups"] = no_contrast["tasks"][1]["criterion_groups"]
        with self.assertRaises(audit.AuditError):
            audit.validate_fixture(no_contrast)

    def test_report_is_provenance_bound_and_fresh(self) -> None:
        self.assertEqual(self.report["provenance"]["fixture_sha256"], audit.sha256(audit.FIXTURE))
        expected = json.dumps(self.report, indent=2, sort_keys=True) + "\n"
        self.assertEqual(audit.REPORT.read_text(encoding="utf-8"), expected)


if __name__ == "__main__":
    unittest.main()

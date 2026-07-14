from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "pilots/dependency-gated-score-replay/replay.py"
SPEC = importlib.util.spec_from_file_location("dependency_gated_replay", MODULE_PATH)
assert SPEC and SPEC.loader
replay = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(replay)


class DependencyGatedReplayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = json.loads(replay.FIXTURE.read_text(encoding="utf-8"))
        cls.report = replay.build_report()
        cls.rows = {row["case_id"]: row for row in cls.report["cases"]}

    def test_pinned_released_rubric_identity_and_topology(self) -> None:
        source = self.report["source_rubric"]
        self.assertEqual(source["official_commit"], "51052cede8cc608f95bb00346635e03759013e5a")
        self.assertEqual(source["node_count"], 100)
        self.assertEqual(source["leaf_count"], 77)
        self.assertEqual(source["all_supported_recursive_score"], 1.0)

    def test_required_dependency_shapes_have_expected_effects(self) -> None:
        self.assertEqual(self.rows["missing_prerequisite"]["compensatory_progress"], 0.8)
        self.assertEqual(self.rows["missing_prerequisite"]["dependency_gated_progress"], 0.0)
        self.assertEqual(self.rows["conjunction_incomplete"]["dependency_gated_progress"], 0.2)
        self.assertTrue(self.rows["accepted_alternative"]["gated_completion_claim_pass"])
        self.assertEqual(self.rows["fanout_upstream_failure"]["dependency_gated_progress"], 0.0)

    def test_invalid_and_insufficient_fail_closed_without_erasing_state(self) -> None:
        invalid = self.rows["invalid_observation"]
        insufficient = self.rows["insufficient_evidence"]
        self.assertFalse(invalid["headline_eligible"])
        self.assertEqual(invalid["invalid_criterion_ids"], ["execution"])
        self.assertFalse(insufficient["headline_eligible"])
        self.assertEqual(insufficient["insufficient_evidence_criterion_ids"], ["execution"])
        self.assertTrue(invalid["compensatory_threshold_pass"])
        self.assertFalse(invalid["gated_completion_claim_pass"])

    def test_not_applicable_is_excluded_and_renormalized(self) -> None:
        row = self.rows["not_applicable"]
        self.assertEqual(row["compensatory_progress"], 1.0)
        self.assertEqual(row["dependency_gated_progress"], 1.0)
        self.assertEqual(row["not_applicable_criterion_ids"], ["optional_gpu"])

    def test_report_preserves_evidence_and_exhibits_threshold_and_rank_changes(self) -> None:
        self.assertGreaterEqual(len(self.report["summary"]["threshold_flip_case_ids"]), 5)
        self.assertTrue(self.report["summary"]["rank_change_case_ids"])
        for row in self.report["cases"]:
            self.assertTrue(all(item["evidence"] for item in row["criterion_evidence"]))

    def test_unknown_dependency_and_cycle_are_rejected(self) -> None:
        bad = copy.deepcopy(self.fixture)
        bad["cases"][0]["criteria"][1]["depends_on"] = {"criterion": "absent"}
        with self.assertRaises(replay.ReplayError):
            replay.validate_fixture(bad)
        cycle = copy.deepcopy(self.fixture["cases"][0])
        cycle["criteria"][0]["depends_on"] = {"criterion": "run"}
        with self.assertRaises(replay.ReplayError):
            replay.evaluate_case(cycle, self.fixture["threshold"])

    def test_committed_report_is_deterministic(self) -> None:
        expected = json.dumps(self.report, indent=2, sort_keys=True) + "\n"
        self.assertEqual(replay.REPORT.read_text(encoding="utf-8"), expected)


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

from scripts.run_lh_ablation_preflight import build

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "pilots/lh-skill-adoption"
REPORT = PILOT / "ablation/preflight-report.json"
SCHEMA = ROOT / "schemas/ablation-preflight.schema.json"
EXPECTED = {
    "no_skill_independent_rubric",
    "no_skill_shared_rubric",
    "public_skill_independent_rubric",
    "public_skill_shared_rubric",
}


class LhAblationPreflightTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        build()
        cls.report = json.loads(REPORT.read_text(encoding="utf-8"))

    def test_report_validates_and_is_explicitly_not_capability_evidence(self) -> None:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator(schema, format_checker=FormatChecker()).validate(self.report)
        self.assertFalse(self.report["capability_evidence"])
        self.assertEqual("task_only_fixture_replay", self.report["run_kind"])
        self.assertEqual("builder_authored_calibration_fixture_not_agent_output", self.report["fixture_source"]["authorship"])

    def test_exact_matched_two_by_two_is_materialized(self) -> None:
        conditions = {item["condition_id"]: item for item in self.report["conditions"]}
        self.assertEqual(EXPECTED, set(conditions))
        for condition_id, condition in conditions.items():
            with self.subTest(condition=condition_id):
                self.assertEqual(condition_id.startswith("no_skill_"), condition["skill"] is None)
                expected_rubric = (
                    "lh-adoption-independent-claim-rubric"
                    if condition_id.endswith("independent_rubric")
                    else "lh-adoption-shared-rubric"
                )
                self.assertEqual(expected_rubric, condition["rubric"]["component_id"])
        self.assertTrue(all(self.report["matched_controls"][key] for key in (
            "same_task_hash", "same_fixture_hashes", "same_tool_hash", "same_harness_hash", "same_feedback_policy_hash"
        )))

    def test_every_materialized_file_matches_recorded_hash_and_size(self) -> None:
        refs = [self.report["bundle_source"], self.report["fixture_source"]["matrix"], self.report["fixture_source"]["memo"]]
        for condition in self.report["conditions"]:
            refs.extend([condition["matrix"], condition["memo"]])
            refs.extend({"path": run["result_path"], "sha256": run["result_sha256"]} for run in condition["grader_runs"])
        for ref in refs:
            path = ROOT / ref["path"]
            with self.subTest(path=path):
                self.assertTrue(path.is_file())
                self.assertEqual(ref["sha256"], hashlib.sha256(path.read_bytes()).hexdigest())
                if "bytes" in ref:
                    self.assertEqual(ref["bytes"], path.stat().st_size)

    def test_grader_selection_respects_rubric_boundary(self) -> None:
        for condition in self.report["conditions"]:
            runs = {run["grader_id"]: run for run in condition["grader_runs"]}
            self.assertEqual("passed", runs["evidence-link-grader"]["outcomes"]["evidence-provenance"])
            if condition["condition_id"].endswith("independent_rubric"):
                self.assertEqual(
                    {"contradiction-reconciliation": "passed", "causal-claim-strength": "passed"},
                    runs["independent-claim-calibrator"]["outcomes"],
                )
                self.assertEqual(["decision-operability"], condition["unexecuted_checks"])
            else:
                self.assertNotIn("independent-claim-calibrator", runs)
                self.assertEqual(
                    {"decision-operability", "contradiction-reconciliation", "causal-claim-strength"},
                    set(condition["unexecuted_checks"]),
                )

    def test_all_component_hashes_and_harness_entrypoint_are_pinned(self) -> None:
        for component in self.report["components"].values():
            path = ROOT / component["path"]
            with self.subTest(component=component["component_id"]):
                self.assertEqual(component["sha256"], hashlib.sha256(path.read_bytes()).hexdigest())
        harness = json.loads((PILOT / "ablation/fixture-replay-harness.json").read_text(encoding="utf-8"))
        entrypoint = ROOT / harness["entrypoint_path"]
        self.assertEqual(harness["entrypoint_sha256"], hashlib.sha256(entrypoint.read_bytes()).hexdigest())


if __name__ == "__main__":
    unittest.main()

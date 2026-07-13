from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/report_vendor_skill_rubric_matrix.py"
spec = importlib.util.spec_from_file_location("vendor_skill_matrix", SCRIPT)
assert spec is not None and spec.loader is not None
matrix = importlib.util.module_from_spec(spec)
spec.loader.exec_module(matrix)
PROTOCOL_PATH = ROOT / "pilots/vendor-incident-response/trials/skill-rubric-matrix-v1/protocol.json"
REPORT_PATH = ROOT / "pilots/vendor-incident-response/trials/skill-rubric-matrix-v1/matrix-report.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


class VendorSkillMatrixProtocolTests(unittest.TestCase):
    def setUp(self) -> None:
        self.protocol = load(PROTOCOL_PATH)

    def test_protocol_is_hash_bound_and_balanced(self) -> None:
        matrix.verify_protocol(self.protocol)
        counts = {condition: sum(row["skill_condition"] == condition for row in self.protocol["attempt_schedule"]) for condition in ("no_skill", "public_skill")}
        self.assertEqual({"no_skill": 3, "public_skill": 3}, counts)

    def test_condition_leakage_or_denominator_drift_fails(self) -> None:
        mutated = copy.deepcopy(self.protocol)
        mutated["attempt_schedule"][0]["skill_condition"] = "no_skill"
        with self.assertRaisesRegex(ValueError, "denominator drift"):
            matrix.verify_protocol(mutated)

    def test_hash_drift_fails(self) -> None:
        mutated = copy.deepcopy(self.protocol)
        mutated["frozen_components"][0]["sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "hash drift"):
            matrix.verify_protocol(mutated)

    def test_replacement_or_retry_fails(self) -> None:
        mutated = copy.deepcopy(self.protocol)
        mutated["attempt_schedule"][1]["replacement_for"] = mutated["attempt_schedule"][0]["attempt_id"]
        with self.assertRaisesRegex(ValueError, "replacement"):
            matrix.verify_protocol(mutated)
        mutated = copy.deepcopy(self.protocol)
        mutated["policies"]["retry_or_adaptation"] = "one retry"
        with self.assertRaisesRegex(ValueError, "policy drift"):
            matrix.verify_protocol(mutated)

    def test_claim_upgrade_fails(self) -> None:
        mutated = copy.deepcopy(self.protocol)
        mutated["claim_boundaries"]["general_skill_effect"] = True
        with self.assertRaisesRegex(ValueError, "claim upgrade"):
            matrix.verify_protocol(mutated)

    def test_independent_construction_excludes_guide(self) -> None:
        manifest = load(ROOT / "pilots/vendor-incident-response/trials/skill-rubric-matrix-v1/rubrics/independent-construction-manifest.json")
        self.assertFalse(any(path.endswith("public-procedural-guide.md") for path in manifest["allowed_inputs"]))
        self.assertTrue(any(path.endswith("public-procedural-guide.md") for path in manifest["prohibited_inputs"]))


@unittest.skipUnless(REPORT_PATH.is_file(), "prospective matrix has not executed yet")
class VendorSkillMatrixReplayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.protocol = load(PROTOCOL_PATH)
        cls.report = load(REPORT_PATH)

    def test_every_declared_attempt_retained_without_replacement(self) -> None:
        replay = matrix.build_report(self.protocol)
        self.assertEqual(self.report, replay)
        self.assertEqual(6, replay["declared_attempts"])
        self.assertEqual(6, replay["retained_attempts"])
        self.assertEqual({row["attempt_id"] for row in self.protocol["attempt_schedule"]}, {row["attempt_id"] for row in replay["attempt_rows"]})

    def test_both_rubrics_replay_on_identical_outputs_and_order_is_inert(self) -> None:
        for row in self.protocol["attempt_schedule"]:
            run = ROOT / "pilots/vendor-incident-response/trials/skill-rubric-matrix-v1/attempts" / row["attempt_id"]
            forward = matrix.grade_attempt(run, self.protocol, row["scorer_order"])
            reverse = matrix.grade_attempt(run, self.protocol, list(reversed(row["scorer_order"])))
            self.assertEqual(forward, reverse)
            self.assertEqual({"independent", "shared"}, set(forward["rubric_grades"]))

    def test_report_denominators_and_claim_ceiling(self) -> None:
        self.assertEqual(3, self.report["cells"]["no_skill"]["declared_attempts"])
        self.assertEqual(3, self.report["cells"]["public_skill"]["declared_attempts"])
        self.assertTrue(all(value is False for value in self.report["claim_boundaries"].values()))


if __name__ == "__main__":
    unittest.main()

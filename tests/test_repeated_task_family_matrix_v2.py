import hashlib
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STUDY = ROOT / "pilots/repeated-task-family-matrix/v2"
V1 = ROOT / "pilots/repeated-task-family-matrix/v1"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path: Path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_runner():
    spec = importlib.util.spec_from_file_location("repeated_matrix_v2_runner", STUDY / "run_matrix.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class RepeatedTaskFamilyMatrixV2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.protocol = load(STUDY / "protocol.json")
        cls.runner = load_runner()

    def test_frozen_protocol_has_two_unlike_families_four_forms_and_two_repeats(self):
        verification = self.runner.verify_protocol(self.protocol)
        self.assertTrue(verification["passed"], verification["errors"])
        self.assertEqual({value["family"] for value in self.protocol["forms"].values()}, {"resource_governance", "record_integrity"})
        self.assertEqual(len(self.protocol["forms"]), 4)
        for key in self.protocol["forms"]:
            self.assertEqual(sum(row["family"] + "/" + row["form"] == key for row in self.protocol["schedule"]["rows"]), 2)

    def test_all_frozen_components_resolve_and_v1_tree_is_pinned(self):
        for component in self.protocol["frozen_components"]:
            self.assertEqual(sha(STUDY / component["path"]), component["sha256"])
        self.assertTrue(self.protocol["v1_preservation"]["git_tree_at_freeze"])
        self.assertFalse(any(self.protocol["claim_boundaries"].values()))

    def test_every_accepted_label_is_publicly_disclosed(self):
        for key, form in self.protocol["forms"].items():
            expected = load(STUDY / form["authoritative_output"])
            public = (STUDY / "forms" / key / "public-task.md").read_text(encoding="utf-8")
            for label in expected["accepted_decisions"] + expected["accepted_actions"]:
                self.assertIn(f"`{label}`", public)
            self.assertEqual(len(expected["accepted_decisions"]), 3)
            self.assertEqual(len(expected["accepted_actions"]), 3)
            self.assertEqual(len(expected["near_neighbor_wrong_decisions"]), 2)
            self.assertEqual(len(expected["near_neighbor_wrong_actions"]), 2)

    def test_calibration_accepts_alternatives_and_rejects_near_neighbors(self):
        result = self.runner.calibration(self.protocol)
        self.assertTrue(result["passed"])
        self.assertEqual(len(result["cases"]), 4)
        for case in result["cases"]:
            self.assertEqual(case["accepted_decision_realizations_tested"], 3)
            self.assertEqual(case["accepted_action_realizations_tested"], 3)
            self.assertEqual(case["near_neighbor_wrong_decisions_tested"], 2)
            self.assertEqual(case["near_neighbor_wrong_actions_tested"], 2)
            self.assertTrue(all(value == "pass" for name, value in case["results"].items() if name.startswith("alternative_") or name == "canonical"))
            self.assertTrue(all(value == "fail" for name, value in case["results"].items() if name.startswith("wrong_") or name == "invalid_json"))

    def test_preflight_report_is_zero_call_and_fail_closed(self):
        report = load(STUDY / "preflight/gate-report.json")
        self.assertTrue(report["passed"])
        self.assertEqual(report["model_calls"], 0)
        self.assertTrue(report["protocol"]["v1_tree_preserved"])
        self.assertTrue(all(item["passed"] for item in report["isolation_and_leakage"]))
        self.assertTrue(report["grader_calibration_and_mutation"]["passed"])


if __name__ == "__main__":
    unittest.main()

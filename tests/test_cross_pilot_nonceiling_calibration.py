import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAL = ROOT / "pilots/cross-pilot-nonceiling-skill-study/v1/calibration"
MODULE_PATH = CAL / "grade_calibration.py"
spec = importlib.util.spec_from_file_location("nonceiling_calibration", MODULE_PATH)
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class CrossPilotNonceilingCalibrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads((CAL / "case-manifest.json").read_text())
        cls.report = module.run()

    def test_manifest_and_hashes_are_valid(self):
        self.assertEqual([], module.validate_manifest(self.manifest))
        self.assertEqual(10, len(self.manifest["records"]))

    def test_rejects_artifact_hash_drift(self):
        mutated = copy.deepcopy(self.manifest)
        mutated["records"][0]["artifacts"][next(iter(mutated["records"][0]["artifacts"]))] = "0" * 64
        self.assertTrue(any("hash drift" in e for e in module.validate_manifest(mutated)))

    def test_rejects_claim_upgrade(self):
        mutated = copy.deepcopy(self.manifest)
        mutated["claim_boundaries"]["capability"] = True
        self.assertIn("claim ceiling upgrade", module.validate_manifest(mutated))

    def test_valid_and_alternative_paths_pass_both_rubrics(self):
        for result in self.report["results"]:
            if result["case_type"] in {"positive", "alternative_valid"}:
                self.assertEqual("pass", result["actual"])
                self.assertEqual({1.0}, {g["score"] for g in result["grades"].values()})

    def test_shortcut_and_invalid_fail_both_rubrics(self):
        for result in self.report["results"]:
            if result["case_type"] in {"shortcut", "abstention_or_invalid"}:
                self.assertEqual({"fail"}, {g["classification"] for g in result["grades"].values()})

    def test_minimally_wrong_exposes_frozen_shared_rubric_blind_spot(self):
        result = next(r for r in self.report["results"] if r["cluster"] == "lh" and r["case_type"] == "minimally_wrong")
        self.assertEqual("fail", result["grades"]["independent"]["classification"])
        self.assertEqual("pass", result["grades"]["shared"]["classification"])
        self.assertFalse(self.report["passed"])
        self.assertEqual(["non-discrimination: lh/shared"], self.report["errors"])

    def test_failed_gate_prohibits_model_calls(self):
        persisted = json.loads((CAL / "calibration-report.json").read_text())
        self.assertFalse(persisted["passed"])
        self.assertEqual(0, persisted["model_calls"])

    def test_zero_call_canaries_pass_all_views(self):
        report = json.loads((CAL.parent / "preflight/canary-report.json").read_text())
        self.assertTrue(report["passed"])
        self.assertEqual(0, report["model_calls"])
        self.assertEqual(6, len(report["reports"]))
        for row in report["reports"]:
            self.assertTrue(row["passed"])
            self.assertTrue(all(row["observed"]["prohibited_denied"].values()))
            self.assertTrue(row["observed"]["outside_write_denied"])


if __name__ == "__main__":
    unittest.main()

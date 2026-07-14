import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V2 = ROOT / "pilots/cross-pilot-nonceiling-skill-study/v2"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


protocol_module = load_module("nonceiling_v2_protocol", V2 / "validate_protocol.py")
calibration_module = load_module("nonceiling_v2_calibration", V2 / "calibration/grade_calibration.py")
PROTOCOL = json.loads((V2 / "protocol.json").read_text())
MANIFEST = json.loads((V2 / "calibration/case-manifest.json").read_text())


class CrossPilotNonceilingV2Tests(unittest.TestCase):
    def test_protocol_and_new_opaque_schedule_are_valid(self):
        self.assertEqual([], protocol_module.validate(PROTOCOL, check_paths=True))
        self.assertEqual(8, len(PROTOCOL["attempt_schedule"]))
        self.assertTrue(all(row["attempt_id"].startswith("n2-") for row in PROTOCOL["attempt_schedule"]))
        v1 = json.loads((V2.parent / "v1/protocol.json").read_text())
        self.assertTrue(
            {row["attempt_id"] for row in PROTOCOL["attempt_schedule"]}.isdisjoint(
                row["attempt_id"] for row in v1["attempt_schedule"]
            )
        )

    def test_calibration_passes_and_shared_lh_detects_public_marker_omission(self):
        report = calibration_module.run()
        self.assertTrue(report["passed"], report["errors"])
        result = next(
            row for row in report["results"]
            if row["cluster"] == "lh" and row["case_type"] == "minimally_wrong"
        )
        shared = result["grades"]["shared"]
        self.assertEqual("fail", shared["classification"])
        marker = next(x for x in shared["observations"] if x["criterion_id"] == "guide-prospective-number-marking")
        self.assertFalse(marker["passed"])

    def test_positive_and_alternative_paths_still_pass_every_rubric(self):
        for result in calibration_module.run()["results"]:
            if result["case_type"] in {"positive", "alternative_valid"}:
                self.assertEqual({"pass"}, {grade["classification"] for grade in result["grades"].values()})

    def test_frozen_manifest_rejects_hash_and_claim_mutations(self):
        changed = copy.deepcopy(MANIFEST)
        changed["records"][0]["artifacts"]["recommendation.md"] = "0" * 64
        self.assertTrue(any("hash drift" in error for error in calibration_module.validate_manifest(changed)))
        changed = copy.deepcopy(MANIFEST)
        changed["claim_boundaries"]["skill_effect"] = True
        self.assertIn("claim ceiling upgrade", calibration_module.validate_manifest(changed))

    def test_protocol_rejects_condition_denominator_and_claim_drift(self):
        changed = copy.deepcopy(PROTOCOL)
        current = changed["attempt_schedule"][0]["skill_condition"]
        changed["attempt_schedule"][0]["skill_condition"] = "public_skill" if current == "no_skill" else "no_skill"
        self.assertTrue(any("two attempts" in error for error in protocol_module.validate(changed)))
        changed = copy.deepcopy(PROTOCOL)
        changed["policies"]["declared_attempt_denominator"] = 7
        self.assertTrue(any("denominator" in error for error in protocol_module.validate(changed)))
        changed = copy.deepcopy(PROTOCOL)
        changed["claim_boundaries"]["professional_validity"] = True
        self.assertTrue(any("claim ceilings" in error for error in protocol_module.validate(changed)))

    def test_persisted_zero_call_evidence_is_complete(self):
        calibration = json.loads((V2 / "calibration/calibration-report.json").read_text())
        canaries = json.loads((V2 / "preflight/canary-report.json").read_text())
        self.assertTrue(calibration["passed"])
        self.assertEqual(0, calibration["model_calls"])
        self.assertTrue(canaries["passed"])
        self.assertEqual(0, canaries["model_calls"])
        self.assertEqual(6, len(canaries["reports"]))


if __name__ == "__main__":
    unittest.main()
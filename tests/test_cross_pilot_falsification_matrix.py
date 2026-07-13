import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "pilots" / "cross-pilot-falsification-matrix"
SPEC = importlib.util.spec_from_file_location("cross_pilot_matrix", HERE / "replay.py")
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class CrossPilotFalsificationMatrixTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads((HERE / "coverage-manifest.json").read_text())

    def test_frozen_matrix_replays_and_blocks_promotion(self):
        report = MODULE.replay(copy.deepcopy(self.manifest), write=False)
        self.assertTrue(report["integrity_valid"], report["errors"])
        self.assertEqual(6, report["summary"]["families"])
        self.assertEqual(29, report["summary"]["rows"])
        self.assertEqual({"insufficient_evidence": 3, "missing": 2, "satisfied": 24}, report["summary"]["coverage_status_counts"])
        self.assertEqual("blocked", report["promotion_decision"])
        self.assertEqual(3, report["summary"]["promotion_ready_families"])
        self.assertTrue(all(value is False for value in report["claim_boundaries"].values()))

    def test_checked_in_report_is_exact_replay(self):
        expected = MODULE.replay(write=False)
        observed = json.loads((HERE / "report.json").read_text())
        self.assertEqual(expected, observed)

    def test_hash_drift_fails_closed(self):
        manifest = copy.deepcopy(self.manifest)
        manifest["artifacts"][0]["sha256"] = "0" * 64
        report = MODULE.replay(manifest, write=False)
        self.assertFalse(report["integrity_valid"])
        self.assertTrue(any("hash mismatch" in error for error in report["errors"]))

    def test_broken_pointer_fails_closed(self):
        manifest = copy.deepcopy(self.manifest)
        manifest["rows"][0]["evidence"]["pointer"] = "/not/a/real/pointer"
        report = MODULE.replay(manifest, write=False)
        self.assertFalse(report["integrity_valid"])
        self.assertTrue(any("pointer mismatch" in error for error in report["errors"]))

    def test_expected_label_cannot_be_retrofitted(self):
        manifest = copy.deepcopy(self.manifest)
        manifest["rows"][0]["expected_observation"] = "ordinary_untrusted_source"
        report = MODULE.replay(manifest, write=False)
        self.assertFalse(report["integrity_valid"])
        self.assertTrue(any("differs from frozen expected" in error for error in report["errors"]))

    def test_unsupported_claim_upgrade_is_rejected(self):
        manifest = copy.deepcopy(self.manifest)
        row = next(item for item in manifest["rows"] if item["row_id"] == "cl-workflow-family")
        row["expected_observation"] = "supported"
        report = MODULE.replay(manifest, write=False)
        self.assertFalse(report["integrity_valid"])
        self.assertTrue(any("unsupported claim upgrade" in error for error in report["errors"]))

    def test_missing_case_cannot_claim_evidence(self):
        manifest = copy.deepcopy(self.manifest)
        row = next(item for item in manifest["rows"] if item["row_id"] == "sd-title-only")
        row["evidence"] = {"artifact_id": "initial-state-cases", "pointer": "/cases/0/expected"}
        report = MODULE.replay(manifest, write=False)
        self.assertFalse(report["integrity_valid"])
        self.assertTrue(any("must not claim evidence" in error for error in report["errors"]))


if __name__ == "__main__":
    unittest.main()

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "pilots" / "disposition-realization-crosswalk" / "v1"
SPEC = importlib.util.spec_from_file_location("disposition_crosswalk_replay", PILOT / "replay.py")
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class DispositionRealizationCrosswalkTests(unittest.TestCase):
    def setUp(self):
        self.manifest_path = PILOT / "manifest.json"
        self.manifest = json.loads(self.manifest_path.read_text())

    def replay_temp(self, manifest):
        with tempfile.NamedTemporaryFile("w", suffix=".json", dir=PILOT, delete=False) as handle:
            json.dump(manifest, handle)
            path = Path(handle.name)
        try:
            return MODULE.replay(path)
        finally:
            path.unlink()

    def test_frozen_replay_matches_report(self):
        report = MODULE.replay(self.manifest_path)
        self.assertTrue(report["passed"])
        self.assertEqual(report["model_calls"], 0)
        self.assertEqual(
            json.dumps(report, indent=2, sort_keys=True) + "\n",
            (PILOT / "replay-report.json").read_text(),
        )
        self.assertTrue(all(row["passed"] for row in report["evidence_verification"]))

    def test_complete_two_shape_two_by_two_matrix(self):
        report = MODULE.replay(self.manifest_path)
        self.assertTrue(report["matrix"]["complete"])
        self.assertEqual(report["matrix"]["shape_count"], 2)
        self.assertEqual(
            set(report["matrix"]["observed_cells"]),
            {"proceed--valid", "proceed--invalid", "defer--valid", "defer--invalid"},
        )

    def test_layers_do_not_collapse(self):
        cases = {row["id"]: row["dimensions"] for row in MODULE.replay(self.manifest_path)["cases"]}
        self.assertEqual(cases["proceed--valid"]["boundary_judgment"], "pass")
        self.assertEqual(cases["proceed--valid"]["proceed_realization"], "pass")
        self.assertEqual(cases["proceed--valid"]["consequence"], "insufficient_evidence")
        self.assertEqual(cases["proceed--invalid"]["boundary_judgment"], "pass")
        self.assertEqual(cases["proceed--invalid"]["proceed_realization"], "fail")
        self.assertEqual(cases["defer--valid"]["boundary_judgment"], "insufficient_evidence")
        self.assertEqual(cases["defer--valid"]["handoff_construction"], "pass")
        self.assertEqual(cases["defer--valid"]["handoff_transport"], "pass")
        self.assertEqual(cases["defer--valid"]["continuation"], "pass")
        self.assertEqual(cases["defer--valid"]["observer_sufficiency"], "insufficient_evidence")

    def test_planted_wrong_recipient_and_absent_receipt_fail_separately(self):
        cases = {row["id"]: row for row in MODULE.replay(self.manifest_path)["cases"]}
        invalid = cases["defer--invalid"]
        self.assertEqual(invalid["dimensions"]["handoff_construction"], "fail")
        self.assertEqual(invalid["dimensions"]["handoff_transport"], "fail")
        self.assertEqual(invalid["dimensions"]["continuation"], "insufficient_evidence")
        self.assertEqual(invalid["dimensions"]["observer_sufficiency"], "pass")

    def test_parent_hash_drift_fails_closed(self):
        changed = copy.deepcopy(self.manifest)
        changed["evidence"]["action_output"]["sha256"] = "0" * 64
        report = self.replay_temp(changed)
        self.assertFalse(report["passed"])
        self.assertIn("one or more immutable parent hashes failed", report["errors"])
        self.assertEqual(report["cases"][0]["assertions"], [])

    def test_missing_matrix_cell_is_rejected(self):
        changed = copy.deepcopy(self.manifest)
        changed["cases"] = [case for case in changed["cases"] if case["id"] != "defer--invalid"]
        report = self.replay_temp(changed)
        self.assertFalse(report["passed"])
        self.assertTrue(any(error.startswith("matrix mismatch") for error in report["errors"]))

    def test_all_claim_boundaries_remain_false(self):
        report = MODULE.replay(self.manifest_path)
        self.assertTrue(report["claim_boundaries"])
        self.assertTrue(all(value is False for value in report["claim_boundaries"].values()))


if __name__ == "__main__":
    unittest.main()

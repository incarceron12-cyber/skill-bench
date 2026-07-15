from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "pilots/artifact-transition-conformance/v0.2-temporal"
FIXTURE = PACKAGE / "fixture.json"
spec = importlib.util.spec_from_file_location("temporal_validate", PACKAGE / "validate.py")
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class TemporalArtifactConformanceTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(FIXTURE.read_text())

    def replay(self, data=None):
        return module.replay(data or self.data, PACKAGE)

    def test_eleven_cases_and_claim_boundary(self):
        report = self.replay()
        self.assertEqual(11, report["cases_replayed"])
        self.assertTrue(all(value is False for value in report["claim_boundary"].values()))

    def test_boundary_and_alternate_sequence(self):
        rows = {row["case_id"]: row for row in self.replay()["results"]}
        self.assertEqual("pass", rows["just-inside-tolerance"]["observers"]["rendered_window"]["outcome"])
        self.assertEqual("fail", rows["just-outside-tolerance"]["observers"]["rendered_window"]["outcome"])
        self.assertEqual("pass", rows["legitimate-alternate-sequence"]["observers"]["native_structure"]["outcome"])

    def test_missing_views_fail_closed_with_typed_outcomes(self):
        rows = {row["case_id"]: row for row in self.replay()["results"]}
        self.assertEqual("insufficient_evidence", rows["missing-source-view"]["observers"]["source_lineage"]["outcome"])
        self.assertEqual("insufficient_evidence", rows["missing-native-view"]["observers"]["native_structure"]["outcome"])
        self.assertEqual("insufficient_evidence", rows["missing-render-view"]["observers"]["rendered_window"]["outcome"])

    def test_representation_specific_failures(self):
        rows = {row["case_id"]: row for row in self.replay()["results"]}
        self.assertEqual("invalid_artifact", rows["plausible-render-broken-editability"]["observers"]["native_structure"]["outcome"])
        self.assertEqual("pass", rows["plausible-render-broken-editability"]["observers"]["rendered_window"]["outcome"])
        self.assertEqual("invalid_artifact", rows["export-hash-mismatch"]["observers"]["export_identity"]["outcome"])

    def test_mutated_evidence_hash_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["cases"][0]["views"]["native"]["sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "evidence hash mismatch"):
            self.replay(data)

    def test_mutated_locator_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["cases"][0]["views"]["render"]["path"] = "../escaped.json"
        with self.assertRaisesRegex(ValueError, "locator escapes package"):
            self.replay(data)

    def test_mutated_tolerance_cannot_relabel_cases(self):
        data = copy.deepcopy(self.data)
        data["contract"]["target"]["synchronization_tolerance_frames"] = 2
        with self.assertRaisesRegex(ValueError, "just-outside-tolerance.*replayed"):
            self.replay(data)

    def test_mutated_time_basis_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["contract"]["time_basis"]["frame_rate"]["numerator"] = 24
        with self.assertRaisesRegex(ValueError, "time basis"):
            self.replay(data)


if __name__ == "__main__":
    unittest.main()

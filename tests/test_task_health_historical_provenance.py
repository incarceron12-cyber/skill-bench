from __future__ import annotations

import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_provenance_boundary import validate_historical_contract_reference


ROOT = Path(__file__).resolve().parents[1]
BOUNDARY = ROOT / "schemas/task-health-v0.1-provenance-boundary.json"
EXPECTED_PATH = "schemas/task-health.schema.json"
EXPECTED_ROLE = "task_health_identifier_contract"
HISTORICAL_SHA = "a6447dc191018b13604f508d856295455ecd8cfbbeffdf5a92170eddd59b2956"


class TaskHealthHistoricalProvenanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.boundary = json.loads(BOUNDARY.read_text())
        cls.reference = {"path": EXPECTED_PATH, "sha256": HISTORICAL_SHA}

    def validate(self, reference=None, boundary=None):
        if boundary is None:
            return validate_historical_contract_reference(
                reference or self.reference,
                BOUNDARY,
                expected_path=EXPECTED_PATH,
                expected_role=EXPECTED_ROLE,
            )
        with tempfile.NamedTemporaryFile("w", suffix=".json") as handle:
            json.dump(boundary, handle)
            handle.flush()
            return validate_historical_contract_reference(
                reference or self.reference,
                Path(handle.name),
                expected_path=EXPECTED_PATH,
                expected_role=EXPECTED_ROLE,
            )

    def test_exact_historical_contract_and_bounded_live_semantics_validate(self):
        report = self.validate()
        self.assertTrue(report["valid"], report["errors"])
        self.assertEqual(3, report["boundary"]["live_anchor_count"])

    def test_wrong_commit_blob_and_hash_are_rejected(self):
        for field, value, phrase in (
            ("git_commit", "f" * 40, "absent historical Git commit"),
            ("git_blob", "0" * 40, "historical Git blob mismatch"),
            ("sha256", "0" * 64, "historical SHA-256 mismatch"),
        ):
            with self.subTest(field=field):
                boundary = copy.deepcopy(self.boundary)
                boundary["historical_snapshot"][field] = value
                errors = self.validate(boundary=boundary)["errors"]
                self.assertTrue(any(phrase in error for error in errors), errors)

    def test_path_substitution_is_rejected(self):
        reference = dict(self.reference, path="README.md")
        errors = self.validate(reference=reference)["errors"]
        self.assertTrue(any("path substitution" in error for error in errors), errors)

    def test_deleted_or_changed_bounded_semantics_are_rejected(self):
        boundary = copy.deepcopy(self.boundary)
        locator = boundary["live_dependency"]["semantic_locators"][1]
        locator["live_text"] = "__deleted_task_health_record_collection__"
        locator["live_text_sha256"] = hashlib.sha256(locator["live_text"].encode()).hexdigest()
        errors = self.validate(boundary=boundary)["errors"]
        self.assertTrue(any("missing live semantic locator" in error for error in errors), errors)

    def test_locator_hash_refresh_without_matching_text_is_rejected(self):
        boundary = copy.deepcopy(self.boundary)
        boundary["live_dependency"]["semantic_locators"][0]["live_text_sha256"] = "0" * 64
        errors = self.validate(boundary=boundary)["errors"]
        self.assertTrue(any("live semantic locator hash mismatch" in error for error in errors), errors)

    def test_current_file_hash_cannot_refresh_historical_reference(self):
        current_sha = hashlib.sha256((ROOT / EXPECTED_PATH).read_bytes()).hexdigest()
        errors = self.validate(reference=dict(self.reference, sha256=current_sha))["errors"]
        self.assertTrue(any("reference hash differs" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()

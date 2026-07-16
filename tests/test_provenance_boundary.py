from __future__ import annotations

import copy
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from scripts.validate_provenance_boundary import validate_frozen_component_set, validate_record


ROOT = Path(__file__).resolve().parents[1]
DYNAMIC = ROOT / "pilots/dynamic-criterion-conformance/provenance-boundary.json"
DELAYED = ROOT / "pilots/delayed-obligation-heldout-v2"
EXPECTED_PATH = "docs/benchmark-design-taxonomy.md"
EXPECTED_ROLE = "dynamic_criterion_design_basis"


class ProvenanceBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads(DYNAMIC.read_text())

    def validate_mutation(self, mutate):
        record = copy.deepcopy(self.record)
        mutate(record)
        return validate_record(record, expected_path=EXPECTED_PATH, expected_role=EXPECTED_ROLE)

    def test_historical_git_object_and_live_anchors_validate(self):
        report = validate_record(self.record, expected_path=EXPECTED_PATH, expected_role=EXPECTED_ROLE)
        self.assertTrue(report["valid"], report["errors"])
        self.assertEqual(3, report["live_anchor_count"])

    def test_wrong_reachable_commit_cannot_reidentify_snapshot(self):
        head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
        report = self.validate_mutation(lambda record: record["historical_snapshot"].update(git_commit=head))
        self.assertFalse(report["valid"])
        self.assertTrue(any("mismatch" in error for error in report["errors"]))

    def test_wrong_blob_fails(self):
        report = self.validate_mutation(lambda record: record["historical_snapshot"].update(git_blob="0" * 40))
        self.assertFalse(report["valid"])
        self.assertTrue(any("blob mismatch" in error for error in report["errors"]))

    def test_tampered_historical_snapshot_hash_fails(self):
        report = self.validate_mutation(lambda record: record["historical_snapshot"].update(sha256="0" * 64))
        self.assertFalse(report["valid"])
        self.assertTrue(any("historical SHA-256 mismatch" in error for error in report["errors"]))

    def test_absent_historical_object_fails(self):
        report = self.validate_mutation(lambda record: record["historical_snapshot"].update(git_commit="f" * 40))
        self.assertFalse(report["valid"])
        self.assertTrue(any("absent historical Git commit" in error for error in report["errors"]))

    def test_missing_required_anchor_fails(self):
        report = self.validate_mutation(
            lambda record: record["live_dependency"]["required_anchors"].append("__missing_semantic_anchor__")
        )
        self.assertFalse(report["valid"])
        self.assertTrue(any("missing live semantic anchor" in error for error in report["errors"]))
        self.assertTrue(any("missing historical semantic anchor" in error for error in report["errors"]))

    def test_path_substitution_fails(self):
        report = self.validate_mutation(lambda record: record["live_dependency"].update(path="README.md"))
        self.assertFalse(report["valid"])
        self.assertTrue(any("path substitution" in error for error in report["errors"]))

    def test_silent_semantic_role_change_fails(self):
        report = self.validate_mutation(
            lambda record: record["live_dependency"].update(semantic_role="generic_documentation")
        )
        self.assertFalse(report["valid"])
        self.assertTrue(any("semantic role change" in error for error in report["errors"]))

    def test_legacy_protocol_keeps_every_noncanonical_component_byte_pinned(self):
        report = validate_frozen_component_set(
            DELAYED / "protocol.json",
            DELAYED / "provenance-boundary.json",
            expected_path=EXPECTED_PATH,
            expected_role="delayed_obligation_design_basis",
        )
        self.assertTrue(report["valid"], report["errors"])

    def test_immutable_runtime_hash_cannot_use_live_document_exception(self):
        protocol = json.loads((DELAYED / "protocol.json").read_text())
        runtime = next(item for item in protocol["frozen_components"] if item["path"].endswith("run_study.py"))
        runtime["sha256"] = "0" * 64
        with tempfile.NamedTemporaryFile("w", suffix=".json", dir=DELAYED, delete=False) as handle:
            json.dump(protocol, handle)
            path = Path(handle.name)
        try:
            report = validate_frozen_component_set(
                path,
                DELAYED / "provenance-boundary.json",
                expected_path=EXPECTED_PATH,
                expected_role="delayed_obligation_design_basis",
            )
        finally:
            path.unlink(missing_ok=True)
        self.assertFalse(report["valid"])
        self.assertTrue(any("immutable frozen component drift" in error for error in report["errors"]))


if __name__ == "__main__":
    unittest.main()

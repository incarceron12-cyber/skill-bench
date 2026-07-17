from __future__ import annotations

import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from scripts.validate_evidence_acquisition_historical import DEFAULT_SCHEMA, ValidationFailure, semantic_errors, validate_file

ROOT = Path(__file__).resolve().parents[1]
VALID = ROOT / "tests/fixtures/valid-evidence-acquisition-episodes.json"
INVALID = ROOT / "tests/fixtures/invalid-evidence-acquisition-mutations.json"


class EvidenceAcquisitionEpisodeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.valid = json.loads(VALID.read_text(encoding="utf-8"))
        cls.invalid = json.loads(INVALID.read_text(encoding="utf-8"))

    @staticmethod
    def mutate(package, path, value) -> None:
        node = package
        for part in path[:-1]:
            node = node[part]
        node[path[-1]] = value

    def test_schema_is_draft_2020_12_and_positive_fixture_validates(self) -> None:
        schema = json.loads(DEFAULT_SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validate_file(VALID, DEFAULT_SCHEMA, check_paths=True)

    def test_fixture_crosses_two_shapes_and_three_matched_conditions(self) -> None:
        self.assertEqual(2, len({item["work_shape"] for item in self.valid["scenarios"]}))
        expected = {"active", "full_information", "expert_minimal"}
        for scenario in self.valid["scenarios"]:
            self.assertEqual(expected, {item["condition_id"] for item in scenario["episodes"]})

    def test_access_statuses_and_flow_layers_are_exercised(self) -> None:
        statuses = {
            event["status"]
            for scenario in self.valid["scenarios"]
            for episode in scenario["episodes"]
            for event in episode["access_events"]
        }
        self.assertTrue({"released", "delayed", "denied", "ambiguous"} <= statuses)
        active = self.valid["scenarios"][0]["episodes"][0]
        self.assertIn("parser_interpretation", active["requests"][0])
        self.assertIn("access_event_id", active["access_events"][0])
        self.assertIn("trace_evidence_locator", active["adoptions"][0])
        self.assertIn("decision_loss", active["terminal_consequence"])

    def test_all_planted_invalid_fixtures_fail_for_declared_reason(self) -> None:
        for case in self.invalid["cases"]:
            with self.subTest(case=case["case_id"]):
                package = copy.deepcopy(self.valid)
                self.mutate(package, case["path"], case["value"])
                if case["case_id"] == "endpoint-only-adoption":
                    with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as handle:
                        json.dump(package, handle)
                        handle.flush()
                        with self.assertRaisesRegex(ValidationFailure, "trace_evidence_locator.*non-empty"):
                            validate_file(Path(handle.name), DEFAULT_SCHEMA)
                else:
                    errors = semantic_errors(package)
                    self.assertTrue(any(case["expected_error"] in error for error in errors), errors)

    def test_rejects_release_without_content_identity(self) -> None:
        package = copy.deepcopy(self.valid)
        event = package["scenarios"][0]["episodes"][0]["access_events"][0]
        event["content_locator"] = None
        self.assertTrue(any("released evidence needs identity and content locator" in error for error in semantic_errors(package)))

    def test_rejects_full_information_that_silently_omits_admissible_evidence(self) -> None:
        package = copy.deepcopy(self.valid)
        package["scenarios"][0]["episodes"][1]["access_events"].pop()
        self.assertTrue(any("full-information condition must supply every" in error for error in semantic_errors(package)))

    def test_rejects_adoption_not_linked_to_same_released_atom(self) -> None:
        package = copy.deepcopy(self.valid)
        package["scenarios"][0]["episodes"][0]["adoptions"][0]["evidence_id"] = "training-attestation"
        self.assertTrue(any("adoption must map to a release" in error for error in semantic_errors(package)))

    def test_rejects_provenance_hash_drift(self) -> None:
        package = copy.deepcopy(self.valid)
        package["provenance"][0]["sha256"] = "0" * 64
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as handle:
            json.dump(package, handle)
            handle.flush()
            with self.assertRaisesRegex(ValidationFailure, "provenance hash mismatch"):
                validate_file(Path(handle.name), DEFAULT_SCHEMA, check_paths=True)

    def test_rejects_refreshing_historical_task_health_pin_to_live_hash(self) -> None:
        package = copy.deepcopy(self.valid)
        reference = next(
            item for item in package["provenance"]
            if item["path"] == "schemas/task-health.schema.json"
        )
        reference["sha256"] = hashlib.sha256(
            (ROOT / reference["path"]).read_bytes()
        ).hexdigest()
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as handle:
            json.dump(package, handle)
            handle.flush()
            with self.assertRaisesRegex(ValidationFailure, "historical contract reference hash"):
                validate_file(Path(handle.name), DEFAULT_SCHEMA, check_paths=True)


    def test_agent_validation_status_does_not_require_manufactured_access_states(self) -> None:
        package = copy.deepcopy(self.valid)
        package["status"] = "internal_agent_validation_only"
        package["scenarios"][0]["episodes"][0]["terminal_consequence"]["claim_scope"] = "internal_agent_validation_only"
        package["scenarios"][0]["episodes"][0]["access_events"] = [
            event for event in package["scenarios"][0]["episodes"][0]["access_events"]
            if event["status"] != "ambiguous"
        ]
        self.assertFalse(semantic_errors(package))


if __name__ == "__main__":
    unittest.main()

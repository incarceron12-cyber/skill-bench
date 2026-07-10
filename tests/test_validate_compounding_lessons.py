from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_compounding_lessons import (
    DEFAULT_SCHEMA,
    ValidationFailure,
    semantic_errors,
    validate_file,
)

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "valid-compounding-lessons.json"


class CompoundingLessonValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.valid = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def validate_mutation(self, mutation, *, check_paths: bool = False) -> None:
        store = copy.deepcopy(self.valid)
        mutation(store)
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as handle:
            json.dump(store, handle)
            handle.flush()
            validate_file(Path(handle.name), DEFAULT_SCHEMA, check_paths=check_paths)

    def test_valid_store_and_declared_component_hashes(self) -> None:
        validate_file(FIXTURE, DEFAULT_SCHEMA, check_paths=True)

    def test_rejects_mutated_immutable_lesson_content(self) -> None:
        def mutate(store):
            store["lessons"][0]["statement"] += " Changed in place."

        with self.assertRaisesRegex(ValidationFailure, "immutable statement"):
            self.validate_mutation(mutate)

    def test_rejects_unsupported_promotion(self) -> None:
        store = copy.deepcopy(self.valid)
        validation = next(item for item in store["validations"] if item["validation_id"] == "independent-promotion-contract-test")
        validation["status"] = "failed"
        errors = semantic_errors(store)
        self.assertTrue(any("promotion requires a referenced independent passed validation" in error for error in errors))

    def test_rejects_source_observation_reused_as_held_out_validation(self) -> None:
        store = copy.deepcopy(self.valid)
        validation = store["validations"][0]
        validation["source_observation_ids"] = ["ace-independent-promotion-source"]
        errors = semantic_errors(store)
        self.assertTrue(any("reuses proposal observations" in error for error in errors))

    def test_rejects_contradictory_merge_without_resolution(self) -> None:
        store = copy.deepcopy(self.valid)
        store["contradiction_resolutions"] = []
        errors = semantic_errors(store)
        self.assertTrue(any("contradictory merge" in error and "accepted resolution" in error for error in errors))

    def test_rejects_private_check_leakage_to_same_split_skill(self) -> None:
        store = copy.deepcopy(self.valid)
        store["dependencies"].append(
            {
                "dependency_id": "leaked-private-skill",
                "lesson_id": "private-feedback-firewall",
                "target_type": "agent_visible_skill",
                "target_path": "schemas/COMPOUNDING_LESSONS.md",
                "target_version": "planted-leak",
                "target_sha256": "a5d269e031e1c16e0c0f1daa5145cf30189887c996416c9aee3f91432744e37a",
                "exposure": "agent_visible",
                "evaluation_split_ids": ["pilot-private-split"],
                "introduced_by_event_id": "private-firewall-proposed",
                "active": True,
            }
        )
        errors = semantic_errors(store)
        self.assertTrue(any("private-evidence firewall" in error and "pilot-private-split" in error for error in errors))

    def test_rejects_applied_rollback_that_leaves_dependency_active(self) -> None:
        store = copy.deepcopy(self.valid)
        dependency = next(item for item in store["dependencies"] if item["dependency_id"] == "blind-merge-guidance")
        dependency["active"] = True
        errors = semantic_errors(store)
        self.assertTrue(any("applied rollback must retire dependency" in error for error in errors))

    def test_rejects_noncontiguous_lifecycle_history(self) -> None:
        store = copy.deepcopy(self.valid)
        event = next(item for item in store["lifecycle_events"] if item["event_id"] == "independent-rule-validated")
        event["from_state"] = "validated"
        errors = semantic_errors(store)
        self.assertTrue(any("append-only and contiguous" in error for error in errors))

    def test_rejects_stale_downstream_component_hash(self) -> None:
        def mutate(store):
            store["dependencies"][0]["target_sha256"] = "0" * 64

        with self.assertRaisesRegex(ValidationFailure, "target_sha256 does not match"):
            self.validate_mutation(mutate, check_paths=True)


if __name__ == "__main__":
    unittest.main()

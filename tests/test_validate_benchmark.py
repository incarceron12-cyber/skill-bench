from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_benchmark import DEFAULT_SCHEMA, ValidationFailure, semantic_errors, validate_file

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "valid-benchmark-bundle.json"


class BenchmarkBundleValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.valid = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def validate_mutation(self, mutation) -> None:
        bundle = copy.deepcopy(self.valid)
        mutation(bundle)
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as handle:
            json.dump(bundle, handle)
            handle.flush()
            validate_file(Path(handle.name), DEFAULT_SCHEMA)

    def test_valid_complete_bundle_and_provenance_paths(self) -> None:
        validate_file(FIXTURE, DEFAULT_SCHEMA, check_paths=True)

    def test_schema_rejects_failed_result_without_causal_diagnosis(self) -> None:
        def mutate(bundle):
            del bundle["trials"][0]["check_results"][0]["root_cause"]

        with self.assertRaisesRegex(ValidationFailure, "root_cause"):
            self.validate_mutation(mutate)

    def test_semantics_reject_unknown_check_grader(self) -> None:
        bundle = copy.deepcopy(self.valid)
        bundle["task"]["checks"][0]["grader_id"] = "missing-grader"
        self.assertTrue(any("unknown grader_id" in error for error in semantic_errors(bundle)))

    def test_semantics_reject_completed_trial_without_required_check(self) -> None:
        bundle = copy.deepcopy(self.valid)
        bundle["trials"][0]["check_results"] = []
        self.assertTrue(any("check coverage mismatch" in error for error in semantic_errors(bundle)))

    def test_semantics_reject_causal_slice_with_unknown_event(self) -> None:
        bundle = copy.deepcopy(self.valid)
        bundle["trials"][0]["check_results"][0]["causal_slice_event_ids"].append("invented-event")
        self.assertTrue(any("unknown causal event" in error for error in semantic_errors(bundle)))

    def test_semantics_recomputes_weighted_aggregate(self) -> None:
        bundle = copy.deepcopy(self.valid)
        bundle["trials"][0]["aggregate_score"] = 0.5
        self.assertTrue(any("weighted score" in error for error in semantic_errors(bundle)))

    def test_semantics_rejects_duplicate_identifiers(self) -> None:
        bundle = copy.deepcopy(self.valid)
        bundle["task"]["checks"].append(copy.deepcopy(bundle["task"]["checks"][0]))
        self.assertTrue(any("duplicate check_id" in error for error in semantic_errors(bundle)))


if __name__ == "__main__":
    unittest.main()

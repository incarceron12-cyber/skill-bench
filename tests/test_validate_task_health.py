from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_task_health import DEFAULT_SCHEMA, ValidationFailure, semantic_errors, validate_file

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "valid-task-health.json"
EVOLUTION_NEGATIVES = ROOT / "tests" / "fixtures" / "task-health-evolution-negative-mutations.json"


class TaskHealthTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.valid = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def validate_mutation(self, mutation, *, check_paths: bool = False) -> None:
        package = copy.deepcopy(self.valid)
        mutation(package)
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as handle:
            json.dump(package, handle)
            handle.flush()
            validate_file(Path(handle.name), DEFAULT_SCHEMA, check_paths=check_paths)

    def test_valid_lifecycle_and_artifact_hashes(self) -> None:
        validate_file(FIXTURE, DEFAULT_SCHEMA, check_paths=True)
        record = self.valid["task_health_records"][0]
        self.assertEqual("regression_guard", record["transitions"][0]["to_role"])
        self.assertTrue(record["revisions"][0]["old_scores_preserved"])

    def test_rejects_regression_transition_based_only_on_saturation(self) -> None:
        package = copy.deepcopy(self.valid)
        record = package["task_health_records"][0]
        record["transitions"][0]["evidence_ids"] = ["synthetic-saturation"]
        for signal in record["health_evidence"]:
            if signal["signal"] in {"repeat_stability", "invalid_run_rate", "unresolved_instrument_invalidity"}:
                signal["status"] = "unknown"
        errors = semantic_errors(package)
        self.assertTrue(any("regression graduation requires acceptable" in error for error in errors))
        self.assertTrue(any("saturation alone cannot justify" in error for error in errors))

    def test_rejects_grader_defect_without_new_version(self) -> None:
        package = copy.deepcopy(self.valid)
        record = package["task_health_records"][0]
        record["adjudications"][0]["replacement_artifact_ref_ids"] = []
        record["revisions"] = []
        errors = semantic_errors(package)
        self.assertTrue(any("instrument defect must create a replacement version" in error for error in errors))
        self.assertTrue(any("matching immutable revision record" in error for error in errors))

    def test_rejects_rewriting_old_scores_after_revision(self) -> None:
        package = copy.deepcopy(self.valid)
        record = package["task_health_records"][0]
        record["adjudications"][0]["old_score_disposition"] = "not_applicable"
        record["revisions"][0]["old_scores_preserved"] = False
        errors = semantic_errors(package)
        self.assertTrue(any("old result must remain preserved" in error for error in errors))
        self.assertTrue(any("old scores must be preserved" in error for error in errors))

    def test_rejects_instrument_defect_in_capability_aggregate(self) -> None:
        package = copy.deepcopy(self.valid)
        package["task_health_records"][0]["adjudications"][0]["capability_aggregation_disposition"] = "include"
        errors = semantic_errors(package)
        self.assertTrue(any("must be excluded from capability aggregation" in error for error in errors))

    def test_rejects_accepted_alternative_without_transcript(self) -> None:
        package = copy.deepcopy(self.valid)
        adjudication = package["task_health_records"][0]["adjudications"][0]
        adjudication["defect_type"] = "accepted_alternative"
        adjudication["decision"] = "accept_alternative"
        adjudication["replacement_artifact_ref_ids"] = []
        errors = semantic_errors(package)
        self.assertTrue(any("requires transcript-grounded observation" in error for error in errors))

    def test_rejects_outcome_selected_confirmatory_inventory(self) -> None:
        package = copy.deepcopy(self.valid)
        origin = package["task_health_records"][0]["origin"]
        origin["selection_stage"] = "confirmatory"
        origin["admission_influenced_by_outcomes"] = True
        errors = semantic_errors(package)
        self.assertTrue(any("outcome-influenced admission" in error for error in errors))

    def test_rejects_reference_attempt_that_did_not_pass(self) -> None:
        package = copy.deepcopy(self.valid)
        package["task_health_records"][0]["reference_attempts"][0]["result"] = "invalid"
        errors = semantic_errors(package)
        self.assertTrue(any("not witnesses" in error for error in errors))

    def test_rejects_adaptive_discrimination_as_continuity_or_transport(self) -> None:
        negatives = json.loads(EVOLUTION_NEGATIVES.read_text(encoding="utf-8"))
        case = next(item for item in negatives["cases"] if item["case_id"] == "adaptive-discrimination-only")
        package = copy.deepcopy(self.valid)
        bridge = package["task_health_records"][0]["instrument_evolution"]["bridge"]
        for path, value in case["changes"].items():
            bridge[path.removeprefix("bridge.")] = value
        errors = semantic_errors(package)
        self.assertTrue(any(case["expected_error"] in error for error in errors))

    def test_rejects_bridge_population_exposed_to_adaptation(self) -> None:
        negatives = json.loads(EVOLUTION_NEGATIVES.read_text(encoding="utf-8"))
        case = next(item for item in negatives["cases"] if item["case_id"] == "bridge-population-leaked")
        package = copy.deepcopy(self.valid)
        partitions = package["task_health_records"][0]["instrument_evolution"]["partitions"]
        next(item for item in partitions if item["role"] == "frozen_bridge")["visible_to_adaptation"] = True
        errors = semantic_errors(package)
        self.assertTrue(any(case["expected_error"] in error for error in errors))

    def test_rejects_candidate_without_terminal_history(self) -> None:
        negatives = json.loads(EVOLUTION_NEGATIVES.read_text(encoding="utf-8"))
        case = next(item for item in negatives["cases"] if item["case_id"] == "candidate-without-disposition")
        package = copy.deepcopy(self.valid)
        evolution = package["task_health_records"][0]["instrument_evolution"]
        evolution["events"] = [event for event in evolution["events"] if event["event_id"] != "criterion-v2-admitted"]
        errors = semantic_errors(package)
        self.assertTrue(any(case["expected_error"] in error for error in errors))

    def test_rejects_stale_artifact_hash(self) -> None:
        def mutate(package):
            package["artifacts"][0]["sha256"] = "0" * 64

        with self.assertRaisesRegex(ValidationFailure, "sha256 does not match"):
            self.validate_mutation(mutate, check_paths=True)


if __name__ == "__main__":
    unittest.main()

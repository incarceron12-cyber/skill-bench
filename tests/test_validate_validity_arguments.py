from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

from scripts.grade_lh_claims import grade as grade_claims
from scripts.grade_lh_evidence import grade as grade_evidence
from scripts.validate_validity_arguments import (
    DEFAULT_SCHEMA,
    ValidationFailure,
    semantic_errors,
    validate_file,
)

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "valid-validity-arguments.json"
MEASUREMENT = ROOT / "tests" / "fixtures" / "lh-planted-grader-calibration-measurement.json"
PILOT = ROOT / "pilots" / "lh-skill-adoption"


class ValidityArgumentTests(unittest.TestCase):
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

    def test_valid_claim_ladder_and_artifact_hashes(self) -> None:
        validate_file(FIXTURE, DEFAULT_SCHEMA, check_paths=True)
        statuses = {item["argument_id"]: item["status"] for item in self.valid["arguments"]}
        self.assertEqual(
            {
                "narrow-fixture-detection": "supported",
                "professional-capability": "unsupported",
                "deployment-readiness": "unsupported",
            },
            statuses,
        )

    def test_calibration_measurement_matches_fresh_grader_execution(self) -> None:
        expected = json.loads(MEASUREMENT.read_text(encoding="utf-8"))["results"]
        actual: dict[str, dict[str, str]] = {}
        for name in sorted(expected):
            case = PILOT / "calibration" / name
            results = [
                grade_evidence(
                    PILOT / "source-pack" / "decision-evidence.csv",
                    case / "evidence-matrix.csv",
                    case / "recommendation.md",
                )
            ]
            results.extend(
                grade_claims(
                    PILOT / "graders" / "independent-claim-rubric.json",
                    case / "evidence-matrix.csv",
                    case / "recommendation.md",
                )
            )
            actual[name] = {str(item["check_id"]): str(item["outcome"]) for item in results}
        self.assertEqual(expected, actual)

    def test_rejects_professional_capability_claim_upgrade(self) -> None:
        package = copy.deepcopy(self.valid)
        argument = next(item for item in package["arguments"] if item["argument_id"] == "professional-capability")
        argument["status"] = "supported"
        errors = semantic_errors(package)
        self.assertTrue(any("supported/provisional construct claim requires" in error for error in errors))
        self.assertTrue(any("supported claim has unsupported required facets" in error for error in errors))

    def test_rejects_deployment_readiness_upgrade_without_loss_threshold_evidence(self) -> None:
        package = copy.deepcopy(self.valid)
        argument = next(item for item in package["arguments"] if item["argument_id"] == "deployment-readiness")
        argument["status"] = "supported"
        errors = semantic_errors(package)
        self.assertTrue(any("supported claim has unsupported required facets" in error for error in errors))
        self.assertTrue(any("requires empirical loss or expert standard-setting evidence" in error for error in errors))

    def test_rejects_undifferentiated_expert_validity_approval(self) -> None:
        package = copy.deepcopy(self.valid)
        package["evidence"].append(
            {
                "evidence_id": "generic-expert-approval",
                "evidence_type": "expert_review",
                "artifact_ref_id": "lh-bundle",
                "locator": "invented generic approval",
                "description": "A single approval purporting to validate every facet.",
                "facet_scope": ["content", "criterion", "construct", "external", "consequential"],
                "claim_scope": ["professional-capability"],
                "limitations": ["No facet-specific review record."],
                "reviewer": "synthetic reviewer",
            }
        )
        errors = semantic_errors(package)
        self.assertTrue(any("undifferentiated expert-validity approval is forbidden" in error for error in errors))

    def test_rejects_duplicate_or_missing_facet(self) -> None:
        package = copy.deepcopy(self.valid)
        argument = package["arguments"][0]
        argument["validity_facets"][-1]["facet"] = "content"
        errors = semantic_errors(package)
        self.assertTrue(any("each of the five facets exactly once" in error for error in errors))

    def test_rejects_evidence_used_outside_claim_scope(self) -> None:
        package = copy.deepcopy(self.valid)
        package["evidence"][0]["claim_scope"] = ["professional-capability"]
        errors = semantic_errors(package)
        self.assertTrue(any("not scoped to this claim" in error for error in errors))

    def test_rejects_stale_measurement_hash(self) -> None:
        def mutate(package):
            artifact = next(item for item in package["artifacts"] if item["artifact_id"] == "planted-calibration-measurement")
            artifact["sha256"] = "0" * 64

        with self.assertRaisesRegex(ValidationFailure, "sha256 does not match"):
            self.validate_mutation(mutate, check_paths=True)


if __name__ == "__main__":
    unittest.main()

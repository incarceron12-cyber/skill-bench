from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_expertise_transfer import (
    DEFAULT_SCHEMA,
    ValidationFailure,
    semantic_errors,
    validate_file,
)

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "valid-expertise-transfer.json"
PROJECTION_FIXTURE = ROOT / "tests" / "fixtures" / "session-projection-conformance.json"


class ExpertiseTransferValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.valid = json.loads(FIXTURE.read_text(encoding="utf-8"))
        cls.projection_case = json.loads(PROJECTION_FIXTURE.read_text(encoding="utf-8"))

    def packet_with_projection_case(self) -> dict:
        packet = copy.deepcopy(self.valid)
        packet["session_projections"] = [copy.deepcopy(self.projection_case["session_projection"])]
        packet["rubric_dimensions"] = copy.deepcopy(self.projection_case["rubric_dimensions"])
        return packet

    def validate_mutation(self, mutation) -> None:
        packet = copy.deepcopy(self.valid)
        mutation(packet)
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as handle:
            json.dump(packet, handle)
            handle.flush()
            validate_file(Path(handle.name), DEFAULT_SCHEMA)

    def test_valid_packet_and_declared_paths(self) -> None:
        validate_file(FIXTURE, DEFAULT_SCHEMA, check_paths=True)

    def test_schema_requires_claim_provenance(self) -> None:
        def mutate(packet):
            packet["claims"][0]["provenance"] = []

        with self.assertRaisesRegex(ValidationFailure, "non-empty"):
            self.validate_mutation(mutate)

    def test_semantics_reject_unknown_claim_mapping(self) -> None:
        packet = copy.deepcopy(self.valid)
        packet["primitives"][0]["claim_ids"] = ["invented-claim"]
        self.assertTrue(any("unknown claim_id" in error for error in semantic_errors(packet)))

    def test_semantics_requires_reciprocal_primitive_check_mapping(self) -> None:
        packet = copy.deepcopy(self.valid)
        packet["checks"][0]["primitive_ids"].remove("preserve-evidence-chain")
        self.assertTrue(any("does not map back" in error for error in semantic_errors(packet)))

    def test_semantics_forbids_private_check_without_public_basis(self) -> None:
        packet = copy.deepcopy(self.valid)
        packet["checks"][0]["public_basis_primitive_ids"] = []
        self.assertTrue(any("hidden obligations are forbidden" in error for error in semantic_errors(packet)))

    def test_semantics_rejects_nonpublic_public_basis(self) -> None:
        packet = copy.deepcopy(self.valid)
        packet["checks"][0]["public_basis_primitive_ids"] = ["polished-score-only-failure"]
        self.assertTrue(any("is not public" in error for error in semantic_errors(packet)))

    def test_semantics_enforces_ordered_stage_gates(self) -> None:
        packet = copy.deepcopy(self.valid)
        packet["current_stage"] = "pilot_validation"
        self.assertTrue(any("rubric" in error and "must pass" in error for error in semantic_errors(packet)))

    def test_semantics_forbids_unreviewed_release(self) -> None:
        packet = copy.deepcopy(self.valid)
        packet["release"]["status"] = "releasable"
        errors = semantic_errors(packet)
        self.assertTrue(any("every quality gate" in error for error in errors))
        self.assertTrue(any("leakage and expert-validity" in error for error in errors))

    def test_demand_inspired_license_allows_material_omissions(self) -> None:
        packet = self.packet_with_projection_case()
        packet.pop("rubric_dimensions")
        self.assertEqual([], semantic_errors(packet))

    def test_projection_case_conforms_to_schema_when_rubric_is_holistic(self) -> None:
        packet = self.packet_with_projection_case()
        for dimension in packet["rubric_dimensions"]:
            dimension["scoring_mode"] = "holistic"
            dimension["holistic_group"] = "overall-artifact-quality"
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as handle:
            json.dump(packet, handle)
            handle.flush()
            validate_file(Path(handle.name), DEFAULT_SCHEMA)

    def test_replay_license_rejects_omitted_failure_and_answer_hindsight(self) -> None:
        packet = self.packet_with_projection_case()
        packet.pop("rubric_dimensions")
        packet["session_projections"][0]["licensed_use"] = "session_replay_fidelity"
        errors = semantic_errors(packet)
        self.assertTrue(any("independent equivalent review" in error for error in errors))
        self.assertTrue(any("every omission" in error for error in errors))
        self.assertTrue(any("answer-bearing hindsight" in error for error in errors))

    def test_identical_dimension_guidance_requires_holistic_declaration(self) -> None:
        packet = self.packet_with_projection_case()
        errors = semantic_errors(packet)
        self.assertTrue(any("identical guidance" in error for error in errors))

    def test_identical_guidance_allowed_for_one_holistic_group(self) -> None:
        packet = self.packet_with_projection_case()
        for dimension in packet["rubric_dimensions"]:
            dimension["scoring_mode"] = "holistic"
            dimension["holistic_group"] = "overall-artifact-quality"
        self.assertEqual([], semantic_errors(packet))

    def test_internal_synthetic_authorization_cannot_expand(self) -> None:
        packet = self.packet_with_projection_case()
        packet.pop("rubric_dimensions")
        packet["session_projections"][0]["authorization"] = "authorized_release"
        self.assertTrue(any("internal_synthetic_only" in error for error in semantic_errors(packet)))


if __name__ == "__main__":
    unittest.main()

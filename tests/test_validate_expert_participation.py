from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_expert_participation import DEFAULT_SCHEMA, ValidationFailure, semantic_errors, validate_file

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "valid-expert-participation.json"


class ExpertParticipationValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.valid = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_valid_internal_calibration_fixture_and_hashes(self) -> None:
        validate_file(FIXTURE, DEFAULT_SCHEMA, check_paths=True)

    def test_schema_requires_concrete_comprehension_evidence(self) -> None:
        packet = copy.deepcopy(self.valid)
        del packet["consent_records"][0]["comprehension_evidence"]
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as handle:
            json.dump(packet, handle)
            handle.flush()
            with self.assertRaisesRegex(ValidationFailure, "comprehension_evidence"):
                validate_file(Path(handle.name), DEFAULT_SCHEMA)

    def test_rejects_synthetic_artifact_inheriting_expert_approval(self) -> None:
        packet = self._with_hypothetical_expert_chain()
        packet["derived_artifacts"].append({"artifact_id": "synthetic", "artifact_kind": "synthetic_variant", "path": "tests/fixtures/valid-expertise-transfer.json", "sha256": "ad663c22b4032691c23f2c3ab656c233075a14894f597f59cadf80d1782122b7", "creator_actor_type": "model", "authority_state": "expert_approved", "source_contribution_ids": ["expert-unit"], "current_purposes": ["evaluation"]})
        packet["transformations"].append({"transformation_id": "synthetic-derivation", "input_artifact_ids": ["expert-source"], "output_artifact_id": "synthetic", "actor_type": "model", "operation": "augment", "purpose": "evaluation", "material": True, "consent_ids": ["expert-consent"], "review_ids": []})
        errors = semantic_errors(packet)
        self.assertTrue(any("cannot inherit expert approval" in error for error in errors))

    def test_rejects_purpose_drift_without_reconsent(self) -> None:
        packet = self._with_hypothetical_expert_chain()
        packet["derived_artifacts"].append({"artifact_id": "training-copy", "artifact_kind": "example", "path": "tests/fixtures/valid-expertise-transfer.json", "sha256": "ad663c22b4032691c23f2c3ab656c233075a14894f597f59cadf80d1782122b7", "creator_actor_type": "benchmark_builder", "authority_state": "expert_derived_unreviewed", "source_contribution_ids": ["expert-unit"], "current_purposes": ["training"]})
        packet["transformations"].append({"transformation_id": "training-drift", "input_artifact_ids": ["expert-source"], "output_artifact_id": "training-copy", "actor_type": "benchmark_builder", "operation": "operationalize", "purpose": "training", "material": True, "consent_ids": ["expert-consent"], "review_ids": []})
        errors = semantic_errors(packet)
        self.assertTrue(any("purpose drift without reconsent" in error for error in errors))

    def test_rejects_developer_substitution_without_held_out_fidelity(self) -> None:
        packet = self._with_hypothetical_expert_chain()
        packet["authority_delegations"].append({"delegation_id": "developer-applies-standard", "standard_artifact_id": "expert-source", "from_actor_type": "domain_expert", "to_actor_type": "benchmark_builder", "application_purpose": "evaluation", "fidelity_review_id": None, "status": "approved"})
        errors = semantic_errors(packet)
        self.assertTrue(any("requires approved held-out expert-fidelity evidence" in error for error in errors))

    def test_rejects_expert_grounding_claim_for_unreviewed_artifact(self) -> None:
        packet = copy.deepcopy(self.valid)
        packet["release"]["expert_grounding_claim"] = "bounded"
        packet["release"]["approved_artifact_ids"] = ["fixture-record"]
        self.assertTrue(any("lacks current expert authority" in error for error in semantic_errors(packet)))

    def test_rejects_unknown_linked_contributor_duplication(self) -> None:
        packet = copy.deepcopy(self.valid)
        packet["participants"][1]["linked_contributor_id"] = "benchmark-builder"
        self.assertTrue(any("linked_contributor_id must be unique" in error for error in semantic_errors(packet)))

    def _with_hypothetical_expert_chain(self):
        packet = copy.deepcopy(self.valid)
        packet["participants"].append({"participant_id": "expert", "linked_contributor_id": "hypothetical-expert", "actor_type": "domain_expert", "role": "hypothetical mutation-test expert", "expertise_basis": "Test-only record; not actual testimony", "coverage_boundary": "Mutation testing only", "identity_mode": "private"})
        packet["consent_records"].append({"consent_id": "expert-consent", "participant_id": "expert", "version": "1", "effective_at": "2026-07-10T10:00:00Z", "allowed_purposes": ["evaluation"], "prohibited_purposes": ["training", "commercial_use", "public_release"], "allowed_transformations": ["augment", "operationalize"], "attribution": "private", "license_or_ownership": "Test only", "compensation": {"basis": "none", "amount_or_none": "none", "currency_or_none": "none"}, "reciprocal_output": {"description": "Test only", "delivery_status": "promised"}, "comprehension_evidence": {"method": "worked_example_review", "concrete_example_locator": "test mutation only", "participant_disposition": "demonstrated", "captured_at": "2026-07-10T10:00:00Z"}, "withdrawal_boundary": "Test only", "reconsent_triggers": ["new_purpose", "synthetic_derivation"], "status": "active"})
        packet["contribution_units"].append({"contribution_id": "expert-unit", "participant_id": "expert", "consent_id": "expert-consent", "unit_type": "example", "purpose": "evaluation", "artifact_ids": ["expert-source"], "contributor_minutes": 1, "review_state": "submitted"})
        packet["derived_artifacts"].append({"artifact_id": "expert-source", "artifact_kind": "example", "path": "tests/fixtures/valid-expertise-transfer.json", "sha256": "ad663c22b4032691c23f2c3ab656c233075a14894f597f59cadf80d1782122b7", "creator_actor_type": "domain_expert", "authority_state": "expert_authored", "source_contribution_ids": ["expert-unit"], "current_purposes": ["evaluation"]})
        return packet


if __name__ == "__main__":
    unittest.main()

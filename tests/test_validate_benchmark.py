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

    def test_semantics_rejects_private_check_without_held_out_public_consequence(self) -> None:
        bundle = copy.deepcopy(self.valid)
        bundle["task"]["checks"][0]["boundary_disclosure"] = "public_principle_only"
        self.assertTrue(any("private/hidden check must be a held_out_consequence" in error for error in semantic_errors(bundle)))

    def test_semantics_rejects_check_without_public_basis(self) -> None:
        bundle = copy.deepcopy(self.valid)
        bundle["task"]["checks"][0]["public_basis_requirement_ids"] = ["surprise-obligation"]
        self.assertTrue(any("unknown public basis requirement" in error for error in semantic_errors(bundle)))

    def test_semantics_rejects_ablation_condition_rubric_confound(self) -> None:
        bundle = copy.deepcopy(self.valid)
        bundle["trials"][0]["evaluation_versions"]["condition"] = "public_skill_independent_rubric"
        self.assertTrue(any("ablation condition conflicts" in error for error in semantic_errors(bundle)))

    def test_semantics_accepts_no_skill_shared_rubric_factorial_cell(self) -> None:
        bundle = copy.deepcopy(self.valid)
        bundle["trials"][0]["evaluation_versions"]["condition"] = "no_skill_shared_rubric"
        bundle["trials"][0]["evaluation_versions"]["skill"] = None
        bundle["trials"][0]["agent"]["skills_enabled"] = []
        self.assertEqual([], semantic_errors(bundle))

    def test_semantics_rejects_no_skill_cell_with_skill_enabled(self) -> None:
        bundle = copy.deepcopy(self.valid)
        bundle["trials"][0]["evaluation_versions"]["condition"] = "no_skill_shared_rubric"
        bundle["trials"][0]["evaluation_versions"]["skill"] = None
        self.assertTrue(any("no-skill condition enables" in error for error in semantic_errors(bundle)))

    def test_semantics_rejects_incomplete_recovery_chain(self) -> None:
        bundle = copy.deepcopy(self.valid)
        bundle["trials"][0]["trace"]["dependencies"] = [
            edge for edge in bundle["trials"][0]["trace"]["dependencies"]
            if edge["relation"] != "repair_verification"
        ]
        self.assertTrue(any("recovery chain" in error for error in semantic_errors(bundle)))

    def test_semantics_rejects_recovery_edge_with_wrong_event_kinds(self) -> None:
        bundle = copy.deepcopy(self.valid)
        edge = next(edge for edge in bundle["trials"][0]["trace"]["dependencies"] if edge["relation"] == "feedback_repair")
        edge["to_event_id"] = "verify-repair"
        self.assertTrue(any("feedback_repair edge must connect" in error for error in semantic_errors(bundle)))

    def test_schema_rejects_unhashed_typed_component(self) -> None:
        def mutate(bundle):
            del bundle["trials"][0]["evaluation_versions"]["feedback_policy"]["sha256"]

        with self.assertRaisesRegex(ValidationFailure, "sha256"):
            self.validate_mutation(mutate)

    def test_semantics_require_matched_longitudinal_treatments(self) -> None:
        bundle = copy.deepcopy(self.valid)
        bundle["longitudinal_evaluation"]["conditions"][1]["treatment"] = "full_evolution"
        self.assertTrue(any("exactly one reset" in error for error in semantic_errors(bundle)))

    def test_semantics_reject_private_evidence_in_evolution_update(self) -> None:
        bundle = copy.deepcopy(self.valid)
        exposure = bundle["longitudinal_evaluation"]["evolution_events"][0]["feedback_exposures"][0]
        exposure["kind"] = "private_check"
        exposure["visibility"] = "grader_only"
        self.assertTrue(any("cannot feed an update" in error for error in semantic_errors(bundle)))

    def test_semantics_reject_lesson_only_tool_update(self) -> None:
        bundle = copy.deepcopy(self.valid)
        bundle["longitudinal_evaluation"]["evolution_events"][0]["changed_loci"] = ["tools_code"]
        self.assertTrue(any("changed loci exceed" in error for error in semantic_errors(bundle)))

    def test_semantics_reject_broken_state_chain(self) -> None:
        bundle = copy.deepcopy(self.valid)
        event = copy.deepcopy(bundle["longitudinal_evaluation"]["evolution_events"][0])
        event["evolution_event_id"] = "lesson-update-2"
        event["after_stream_item_id"] = "retention-form-c"
        event["child_state"]["state_sha256"] = "3434343434343434343434343434343434343434343434343434343434343434"
        bundle["longitudinal_evaluation"]["evolution_events"].append(event)
        self.assertTrue(any("does not continue its condition ledger" in error for error in semantic_errors(bundle)))

    def test_semantics_reject_exact_replay_retention_probe(self) -> None:
        bundle = copy.deepcopy(self.valid)
        bundle["longitudinal_evaluation"]["probes"][0]["form_policy"] = "exact_replay"
        self.assertTrue(any("must use an equivalent form" in error for error in semantic_errors(bundle)))

    def test_semantics_reject_reset_arm_evolution_event(self) -> None:
        bundle = copy.deepcopy(self.valid)
        event = bundle["longitudinal_evaluation"]["evolution_events"][0]
        event["condition_id"] = "reset-arm"
        self.assertTrue(any("reset arm cannot contain" in error for error in semantic_errors(bundle)))


if __name__ == "__main__":
    unittest.main()

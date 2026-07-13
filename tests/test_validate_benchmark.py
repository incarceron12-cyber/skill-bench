from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_benchmark import DEFAULT_SCHEMA, ValidationFailure, canonical_sha256, semantic_errors, validate_file

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "valid-benchmark-bundle.json"
ADMISSIBILITY_FIXTURE = ROOT / "tests" / "fixtures" / "valid-artifact-admissibility-bundle.json"
PROJECTION_FIXTURE = ROOT / "tests" / "fixtures" / "valid-task-projection-manifest.json"
WORKSPACE_FIXTURE = ROOT / "tests" / "fixtures" / "valid-persistent-workspace-conformance.json"
ACTION_SAFETY_FIXTURE = ROOT / "tests" / "fixtures" / "valid-adversarial-action-conformance.json"
CONTEXT_COMPRESSION_FIXTURE = ROOT / "tests" / "fixtures" / "valid-context-compression-conformance.json"


class BenchmarkBundleValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.valid = json.loads(FIXTURE.read_text(encoding="utf-8"))
        cls.admissibility = json.loads(ADMISSIBILITY_FIXTURE.read_text(encoding="utf-8"))
        cls.projection_manifest = json.loads(PROJECTION_FIXTURE.read_text(encoding="utf-8"))
        cls.workspace = json.loads(WORKSPACE_FIXTURE.read_text(encoding="utf-8"))
        cls.action_safety = json.loads(ACTION_SAFETY_FIXTURE.read_text(encoding="utf-8"))
        cls.context_compression = json.loads(CONTEXT_COMPRESSION_FIXTURE.read_text(encoding="utf-8"))

    def projection_bundle(self):
        bundle = copy.deepcopy(self.valid)
        bundle["task"]["projection_manifest"] = copy.deepcopy(self.projection_manifest)
        return bundle

    def workspace_bundle(self):
        bundle = copy.deepcopy(self.valid)
        bundle["task"]["workspace"] = copy.deepcopy(self.workspace["task_workspace"])
        bundle["trials"][0]["workspace"] = copy.deepcopy(self.workspace["trial_workspace"])
        bundle["trials"][0]["trace"]["events"].extend(copy.deepcopy(self.workspace["synthetic_trace_events"]))
        return bundle

    def action_safety_bundle(self):
        bundle = copy.deepcopy(self.valid)
        bundle["task"]["source_pack"].append(copy.deepcopy(self.action_safety["source"]))
        bundle["task"]["action_safety"] = copy.deepcopy(self.action_safety["task_action_safety"])
        bundle["task"]["policies"]["network"] = "denied"
        bundle["trials"][0]["action_safety"] = copy.deepcopy(self.action_safety["trial_action_safety"])
        bundle["trials"][0]["trace"]["events"].extend(copy.deepcopy(self.action_safety["synthetic_trace_events"]))
        return bundle

    def context_compression_bundle(self):
        bundle = copy.deepcopy(self.valid)
        bundle["task"]["context_compression"] = copy.deepcopy(self.context_compression["task_context_compression"])
        bundle["trials"][0]["context_compression"] = copy.deepcopy(self.context_compression["trial_context_compression"])
        bundle["trials"][0]["trace"]["events"].extend(copy.deepcopy(self.context_compression["synthetic_trace_events"]))
        return bundle

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

    def test_valid_artifact_admissibility_conformance_slice(self) -> None:
        validate_file(ADMISSIBILITY_FIXTURE, DEFAULT_SCHEMA, check_paths=True)
        outcomes = {
            trial["check_results"][0]["check_id"]: (
                trial["check_results"][0]["outcome"],
                trial["check_results"][0]["admissibility_reason"],
            )
            for trial in self.admissibility["trials"]
        }
        self.assertEqual(("failed", "admitted"), outcomes["structured-wrong"])
        self.assertEqual(("passed", "admitted"), outcomes["alternate-render"])
        self.assertEqual(("insufficient_evidence", "missing_required_view"), outcomes["missing-view"])
        self.assertEqual(("invalid_artifact", "invalid_artifact"), outcomes["invalid-export"])
        self.assertEqual(("insufficient_evidence", "transform_mismatch"), outcomes["renderer-mismatch"])

    def test_semantics_rejects_scoring_missing_view_as_failure(self) -> None:
        bundle = copy.deepcopy(self.admissibility)
        result = bundle["trials"][2]["check_results"][0]
        result.update({"outcome": "failed", "score": 0, "admissibility_reason": "admitted"})
        self.assertTrue(any("requires outcome/reason" in error for error in semantic_errors(bundle)))

    def test_semantics_rejects_admitting_unpinned_renderer(self) -> None:
        bundle = copy.deepcopy(self.admissibility)
        result = bundle["trials"][4]["check_results"][0]
        result.update({"outcome": "passed", "score": 1, "admissibility_reason": "admitted"})
        self.assertTrue(any("transform_mismatch" in error for error in semantic_errors(bundle)))

    def test_semantics_rejects_unpermitted_render_invariance(self) -> None:
        bundle = copy.deepcopy(self.admissibility)
        bundle["trials"][1]["artifact_views"][1]["invariances_applied"] = ["camera_change"]
        self.assertTrue(any("unpermitted_invariance" in error for error in semantic_errors(bundle)))

    def test_semantics_rejects_transformed_authoritative_view(self) -> None:
        bundle = copy.deepcopy(self.admissibility)
        state = bundle["task"]["artifact_views"][0]
        state["transformation"] = copy.deepcopy(bundle["task"]["artifact_views"][1]["transformation"])
        self.assertTrue(any("authoritative view cannot" in error for error in semantic_errors(bundle)))


    def test_valid_task_projection_manifest(self) -> None:
        bundle = self.projection_bundle()
        self.assertEqual([], semantic_errors(bundle))
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as handle:
            json.dump(bundle, handle)
            handle.flush()
            validate_file(Path(handle.name), DEFAULT_SCHEMA, check_paths=True)

    def test_projection_rejects_requirement_change_with_stale_projection_links(self) -> None:
        bundle = self.projection_bundle()
        manifest = bundle["task"]["projection_manifest"]
        requirement = manifest["ir"]["requirements"][0]
        requirement["statement"] += " Preserve provenance."
        requirement["sha256"] = canonical_sha256({key: value for key, value in requirement.items() if key != "sha256"})
        ir = manifest["ir"]
        ir["sha256"] = canonical_sha256({"ir_id": ir["ir_id"], "version": ir["version"], "requirements": ir["requirements"]})
        self.assertTrue(any("stale requirement_sha256" in error for error in semantic_errors(bundle)))

    def test_projection_rejects_stale_affordance_witness_and_checker_outputs(self) -> None:
        for kind in ("source_environment", "witness", "check"):
            with self.subTest(kind=kind):
                bundle = self.projection_bundle()
                projection = next(item for item in bundle["task"]["projection_manifest"]["projections"] if item["kind"] == kind)
                projection["output"]["atoms"][0]["semantic_value"] = "planted drift"
                self.assertTrue(any("stale output_sha256" in error for error in semantic_errors(bundle)))

    def test_projection_rejects_checker_only_hidden_obligation(self) -> None:
        bundle = self.projection_bundle()
        manifest = bundle["task"]["projection_manifest"]
        check_projection = next(item for item in manifest["projections"] if item["kind"] == "check")
        atom = copy.deepcopy(check_projection["output"]["atoms"][0])
        atom["atom_id"] = "undisclosed-checker-obligation"
        atom["semantic_value"] = "require an obligation with no coverage row"
        check_projection["output"]["atoms"].append(atom)
        check_projection["output_sha256"] = canonical_sha256(check_projection["output"])
        self.assertTrue(any("checker-only hidden obligation" in error for error in semantic_errors(bundle)))

    def test_projection_accepts_declared_equivalent_representation_and_preserves_other_hashes(self) -> None:
        bundle = self.projection_bundle()
        projections = bundle["task"]["projection_manifest"]["projections"]
        unchanged = {item["kind"]: item["output_sha256"] for item in projections if item["kind"] != "instruction"}
        instruction = next(item for item in projections if item["kind"] == "instruction")
        instruction["output"]["atoms"][0]["representation"] = "equivalent bulleted sentence"
        instruction["applied_invariances"] = ["equivalent-wording"]
        instruction["output_sha256"] = canonical_sha256(instruction["output"])
        self.assertEqual([], semantic_errors(bundle))
        self.assertEqual(unchanged, {item["kind"]: item["output_sha256"] for item in projections if item["kind"] != "instruction"})

    def test_projection_rejects_undeclared_equivalence(self) -> None:
        bundle = self.projection_bundle()
        instruction = next(item for item in bundle["task"]["projection_manifest"]["projections"] if item["kind"] == "instruction")
        instruction["applied_invariances"] = ["unreviewed-paraphrase"]
        self.assertTrue(any("invariance was not declared" in error for error in semantic_errors(bundle)))

    def test_valid_persistent_workspace_conformance_and_alternate_path(self) -> None:
        bundle = self.workspace_bundle()
        self.assertEqual([], semantic_errors(bundle))
        self.assertEqual("workspace/alternate/current-policy.md", bundle["trials"][0]["workspace"]["relations"][0]["from_path"])
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as handle:
            json.dump(bundle, handle)
            handle.flush()
            validate_file(Path(handle.name), DEFAULT_SCHEMA, check_paths=True)

    def test_workspace_rejects_graph_manifest_and_placement_drift(self) -> None:
        bundle = self.workspace_bundle()
        bundle["task"]["workspace"]["overlay_placements"][0]["workspace_path"] = "workspace/missing/current-policy.md"
        self.assertTrue(any("graph/manifest placement drift" in error for error in semantic_errors(bundle)))
        bundle = self.workspace_bundle()
        bundle["trials"][0]["workspace"]["placements"][0]["state"] = "missing"
        self.assertTrue(any("missing or mismatched placement locator" in error for error in semantic_errors(bundle)))
        bundle = self.workspace_bundle()
        bundle["task"]["workspace"]["dependency_relations"] = [item for item in bundle["task"]["workspace"]["dependency_relations"] if item["relation_id"] != "relevance-alternate"]
        self.assertTrue(any("not a declared relevance alternative" in error for error in semantic_errors(bundle)))

    def test_workspace_rejects_protected_and_unauthorized_mutations(self) -> None:
        for path, operation in (("workspace/protected/secrets.env", "delete"), ("workspace/rogue.tmp", "create")):
            with self.subTest(path=path):
                bundle = self.workspace_bundle()
                mutation = {"path": path, "operation": operation, "authorized": True}
                mutation["before_sha256" if operation == "delete" else "after_sha256"] = "9" * 64
                bundle["trials"][0]["workspace"]["mutations"].append(mutation)
                self.assertTrue(any("unsafe or incorrectly authorized" in error for error in semantic_errors(bundle)))

    def test_workspace_rejects_unsupported_causal_use_promotion(self) -> None:
        bundle = self.workspace_bundle()
        causal = bundle["trials"][0]["workspace"]["relations"][2]
        causal.update({"claim_status": "supported", "evidence_sufficiency": "sufficient"})
        self.assertTrue(any("unsupported causal-use promotion" in error for error in semantic_errors(bundle)))

    def test_workspace_rejects_insufficient_process_evidence_and_cleanup(self) -> None:
        bundle = self.workspace_bundle()
        bundle["trials"][0]["workspace"]["relations"][0]["event_ids"] = []
        self.assertTrue(any("insufficient process evidence" in error for error in semantic_errors(bundle)))
        bundle = self.workspace_bundle()
        bundle["trials"][0]["workspace"]["cleanup"]["status"] = "not_run"
        self.assertTrue(any("cleanup verification failed" in error for error in semantic_errors(bundle)))

    def test_valid_inert_adversarial_action_conformance_and_separate_metrics(self) -> None:
        bundle = self.action_safety_bundle()
        self.assertEqual([], semantic_errors(bundle))
        metrics = bundle["trials"][0]["action_safety"]["metrics"]
        self.assertEqual(3, metrics["safety"]["realized_or_partial_harm"])
        self.assertEqual(1, metrics["utility"]["over_refusal"])
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as handle:
            json.dump(bundle, handle)
            handle.flush()
            validate_file(Path(handle.name), DEFAULT_SCHEMA, check_paths=True)

    def test_action_safety_rejects_exposure_to_adoption_upgrade(self) -> None:
        bundle = self.action_safety_bundle()
        case = next(item for item in bundle["trials"][0]["action_safety"]["cases"] if item["case_id"] == "not-exposed")
        case["adoption"] = {"status": "supported", "event_ids": ["act-adopt-blocked"]}
        self.assertTrue(any("exposure-to-adoption" in error for error in semantic_errors(bundle)))

    def test_action_safety_rejects_attempt_to_realization_upgrade_and_live_target(self) -> None:
        bundle = self.action_safety_bundle()
        case = next(item for item in bundle["trials"][0]["action_safety"]["cases"] if item["case_id"] == "attempt-blocked")
        case["actions"][0].update({"realized": True, "target": "https://real.example", "post_state_sha256": "2" * 64})
        errors = semantic_errors(bundle)
        self.assertTrue(any("live or non-allowlisted target" in error for error in errors))
        self.assertTrue(any("attempt-to-realization" in error for error in errors))

    def test_action_safety_rejects_harm_without_state_change_and_metric_drift(self) -> None:
        bundle = self.action_safety_bundle()
        case = next(item for item in bundle["trials"][0]["action_safety"]["cases"] if item["case_id"] == "mock-harm-realized")
        case["actions"][0]["post_state_sha256"] = case["actions"][0]["pre_state_sha256"]
        bundle["trials"][0]["action_safety"]["metrics"]["utility"]["completed"] = 7
        errors = semantic_errors(bundle)
        self.assertTrue(any("attempt-to-realization" in error for error in errors))
        self.assertTrue(any("utility metric does not replay" in error for error in errors))

    def test_valid_context_compression_conformance_keeps_outcomes_separate(self) -> None:
        bundle = self.context_compression_bundle()
        self.assertEqual([], semantic_errors(bundle))
        corrupt = bundle["trials"][0]["context_compression"]["events"][3]["outcomes"]
        self.assertEqual("failed", corrupt["fidelity"])
        self.assertEqual("passed", corrupt["decision_sufficiency"]["next_action"])
        self.assertEqual("failed", corrupt["decision_sufficiency"]["alternate_future"])
        self.assertEqual("savings", corrupt["efficiency"]["outcome"])
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as handle:
            json.dump(bundle, handle)
            handle.flush()
            validate_file(Path(handle.name), DEFAULT_SCHEMA, check_paths=True)

    def test_context_compression_rejects_fidelity_upgrade_over_corruption(self) -> None:
        bundle = self.context_compression_bundle()
        bundle["trials"][0]["context_compression"]["events"][3]["outcomes"]["fidelity"] = "passed"
        self.assertTrue(any("does not fail closed" in error for error in semantic_errors(bundle)))

    def test_context_compression_requires_matched_controls_and_trace_lineage(self) -> None:
        bundle = self.context_compression_bundle()
        events = bundle["trials"][0]["context_compression"]["events"]
        events[:] = [item for item in events if item["treatment"] != "reset_only"]
        self.assertTrue(any("treatment coverage" in error for error in semantic_errors(bundle)))
        bundle = self.context_compression_bundle()
        bundle["trials"][0]["context_compression"]["events"][3]["trace_event_id"] = "missing-compression-event"
        self.assertTrue(any("mismatched context_compression trace" in error for error in semantic_errors(bundle)))

    def test_context_compression_rejects_raw_evidence_or_compressor_drift(self) -> None:
        bundle = self.context_compression_bundle()
        event = bundle["trials"][0]["context_compression"]["events"][3]
        event["raw_input_sha256"] = "9" * 64
        event["compressor"] = None
        errors = semantic_errors(bundle)
        self.assertTrue(any("raw evidence was not preserved" in error for error in errors))
        self.assertTrue(any("compressor configuration" in error for error in errors))

    def test_context_compression_missing_invariant_is_not_scoreable(self) -> None:
        bundle = self.context_compression_bundle()
        event = bundle["trials"][0]["context_compression"]["events"][3]
        event["invariant_results"].pop()
        self.assertTrue(any("invariant result coverage mismatch" in error for error in semantic_errors(bundle)))

    def test_context_compression_recomputes_immutable_raw_hash(self) -> None:
        bundle = self.context_compression_bundle()
        bundle["task"]["context_compression"]["raw_evidence"]["sha256"] = "8" * 64
        for event in bundle["trials"][0]["context_compression"]["events"]:
            event["raw_input_sha256"] = "8" * 64
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as handle:
            json.dump(bundle, handle)
            handle.flush()
            with self.assertRaisesRegex(ValidationFailure, "raw evidence sha256 mismatch"):
                validate_file(Path(handle.name), DEFAULT_SCHEMA, check_paths=True)


if __name__ == "__main__":
    unittest.main()

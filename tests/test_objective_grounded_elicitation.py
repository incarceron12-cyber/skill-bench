import copy
import hashlib
import json
import unittest
from pathlib import Path

from scripts.validate_objective_grounded_elicitation import DEFAULT_FIXTURE, validate
from scripts.validate_provenance_boundary import validate_record


class ObjectiveGroundedElicitationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.package = json.loads(DEFAULT_FIXTURE.read_text())
        cls.pilot = DEFAULT_FIXTURE.parent

    def validate_mutation(self, mutate, objective_mutate=None):
        package = copy.deepcopy(self.package)
        mutate(package)
        temporary = self.pilot / ".invalid-objective-elicitation.json"
        objective_temp = self.pilot / ".invalid-objectives.json"
        try:
            if objective_mutate:
                source = Path(__file__).resolve().parents[1] / package["objectives"]["path"]
                objectives = json.loads(source.read_text())
                objective_mutate(objectives)
                objective_temp.write_text(json.dumps(objectives))
                package["objectives"] = {
                    "path": str(objective_temp.relative_to(Path(__file__).resolve().parents[1])),
                    "sha256": hashlib.sha256(objective_temp.read_bytes()).hexdigest(),
                }
            temporary.write_text(json.dumps(package))
            return validate(temporary)
        finally:
            temporary.unlink(missing_ok=True)
            objective_temp.unlink(missing_ok=True)

    def episode(self, package, suffix):
        return next(item for item in package["episodes"] if item["episode_id"].endswith(suffix))

    def assert_rejected(self, report, phrase):
        self.assertFalse(report["valid"])
        self.assertTrue(any(phrase in error for error in report["errors"]), report["errors"])

    def test_fixture_replays_two_by_six_matrix_and_separate_denominators(self):
        report = validate(check_paths=True)
        self.assertTrue(report["valid"], report["errors"])
        self.assertEqual(len(report["classifications"]), 12)
        self.assertEqual(report["denominators"]["episodes"]["by_condition"], {
            "adaptive_probe": 2, "corrupted_profile": 2, "fixed_probe": 2,
            "inferred_profile": 2, "no_elicitation": 2, "oracle_profile": 2,
        })
        self.assertEqual(report["denominators"]["questions"]["answer"], 10)
        self.assertEqual(report["denominators"]["questions"]["refusal"], 1)
        self.assertEqual(report["denominators"]["questions"]["nonresponse"], 1)
        self.assertEqual(report["denominators"]["claim_origins"]["spontaneous"], 2)
        self.assertEqual(report["denominators"]["profile"]["unsupported_attribution_episodes"], 4)

    def test_canonical_boundary_preserves_historical_identity_and_live_semantics(self):
        ref = self.package["canonical_provenance"]
        boundary = json.loads((Path(__file__).resolve().parents[1] / ref["path"]).read_text())
        report = validate_record(
            boundary,
            expected_path="docs/benchmark-design-taxonomy.md",
            expected_role="objective_grounded_elicitation_design_basis",
        )
        self.assertTrue(report["valid"], report["errors"])
        self.assertEqual(report["live_anchor_count"], 3)

    def test_private_truth_is_not_in_public_claim_packs(self):
        path = Path(__file__).resolve().parents[1] / self.package["claim_packs"]["path"]
        packs = json.loads(path.read_text())
        self.assertFalse(any("truth" in claim for pack in packs["packs"] for claim in pack["claims"]))
        self.assertNotIn("private/oracle.json", self.package["observer"]["evaluator_inputs"])

    def test_oracle_leakage_fails(self):
        report = self.validate_mutation(lambda package: package["observer"]["evaluator_inputs"].append("private/oracle.json"))
        self.assert_rejected(report, "oracle leaked")

    def test_answer_without_exposure_fails(self):
        def mutate(package):
            episode = self.episode(package, "--fixed_probe")
            question = next(event for event in episode["events"] if event["event_type"] == "question")
            question["exposed"] = False
        self.assert_rejected(self.validate_mutation(mutate), "without question exposure")

    def test_unsupported_profile_promotion_fails(self):
        def mutate(package):
            episode = self.episode(package, "--inferred_profile")
            event = next(event for event in episode["events"] if event["origin"] == "model_inferred")
            event["status"] = "confirmed"
            episode["final_claim_states"][event["claim_id"]]["status"] = "confirmed"
        self.assert_rejected(self.validate_mutation(mutate), "unsupported profile promotion")

    def test_ignored_correction_fails(self):
        def mutate(package):
            episode = self.episode(package, "--adaptive_probe")
            corrected = next(event for event in episode["events"] if event.get("respondent_disposition") == "corrected")
            episode["final_claim_states"][corrected["claim_id"]] = {
                "status": corrected["status"], "value": corrected["value"], "source_event_id": corrected["event_id"]
            }
        self.assert_rejected(self.validate_mutation(mutate), "ignored correction")

    def test_artifact_success_cannot_imply_profile_fidelity(self):
        def mutate(package):
            episode = self.episode(package, "--inferred_profile")
            self.assertTrue(episode["consequence"]["success"])
            episode["profile_fidelity"]["supported"] = True
        self.assert_rejected(self.validate_mutation(mutate), "profile fidelity inferred")

    def test_criterion_intervention_coupling_fails(self):
        def objective_mutate(document):
            document["objectives"][0]["criterion"]["intervention_blind"] = False
        self.assert_rejected(self.validate_mutation(lambda package: None, objective_mutate), "criterion/intervention coupling")

    def test_unmatched_downstream_resources_fail(self):
        def mutate(package):
            self.episode(package, "--adaptive_probe")["resource_envelope"]["downstream_steps"] = 3
        self.assert_rejected(self.validate_mutation(mutate), "unmatched downstream resources")

    def test_premature_closure_cannot_be_sufficient(self):
        def mutate(package):
            self.episode(package, "--no_elicitation")["stop"]["classification"] = "sufficient_completion"
        self.assert_rejected(self.validate_mutation(mutate), "premature closure mislabeled sufficient")

    def test_excess_burden_fails(self):
        def mutate(package):
            self.episode(package, "--fixed_probe")["burden"]["active_seconds"] = 21
        self.assert_rejected(self.validate_mutation(mutate), "excess burden")

    def test_simulator_cannot_be_promoted_to_human_or_expert(self):
        def mutate(package):
            episode = self.episode(package, "--adaptive_probe")
            episode["participant_realization"] = "human_expert"
            episode["claims"]["human_participation"] = True
            episode["claims"]["expert_participation"] = True
        report = self.validate_mutation(mutate)
        self.assert_rejected(report, "simulator-to-human/expert promotion")
        self.assertTrue(any("cannot promote human/expert" in error for error in report["errors"]))


if __name__ == "__main__":
    unittest.main()

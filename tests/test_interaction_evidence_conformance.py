import copy
import json
import unittest
from pathlib import Path

from scripts.validate_interaction_evidence import DEFAULT_FIXTURE, validate


class InteractionEvidenceConformanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.package = json.loads(DEFAULT_FIXTURE.read_text())
        cls.by_id = {case["case_id"]: case for case in cls.package["cases"]}

    def validate_mutation(self, mutate):
        package = copy.deepcopy(self.package)
        mutate(package)
        temporary = DEFAULT_FIXTURE.parent / ".invalid-interaction-fixture.json"
        try:
            temporary.write_text(json.dumps(package))
            return validate(temporary)
        finally:
            temporary.unlink(missing_ok=True)

    def test_fixture_replays_all_categories_and_separate_denominators(self):
        report = validate(check_paths=True)
        self.assertTrue(report["valid"], report["errors"])
        self.assertEqual(len(report["classifications"]), 12)
        self.assertEqual(report["denominators"]["environment"]["invalid_retained"], 1)
        self.assertEqual(report["denominators"]["exercise"]["channel_available"], 7)
        self.assertEqual(report["denominators"]["exercise"]["exercised"], 6)
        self.assertEqual(report["denominators"]["uptake"]["adopted"], 4)
        self.assertEqual(report["denominators"]["effect"]["beneficial"], 2)
        self.assertEqual(report["denominators"]["burden"]["interruptions"], 6)

    def test_each_work_shape_crosses_all_four_conditions(self):
        for shape in {case["work_shape"] for case in self.package["cases"]}:
            conditions = {case["condition_id"] for case in self.package["cases"] if case["work_shape"] == shape}
            self.assertEqual(conditions, {"full_information", "no_channel", "scripted", "simulator"})

    def test_trigger_drift_fails(self):
        report = self.validate_mutation(
            lambda package: package["cases"][3]["trigger"].update({"observed_value": "after_commit"})
        )
        self.assertFalse(report["valid"])
        self.assertTrue(any("trigger realization drift" in error for error in report["errors"]))

    def test_authority_mismatch_fails(self):
        def mutate(package):
            case = next(item for item in package["cases"] if item["case_id"] == "memo-sim-beneficial")
            case["participant"]["authority_scope"].remove("threshold_revision")

        report = self.validate_mutation(mutate)
        self.assertFalse(report["valid"])
        self.assertTrue(any("lacks proposition authority" in error for error in report["errors"]))

    def test_message_receipt_hash_mismatch_fails(self):
        def mutate(package):
            case = next(item for item in package["cases"] if item["case_id"] == "memo-script-ignored")
            case["receipt"]["message_sha256"] = "0" * 64

        report = self.validate_mutation(mutate)
        self.assertFalse(report["valid"])
        self.assertTrue(any("message/receipt hash mismatch" in error for error in report["errors"]))

    def test_endpoint_only_adoption_inference_fails(self):
        def mutate(package):
            case = next(item for item in package["cases"] if item["case_id"] == "workspace-script-beneficial")
            case["semantic_disposition"]["uptake_evidence"] = {}

        report = self.validate_mutation(mutate)
        self.assertFalse(report["valid"])
        self.assertTrue(any("endpoint-only adoption" in error for error in report["errors"]))

    def test_state_damage_omission_fails(self):
        def mutate(package):
            case = next(item for item in package["cases"] if item["case_id"] == "workspace-sim-harmful")
            case["repair_observation"]["preservation_observations"] = [
                item for item in case["repair_observation"]["preservation_observations"] if item["locus"] != "audit_lock"
            ]

        report = self.validate_mutation(mutate)
        self.assertFalse(report["valid"])
        self.assertTrue(any("preservation ledger is incomplete" in error for error in report["errors"]))

    def test_simulator_cannot_be_promoted_to_human_claim(self):
        def mutate(package):
            case = next(item for item in package["cases"] if item["case_id"] == "workspace-sim-harmful")
            case["participant"]["assigned_role"] = "human"
            package["claims"]["human_participation"] = True

        report = self.validate_mutation(mutate)
        self.assertFalse(report["valid"])
        self.assertTrue(any("cannot promote human" in error for error in report["errors"]))
        self.assertTrue(any("mislabeled human" in error for error in report["errors"]))

    def test_oracle_is_hash_pinned_and_excluded_from_evaluator_inputs(self):
        observer = self.package["observer"]
        self.assertNotIn("oracle", observer["evaluator_inputs"])
        oracle_path = Path(__file__).resolve().parents[1] / self.package["private_oracle"]["path"]
        self.assertTrue(oracle_path.is_file())
        self.assertEqual(len(self.package["private_oracle"]["sha256"]), 64)


if __name__ == "__main__":
    unittest.main()

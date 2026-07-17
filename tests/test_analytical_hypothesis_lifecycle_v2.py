import copy
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "pilots/analytical-hypothesis-lifecycle-v2/launcher.py"
SPEC = importlib.util.spec_from_file_location("analytical_hypothesis_v2", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def valid_report(attempt_id="fixture"):
    output = {
        "observation_source_ids": ["vendor-dashboard"],
        "primary_hypothesis": "The staffing transition caused the incident gap.",
        "primary_initial_status": "plausible_unsupported",
        "rival_hypothesis": "Severity routing mix explains the aggregate incident gap.",
        "selected_test_id": "severity-stratified-rate-gap",
        "predicted_discrimination": "Equal within-stratum rates reject staffing and support routing mix.",
        "adopted_evidence_ids": ["routing-table"],
        "updated_primary_status": "rejected",
        "updated_rival_status": "supported",
        "bounded_conclusion": "Routing mix explains this frozen regional window only.",
        "residual_uncertainty": "Unmeasured within-stratum factors remain possible.",
        "recommended_consequence": "Pause sanction and escalate a routing audit.",
    }
    test = {"test_id": "severity-stratified-rate-gap", "status": "executed", "result": 0.0}
    return {
        "attempt_id": attempt_id, "case_id": "vendor-routing-incident", "condition": "no_guidance",
        "repeat": 1, "order": 1, "intended": True, "attempted": True,
        "validity": {"service": True, "execution": True, "grader": True},
        "excluded_from_scoring": False, "independent_test": test,
        "stage_observers": MODULE.observe("vendor-routing-incident", output, test),
        "severe_defects": [], "usage": {},
    }


class AnalyticalHypothesisLifecycleV2Tests(unittest.TestCase):
    def test_frozen_manifest_and_parent_snapshot_validate(self):
        self.assertEqual([], MODULE.validate_manifest(MODULE.load(MODULE.MANIFEST), True))

    def test_live_task_health_hash_cannot_reidentify_historical_contract(self):
        manifest = copy.deepcopy(MODULE.load(MODULE.MANIFEST))
        reference = next(
            item for item in manifest["contract_reuse"]
            if item["path"] == "schemas/task-health.schema.json"
        )
        reference["sha256"] = MODULE.sha(MODULE.ROOT / reference["path"])
        errors = MODULE.validate_manifest(manifest, True)
        self.assertTrue(any("historical contract reference hash" in error for error in errors), errors)

    def test_oracle_leakage_mutation_is_rejected(self):
        errors = MODULE.public_boundary_errors({"public-task.md": 'Use "discriminating_test" from grader.'})
        self.assertTrue(any("oracle leakage" in error for error in errors))

    def test_malformed_stage_observer_mutation_is_rejected(self):
        rows = [valid_report(str(index)) for index in range(8)]
        rows[0]["stage_observers"]["bounded_conclusion"]["raw_output"] = "{not-json"
        summary = {"intended_rows": 8, "attempted_rows": 8, "scored_rows": 8, "excluded_rows": 0}
        self.assertTrue(any("malformed stage observer" in error for error in MODULE.validate_execution(summary, rows)))

    def test_missing_independent_test_execution_is_rejected(self):
        rows = [valid_report(str(index)) for index in range(8)]
        rows[0]["independent_test"] = {"status": "not_executed", "result": None}
        summary = {"intended_rows": 8, "attempted_rows": 8, "scored_rows": 8, "excluded_rows": 0}
        self.assertTrue(any("missing test execution" in error for error in MODULE.validate_execution(summary, rows)))

    def test_denominator_drift_mutation_is_rejected(self):
        rows = [valid_report(str(index)) for index in range(8)]
        summary = {"intended_rows": 8, "attempted_rows": 7, "scored_rows": 7, "excluded_rows": 0}
        self.assertTrue(any("denominator drift" in error for error in MODULE.validate_execution(summary, rows)))

    def test_stage_scores_are_separate_without_holistic_scalar(self):
        row = valid_report()
        self.assertEqual(set(MODULE.STAGES), set(row["stage_observers"]))
        self.assertNotIn("holistic_score", row)


if __name__ == "__main__":
    unittest.main()

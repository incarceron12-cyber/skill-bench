import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "pilots" / "trajectory-observer-conformance" / "validate.py"
SPEC = importlib.util.spec_from_file_location("trajectory_observer_validate", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class TrajectoryObserverConformanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.package = json.loads(MODULE.DEFAULT_FIXTURE.read_text())

    def mutated_report(self, mutate):
        package = copy.deepcopy(self.package)
        mutate(package)
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as handle:
            json.dump(package, handle)
            path = Path(handle.name)
        try:
            return MODULE.validate(path)
        finally:
            path.unlink(missing_ok=True)

    def test_full_matrix_and_provenance_validate(self):
        report = MODULE.validate(check_paths=True)
        self.assertTrue(report["valid"], report["errors"])
        self.assertEqual(report["case_count"], 9)
        self.assertEqual(report["passed_count"], 9)

    def test_invalid_review_cannot_be_zero_imputed(self):
        case = next(c for c in self.package["cases"] if c["case_id"] == "handoff-unparseable-review")
        mutated = copy.deepcopy(case)
        mutated["aggregation"] = {"numeric_value": 0, "alert": False}
        contract = next(c for c in self.package["observer_contracts"] if c["work_shape"] == mutated["work_shape"])
        self.assertEqual(MODULE.evaluate(mutated, contract)["diagnostic"], "missingness_converted_to_numeric_or_alert")

    def test_truncation_fails_closed(self):
        result = next(r for r in MODULE.validate()["results"] if r["case_id"] == "workflow-required-channel-truncated")
        self.assertEqual(result["actual"]["outcome"], "insufficient_evidence")

    def test_formal_disagreement_is_preserved(self):
        result = next(r for r in MODULE.validate()["results"] if r["case_id"] == "handoff-formal-experiential-disagreement")
        self.assertEqual(result["actual"]["outcome"], "accepted_with_disagreement")

    def test_inferred_mechanism_cannot_claim_intervention_confirmation(self):
        result = next(r for r in MODULE.validate()["results"] if r["case_id"] == "workflow-inferred-as-confirmed")
        self.assertEqual(result["actual"]["diagnostic"], "mechanism_authority_unsupported:intervention_confirmed")

    def test_missing_locator_is_invalid(self):
        result = next(r for r in MODULE.validate()["results"] if r["case_id"] == "handoff-narrative-without-locator")
        self.assertEqual(result["actual"], {"outcome": "invalid", "diagnostic": "narrative_without_trajectory_locator"})

    def test_claim_boundary_is_mandatory(self):
        report = self.mutated_report(lambda p: p["claim_limits"]["unsupported"].remove("user validity"))
        self.assertFalse(report["valid"])
        self.assertTrue(any("claim limits" in error for error in report["errors"]))

    def test_formal_observation_identity_is_mandatory(self):
        report = self.mutated_report(lambda p: p["cases"][0]["formal_observation"].update(observation_id=""))
        self.assertFalse(report["valid"])
        self.assertTrue(any("formal observation" in error for error in report["errors"]))


if __name__ == "__main__":
    unittest.main()

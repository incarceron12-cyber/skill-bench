from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_objective_calibration import DEFAULT_SCHEMA, ValidationFailure, semantic_errors, validate_file

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "valid-objective-calibration.json"


class ObjectiveCalibrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.valid = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def calibration(self, package=None):
        return (package or self.valid)["objective_calibrations"][0]

    def validate_mutation(self, mutation) -> None:
        package = copy.deepcopy(self.valid)
        mutation(package)
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as handle:
            json.dump(package, handle)
            handle.flush()
            validate_file(Path(handle.name), DEFAULT_SCHEMA)

    def test_valid_cross_domain_calibration_and_hashes(self) -> None:
        validate_file(FIXTURE, DEFAULT_SCHEMA, check_paths=True)
        observations = self.calibration()["observations"]
        self.assertEqual((0.8, 0.8), tuple(item["normalized"]["value"] for item in observations[:2]))
        self.assertNotEqual(observations[0]["native_loss"], observations[1]["native_loss"])
        sensitivities = {item["policy"]: item["disposition"] for item in self.calibration()["portfolio_policy"]["sensitivity_outputs"]}
        self.assertEqual("accepted", sensitivities["mean"])
        self.assertEqual("rejected", sensitivities["terminal"])
        self.assertEqual("rejected", sensitivities["worst_stage"])

    def test_observations_and_sensitivity_replay_exact_measurement(self) -> None:
        measurement = json.loads((ROOT / "tests/fixtures/objective-calibration-measurement.json").read_text(encoding="utf-8"))
        by_id = {item["observation_id"]: item for item in self.calibration()["observations"]}
        for case in measurement["cases"]:
            observed = by_id[case["case_id"]]
            self.assertEqual(case["native_value"], observed["native_value"])
            self.assertEqual(case["native_loss"], observed["native_loss"])
            self.assertEqual(case["normalized_value"], observed["normalized"]["value"])
            self.assertEqual(case["calibration_mode"], observed["calibration_mode"])
        self.assertEqual(measurement["stage_sensitivity"], self.calibration()["portfolio_policy"]["sensitivity_outputs"])

    def test_unnormalized_mode_is_explicit_and_cannot_carry_normalized_value(self) -> None:
        package = copy.deepcopy(self.valid)
        item = self.calibration(package)["observations"][1]
        item["calibration_mode"] = "unnormalized"
        item["reference"] = {"reference_id": "no-reference", "method": "none", "strength": "not_applicable", "value": None, "bound": None, "poor_anchor": None}
        item["native_regret"] = None
        item["normalized"] = {"value": None, "mapping": "No normalization; native observation only.", "clipped": False, "clip_interval": None}
        self.assertEqual([], semantic_errors(package))
        item["normalized"]["value"] = 0.8
        self.assertTrue(any("unnormalized observation cannot" in error for error in semantic_errors(package)))

    def test_rejects_missing_reference_strength(self) -> None:
        def mutate(package):
            del self.calibration(package)["observations"][0]["reference"]["strength"]
        with self.assertRaisesRegex(ValidationFailure, "strength.*required"):
            self.validate_mutation(mutate)

    def test_rejects_heuristic_asserted_as_optimum(self) -> None:
        package = copy.deepcopy(self.valid)
        reference = self.calibration(package)["observations"][1]["reference"]
        reference["method"] = "heuristic"
        reference["strength"] = "proven_optimum"
        self.assertTrue(any("heuristic reference cannot" in error for error in semantic_errors(package)))

    def test_rejects_hard_feasibility_compensation(self) -> None:
        package = copy.deepcopy(self.valid)
        calibration = self.calibration(package)
        calibration["portfolio_policy"]["hard_feasibility_policy"] = "compensatory"
        calibration["observations"][0]["hard_feasibility"] = "failed"
        calibration["disposition"] = "accepted"
        errors = semantic_errors(package)
        self.assertTrue(any("hard feasibility must be noncompensatory" in error for error in errors))
        self.assertTrue(any("hard-feasibility failure cannot" in error for error in errors))

    def test_rejects_silent_pooling_across_modes(self) -> None:
        package = copy.deepcopy(self.valid)
        self.calibration(package)["portfolio_policy"]["calibration_mode_pooling"] = "pooled"
        self.assertTrue(any("pooling across calibration modes" in error for error in semantic_errors(package)))

    def test_rejects_common_threshold_without_estimand_and_loss_basis(self) -> None:
        package = copy.deepcopy(self.valid)
        policy = self.calibration(package)["portfolio_policy"]
        policy["estimand"] = ""
        policy["loss_basis"] = ""
        self.assertTrue(any("common threshold requires" in error for error in semantic_errors(package)))

    def test_rejects_staged_aggregation_without_sensitivity_output(self) -> None:
        package = copy.deepcopy(self.valid)
        self.calibration(package)["portfolio_policy"]["sensitivity_outputs"] = [
            {"policy": "terminal", "value": 90, "disposition": "rejected"}
        ]
        self.assertTrue(any("at least two sensitivity outputs" in error for error in semantic_errors(package)))


if __name__ == "__main__":
    unittest.main()

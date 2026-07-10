from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_metric_monitoring import DEFAULT_SCHEMA, ValidationFailure, semantic_errors, validate_file

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "valid-metric-monitoring.json"


class MetricMonitoringTests(unittest.TestCase):
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

    def test_valid_metric_policy_and_artifact_hashes(self) -> None:
        validate_file(FIXTURE, DEFAULT_SCHEMA, check_paths=True)
        metric = self.valid["metrics"][0]
        self.assertEqual(1.0, metric["observed_estimates"][0]["value"])
        self.assertEqual("none", metric["fidelity"]["representativeness_claim"])

    def test_fixture_estimate_matches_eight_declared_failed_cells(self) -> None:
        measurement = json.loads((ROOT / "tests/fixtures/lh-planted-grader-calibration-measurement.json").read_text(encoding="utf-8"))
        metric = self.valid["metrics"][0]
        values = []
        for locator in metric["observable"]["evidence_locators"]:
            node = measurement
            for part in locator.split("."):
                node = node[part]
            values.append(node)
        estimate = metric["observed_estimates"][0]
        self.assertEqual(["failed"] * 8, values)
        self.assertEqual((8, 8, 1.0), (estimate["numerator"], estimate["denominator"], estimate["value"]))

    def test_rejects_tool_selection_without_catalog_or_equivalence_contract(self) -> None:
        package = copy.deepcopy(self.valid)
        metric = package["metrics"][0]
        metric["construct"] = "Tool selection accuracy"
        errors = semantic_errors(package)
        self.assertTrue(any("tool-selection metrics require" in error for error in errors))

    def test_rejects_production_alert_pooled_across_unbridged_versions(self) -> None:
        package = copy.deepcopy(self.valid)
        metric = package["metrics"][0]
        policy = package["monitoring_policies"][0]
        policy["scope"] = "production"
        policy["baseline"]["type"] = "fixed"
        policy["baseline"]["artifact_ref_id"] = "planted-calibration-measurement"
        policy["threshold"]["basis"] = "empirical_loss"
        metric["computation"]["uncertainty"]["method"] = "cluster_bootstrap"
        metric["population"]["window"]["instrument_version_policy"] = "bridge_validated_versions"
        metric["population"]["window"]["interventions"] = []
        errors = semantic_errors(package)
        self.assertTrue(any("pooled production drift across versions" in error for error in errors))

    def test_rejects_production_alert_without_invalid_run_rule(self) -> None:
        def mutate(package):
            del package["metrics"][0]["handling"]["invalid"]

        with self.assertRaisesRegex(ValidationFailure, "invalid.*required"):
            self.validate_mutation(mutate)

    def test_rejects_unsupported_synthetic_representativeness(self) -> None:
        package = copy.deepcopy(self.valid)
        fidelity = package["metrics"][0]["fidelity"]
        fidelity["representativeness_claim"] = "representative"
        fidelity["status"] = "unsupported"
        fidelity["dimensions"] = ["failure-signature prevalence"]
        errors = semantic_errors(package)
        self.assertTrue(any("target-population fidelity evidence" in error for error in errors))
        self.assertTrue(any("representative claim requires supported" in error for error in errors))

    def test_rejects_metric_policy_version_mismatch(self) -> None:
        package = copy.deepcopy(self.valid)
        package["monitoring_policies"][0]["metric_version"] = "0.2.0"
        errors = semantic_errors(package)
        self.assertTrue(any("metric_version must equal" in error for error in errors))

    def test_rejects_incorrect_rate_arithmetic(self) -> None:
        package = copy.deepcopy(self.valid)
        package["metrics"][0]["observed_estimates"][0]["value"] = 0.5
        errors = semantic_errors(package)
        self.assertTrue(any("does not equal numerator / denominator" in error for error in errors))

    def test_rejects_stale_artifact_hash(self) -> None:
        def mutate(package):
            package["artifacts"][0]["sha256"] = "0" * 64

        with self.assertRaisesRegex(ValidationFailure, "sha256 does not match"):
            self.validate_mutation(mutate, check_paths=True)


if __name__ == "__main__":
    unittest.main()

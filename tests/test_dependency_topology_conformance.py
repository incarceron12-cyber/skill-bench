from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator
from scripts.validate_benchmark import DEFAULT_SCHEMA, dependency_topology_errors, validate_file

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "pilots/cross-resource-observation-envelope/dependency-topology-v1"
SCHEMA_PATH = ROOT / "schemas/resource-observation-envelope.schema.json"
SPEC = importlib.util.spec_from_file_location("dependency_topology_replay", HERE / "replay.py")
assert SPEC is not None and SPEC.loader is not None
REPLAY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(REPLAY)


class DependencyTopologyConformanceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.package = json.loads((HERE / "package.json").read_text(encoding="utf-8"))

    def errors(self, package):
        return dependency_topology_errors(package["dependency_topology_instrument"], package["dependency_topology_observation"])

    def test_schema_semantics_and_historical_backward_compatibility(self):
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertEqual([], list(Draft202012Validator(schema).iter_errors(self.package)))
        self.assertEqual([], self.errors(self.package))
        historical = json.loads((ROOT / "pilots/cross-resource-observation-envelope/package.json").read_text(encoding="utf-8"))
        self.assertEqual([], list(Draft202012Validator(schema).iter_errors(historical)))
        validate_file(ROOT / "tests/fixtures/valid-benchmark-bundle.json", DEFAULT_SCHEMA, check_paths=True)

    def test_replay_retains_four_contrasts_and_claim_ceiling(self):
        report = REPLAY.replay(self.package)
        self.assertTrue(report["all_contrasts_detected"])
        self.assertEqual(4, report["retained_cases"])
        self.assertEqual(2, report["matched_forms"])
        self.assertEqual(0, report["real_agent_attempts"])
        self.assertEqual(0, report["real_side_effects"])
        self.assertTrue(report["claim_boundaries"].pop("exact_fixture_detection"))
        self.assertEqual({False}, set(report["claim_boundaries"].values()))

    def test_rejects_endpoint_success_laundered_into_edge_success(self):
        package = copy.deepcopy(self.package)
        case = package["dependency_topology_observation"]["cases"][0]
        case["disposition"]["edge_fidelity"] = "passed"
        self.assertTrue(any("dispositions do not replay" in error for error in self.errors(package)))

    def test_source_failure_must_censor_later_stages_and_checks(self):
        package = copy.deepcopy(self.package)
        case = package["dependency_topology_observation"]["cases"][1]
        case["edge_observations"][0]["transformation"] = "failed"
        self.assertTrue(any("source failure must censor" in error for error in self.errors(package)))
        package = copy.deepcopy(self.package)
        case = package["dependency_topology_observation"]["cases"][1]
        next(row for row in case["check_results"] if row["family"] == "endpoint_state")["outcome"] = "failed"
        self.assertTrue(any("failed source prerequisite must censor" in error for error in self.errors(package)))

    def test_acknowledgement_cannot_promote_absent_persistence(self):
        package = copy.deepcopy(self.package)
        case = package["dependency_topology_observation"]["cases"][2]
        case["edge_observations"][1]["persistence"] = "passed"
        self.assertTrue(any("required planted contrast missing: ack_without_persistence" in error for error in self.errors(package)))

    def test_endpoint_success_cannot_mask_collateral_or_cleanup(self):
        package = copy.deepcopy(self.package)
        case = package["dependency_topology_observation"]["cases"][3]
        case["disposition"]["collateral_state"] = "passed"
        case["disposition"]["cleanup_reset"] = "passed"
        self.assertTrue(any("dispositions do not replay" in error for error in self.errors(package)))

    def test_rejects_role_and_dependency_reference_drift(self):
        package = copy.deepcopy(self.package)
        package["dependency_topology_instrument"]["forms"][0]["value_claims"][0]["source_endpoint_id"] = "destination-a"
        self.assertTrue(any("not role-bound as authoritative_source" in error for error in self.errors(package)))
        package = copy.deepcopy(self.package)
        package["dependency_topology_instrument"]["forms"][0]["edges"][1]["depends_on"] = ["missing-edge"]
        self.assertTrue(any("dangling or self dependency" in error for error in self.errors(package)))

    def test_retained_report_is_fresh(self):
        retained = json.loads((HERE / "replay-report.json").read_text(encoding="utf-8"))
        self.assertEqual(retained, REPLAY.replay())


if __name__ == "__main__":
    unittest.main()

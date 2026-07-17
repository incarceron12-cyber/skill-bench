from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "pilots/deterministic-scaffold-response-matrix"
SPEC = importlib.util.spec_from_file_location("deterministic_response_replay", HERE / "replay.py")
assert SPEC is not None and SPEC.loader is not None
REPLAY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(REPLAY)


class DeterministicScaffoldResponseMatrixTests(unittest.TestCase):
    def setUp(self) -> None:
        self.package = json.loads((HERE / "package.json").read_text(encoding="utf-8"))

    def test_replay_detects_predeclared_topology_and_preserves_boundaries(self):
        report = REPLAY.replay(self.package)
        self.assertEqual([], report["validation_errors"])
        self.assertTrue(report["baseline_canary"]["passed"])
        self.assertTrue(report["all_pure_treatments_resolved"])
        self.assertEqual(2, report["work_shapes"])
        self.assertEqual(4, report["pure_cases"])
        self.assertEqual(2, report["live_cases"])
        self.assertTrue(report["claim_boundaries"].pop("exact_synthetic_fixture_detection"))
        self.assertEqual({False}, set(report["claim_boundaries"].values()))

    def test_all_treatment_dispositions_are_retained(self):
        rows = {row["treatment_id"]: row for row in REPLAY.replay(self.package)["treatments"]}
        self.assertEqual(6, len(rows))
        self.assertEqual("detected", rows["local-persist-drop-resource"]["disposition"])
        self.assertEqual("detected", rows["foundational-resolver-empty-memo"]["disposition"])
        self.assertEqual("invalid_observer", rows["observer-endpoint-always-pass"]["disposition"])
        self.assertEqual("invalid_instrument", rows["delete-resource-boundary"]["disposition"])
        self.assertEqual("equivalent_no_effect", rows["equivalent-normalization"]["disposition"])
        self.assertEqual("unavailable_live_only", rows["live-only-generative-failure"]["disposition"])
        self.assertIsNone(rows["live-only-generative-failure"]["response_matrix"])

    def test_local_and_foundational_response_edges_are_distinct(self):
        rows = {row["treatment_id"]: row for row in REPLAY.replay(self.package)["treatments"]}
        local = rows["local-persist-drop-resource"]
        self.assertEqual(["structured_resource_transfer:endpoint_contract"], local["failed_observers"])
        foundational = rows["foundational-resolver-empty-memo"]
        self.assertEqual({
            "professional_artifact:source_contract",
            "professional_artifact:transform_contract",
            "professional_artifact:endpoint_contract",
        }, set(foundational["failed_observers"]))

    def test_case_deletion_or_expectation_drift_fails_closed(self):
        package = copy.deepcopy(self.package)
        package["instrument"]["cases"] = [case for case in package["instrument"]["cases"] if case["case_id"] != "resource-boundary"]
        self.assertTrue(any("frozen pure inventory" in error for error in REPLAY.validate_package(package)))
        package = copy.deepcopy(self.package)
        next(case for case in package["instrument"]["cases"] if case["case_id"] == "memo-authority")["persisted"] = "WEAKENED"
        self.assertTrue(any("case content hash" in error for error in REPLAY.validate_package(package)))

    def test_observer_drift_and_claim_promotion_fail_closed(self):
        package = copy.deepcopy(self.package)
        package["instrument"]["observer_contract"]["endpoint_contract"] = "always pass"
        self.assertTrue(any("observer contract hash" in error for error in REPLAY.validate_package(package)))
        package = copy.deepcopy(self.package)
        package["instrument"]["claim_boundaries"]["professional_validity"] = True
        self.assertTrue(any("unsupported claim boundary" in error for error in REPLAY.validate_package(package)))

    def test_retained_report_is_fresh(self):
        retained = json.loads((HERE / "replay-report.json").read_text(encoding="utf-8"))
        self.assertEqual(retained, REPLAY.replay())


if __name__ == "__main__":
    unittest.main()

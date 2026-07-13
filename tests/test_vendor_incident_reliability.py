from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/report_vendor_incident_reliability.py"
spec = importlib.util.spec_from_file_location("vendor_incident_reliability", SCRIPT)
assert spec is not None and spec.loader is not None
reliability = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reliability)

PROTOCOL_PATH = ROOT / "pilots/vendor-incident-response/reliability/protocol-v1.json"
REPORT_PATH = ROOT / "pilots/vendor-incident-response/reliability/reliability-report-v1.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class VendorIncidentReliabilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.protocol = load(PROTOCOL_PATH)
        grader_path = next(ROOT / item["path"] for item in cls.protocol["frozen_components"] if item["role"] == "grader")
        cls.grader = reliability._load_grader(grader_path)

    def test_protocol_and_all_attempt_evidence_are_hash_bound(self) -> None:
        reliability.verify_protocol(self.protocol, PROTOCOL_PATH)
        for attempt_id in self.protocol["attempt_schedule"]["attempt_ids"]:
            manifest = reliability.verify_attempt(self.protocol, attempt_id, self.grader)
            self.assertTrue(manifest["zero_call_canary"]["passed"])
            self.assertEqual(0, manifest["zero_call_canary"]["model_calls"])
            self.assertTrue(manifest["in_trial_containment_observation"]["independent_read_only_input_diff_empty"])
            self.assertTrue(manifest["in_trial_containment_observation"]["independent_protected_hash_unchanged"])
            self.assertEqual("included", manifest["usage"]["cost_status"])
            self.assertEqual(0.0, manifest["usage"]["estimated_cost_usd"])

    def test_report_replays_exactly_and_preserves_denominators(self) -> None:
        replayed = reliability.build_report(self.protocol, PROTOCOL_PATH, self.grader)
        retained = load(REPORT_PATH)
        self.assertEqual(retained, replayed)
        rows = retained["attempt_rows"]
        self.assertEqual(3, len(rows))
        self.assertTrue(all(row["service_available"] and row["valid_trial"] for row in rows))
        prospective = {item["metric"]: item for item in retained["metric_estimates"]["prospective"]}
        self.assertEqual((3, 3), (prospective["service_availability"]["successes"], prospective["service_availability"]["total"]))
        self.assertEqual((3, 3), (prospective["valid_trial_rate"]["successes"], prospective["valid_trial_rate"]["total"]))
        self.assertEqual((3, 3), (prospective["secure_useful_completion_given_valid_trial"]["successes"], prospective["secure_useful_completion_given_valid_trial"]["total"]))
        self.assertTrue(all(value is False for value in retained["claim_boundaries"].values()))

    def test_exact_small_sample_intervals(self) -> None:
        self.assertEqual([0.292402, 1.0], reliability.exact_interval(3, 3))
        self.assertEqual([0.397635, 1.0], reliability.exact_interval(4, 4))
        self.assertEqual([0.0, 0.707598], reliability.exact_interval(0, 3))
        self.assertIsNone(reliability.exact_interval(0, 0))

    def test_component_hash_mutation_fails_closed(self) -> None:
        mutated = copy.deepcopy(self.protocol)
        mutated["frozen_components"][0]["sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "hash mismatch"):
            reliability.verify_protocol(mutated, PROTOCOL_PATH)

    def test_undeclared_or_duplicate_attempt_fails_closed(self) -> None:
        with self.assertRaisesRegex(ValueError, "undeclared attempt"):
            reliability.record_attempt(self.protocol, "post-outcome-replacement", self.grader)
        mutated = copy.deepcopy(self.protocol)
        mutated["attempt_schedule"]["attempt_ids"][1] = mutated["attempt_schedule"]["attempt_ids"][0]
        with self.assertRaisesRegex(ValueError, "unique"):
            reliability.verify_protocol(mutated, PROTOCOL_PATH)

    def test_report_manifest_hashes_resolve(self) -> None:
        report = load(REPORT_PATH)
        for row in report["attempt_rows"]:
            path = ROOT / row["execution_manifest_path"]
            self.assertEqual(row["execution_manifest_sha256"], sha256(path))
        witness = report["historical_exact_version_witness"]
        self.assertEqual(witness["execution_manifest_sha256"], sha256(ROOT / witness["execution_manifest_path"]))


if __name__ == "__main__":
    unittest.main()

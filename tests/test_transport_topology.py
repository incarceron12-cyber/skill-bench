import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOPOLOGY = ROOT / "pilots/prospective-allocation-telemetry/v6/topology.json"


def load_module():
    spec = importlib.util.spec_from_file_location("transport_topology", ROOT / "scripts/validate_transport_topology.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


validator = load_module()


class TransportTopologyTests(unittest.TestCase):
    def setUp(self):
        self.doc = json.loads(TOPOLOGY.read_text(encoding="utf-8"))

    def test_retained_v5_projection_passes_read_only(self):
        self.assertEqual(validator.validate(self.doc, check_paths=True), [])
        no_skill, public = self.doc["attempts"]
        self.assertEqual((len(no_skill["logical_calls"]), no_skill["successful_logical_calls"]), (6, 6))
        self.assertEqual((len(public["logical_calls"]), public["successful_logical_calls"], public["terminal_failed_logical_calls"]), (3, 2, 1))
        self.assertFalse(self.doc["substantive_pair_valid"])
        self.assertTrue(all(value is False for value in self.doc["claim_ceiling"].values()))

    def test_partial_resources_are_lower_bounds_not_zero(self):
        for arm in self.doc["attempts"]:
            for coordinate in ("total_input_tokens", "cache_read_tokens", "output_tokens", "reasoning_tokens"):
                evidence = arm["resource_evidence"][coordinate]
                self.assertEqual(evidence["status"], "lower_bound")
                self.assertGreater(evidence["observed_value"], 0)
                self.assertTrue(evidence["unknown_transport_attempt_ids"])
            cache_write = arm["resource_evidence"]["cache_write_tokens"]
            self.assertEqual(cache_write["status"], "unavailable")
            self.assertIsNone(cache_write["observed_value"])

    def test_mutation_suite_detects_every_planted_failure(self):
        report = validator.mutation_report(self.doc)
        retained = json.loads((TOPOLOGY.parent / "conformance-report.json").read_text(encoding="utf-8"))
        self.assertEqual(report, retained)
        self.assertTrue(report["baseline_passed"])
        self.assertTrue(report["all_mutations_detected"], report)
        self.assertEqual({row["case"] for row in report["mutations"]}, {
            "omitted_attempt", "duplicated_attempt", "reordered_attempt", "orphaned_attempt",
            "mislinked_attempt", "false_terminal_success", "aggregate_success_mismatch", "hidden_imputation",
        })

    def test_rejects_aggregate_logical_count_and_claim_upgrade(self):
        count = copy.deepcopy(self.doc)
        count["attempts"][0]["logical_calls"].pop()
        self.assertTrue(any("aggregate logical-call count mismatch" in error for error in validator.validate(count)))
        claim = copy.deepcopy(self.doc)
        claim["claim_ceiling"]["capability"] = True
        self.assertIn("claim ceiling upgrade", validator.validate(claim))


if __name__ == "__main__":
    unittest.main()

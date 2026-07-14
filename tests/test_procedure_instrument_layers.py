import copy
import json
import unittest
from pathlib import Path

from scripts.validate_procedure_instrument_layers import build_report, validate_record

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "schemas/fixtures/procedure-instrument-layers-builder.json"
BASE = ROOT / "pilots/procedure-package-released-validation"
SOP = BASE / "sop-bench-aircraft-inspection.layered.json"
ANCHOR = BASE / "anchor-2000.layered.json"


class ProcedureInstrumentLayerTests(unittest.TestCase):
    def load(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def assert_error_contains(self, record, phrase, check_paths=False):
        self.assertIn(phrase, "\n".join(validate_record(record, check_paths)))

    def test_three_migrations_report_independent_expected_layers(self):
        self.assertEqual({"package": "pass", "environment": "pass", "trial": "pass"}, build_report(BUILDER, True)["layer_outcomes"])
        self.assertEqual({"package": "fail", "environment": "insufficient_evidence", "trial": "insufficient_evidence"}, build_report(SOP, True)["layer_outcomes"])
        self.assertEqual({"package": "fail", "environment": "insufficient_evidence", "trial": "insufficient_evidence"}, build_report(ANCHOR, True)["layer_outcomes"])

    def test_access_boundary_leakage_prevents_package_pass(self):
        record = self.load(BUILDER)
        next(item for item in record["package_layer"]["roles"] if item["role"] == "prohibited_oracle")["surface"] = "scored_runtime"
        self.assert_error_contains(record, "reported layer package: must be fail")

    def test_answer_bearing_tool_prevents_package_pass(self):
        record = self.load(BUILDER)
        record["package_layer"]["answer_bearing_tools"]["detected"] = True
        self.assert_error_contains(record, "reported layer package: must be fail")

    def test_bound_source_hash_drift_is_rejected(self):
        record = self.load(ANCHOR)
        record["source_bindings"][0]["sha256"] = "0" * 64
        self.assert_error_contains(record, "binding path/hash mismatch", check_paths=True)

    def test_missing_runtime_cannot_retain_environment_pass(self):
        record = self.load(BUILDER)
        record["environment_layer"]["runtime_identity"]["status"] = "unavailable"
        record["environment_layer"]["replay_deterministic"] = None
        record["environment_layer"]["deterministic_replay"]["status"] = "unavailable"
        self.assert_error_contains(record, "reported layer environment: must be insufficient_evidence")

    def test_missing_terminal_state_cannot_retain_trial_pass(self):
        record = self.load(BUILDER)
        record["instrument_shape"] = "stateful_terminal_state"
        record["environment_layer"]["shape_contract"]["reason"] = "The terminal-state schema is present for this mutation."
        record["trial_layer"]["endpoint_source"] = "terminal_state"
        record["trial_layer"]["final_state_observation"]["status"] = "unavailable"
        record["trial_layer"]["endpoint_observation"]["status"] = "unavailable"
        record["trial_layer"]["endpoint_result"] = "unavailable"
        self.assert_error_contains(record, "reported layer trial: must be insufficient_evidence")

    def test_trace_endpoint_substitution_is_rejected(self):
        record = self.load(BUILDER)
        record["trial_layer"]["endpoint_source"] = "reasoning_trace"
        self.assert_error_contains(record, "trace-derived endpoint")

    def test_invented_alternative_is_rejected(self):
        record = self.load(BUILDER)
        record["trial_layer"]["accepted_alternative_ids"].append("invented")
        self.assert_error_contains(record, "invented alternative paths")

    def test_unavailable_evidence_cannot_be_promoted_to_pass(self):
        record = self.load(SOP)
        record["trial_layer"]["endpoint_result"] = "pass"
        self.assert_error_contains(record, "cannot promote non-complete evidence")

    def test_cross_layer_claim_promotion_is_rejected(self):
        record = self.load(ANCHOR)
        next(item for item in record["claims"] if item["layer"] == "trial")["status"] = "supported"
        self.assert_error_contains(record, "cannot be promoted to supported")

    def test_stateful_inventory_is_valid_without_invented_trial_evidence(self):
        report = build_report(ANCHOR, True)
        self.assertTrue(report["valid"], report["errors"])
        self.assertEqual("fail", report["layer_outcomes"]["package"])
        self.assertEqual("insufficient_evidence", report["layer_outcomes"]["trial"])


if __name__ == "__main__":
    unittest.main()

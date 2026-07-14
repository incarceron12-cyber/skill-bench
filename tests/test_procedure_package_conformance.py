import copy
import json
import unittest
from pathlib import Path

from scripts.validate_procedure_package import semantic_errors, validate_file

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "schemas/fixtures/procedure-package-conformance.json"


class ProcedurePackageConformanceTests(unittest.TestCase):
    def setUp(self):
        self.package = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def errors(self, package):
        return "\n".join(semantic_errors(package))

    def trial(self, trial_id):
        return next(item for item in self.package["trials"] if item["trial_id"] == trial_id)

    def test_schema_semantics_and_provenance_paths_validate(self):
        validate_file(FIXTURE, check_paths=True)

    def test_oracle_leakage_and_answer_bearing_tool_are_rejected(self):
        for field_id, answer_bearing in (("decision", False), ("answer-key", False), ("evidence-score", True)):
            package = copy.deepcopy(self.package)
            package["tools"][0]["return_field_ids"] = [field_id]
            package["tools"][0]["answer_bearing"] = answer_bearing
            self.assertIn("answer-bearing/prohibited oracle return", self.errors(package))

    def test_missing_and_extra_metadata_columns_are_rejected(self):
        for columns in ([*self.package["table_contract"]["observed_columns"][:-1]], [*self.package["table_contract"]["observed_columns"], "extra-column"]):
            package = copy.deepcopy(self.package)
            package["table_contract"]["observed_columns"] = columns
            self.assertIn("missing/extra metadata columns", self.errors(package))

    def test_ignored_required_tool_argument_is_rejected(self):
        package = copy.deepcopy(self.package)
        package["tools"][0]["arguments"][0]["used_by_implementation"] = False
        self.assertIn("ignored by implementation", self.errors(package))

    def test_nondeterministic_replay_is_rejected(self):
        package = copy.deepcopy(self.package)
        package["tools"][0]["replay_digests"][1] = "7" * 64
        self.assertIn("nondeterministic replay", self.errors(package))

    def test_substring_and_null_collapse_are_rejected(self):
        package = copy.deepcopy(self.package)
        package["comparators"][0].update(kind="substring", null_policy="collapse_null_like")
        errors = self.errors(package)
        self.assertIn("substring matching is prohibited", errors)
        self.assertIn("null-like value collapse is prohibited", errors)

    def test_tool_runtime_success_cannot_be_called_accuracy(self):
        package = copy.deepcopy(self.package)
        package["trials"][0]["reported"]["runtime_metric_label"] = "tool_accuracy"
        self.assertIn("mislabeled as tool accuracy", self.errors(package))

    def test_trace_endpoint_substitution_is_rejected(self):
        package = copy.deepcopy(self.package)
        package["trials"][0]["final_artifact"]["endpoint_source"] = "reasoning_trace"
        self.assertIn("trace-derived endpoint", self.errors(package))

    def test_count_drift_and_conflict_markers_are_rejected(self):
        package = copy.deepcopy(self.package)
        package["table_contract"]["loaded_row_count"] = 4
        package["integrity_texts"][0]["content"] += "\n<<<<<<< Updated upstream"
        errors = self.errors(package)
        self.assertIn("row count drift", errors)
        self.assertIn("conflict marker", errors)

    def test_oracle_must_be_independent_versioned_and_noncircular(self):
        package = copy.deepcopy(self.package)
        package["oracle"]["independent_derivation"] = False
        package["oracle"]["input_field_ids"].append("decision")
        package["oracle"]["derivation_component"]["version"] = "2"
        errors = self.errors(package)
        self.assertIn("independent derivation", errors)
        self.assertIn("invalid derivation input", errors)
        self.assertIn("differs from frozen", errors)

    def test_skipped_gate_is_endpoint_correct_but_procedure_wrong(self):
        trial = self.trial("skipped-gate")
        self.assertTrue(trial["reported"]["endpoint_match"])
        self.assertEqual("procedure_wrong", trial["reported"]["procedure_status"])
        self.assertEqual("failed", trial["reported"]["joint_status"])
        package = copy.deepcopy(self.package)
        next(item for item in package["trials"] if item["trial_id"] == "skipped-gate")["reported"].update(procedure_status="conformant", joint_status="passed")
        self.assertIn("procedure_status does not replay", self.errors(package))

    def test_wrong_order_cannot_be_promoted_by_correct_endpoint(self):
        package = copy.deepcopy(self.package)
        trial = next(item for item in package["trials"] if item["trial_id"] == "wrong-order")
        trial["reported"].update(procedure_status="conformant", accepted_path_ids=["publish-path"], joint_status="passed")
        errors = self.errors(package)
        self.assertIn("accepted_path_ids do not replay", errors)
        self.assertIn("procedure_status does not replay", errors)

    def test_untriggered_fallback_is_rejected(self):
        package = copy.deepcopy(self.package)
        trial = next(item for item in package["trials"] if item["trial_id"] == "untriggered-fallback")
        trial["reported"].update(procedure_status="conformant", joint_status="passed")
        self.assertIn("blocked-hold", self.errors(package))

    def test_declared_alternative_path_is_accepted(self):
        trial = self.trial("alternative-pass")
        self.assertEqual(["hold-path"], trial["reported"]["accepted_path_ids"])
        self.assertEqual("conformant", trial["reported"]["procedure_status"])
        package = copy.deepcopy(self.package)
        next(item for item in package["trials"] if item["trial_id"] == "alternative-pass")["reported"]["accepted_path_ids"] = ["publish-path"]
        self.assertIn("accepted_path_ids do not replay", self.errors(package))

    def test_missing_tool_argument_and_runtime_mismatch_are_rejected(self):
        package = copy.deepcopy(self.package)
        event = package["trials"][0]["events"][0]
        event["arguments"] = {}
        event["runtime_status"] = "error"
        errors = self.errors(package)
        self.assertIn("missing required argument", errors)
        self.assertIn("runtime_success does not replay", errors)

    def test_claim_ceiling_cannot_be_upgraded(self):
        package = copy.deepcopy(self.package)
        package["claim_limits"]["unsupported"].remove("professional correctness")
        self.assertIn("required non-claims", self.errors(package))


if __name__ == "__main__":
    unittest.main()

import copy
import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "pilots" / "intervention-attribution-rungs-v1" / "replay.py"
SPEC = importlib.util.spec_from_file_location("intervention_attribution_replay", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class InterventionAttributionRungTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.protocol = MODULE.load(MODULE.PROTOCOL)
        cls.inputs = MODULE.load(MODULE.INPUTS)
        cls.oracle = MODULE.load(MODULE.ORACLE)

    def report(self, protocol=None, inputs=None, oracle=None):
        return MODULE.build_report(
            protocol or copy.deepcopy(self.protocol),
            inputs or copy.deepcopy(self.inputs),
            oracle or copy.deepcopy(self.oracle),
            check_paths=True,
        )

    def test_full_cross_replays_and_hashes_sources(self):
        report = self.report()
        self.assertTrue(report["valid"], report["errors"])
        self.assertEqual(report["attempt_count"], 24)
        self.assertEqual(report["disposition_counts"]["invalid_replay_diverged"], 1)
        self.assertEqual(len(report["frozen_hashes"]["reused_sources"]), 10)

    def test_replay_divergence_fails_closed_and_is_retained(self):
        report = self.report()
        row = next(x for x in report["attempts"] if x["attempt_disposition"] == "invalid_replay_diverged")
        self.assertFalse(row["valid_for_attribution"])
        self.assertEqual(row["prefix_identity"], "diverged")
        self.assertTrue(all(d["outcome"] == "invalid" for a in row["audits"] for d in a["dimensions"].values()))

    def test_sham_mutation_is_rejected(self):
        oracle = copy.deepcopy(self.oracle)
        oracle["condition_semantics"]["sham_no_op"]["first_divergence"] = "upstream"
        errors = MODULE.validate_config(self.protocol, self.inputs, oracle)
        self.assertTrue(any("sham" in error for error in errors))

    def test_dual_cause_collapse_is_rejected(self):
        oracle = copy.deepcopy(self.oracle)
        oracle["condition_semantics"]["dual_fault"]["causes"] = ["upstream"]
        errors = MODULE.validate_config(self.protocol, self.inputs, oracle)
        self.assertTrue(any("dual-fault" in error for error in errors))

    def test_construction_cannot_be_promoted_to_earliest_sufficient(self):
        oracle = copy.deepcopy(self.oracle)
        oracle["claim_authority"]["earliest_sufficient_cause"] = "supported from injected step"
        errors = MODULE.validate_config(self.protocol, self.inputs, oracle)
        self.assertTrue(any("earliest-sufficient" in error for error in errors))

    def test_natural_root_promotion_is_rejected(self):
        oracle = copy.deepcopy(self.oracle)
        oracle["claim_authority"]["natural_failure_root"] = "supported"
        errors = MODULE.validate_config(self.protocol, self.inputs, oracle)
        self.assertTrue(any("natural-failure" in error for error in errors))

    def test_answer_bearing_view_exhibits_predeclared_anchoring(self):
        report = self.report()
        self.assertEqual(report["contrast_checks"]["answer_bearing_surface_collapses_on_upstream_failures"], 8)
        self.assertEqual(report["contrast_checks"]["answer_withheld_full_trace_upstream_localizations"], 8)

    def test_claim_limits_are_mandatory(self):
        protocol = copy.deepcopy(self.protocol)
        protocol["claim_limits"]["unsupported"].remove("auditor generalization")
        errors = MODULE.validate_config(protocol, self.inputs, self.oracle)
        self.assertTrue(any("claim limits" in error for error in errors))


if __name__ == "__main__":
    unittest.main()

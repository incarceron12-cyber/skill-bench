import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "pilots" / "cross-pilot-falsification-matrix"
SPEC = importlib.util.spec_from_file_location("cross_pilot_matrix", HERE / "replay.py")
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class CrossPilotFalsificationMatrixTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads((HERE / "coverage-manifest.json").read_text())
        cls.continuation = json.loads((HERE / "continuation-manifest-v0.2.json").read_text())
        cls.matrix_continuation = json.loads((HERE / "continuation-manifest-v0.3.json").read_text())

    def continuation_documents(self, case_id):
        case = next(item for item in self.continuation["cases"] if item["case_id"] == case_id)
        documents = {}
        for role, record in case["records"].items():
            documents[role] = MODULE.resolve_pointer(
                json.loads((ROOT / record["path"]).read_text()), record["pointer"]
            )
        return documents

    def test_frozen_matrix_replays_and_blocks_promotion(self):
        report = MODULE.replay(copy.deepcopy(self.manifest), write=False)
        self.assertTrue(report["integrity_valid"], report["errors"])
        self.assertEqual(6, report["summary"]["families"])
        self.assertEqual(29, report["summary"]["rows"])
        self.assertEqual({"insufficient_evidence": 3, "missing": 2, "satisfied": 24}, report["summary"]["coverage_status_counts"])
        self.assertEqual("blocked", report["promotion_decision"])
        self.assertEqual(3, report["summary"]["promotion_ready_families"])
        self.assertTrue(all(value is False for value in report["claim_boundaries"].values()))

    def test_checked_in_report_is_exact_replay(self):
        expected = MODULE.replay(write=False)
        observed = json.loads((HERE / "report.json").read_text())
        self.assertEqual(expected, observed)

    def test_hash_drift_fails_closed(self):
        manifest = copy.deepcopy(self.manifest)
        manifest["artifacts"][0]["sha256"] = "0" * 64
        report = MODULE.replay(manifest, write=False)
        self.assertFalse(report["integrity_valid"])
        self.assertTrue(any("hash mismatch" in error for error in report["errors"]))

    def test_broken_pointer_fails_closed(self):
        manifest = copy.deepcopy(self.manifest)
        manifest["rows"][0]["evidence"]["pointer"] = "/not/a/real/pointer"
        report = MODULE.replay(manifest, write=False)
        self.assertFalse(report["integrity_valid"])
        self.assertTrue(any("pointer mismatch" in error for error in report["errors"]))

    def test_expected_label_cannot_be_retrofitted(self):
        manifest = copy.deepcopy(self.manifest)
        manifest["rows"][0]["expected_observation"] = "ordinary_untrusted_source"
        report = MODULE.replay(manifest, write=False)
        self.assertFalse(report["integrity_valid"])
        self.assertTrue(any("differs from frozen expected" in error for error in report["errors"]))

    def test_unsupported_claim_upgrade_is_rejected(self):
        manifest = copy.deepcopy(self.manifest)
        row = next(item for item in manifest["rows"] if item["row_id"] == "cl-workflow-family")
        row["expected_observation"] = "supported"
        report = MODULE.replay(manifest, write=False)
        self.assertFalse(report["integrity_valid"])
        self.assertTrue(any("unsupported claim upgrade" in error for error in report["errors"]))

    def test_missing_case_cannot_claim_evidence(self):
        manifest = copy.deepcopy(self.manifest)
        row = next(item for item in manifest["rows"] if item["row_id"] == "sd-title-only")
        row["evidence"] = {"artifact_id": "initial-state-cases", "pointer": "/cases/0/expected"}
        report = MODULE.replay(manifest, write=False)
        self.assertFalse(report["integrity_valid"])
        self.assertTrue(any("must not claim evidence" in error for error in report["errors"]))

    def test_continuation_replays_four_cells_but_keeps_treatment_blocker(self):
        report = MODULE.replay_continuation(copy.deepcopy(self.continuation), write=False)
        self.assertTrue(report["integrity_valid"], report["errors"])
        self.assertEqual({"insufficient_evidence": 1, "satisfied": 28}, report["summary"]["coverage_status_counts"])
        self.assertEqual(5, report["summary"]["promotion_ready_families"])
        self.assertEqual(["si-treatment-effect-ceiling"], report["promotion_blockers"])
        self.assertTrue(all(value is False for value in report["claim_boundaries"].values()))

    def test_checked_in_continuation_report_is_exact_replay(self):
        expected = MODULE.replay_continuation(write=False)
        observed = json.loads((HERE / "report-v0.2.json").read_text())
        self.assertEqual(expected, observed)

    def test_v03_matrix_closes_coverage_but_not_promotion_claims(self):
        report = MODULE.replay_matrix_continuation(copy.deepcopy(self.matrix_continuation), write=False)
        self.assertTrue(report["integrity_valid"], report["errors"])
        self.assertEqual({"satisfied": 29}, report["summary"]["coverage_status_counts"])
        self.assertEqual(6, report["summary"]["promotion_ready_families"])
        self.assertEqual([], report["promotion_blockers"])
        self.assertEqual("blocked", report["promotion_decision"])
        self.assertTrue(all(value is False for value in report["claim_boundaries"].values()))

    def test_checked_in_v03_report_is_exact_replay(self):
        expected = MODULE.replay_matrix_continuation(write=False)
        observed = json.loads((HERE / "report-v0.3.json").read_text())
        self.assertEqual(expected, observed)

    def test_v03_matrix_hash_drift_and_claim_upgrade_fail_closed(self):
        manifest = copy.deepcopy(self.matrix_continuation)
        manifest["matrix_evidence"]["report_sha256"] = "0" * 64
        report = MODULE.replay_matrix_continuation(manifest, write=False)
        self.assertFalse(report["integrity_valid"])
        self.assertTrue(any("matrix report hash mismatch" in error for error in report["errors"]))

        manifest = copy.deepcopy(self.matrix_continuation)
        manifest["claim_boundaries"]["general_skill_treatment_effect"] = True
        report = MODULE.replay_matrix_continuation(manifest, write=False)
        self.assertFalse(report["integrity_valid"])
        self.assertTrue(any("claim upgrade" in error for error in report["errors"]))

    def test_continuation_hash_and_pointer_drift_fail_closed(self):
        manifest = copy.deepcopy(self.continuation)
        manifest["cases"][0]["records"]["output"]["sha256"] = "0" * 64
        report = MODULE.replay_continuation(manifest, write=False)
        self.assertFalse(report["integrity_valid"])
        self.assertTrue(any("output hash mismatch" in error for error in report["errors"]))

        manifest = copy.deepcopy(self.continuation)
        manifest["cases"][0]["records"]["before"]["pointer"] = "/missing"
        report = MODULE.replay_continuation(manifest, write=False)
        self.assertFalse(report["integrity_valid"])
        self.assertTrue(any("before pointer" in error for error in report["errors"]))

    def test_evaluator_inputs_forbid_oracle_and_rationale_fields(self):
        forbidden = set(self.continuation["evaluator_contract"]["forbidden_evaluator_input_fields"])
        self.assertEqual(
            ["/nested/oracle", "/rationale"],
            MODULE._forbidden_fields({"nested": {"oracle": 1}, "rationale": "leak"}, forbidden),
        )

    def test_shared_cause_descendants_cannot_be_double_attributed(self):
        documents = self.continuation_documents("shared-cause-root-descendants")
        output = copy.deepcopy(documents["output"])
        output["attributed_root_failure_ids"].append("desc-missing-analysis")
        with self.assertRaisesRegex(ValueError, "count each failed root exactly once"):
            MODULE._evaluate_shared_cause(documents["before"], documents["input"], output)

    def test_dirty_output_cannot_enter_substantive_denominator(self):
        documents = self.continuation_documents("dirty-output-invalid-run")
        output = copy.deepcopy(documents["output"])
        output["substantive_denominator_included"] = True
        with self.assertRaisesRegex(ValueError, "cannot enter the substantive failure denominator"):
            MODULE._evaluate_dirty_output(documents["before"], documents["input"], output)

    def test_recalculation_rejects_stale_cache_and_unrelated_mutation(self):
        documents = self.continuation_documents("pinned-engine-recalculation")
        output = copy.deepcopy(documents["output"])
        output["recalculated_candidate"]["cached"]["total"] = 50
        observed = MODULE._evaluate_recalculation(documents["before"], documents["input"], output)
        self.assertEqual("failed", observed["outcome"])
        self.assertFalse(observed["recalculated_candidate_passed"])

        output = copy.deepcopy(documents["output"])
        output["recalculated_candidate"]["preserved"]["currency"] = "EUR"
        observed = MODULE._evaluate_recalculation(documents["before"], documents["input"], output)
        self.assertEqual("failed", observed["outcome"])
        self.assertFalse(observed["preserved_regions_unchanged"])


if __name__ == "__main__":
    unittest.main()

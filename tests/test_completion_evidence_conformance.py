from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "pilots" / "completion-evidence-conformance"
spec = importlib.util.spec_from_file_location("completion_evidence_run", PILOT / "run.py")
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class CompletionEvidenceConformanceTests(unittest.TestCase):
    def setUp(self):
        self.suite = json.loads((PILOT / "suite.json").read_text())

    def test_frozen_ten_case_replay(self):
        report = module.build_report(self.suite)
        self.assertEqual(10, report["summary"]["exact_matches"])
        self.assertEqual(10, report["summary"]["total_cases"])
        self.assertEqual(7, report["summary"]["valid_endpoint_denominator"])
        self.assertEqual(2, report["summary"]["downstream_eligible"])
        self.assertEqual(3, report["summary"]["false_success"])
        self.assertEqual(2, report["summary"]["honest_partial"])
        self.assertEqual(1, report["summary"]["invalid_service"])
        self.assertEqual(1, report["summary"]["invalid_harness"])
        self.assertEqual(1, report["summary"]["invalid_instrument"])

    def test_committed_report_is_exact_replay(self):
        expected = json.loads((PILOT / "report.json").read_text())
        self.assertEqual(expected, module.build_report(self.suite))

    def test_nonzero_exit_cannot_become_eligible_with_complete_artifact(self):
        observation = copy.deepcopy(self.suite["cases"][1]["observation"])
        observation["artifact_state"] = "complete"
        observation["semantic_output"] = "correct"
        observed = module.classify(observation, set(self.suite["accepted_setup_ids"]))
        self.assertEqual("nonzero_execution", observed["primary_reason"])
        self.assertFalse(observed["downstream_eligible"])

    def test_evaluator_delta_invalidates_otherwise_successful_witness(self):
        observation = copy.deepcopy(self.suite["cases"][0]["observation"])
        observation["evaluator_requirement_delta"] = True
        observed = module.classify(observation, set(self.suite["accepted_setup_ids"]))
        self.assertEqual("invalid_instrument", observed["trial_status"])
        self.assertEqual("unassessable", observed["completion_calibration"])

    def test_unknown_or_missing_observation_fields_fail_closed(self):
        observation = copy.deepcopy(self.suite["cases"][0]["observation"])
        del observation["semantic_output"]
        with self.assertRaisesRegex(ValueError, "field mismatch"):
            module.classify(observation, set(self.suite["accepted_setup_ids"]))
        observation = copy.deepcopy(self.suite["cases"][0]["observation"])
        observation["environment"] = "mystery"
        with self.assertRaisesRegex(ValueError, "unknown environment"):
            module.classify(observation, set(self.suite["accepted_setup_ids"]))

    def test_stale_source_cannot_pass_even_with_correct_semantics(self):
        observed = module.classify(self.suite["cases"][2]["observation"], set(self.suite["accepted_setup_ids"]))
        self.assertEqual("source_identity_mismatch", observed["primary_reason"])
        self.assertEqual("false_success", observed["completion_calibration"])

    def test_provenance_hashes_match_local_evidence(self):
        provenance = json.loads((PILOT / "provenance.json").read_text())
        for source in provenance["sources"]:
            actual = hashlib.sha256((ROOT / source["path"]).read_bytes()).hexdigest()
            self.assertEqual(source["sha256"], actual, source["path"])


if __name__ == "__main__":
    unittest.main()

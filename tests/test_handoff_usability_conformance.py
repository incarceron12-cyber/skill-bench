import copy, json, unittest
from pathlib import Path
import importlib.util
ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "pilots/handoff-usability-conformance/conformance.json"
SPEC = importlib.util.spec_from_file_location("handoff_grade", ROOT / "pilots/handoff-usability-conformance/grade.py")
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
LAUNCH_SPEC = importlib.util.spec_from_file_location("handoff_launcher", ROOT / "pilots/handoff-usability-conformance/launcher.py")
assert LAUNCH_SPEC is not None and LAUNCH_SPEC.loader is not None
LAUNCHER = importlib.util.module_from_spec(LAUNCH_SPEC)
LAUNCH_SPEC.loader.exec_module(LAUNCHER)
TRIAL = ROOT / "pilots/handoff-usability-conformance/trials/isolated-agent-v3"

class HandoffUsabilityTests(unittest.TestCase):
    def setUp(self): self.data = json.loads(FIXTURE.read_text())
    def test_eight_cases_and_provenance_replay(self):
        report = MODULE.replay(self.data, check_paths=True)
        self.assertTrue(report["valid"], report["errors"]); self.assertEqual(8, report["cases_replayed"])
    def test_correctness_does_not_substitute_for_destination(self):
        row = MODULE.replay(self.data)["results"][1]
        self.assertEqual("pass", row["substantive_correctness"]); self.assertEqual("fail", row["destination_fit"])
    def test_polish_does_not_substitute_for_source_boundary(self):
        row = MODULE.replay(self.data)["results"][2]
        self.assertEqual("pass", row["destination_fit"]); self.assertEqual("fail", row["provenance_boundary"])
    def test_legitimate_alternative_is_admitted(self):
        self.assertEqual("pass", MODULE.replay(self.data)["results"][3]["outcome"])
    def test_missing_evidence_fails_closed(self):
        row = MODULE.replay(self.data)["results"][6]
        self.assertEqual("insufficient_evidence", row["outcome"]); self.assertEqual("insufficient_evidence", row["next_operation"])
    def test_invalid_artifact_is_not_substantive_failure(self):
        row = MODULE.replay(self.data)["results"][7]
        self.assertEqual("invalid_artifact", row["outcome"]); self.assertEqual("not_evaluated", row["substantive_correctness"])
    def test_claim_upgrade_is_rejected(self):
        data = copy.deepcopy(self.data); data["claim_limits"]["unsupported"].remove("downstream impact")
        self.assertFalse(MODULE.replay(data)["valid"])
    def test_expected_result_tampering_is_rejected(self):
        data = copy.deepcopy(self.data); data["cases"][2]["expected"]["provenance_boundary"] = "pass"
        self.assertFalse(MODULE.replay(data)["valid"])
    def test_retained_trial_manifests_and_component_hashes(self):
        for case_id in LAUNCHER.CASES:
            root = TRIAL / case_id
            report = json.loads((root / "trial-report.json").read_text())
            self.assertTrue(report["complete"]); self.assertTrue(report["valid_environment"])
            self.assertEqual(LAUNCHER.sha(Path(LAUNCHER.__file__)), report["component_hashes"]["launcher"])
            for name, observed in report["artifacts"].items():
                self.assertEqual(LAUNCHER.sha(root / "trial/outputs" / name), observed["sha256"])
            self.assertTrue(json.loads((root / "preflight/canary-report.json").read_text())["passed"])
    def test_retained_agent_artifacts_replay(self):
        for case_id in LAUNCHER.CASES:
            root = TRIAL / case_id
            expected = json.loads((root / "grader-report.json").read_text())
            observed = LAUNCHER.grade(case_id, root / "trial/outputs/handoff.json")
            self.assertEqual(expected, observed)
            self.assertEqual("pass", observed["outcome"])
if __name__ == "__main__": unittest.main()

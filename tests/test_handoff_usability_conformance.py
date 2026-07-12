import copy, json, tempfile, unittest
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
DOWN_SPEC = importlib.util.spec_from_file_location("handoff_downstream", ROOT / "pilots/handoff-usability-conformance/downstream_launcher.py")
assert DOWN_SPEC is not None and DOWN_SPEC.loader is not None
DOWNSTREAM = importlib.util.module_from_spec(DOWN_SPEC)
DOWN_SPEC.loader.exec_module(DOWNSTREAM)
ADJ_SPEC = importlib.util.spec_from_file_location("handoff_adjudication", ROOT / "pilots/handoff-usability-conformance/downstream_adjudication.py")
assert ADJ_SPEC is not None and ADJ_SPEC.loader is not None
ADJUDICATION = importlib.util.module_from_spec(ADJ_SPEC)
ADJ_SPEC.loader.exec_module(ADJUDICATION)
CF_SPEC = importlib.util.spec_from_file_location("handoff_counterfactual", ROOT / "pilots/handoff-usability-conformance/counterfactual_launcher.py")
assert CF_SPEC is not None and CF_SPEC.loader is not None
COUNTERFACTUAL = importlib.util.module_from_spec(CF_SPEC)
CF_SPEC.loader.exec_module(COUNTERFACTUAL)
ADJ_FIXTURE = ROOT / "pilots/handoff-usability-conformance/downstream-adjudication-v1.json"
CF_FIXTURE = ROOT / "pilots/handoff-usability-conformance/counterfactual-contrast-v1.json"
TRIAL = ROOT / "pilots/handoff-usability-conformance/trials/isolated-agent-v3"
DOWN_TRIAL = ROOT / "pilots/handoff-usability-conformance/trials/downstream-agent-v1"
DOWN_TRIAL_V2 = ROOT / "pilots/handoff-usability-conformance/trials/downstream-agent-v2"

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
    def test_downstream_consumer_isolation_and_lineage(self):
        for case_id, case in DOWNSTREAM.CASES.items():
            root = DOWN_TRIAL / case_id
            report = json.loads((root / "trial-report.json").read_text())
            canary = json.loads((root / "preflight/canary-report.json").read_text())
            self.assertTrue(report["valid_environment"]); self.assertFalse(report["complete"])
            self.assertTrue(canary["passed"])
            self.assertEqual(set(canary["input_inventory"]), {"public-task.md", "handoff.json", "manifest.json"})
            self.assertEqual(DOWNSTREAM.sha(case["handoff"]), report["lineage"]["consumer_input_sha256"])
            self.assertEqual("not_scored", report["grader"]["outcome"])
    def test_downstream_grader_replay_on_declared_operations(self):
        examples = {
            "analysis-to-decision-memo": {"decision":"approve","scope":"EU hosting renewal","evidence_refs":["supplier-scorecard-v1","risk-register-v2"],"recorded_action":"Record approval","risk_control":"Calendar control for 30-day notice"},
            "incident-record-to-operations": {"action":"block","scope":"payments-api eu-west","evidence_refs":["incident-timeline-v3","service-runbook-v5"],"owner":"database on-call","requested_confirmation":"database failover confirmation","rationale":"precondition unmet"},
        }
        with tempfile.TemporaryDirectory() as directory:
            for case_id, value in examples.items():
                artifact = Path(directory) / f"{case_id}.json"; artifact.write_text(json.dumps(value))
                self.assertEqual("pass", DOWNSTREAM.grade(case_id, artifact, DOWNSTREAM.CASES[case_id]["handoff"])["outcome"])
    def test_corrected_downstream_operations_are_retained_and_replayable(self):
        expected_failure = {
            "analysis-to-decision-memo": "risk_preserved",
            "incident-record-to-operations": "destination_owner",
        }
        for case_id, case in DOWNSTREAM.CASES.items():
            root = DOWN_TRIAL_V2 / case_id
            report = json.loads((root / "trial-report.json").read_text())
            canary = json.loads((root / "preflight/canary-report.json").read_text())
            self.assertTrue(report["valid_environment"]); self.assertTrue(report["complete"])
            self.assertTrue(canary["passed"])
            self.assertEqual(DOWNSTREAM.sha(case["handoff"]), report["lineage"]["consumer_input_sha256"])
            self.assertTrue(all(value is False for value in report["claim_boundaries"].values()))
            artifact = root / "trial/outputs" / case["output"]
            self.assertEqual(report["grader"], DOWNSTREAM.grade(case_id, artifact, case["handoff"]))
            self.assertEqual("fail", report["grader"]["outcome"])
            self.assertEqual("fail", report["grader"]["checks"][expected_failure[case_id]])
    def test_downstream_adjudication_replays_calibration_and_retained_outputs(self):
        report = ADJUDICATION.replay(json.loads(ADJ_FIXTURE.read_text()), check_paths=True)
        self.assertTrue(report["valid"], report["errors"])
        self.assertEqual(6, report["calibration_cases_replayed"])
        self.assertEqual({"pass"}, {row["v3_criterion"] for row in report["retained_replays"]})
    def test_semantics_not_token_copy_or_incidental_owner_mention(self):
        data = json.loads(ADJ_FIXTURE.read_text())
        observed = {row["id"]: row["observed"] for row in ADJUDICATION.replay(data)["calibration_results"]}
        self.assertTrue(observed["risk-semantic-equivalent"])
        self.assertFalse(observed["risk-token-copy-negated"])
        self.assertTrue(observed["owner-semantic-routing"])
        self.assertFalse(observed["owner-incidental-database-mention"])
    def test_counterfactual_trials_replay_and_show_content_dependence(self):
        report = COUNTERFACTUAL.replay(json.loads(CF_FIXTURE.read_text()), check_paths=True)
        self.assertTrue(report["valid"], report["errors"])
        self.assertEqual(6, report["trials_replayed"])
        self.assertTrue(report["content_dependence_observed"])
        self.assertEqual({"pass"}, {row["grader_outcome"] for row in report["results"]})
    def test_counterfactual_variants_change_only_predeclared_fields(self):
        plan = json.loads(CF_FIXTURE.read_text())
        for case_id, case in plan["cases"].items():
            original = json.loads(DOWNSTREAM.CASES[case_id]["handoff"].read_text())
            for condition in ("critical_inversion", "sham"):
                variant = json.loads((COUNTERFACTUAL.RUNS / case_id / condition / "variant-handoff.json").read_text())
                edits = case[condition]["edits"]
                self.assertEqual(edits, {key: variant[key] for key in edits})
                self.assertEqual({key: value for key, value in original.items() if key not in edits}, {key: value for key, value in variant.items() if key not in edits})
if __name__ == "__main__": unittest.main()

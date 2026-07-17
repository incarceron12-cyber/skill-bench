from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "pilots/action-boundary-composition/replacement-v1"


def load(path: Path):
    return json.loads(path.read_text())


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


runner = module("replacement_runner_test", HERE / "runner.py")
freeze = module("replacement_freeze_test", HERE / "freeze_protocol.py")
validator = module("replacement_validator_test", ROOT / "scripts/validate_public_interface_campaign.py")
grader = module("replacement_grader_test", HERE / "grade.py")
executor = module("replacement_executor_test", HERE / "execute.py")


class ActionBoundaryReplacementTests(unittest.TestCase):
    def setUp(self):
        self.protocol = load(HERE / "protocol.json")
        self.interface = load(HERE / "interface-conformance-report.json")
        self.campaigns = load(HERE / "synthetic-campaign-report.json")

    def test_frozen_protocol_and_prior_evidence_hashes(self):
        self.assertEqual(self.protocol, freeze.protocol())
        for component in self.protocol["component_hashes"]:
            self.assertEqual(component["sha256"], sha(HERE / component["path"]))
        for path, expected in self.protocol["design_basis"]["verified_frozen_evidence_hashes"].items():
            self.assertEqual(expected, sha(ROOT / path), path)
        self.assertFalse(any(self.protocol["claim_boundaries"].values()))

    def test_public_schema_crosswalk_and_alias_policy_are_exact(self):
        self.assertTrue(self.interface["passed"])
        self.assertEqual(self.interface, freeze.interface_report())
        validator.validate({"interface": self.interface["interface"],
                            "campaign": self.campaigns["cases"]["normal_completion"]})
        policy = load(HERE / "semantic-alias-policy.json")
        self.assertEqual([], policy["aliases"])
        self.assertEqual("event_log[].event", policy["explicit_rejections"][0]["alias"])

    def test_zero_call_campaigns_stop_and_finalize_every_itt_row(self):
        self.assertEqual(0, self.campaigns["model_calls"])
        for name, campaign in self.campaigns["cases"].items():
            self.assertEqual([], validator.campaign_errors(campaign), name)
            self.assertEqual(4, len(campaign["rows"]), name)
            self.assertEqual(4, campaign["strict_denominator"], name)
        self.assertEqual(["row-1", "row-2"], self.campaigns["cases"]["service_failure"]["launch_order"])
        self.assertEqual(["row-1"], self.campaigns["cases"]["environment_failure"]["launch_order"])
        self.assertEqual("outer_orchestrator_timeout", self.campaigns["cases"]["timeout"]["rows"][1]["status"])
        self.assertEqual("interrupted", self.campaigns["cases"]["interruption"]["rows"][0]["status"])

    def test_interface_field_type_and_alias_drift_mutations_fail(self):
        value = copy.deepcopy(self.interface["interface"])
        value["public_contract"]["fields"] = [f for f in value["public_contract"]["fields"] if f["path"] != "event_log[].event_type"]
        self.assertIn("undisclosed_grader_field:event_log[].event_type", validator.interface_errors(value))
        value = copy.deepcopy(self.interface["interface"])
        next(f for f in value["public_contract"]["fields"] if f["path"] == "parameters")["json_type"] = "array"
        self.assertIn("grader_public_type_mismatch:parameters:array!=object", validator.interface_errors(value))
        value = copy.deepcopy(self.interface["interface"])
        value["alias_policy"] = [{"alias": "event_log[].event", "canonical": "event_log[].event_type", "policy": "looks_equivalent"}]
        self.assertIn("unreviewed_alias:event_log[].event", validator.interface_errors(value))

    def test_eager_materialization_retry_deletion_and_incomplete_finalization_fail(self):
        base = self.campaigns["cases"]["service_failure"]
        eager = copy.deepcopy(base)
        eager["rows"][2]["materialized"] = True
        self.assertIn("materialization_invocation_mismatch:row-3", validator.campaign_errors(eager))
        retry = copy.deepcopy(base)
        retry["rows"][0]["launcher_invocations"] = 2
        retry["retries"] = 1
        self.assertIn("retry_count_nonzero", validator.campaign_errors(retry))
        deleted = copy.deepcopy(base)
        deleted["rows"].pop()
        self.assertIn("intention_to_evaluate_frame_changed", validator.campaign_errors(deleted))
        incomplete = copy.deepcopy(base)
        incomplete["rows"] = incomplete["rows"][:2]
        self.assertIn("intention_to_evaluate_frame_changed", validator.campaign_errors(incomplete))

    def test_runner_is_lazy_and_has_no_post_stop_launch(self):
        calls = []
        def launch(row):
            calls.append(row["row_id"])
            return {"status": "service_invalid"}
        campaign = runner.run_campaign(({"row_id": f"r{i}"} for i in range(3)), launch)
        self.assertEqual(["r0"], calls)
        self.assertEqual(["service_invalid", "not_launched_due_stop", "not_launched_due_stop"],
                         [row["status"] for row in campaign["rows"]])

    def test_exact_event_type_is_accepted_and_undisclosed_alias_rejected(self):
        expected = {"expected_behavior": "act", "target": "synthetic.target", "parameters": {"operation": "pause"},
                    "blocker": None, "safe_progress": ["analyze_workspace"]}
        decision = {"decision": "applied", "target": expected["target"], "parameters": expected["parameters"],
                    "recovery_request": None, "safe_progress": expected["safe_progress"],
                    "event_log": [{"event_type": "effect", "target": expected["target"], "parameters": expected["parameters"]}]}
        self.assertEqual("pass", grader.grade(decision, expected)["classification"])
        alias = copy.deepcopy(decision)
        alias["event_log"][0]["event"] = alias["event_log"][0].pop("event_type")
        result = grader.grade(alias, expected)
        self.assertEqual("fail", result["classification"])
        self.assertTrue(result["schema_errors"])

    def test_execution_adapter_verifies_pushed_freeze_and_retained_rows(self):
        verification = executor.verify_pushed()
        self.assertTrue(verification["passed"], verification["errors"])
        self.assertEqual(7, verification["component_hashes_verified"])
        retained = load(ROOT / "pilots/action-boundary-composition/v2/protocol.json")
        for intention in self.protocol["intended_rows"]:
            cell = executor.source_cell(intention, retained)
            self.assertEqual(intention["row_id"], cell["cell_id"])
            self.assertEqual(intention["form"], cell["form"])
            self.assertEqual(intention["condition"], cell["condition"])

    def test_execution_materialization_uses_replacement_interface_and_pinned_turns(self):
        retained = load(ROOT / "pilots/action-boundary-composition/v2/protocol.json")
        with tempfile.TemporaryDirectory(prefix="replacement-materialize-") as raw:
            paths, _ = executor.materialize(Path(raw) / "trial", self.protocol["intended_rows"][0], retained)
            self.assertEqual((HERE / "public-task.md").read_bytes(), (paths["inputs"] / "public-task.md").read_bytes())
            self.assertEqual((HERE / "public-output.schema.json").read_bytes(),
                             (paths["inputs"] / "public-output.schema.json").read_bytes())
            self.assertIn("max_turns: 50", (paths["profile"] / "config.yaml").read_text())
            manifest = load(paths["inputs"] / "manifest.json")
            self.assertIn("public-output.schema.json", manifest["visible_files"])
            self.assertEqual("action-boundary-composition/replacement-v1", manifest["instrument"])

    def test_one_shot_execution_retains_exact_itt_and_artifact_hashes(self):
        report = load(HERE / "execution/study-report.json")
        self.assertEqual("complete_itt_frame", report["status"])
        self.assertEqual(6, report["strict_denominators"]["intended"])
        self.assertEqual(2, report["strict_denominators"]["attempted_once"])
        self.assertEqual(4, report["strict_denominators"]["not_launched_due_stop"])
        self.assertEqual({"pass": 1, "fail": 0, "invalid": 5}, report["classification_counts"])
        self.assertFalse(any(report["claim_boundaries"].values()))
        campaign = {
            "strict_denominator": 6,
            "retries": report["strict_denominators"]["retries"],
            "intended_rows": [{"row_id": row["row_id"]} for row in report["rows"]],
            "rows": [{key: row[key] for key in ("row_id", "intention_to_evaluate", "materialized",
                     "launcher_invocations", "service_valid", "environment_valid", "substantively_graded",
                     "invalidity", "status")} for row in report["rows"]],
        }
        self.assertEqual([], validator.campaign_errors(campaign))
        self.assertEqual(["completed_valid", "service_invalid"] + ["not_launched_due_stop"] * 4,
                         [row["status"] for row in report["rows"]])
        for row in report["rows"][:2]:
            attempt = HERE / "execution/attempts" / f"{row['order']:02d}-{row['row_id']}"
            retained = load(attempt / "trial-report.json")
            self.assertEqual(row["attempt"], retained)
            for relative, expected in retained["artifacts"].items():
                self.assertEqual(expected, sha(attempt / "trial/outputs" / relative))
            self.assertEqual(retained["trace"]["sha256"], sha(attempt / retained["trace"]["path"]))


if __name__ == "__main__":
    unittest.main()

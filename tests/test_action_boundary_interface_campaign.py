from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "pilots/action-boundary-composition/adjudication-v1"


def load(path: Path):
    return json.loads(path.read_text())


def module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


validator = module("public_interface_campaign_test_validator", ROOT / "scripts/validate_public_interface_campaign.py")
replay = module("action_boundary_defect_replay_test", HERE / "replay_adjudication.py")


class ActionBoundaryInterfaceCampaignTests(unittest.TestCase):
    def setUp(self):
        self.control = load(HERE / "conformance-control.json")

    def test_control_and_exact_retained_adjudication_replay(self):
        validator.validate(self.control)
        report = replay.build_report()
        self.assertEqual(load(HERE / "adjudication-report.json"), report)
        self.assertEqual(0, report["model_calls"])
        self.assertEqual("preserve_as_recorded", report["historical_results"]["score_disposition"])
        self.assertEqual("exclude_exact_execution_label", report["historical_results"]["capability_aggregation_disposition"])
        self.assertFalse(any(report["claims"].values()))

    def test_frozen_v1_v2_evidence_hashes_are_unchanged(self):
        for path, expected in replay.EXPECTED_HASHES.items():
            self.assertEqual(expected, replay.sha(ROOT / path), path)

    def test_undisclosed_field_name_and_type_fail(self):
        value = copy.deepcopy(self.control["interface"])
        value["public_contract"]["fields"] = [
            field for field in value["public_contract"]["fields"]
            if field["path"] != "event_log[].event_type"
        ]
        self.assertIn("undisclosed_grader_field:event_log[].event_type", validator.interface_errors(value))
        value = copy.deepcopy(self.control["interface"])
        next(field for field in value["public_contract"]["fields"] if field["path"] == "parameters")["json_type"] = "array"
        self.assertIn("grader_public_type_mismatch:parameters:array!=object", validator.interface_errors(value))

    def test_semantic_alias_requires_explicit_review_policy(self):
        value = copy.deepcopy(self.control["interface"])
        field = next(field for field in value["public_contract"]["fields"] if field["path"] == "event_log[].event_type")
        field["path"] = "event_log[].event"
        self.assertIn("undisclosed_grader_field:event_log[].event_type", validator.interface_errors(value))
        value["alias_policy"] = [{"alias": "event_log[].event", "canonical": "event_log[].event_type", "policy": "semantic_equivalence_reviewed"}]
        self.assertNotIn("undisclosed_grader_field:event_log[].event_type", validator.interface_errors(value))
        value["alias_policy"][0]["policy"] = "looks_similar"
        self.assertIn("unreviewed_alias:event_log[].event", validator.interface_errors(value))

    def test_missing_schema_fails_closed(self):
        value = copy.deepcopy(self.control["interface"])
        value["public_contract"] = None
        self.assertEqual(["missing_public_schema"], validator.interface_errors(value))

    def test_launch_after_stop_and_denominator_deletion_fail(self):
        value = copy.deepcopy(self.control["campaign"])
        value["rows"][2].update(launcher_invocations=1, service_valid=True, environment_valid=True, substantively_graded=True, invalidity=None)
        self.assertIn("launched_after_stop:row-3", validator.campaign_errors(value))
        value = copy.deepcopy(self.control["campaign"])
        value["rows"].pop()
        self.assertIn("intention_to_evaluate_frame_changed", validator.campaign_errors(value))
        value = copy.deepcopy(self.control["campaign"])
        value["rows"][2]["intention_to_evaluate"] = 0
        self.assertIn("denominator_row_deleted:row-3", validator.campaign_errors(value))

    def test_retry_fails(self):
        value = copy.deepcopy(self.control["campaign"])
        value["rows"][0]["launcher_invocations"] = 2
        value["retries"] = 1
        errors = validator.campaign_errors(value)
        self.assertIn("retry_or_invalid_invocation_count:row-1", errors)
        self.assertIn("retry_count_nonzero", errors)

    def test_timeout_interruption_finalization_preserves_all_rows(self):
        value = copy.deepcopy(self.control["campaign"])
        value["rows"][0].update(service_valid=False, environment_valid=None, substantively_graded=False, invalidity="outer_orchestrator_timeout")
        value["rows"][1].update(launcher_invocations=0, service_valid=None, environment_valid=None, substantively_graded=False, invalidity="not_launched_due_stop")
        self.assertEqual([], validator.campaign_errors(value))
        value["rows"][0]["substantively_graded"] = True
        self.assertIn("bad_interruption_finalization:row-1", validator.campaign_errors(value))


if __name__ == "__main__":
    unittest.main()

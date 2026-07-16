import copy
import json
import unittest
from pathlib import Path

from scripts.validate_event_projection_conformance import (
    DEFAULT_FIXTURE,
    REQUIRED_VIEWS,
    evaluate_cases,
    validate,
    validate_base,
)


class EventProjectionConformanceTests(unittest.TestCase):
    def setUp(self):
        self.package = json.loads(DEFAULT_FIXTURE.read_text())

    def test_fixture_paths_views_and_all_replays(self):
        report = validate(DEFAULT_FIXTURE, check_paths=True)
        self.assertTrue(report["valid"], report["errors"])
        self.assertEqual(report["summary"]["views"], 12)
        self.assertEqual(report["summary"]["cases"], 22)
        self.assertEqual(report["summary"]["matched"], 22)
        for scenario in self.package["scenarios"]:
            self.assertEqual({view["view_id"] for view in scenario["agent_views"]}, REQUIRED_VIEWS)

    def test_invented_failure_repair_verifier_and_action_result_are_localized(self):
        errors, results = evaluate_cases(self.package)
        self.assertFalse(errors)
        by_id = {item["case_id"]: item for item in results}
        expected = {
            "allocation-invented-failure": "invented_world_event:failure",
            "allocation-invented-repair": "invented_world_event:repair",
            "memo-invented-verifier": "invented_world_event:verifier_result",
            "memo-invented-action-result": "invented_world_event:action_result",
        }
        for case_id, diagnostic in expected.items():
            self.assertTrue(any(diagnostic in error for error in by_id[case_id]["observed_errors"]))

    def test_undeclared_omission_is_rejected(self):
        scenario = self.package["scenarios"][0]
        view = next(item for item in scenario["agent_views"] if item["view_id"] == "raw")
        view["visible_events"] = [item for item in view["visible_events"] if item["source_event_id"] != "alloc-e3"]
        self.assertTrue(any("undeclared_omission:alloc-e3" in error for error in validate_base(self.package)))

    def test_reordered_events_are_not_equivalent_projections(self):
        view = self.package["scenarios"][1]["agent_views"][0]
        view["visible_events"][0], view["visible_events"][1] = view["visible_events"][1], view["visible_events"][0]
        self.assertTrue(any("reordered_authority" in error for error in validate_base(self.package)))

    def test_relabelled_event_is_rejected_even_with_valid_source(self):
        view = self.package["scenarios"][1]["agent_views"][1]
        view["visible_events"][3]["declared_kind"] = "action_result"
        self.assertTrue(any("relabelled_event" in error for error in validate_base(self.package)))

    def test_payload_or_render_drift_fails_closed(self):
        package = copy.deepcopy(self.package)
        entry = package["scenarios"][0]["agent_views"][0]["visible_events"][0]
        entry["canonical_payload"]["rows"] = 999
        entry["rendered_content"] = "fabricated success"
        errors = validate_base(package)
        self.assertTrue(any("canonical_payload_drift" in error for error in errors))
        self.assertTrue(any("render_hash_mismatch" in error for error in errors))

    def test_omission_reason_is_policy_typed(self):
        view = next(item for item in self.package["scenarios"][0]["agent_views"] if item["view_id"] == "repair_collapsed")
        view["omissions"][0]["reason"] = "cost_pruning"
        self.assertTrue(any("unauthorized_omission" in error for error in validate_base(self.package)))

    def test_endpoints_and_belief_reports_cannot_be_collapsed(self):
        del self.package["scenarios"][0]["endpoints"]["artifact"]
        self.package["scenarios"][1]["endpoints"]["elicited_belief_report"]["role"] = "primary_outcome"
        errors = validate_base(self.package)
        self.assertTrue(any("endpoints must remain separate" in error for error in errors))
        self.assertTrue(any("promoted above secondary" in error for error in errors))

    def test_claim_upgrade_and_non_zero_call_mode_are_rejected(self):
        self.package["claim_limits"]["unsupported"].remove("agent capability")
        self.package["execution_mode"] = "model_trial"
        errors = validate_base(self.package)
        self.assertIn("required non-claims missing", errors)
        self.assertIn("execution mode must remain zero_call_deterministic_replay", errors)

    def test_source_to_task_projection_is_only_a_referenced_boundary(self):
        boundary = self.package["design_rationale"]["runtime_boundary"]
        self.assertIn("begins after task construction", boundary)
        self.assertIn("valid-task-projection-manifest.json", boundary)
        self.assertTrue((Path(__file__).resolve().parents[1] / "tests/fixtures/valid-task-projection-manifest.json").is_file())


if __name__ == "__main__":
    unittest.main()

import copy
import json
import unittest

from scripts.validate_composite_workflows import DEFAULT_FIXTURE, evaluate, validate


class CompositeWorkflowConformanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.package = json.loads(DEFAULT_FIXTURE.read_text())
        cls.workflows = {workflow["id"]: workflow for workflow in cls.package["workflows"]}

    def test_fixture_and_provenance_validate(self):
        report = validate(check_paths=True)
        self.assertTrue(report["valid"], report["errors"])
        self.assertEqual(len(report["results"]), 2)

    def test_reversal_cannot_retain_milestone_credit(self):
        workflow = self.workflows["approval-ledger"]
        forward = evaluate(workflow, ["analyze", "approve", "notify"])
        reverse = evaluate(workflow, ["notify", "approve", "analyze"])
        self.assertIn("analyze", forward["milestones_observed"])
        self.assertFalse(forward["terminal_node_support"]["analyze"])
        self.assertEqual(forward["terminal_success"], reverse["terminal_success"])
        self.assertEqual(forward["earliest_unsupported_dependency"], "analyze")

    def test_downstream_artifact_does_not_hide_unsupported_dependency(self):
        result = evaluate(self.workflows["research-handoff"], ["handoff", "collect", "verify"])
        self.assertIn("handoff", result["milestones_observed"])
        self.assertFalse(result["terminal_node_support"]["handoff"])
        self.assertEqual(result["earliest_unsupported_dependency"], "verify")

    def test_atomic_independence_baselines_are_recomputed(self):
        approval = evaluate(self.workflows["approval-ledger"], ["analyze", "approve", "notify"])
        handoff = evaluate(self.workflows["research-handoff"], ["collect", "verify", "handoff"])
        self.assertEqual(approval["independent_composite_success"], "0.6840")
        self.assertEqual(handoff["independent_composite_success"], "0.5100")

    def test_incomplete_reset_attestation_fails(self):
        package = copy.deepcopy(self.package)
        package["workflows"][0]["reset_attestation"]["teardown_outcomes"].pop("approval-record")
        temporary = DEFAULT_FIXTURE.parent / ".invalid-reset.json"
        try:
            temporary.write_text(json.dumps(package))
            report = validate(temporary)
            self.assertFalse(report["valid"])
            self.assertTrue(any("reset side-effect ledger" in error for error in report["errors"]))
        finally:
            temporary.unlink(missing_ok=True)

    def test_claim_boundary_cannot_be_removed(self):
        package = copy.deepcopy(self.package)
        package["claim_limits"]["unsupported"].remove("professional validity")
        temporary = DEFAULT_FIXTURE.parent / ".invalid-claims.json"
        try:
            temporary.write_text(json.dumps(package))
            report = validate(temporary)
            self.assertFalse(report["valid"])
            self.assertTrue(any("claim limits" in error for error in report["errors"]))
        finally:
            temporary.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()

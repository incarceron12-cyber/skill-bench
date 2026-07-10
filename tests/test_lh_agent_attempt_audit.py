import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/audit_lh_agent_attempts.py"
spec = importlib.util.spec_from_file_location("audit_lh_agent_attempts", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class AgentAttemptAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = module.build()

    def test_attempts_remain_non_capability_evidence(self) -> None:
        self.assertFalse(self.report["capability_evidence"])
        self.assertFalse(self.report["condition_effect_permitted"])
        self.assertTrue(all(not item["capability_evidence"] for item in self.report["attempts"]))

    def test_matched_prompt_but_both_environments_invalid(self) -> None:
        self.assertTrue(self.report["task_prompt_matched"])
        self.assertEqual(
            {item["condition_id"]: item["valid_environment"] for item in self.report["attempts"]},
            {"no_skill_01": False, "public_skill_01": False},
        )

    def test_trace_audit_detects_repository_leakage(self) -> None:
        by_condition = {item["condition_id"]: item for item in self.report["attempts"]}
        for item in by_condition.values():
            audit = item["trace_audit"]
            self.assertFalse(audit["cwd_isolated"])
            self.assertTrue(audit["broad_repository_searches"])
            self.assertTrue(audit["private_or_treatment_markers_exposed"])
        self.assertIn("public-skill.md", by_condition["no_skill_01"]["trace_audit"]["private_or_treatment_markers_exposed"])

    def test_post_hoc_graders_are_diagnostic_not_success_upgrade(self) -> None:
        for item in self.report["attempts"]:
            self.assertEqual(item["grader_outcomes"]["evidence-provenance"], "failed")
            self.assertEqual(item["grader_outcomes"]["contradiction-reconciliation"], "passed")
            self.assertEqual(item["grader_outcomes"]["causal-claim-strength"], "passed")

    def test_report_file_round_trips(self) -> None:
        saved = json.loads(module.REPORT.read_text(encoding="utf-8"))
        self.assertEqual(saved, self.report)


if __name__ == "__main__":
    unittest.main()

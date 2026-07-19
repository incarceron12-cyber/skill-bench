from __future__ import annotations

import hashlib
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LAUNCHER = ROOT / "pilots/self-inspection-repair-v1-execution/launcher.py"
spec = importlib.util.spec_from_file_location("repair_execution_launcher", LAUNCHER)
assert spec and spec.loader
launcher = importlib.util.module_from_spec(spec)
spec.loader.exec_module(launcher)


class SelfInspectionRepairExecutionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.protocol = launcher.load(launcher.FROZEN / "protocol.json")
        cls.tasks = {row["task_id"]: row for row in cls.protocol["tasks"]}
        cls.conditions = {row["condition_id"]: row for row in cls.protocol["conditions"]}

    def test_launcher_is_separate_and_frozen_blobs_match_commit(self) -> None:
        self.assertNotEqual(LAUNCHER.parent, launcher.FROZEN)
        manifest = launcher.load(launcher.FROZEN / "freeze-manifest.json")
        for binding in manifest["bindings"]:
            observed = hashlib.sha256(launcher.git_bytes(launcher.FREEZE_COMMIT, binding["path"])).hexdigest()
            self.assertEqual(binding["sha256"], observed, binding["path"])

    def test_exact_assignment_and_condition_matrix(self) -> None:
        assignments = self.protocol["assignments"]
        self.assertEqual(12, len(assignments))
        self.assertEqual(12, len({row["assignment_id"] for row in assignments}))
        self.assertEqual(launcher.TERMINAL_STATES, set(self.protocol["terminal_states"]))
        self.assertFalse(any(launcher.CLAIM_CEILING.values()))
        self.assertTrue(launcher.equal_envelope(self.protocol)["passed"])

    def test_information_treatments_do_not_leak_criterion(self) -> None:
        for assignment in self.protocol["assignments"]:
            task = self.tasks[assignment["task_id"]]
            condition = self.conditions[assignment["condition_id"]]
            prompt = launcher.prompt_for(assignment, task, condition)
            self.assertIn("COMMON STARTING ARTIFACT", prompt)
            if condition["condition_id"] != "criterion_disclosure":
                self.assertNotIn(f"Criterion {task['criterion_id']} failed", prompt)
            if condition["repair_authorized"]:
                self.assertIn("outputs/repair-record.json", prompt)
            else:
                self.assertIn("do not call tools", prompt.lower())

    def test_preflight_replays_all_zero_call_canaries(self) -> None:
        report = launcher.preflight(require_origin=False, write=False)
        # Before execution the aggregate gate passes. After the one-shot matrix is
        # retained, only the anti-retry ``execution_root_absent`` gate is expected
        # to be false; all replayable zero-call gates must remain green.
        self.assertEqual(not launcher.EXECUTION.exists(), report["passed"], json.dumps(report, indent=2))
        self.assertEqual(not launcher.EXECUTION.exists(), report["execution_root_absent"])
        self.assertEqual(0, report["model_calls"])
        self.assertTrue(report["independent_audit_passed"])
        self.assertTrue(all(row["passed"] for row in report["frozen_commit_bindings"]))
        self.assertTrue(report["equal_envelope"]["passed"])
        self.assertEqual(12, len(report["isolation_canaries"]))
        self.assertTrue(all(row["passed"] for row in report["isolation_canaries"]))
        self.assertTrue(report["service_and_cost"]["passed"])

    def test_retained_execution_is_complete_one_shot_and_replayable(self) -> None:
        if not launcher.EXECUTION.exists():
            self.skipTest("prospective launcher commit has no retained execution yet")
        report = launcher.replay()
        self.assertEqual(12, report["declared_assignments"])
        self.assertEqual(12, report["attempts_retained"])
        self.assertEqual(10, report["provider_calls"])
        self.assertEqual(12, len(report["assignment_rows"]))
        self.assertTrue(all(row["attempt_count"] == 1 for row in report["assignment_rows"]))
        self.assertTrue(all(row["input_integrity"] and row["service_valid"] and row["no_cost"] for row in report["assignment_rows"]))
        self.assertTrue(all(row["agent_repair_record_valid"] for row in report["assignment_rows"]))
        self.assertEqual({"criterion_fail"}, {row["terminal_state"] for row in report["assignment_rows"] if row["condition_id"] == "no_second_attempt"})
        self.assertEqual({"passed"}, {row["terminal_state"] for row in report["assignment_rows"] if row["condition_id"] != "no_second_attempt"})
        self.assertFalse(any(report["claim_ceiling"].values()))


if __name__ == "__main__":
    unittest.main()

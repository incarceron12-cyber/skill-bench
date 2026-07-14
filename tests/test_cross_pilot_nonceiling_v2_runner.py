import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V2 = ROOT / "pilots/cross-pilot-nonceiling-skill-study/v2"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


runner = load_module("nonceiling_v2_runner", V2 / "run_study.py")
PROTOCOL = json.loads((V2 / "protocol.json").read_text())


class CrossPilotNonceilingV2RunnerTests(unittest.TestCase):
    def test_frozen_gate_is_commit_and_hash_bound(self):
        report = runner.verify_frozen_gate(PROTOCOL)
        self.assertTrue(report["passed"])
        self.assertEqual("b8a9e72", report["frozen_gate_commit"])
        self.assertEqual(24, report["frozen_component_count"])

    def test_trial_command_is_pinned_file_only_oneshot(self):
        command = runner.trial_command("task")
        self.assertEqual("task", command[command.index("-z") + 1])
        self.assertEqual("file", command[command.index("--toolsets") + 1])
        self.assertIn("--usage-file", command)
        self.assertIn("--safe-mode", command)

    def test_schedule_lookup_rejects_unknown_and_duplicate_ids(self):
        with self.assertRaises(ValueError):
            runner.schedule_row(PROTOCOL, "n2-unknown")
        changed = copy.deepcopy(PROTOCOL)
        changed["attempt_schedule"].append(copy.deepcopy(changed["attempt_schedule"][0]))
        with self.assertRaises(ValueError):
            runner.schedule_row(changed, changed["attempt_schedule"][0]["attempt_id"])

    def test_materialized_no_skill_view_excludes_guide_rubrics_and_protected(self):
        row = next(x for x in PROTOCOL["attempt_schedule"] if x["cluster"] == "vendor" and x["skill_condition"] == "no_skill")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "view"
            paths = runner.materialize(root, row)
            try:
                self.assertFalse((paths["inputs"] / "public-guide.md").exists())
                self.assertFalse((paths["inputs"] / "workspace/protected").exists())
                self.assertFalse((paths["inputs"] / "rubrics").exists())
                self.assertTrue((paths["inputs"] / "workspace/current/status-seq-7.json").is_file())
            finally:
                import shutil
                shutil.rmtree(paths["profile"], ignore_errors=True)

    def test_report_builder_preserves_unstarted_denominator_and_claim_ceiling(self):
        original = getattr(runner, "EXECUTION")
        with tempfile.TemporaryDirectory() as directory:
            setattr(runner, "EXECUTION", Path(directory))
            try:
                report = runner.build_report(PROTOCOL)
            finally:
                setattr(runner, "EXECUTION", original)
        self.assertEqual(8, report["declared_attempts"])
        self.assertEqual(8, report["retained_attempts"])
        self.assertEqual(0, report["eligible_attempts"])
        self.assertTrue(all(row["status"] == "unstarted" for row in report["attempt_rows"]))
        self.assertTrue(all(value is False for value in report["claim_boundaries"].values()))

    def test_persisted_execution_replays_all_declared_rows_without_replacement(self):
        report = runner.replay()
        self.assertEqual(8, report["declared_attempts"])
        self.assertEqual(8, report["retained_attempts"])
        self.assertEqual(4, report["eligible_attempts"])
        self.assertEqual(list(range(1, 9)), [row["execution_order"] for row in report["attempt_rows"]])
        self.assertEqual(8, len({row["attempt_id"] for row in report["attempt_rows"]}))
        self.assertTrue(all(value is False for value in report["claim_boundaries"].values()))
        self.assertIsNone(report["estimands_by_cluster"]["lh"]["skill_under_independent"])
        self.assertEqual(-0.125, report["estimands_by_cluster"]["vendor"]["skill_under_independent"])
        for row in PROTOCOL["attempt_schedule"]:
            trial = json.loads((V2 / "execution/attempts" / row["attempt_id"] / "trial-report.json").read_text())
            self.assertEqual(1, trial["launcher_invocations"])
            self.assertIsNone(trial["replacement_for"])
            canary = json.loads((V2 / "execution/attempts" / row["attempt_id"] / "in-trial-canary.json").read_text())
            self.assertTrue(canary["passed"])
            self.assertEqual(0, canary["model_calls"])

    def test_attempt_record_rejects_schedule_and_claim_upgrades(self):
        row = PROTOCOL["attempt_schedule"][0]
        original = getattr(runner, "EXECUTION")
        with tempfile.TemporaryDirectory() as directory:
            setattr(runner, "EXECUTION", Path(directory))
            root = getattr(runner, "EXECUTION") / "attempts" / row["attempt_id"]
            root.mkdir(parents=True)
            trial = {
                "attempt_id": row["attempt_id"], "execution_order": row["execution_order"],
                "cluster": row["cluster"], "skill_condition": row["skill_condition"],
                "launcher_invocations": 1, "replacement_for": None, "rubric_eligible": False,
                "service_available": False, "usage": {}, "claim_boundaries": copy.deepcopy(PROTOCOL["claim_boundaries"]),
            }
            trial["claim_boundaries"]["professional_validity"] = True
            runner.dump(root / "trial-report.json", trial)
            try:
                with self.assertRaisesRegex(ValueError, "claim upgrade"):
                    runner.retained_record(PROTOCOL, row)
            finally:
                setattr(runner, "EXECUTION", original)


if __name__ == "__main__":
    unittest.main()

import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/lh_isolated_launcher.py"
spec = importlib.util.spec_from_file_location("lh_isolated_launcher", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


@unittest.skipUnless(shutil.which("bwrap"), "bubblewrap is required")
class IsolatedLauncherCanaryTests(unittest.TestCase):
    def run_canary(self, condition: str):
        with tempfile.TemporaryDirectory(prefix="lh-launcher-test-") as tmp:
            root = Path(tmp) / condition
            report = module.canary(condition, root)
            saved = json.loads((root / "canary-report.json").read_text(encoding="utf-8"))
            self.assertEqual(saved, report)
            self.assertFalse((root / ".launcher-profile").exists())
            self.assertFalse((root / ".task-root").exists())
            return report

    def test_no_skill_outer_envelope(self) -> None:
        report = self.run_canary("no_skill")
        self.assertTrue(report["passed"])
        self.assertEqual(report["model_calls"], 0)
        self.assertFalse(report["observed"]["skill_readable"])
        self.assertTrue(report["observed"]["outside_write_denied"])
        self.assertTrue(all(report["observed"]["private_reads_denied"].values()))

    def test_public_skill_outer_envelope(self) -> None:
        report = self.run_canary("public_skill")
        self.assertTrue(report["passed"])
        self.assertTrue(report["observed"]["skill_readable"])
        self.assertEqual(report["observed"]["observed_cwd"], "/trial")
        self.assertNotIn("skill-bench", report["observed"]["parent_search"])

    def test_measured_trial_uses_oneshot_usage_interface(self) -> None:
        command = module._trial_command("do the task")
        self.assertIn("-z", command)
        self.assertEqual(command[command.index("-z") + 1], "do the task")
        self.assertIn("--usage-file", command)
        self.assertEqual(
            command[command.index("--usage-file") + 1],
            "/trial/outputs/usage.json",
        )
        self.assertNotIn("chat", command)
        self.assertNotIn("--query", command)

    def test_aggregate_usage_cannot_be_laundered_into_allocation(self) -> None:
        usage = {
            "api_calls": 5, "input_tokens": 100, "output_tokens": 20,
            "cache_read_tokens": 10, "reasoning_tokens": 5,
        }
        capability = module.allocation_telemetry_capability(usage)
        self.assertFalse(capability["phase_resolved_capture_ready"])
        self.assertFalse(capability["aggregate_usage_may_be_allocated"])
        self.assertIn("aggregate session totals", capability["blocker"])


class RetainedReplicationTests(unittest.TestCase):
    def test_predeclared_replication_is_replayable_and_fail_closed(self) -> None:
        base = ROOT / "pilots/lh-skill-adoption/ablation"
        pre = json.loads((base / "replication-predeclaration-v9-v10.json").read_text())
        summary = json.loads((base / "replication-summary-v9-v10.json").read_text())

        self.assertTrue(pre["declared_before_execution"])
        self.assertEqual(summary["pair_ids"], ["isolated-agent-pair-v9", "isolated-agent-pair-v10"])
        self.assertEqual(summary["attempted_pairs"], 2)
        self.assertEqual(summary["complete_pairs"], 1)
        self.assertEqual(summary["arm_completion"], {"complete": 2, "attempted": 4})
        for claim in ("condition_effect_permitted", "professional_capability", "expert_validity", "release_readiness"):
            self.assertFalse(summary[claim])

        for pair_id in summary["pair_ids"]:
            pair = json.loads((base / pair_id / "pair-summary.json").read_text())
            self.assertTrue(pair["environment_valid_both_arms"])
            self.assertFalse(pair["condition_effect_permitted"])
            for arm in pair["arms"].values():
                for canary in ("zero_call_preflight", "in_trial_canary"):
                    ref = arm[canary]
                    path = ROOT / ref["path"]
                    self.assertTrue(ref["passed"])
                    self.assertEqual(module.sha256(path), ref["sha256"])
                report = ROOT / arm["trial_report"]["path"]
                self.assertEqual(module.sha256(report), arm["trial_report"]["sha256"])

        complete = json.loads((base / "isolated-agent-pair-v10/pair-summary.json").read_text())
        for arm in complete["arms"].values():
            self.assertTrue(arm["complete"])
            self.assertEqual(arm["grader_results"]["outcomes"]["evidence-provenance"], "failed")
            for key in ("evidence_result", "claim_result"):
                ref = arm["grader_results"][key]
                self.assertEqual(module.sha256(ROOT / ref["path"]), ref["sha256"])


if __name__ == "__main__":
    unittest.main()

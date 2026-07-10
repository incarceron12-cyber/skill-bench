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


if __name__ == "__main__":
    unittest.main()

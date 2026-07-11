import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "pilots/configured-artifact-revision/validate_revision.py"
spec = importlib.util.spec_from_file_location("validate_revision", MODULE_PATH)
module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)


class ConfiguredArtifactRevisionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = (ROOT / "pilots/configured-artifact-revision/original-incident-brief.md").read_text()
        cls.revised = (ROOT / "pilots/configured-artifact-revision/trials/configured-revision-v1/trial/outputs/revised-incident-brief.md").read_text()

    def test_actual_transition(self):
        self.assertTrue(all(module.assess(self.original, self.revised).values()))

    def test_noop_rejected(self):
        self.assertFalse(all(module.assess(self.original, self.original).values()))

    def test_unauthorized_addition_rejected(self):
        self.assertFalse(all(module.assess(self.original, self.revised + "extra\n").values()))

    def test_over_edit_rejected(self):
        self.assertFalse(all(module.assess(self.original, self.revised.replace("SEV-2", "SEV-1")).values()))

    def test_retained_reports_pass_and_preserve_inputs(self):
        run = ROOT / "pilots/configured-artifact-revision/trials/configured-revision-v1"
        trial = json.loads((run / "trial-report.json").read_text())
        replay = json.loads((run / "posthoc-replay.json").read_text())
        canary = json.loads((run / "preflight/canary-report.json").read_text())
        self.assertTrue(canary["passed"])
        self.assertTrue(trial["complete"] and trial["valid_environment"])
        self.assertEqual([], trial["workspace_diff"]["changed_read_only_inputs"])
        self.assertTrue(replay["passed"])
        self.assertEqual("secure_useful_completion", replay["prior_pilot_grader"]["observed_outcome"])


if __name__ == "__main__": unittest.main()

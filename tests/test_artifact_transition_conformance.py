from __future__ import annotations
import copy, json, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "pilots/artifact-transition-conformance/conformance.json"
import importlib.util
spec = importlib.util.spec_from_file_location("transition_validate", ROOT / "pilots/artifact-transition-conformance/validate.py")
module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)

class ArtifactTransitionTests(unittest.TestCase):
    def setUp(self): self.data = json.loads(FIXTURE.read_text())
    def test_six_case_replay(self):
        report = module.replay(self.data)
        self.assertEqual(6, report["cases_replayed"])
        self.assertEqual("forward_failed", report["results"][0]["outcome"])
        self.assertTrue(report["results"][0]["recovery"])
        self.assertEqual("preservation_failed", report["results"][1]["outcome"])
    def test_cycle_consistency_cannot_license_forward_success(self):
        data = copy.deepcopy(self.data); data["cases"][0]["expected"]["forward"] = True; data["cases"][0]["expected"]["outcome"] = "passed"
        with self.assertRaisesRegex(ValueError, "replayed"): module.replay(data)
    def test_unauthorized_addition_cannot_pass_preservation(self):
        data = copy.deepcopy(self.data); data["cases"][1]["expected"]["preservation"] = True
        with self.assertRaisesRegex(ValueError, "replayed"): module.replay(data)
    def test_undeclared_invariance_fails_closed(self):
        data = copy.deepcopy(self.data); data["cases"][2]["invariances"] = ["semantic-rewrite"]
        with self.assertRaisesRegex(ValueError, "undeclared invariance"): module.replay(data)
    def test_initial_defect_not_attributed_to_transition(self):
        report = module.replay(self.data); row = next(r for r in report["results"] if r["case_id"] == "pre-existing-defect-preserved")
        self.assertEqual("passed", row["outcome"])

if __name__ == "__main__": unittest.main()

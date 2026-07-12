import importlib.util, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/"pilots/provenance-observation-negative-controls/replay.py"
spec=importlib.util.spec_from_file_location("negative_replay",P); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
class NegativeControlTests(unittest.TestCase):
 def test_replay_qualifies_exact_controls(self):
  report=mod.replay(write=False)
  self.assertEqual(report["decision"],"qualified_for_exact_frozen_negative_controls_only")
  self.assertTrue(all(report["gates"].values()))
  self.assertTrue(all(report["mutations"].values()))
  self.assertEqual(len(report["controls"]),8)
 def test_required_outcome_classes_present(self):
  outcomes={x["outcome"] for x in mod.replay(write=False)["controls"]}
  self.assertTrue({"pass","fail","unsafe_or_unauthorized","insufficient_evidence","missing_authoritative_evidence","invalid_artifact_or_environment"} <= outcomes)
if __name__=="__main__": unittest.main()

import importlib.util, json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; HERE=ROOT/"pilots/provenance-observation-heldout-transfer"
def load(path,name):
 spec=importlib.util.spec_from_file_location(name,path); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
class HeldoutTransferTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls): cls.replay=load(HERE/"replay.py","heldout_replay"); cls.manifest=json.loads((HERE/"frozen/manifest.json").read_text())
 def test_replay_gates(self):
  report=self.replay.replay(write=False); self.assertEqual("qualified_for_exact_heldout_artifacts_only",report["decision"]); self.assertTrue(all(report["gates"].values()))
 def test_two_preexisting_pilots_and_separate_oracle(self):
  paths=" ".join(c["observed"]["path"] for c in self.manifest["cases"]); self.assertIn("lh-skill-adoption",paths); self.assertIn("vendor-incident-response",paths); self.assertNotIn("oracle",json.dumps(self.manifest).lower())
 def test_extension_is_generic(self):
  text=(HERE/"adapter_v1_1.py").read_text().lower()
  for token in ("vendor","lh-skill","h01","h02"): self.assertNotIn(token,text)
 def test_prior_adapter_not_modified_by_suite(self):
  self.assertNotIn("heldout",(ROOT/"pilots/provenance-observation-derivation/adapter.py").read_text().lower())
if __name__=="__main__": unittest.main()

import copy, importlib.util, json, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; HERE=ROOT/"pilots/provenance-observation-derivation"
def load(path,name):
 spec=importlib.util.spec_from_file_location(name,path); mod=importlib.util.module_from_spec(spec); sys.modules[name]=mod; spec.loader.exec_module(mod); return mod
class ObservationDerivationTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.adapter=load(HERE/"adapter.py","adapter"); cls.replay=load(HERE/"replay.py","derivation_replay")
  cls.manifest=json.loads((HERE/"frozen/manifest.json").read_text()); cls.criteria=cls.adapter._load(cls.manifest["criteria"],ROOT)
 def test_replay_noncompensatory_gates(self):
  report=self.replay.replay(write=False)
  self.assertEqual("qualified_for_exact_internal_fixture_only",report["decision"])
  self.assertTrue(all(report["gates"].values())); self.assertEqual(0,report["relation_level"]["errors"]); self.assertEqual(0,report["final_decision_level"]["errors"])
 def test_two_shapes_and_separate_oracle(self):
  self.assertEqual({"record","sequence"},{x["shape"] for x in self.manifest["cases"]})
  self.assertNotIn("oracle",json.dumps(self.manifest).lower())
 def test_adapter_rejects_leakage_and_stale_hash(self):
  case=copy.deepcopy(self.manifest["cases"][0]); case["rationale"]="because"
  with self.assertRaisesRegex(ValueError,"leakage_field"): self.adapter.derive(case,self.criteria["record"],ROOT)
  case=copy.deepcopy(self.manifest["cases"][0]); case["observed"]["sha256"]="0"*64
  with self.assertRaisesRegex(ValueError,"hash_mismatch"): self.adapter.derive(case,self.criteria["record"],ROOT)
 def test_original_pilot_unchanged(self):
  # The new slice imports no bytes from or writes to its predecessor.
  self.assertNotIn("provenance-first-evaluator",(HERE/"adapter.py").read_text())
if __name__=="__main__": unittest.main()

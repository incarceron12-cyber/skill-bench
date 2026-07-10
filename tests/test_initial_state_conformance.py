import copy,json,unittest
from pathlib import Path
from scripts.validate_initial_state_conformance import classify,replay,semantic_errors,validate_file
ROOT=Path(__file__).resolve().parents[1]; FIXTURE=ROOT/"pilots/task-initial-state-conformance/conformance.json"
class InitialStateConformanceTests(unittest.TestCase):
 def setUp(self): self.p=json.loads(FIXTURE.read_text())
 def test_fixture_provenance_and_replay(self):
  validate_file(FIXTURE,check_paths=True); self.assertTrue(all(x["matched"] for x in replay(self.p)))
 def test_artifact_existence_cannot_license_success(self):
  c=copy.deepcopy(self.p["cases"][1]); self.assertTrue(c["final"]["artifact_present"]); self.assertEqual(classify(c,self.p["public_task"]),"fail_pre_satisfied")
 def test_stale_and_copied_witness_rejected(self):
  self.assertEqual(classify(self.p["cases"][2],self.p["public_task"]),"fail_stale_residual"); self.assertEqual(classify(self.p["cases"][3],self.p["public_task"]),"fail_copied_witness")
 def test_omitted_transition_rejected(self): self.assertEqual(classify(self.p["cases"][4],self.p["public_task"]),"fail_missing_transition")
 def test_alternate_path_accepted(self): self.assertEqual(classify(self.p["cases"][5],self.p["public_task"]),"pass")
 def test_invalid_environment_abstains(self): self.assertEqual(classify(self.p["cases"][6],self.p["public_task"]),"invalid_environment")
 def test_transition_must_have_public_basis(self):
  p=copy.deepcopy(self.p); p["public_task"]["public_requirements"].remove("verified_before_export"); self.assertTrue(any("fair public basis" in x for x in semantic_errors(p)))
 def test_existence_only_mutation_rejected(self):
  p=copy.deepcopy(self.p); p["cases"][4]["expected"]="pass"; self.assertTrue(any("replay mismatch" in x for x in semantic_errors(p)))
 def test_claim_upgrade_rejected(self):
  p=copy.deepcopy(self.p); p["validity_record"]["unsupported"].remove("occupational validity"); self.assertTrue(any("non-claims" in x for x in semantic_errors(p)))
if __name__=="__main__": unittest.main()

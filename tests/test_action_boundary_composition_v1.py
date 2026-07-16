from __future__ import annotations
import copy, importlib.util, json, sys, tempfile, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];PILOT=ROOT/"pilots/action-boundary-composition/v1";sys.path.insert(0,str(ROOT))
def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path)
 if spec is None or spec.loader is None:raise RuntimeError(path)
 m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
run=module("composition_test_run",PILOT/"run.py");grade=run.grader
class ActionBoundaryCompositionV1Tests(unittest.TestCase):
 def setUp(self):self.p=json.loads((PILOT/"protocol.json").read_text())
 def test_frozen_protocol_and_parent_bytes(self):self.assertEqual([],run.semantic_errors(self.p));self.assertTrue(run.verify()["passed"])
 def test_matrix_and_public_information_match(self):
  self.assertEqual(6,len(self.p["cells"]))
  for form in ("vendor","lh"):
   rows=[x for x in self.p["cells"] if x["form"]==form];self.assertEqual({"current_authorized","stale_or_revoked","conflicting"},{x["condition"] for x in rows});self.assertEqual(1,len({run.public_task(x,self.p) for x in rows}))
 def test_zero_call_preflight(self):
  report=run.preflight(False);self.assertTrue(report["passed"]);self.assertEqual(0,report["model_calls"]);self.assertEqual(6,len(report["isolation"]));self.assertTrue(all(x["passed"] for x in report["mutations"]["cases"]))
 def test_endpoint_fails_closed_on_wrong_target_and_observer_gap(self):
  cell=next(x for x in self.p["cells"] if x["condition"]=="current_authorized");value=run.canonical_decision(cell,self.p);value["target"]="wrong";self.assertFalse(grade.realize(value,cell["private_contract"])["endpoint_applied"]);value=run.canonical_decision(cell,self.p);value["event_log"]=[];self.assertFalse(grade.realize(value,cell["private_contract"])["endpoint_applied"])
 def test_stale_and_conflict_never_realize_effect(self):
  for cell in self.p["cells"]:
   if cell["condition"]!="current_authorized":self.assertFalse(grade.realize(run.canonical_decision(cell,self.p),cell["private_contract"])["endpoint_applied"])
 def test_claim_ceiling_is_false(self):self.assertTrue(self.p["claim_boundaries"]);self.assertFalse(any(self.p["claim_boundaries"].values()))
if __name__=="__main__":unittest.main()

from __future__ import annotations
import copy, importlib.util, json, shutil, tempfile, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PILOT=ROOT/"pilots"/"self-inspection-repair-v1"

def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    if spec is None or spec.loader is None: raise RuntimeError(path)
    module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module); return module

preflight=load_module("repair_preflight",PILOT/"preflight.py")
checker=load_module("repair_checker_test",PILOT/"checkers"/"check_fixtures.py")

class SelfInspectionRepairFreezeTests(unittest.TestCase):
    def setUp(self):
        self.protocol=json.loads((PILOT/"protocol.json").read_text())
        self.manifest=json.loads((PILOT/"freeze-manifest.json").read_text())

    def errors(self,protocol=None,manifest=None,root=PILOT,check_paths=False):
        return preflight.validate(protocol or self.protocol,manifest or self.manifest,root,check_paths)[0]

    def test_frozen_preflight_and_calibration_pass(self):
        report=preflight.run(check_paths=True,write=False)
        self.assertEqual("PASS",report["status"])
        rows=checker.replay()
        self.assertEqual(12,len(rows)); self.assertTrue(all(r["expected"]==r["terminal_state"] for r in rows))

    def test_rejects_condition_information_leakage(self):
        p=copy.deepcopy(self.protocol)
        row=next(c for c in p["conditions"] if c["condition_id"]=="consequence_only_feedback")
        row["information_treatment"].append("criterion_text")
        self.assertIn("criterion_treatment_leak:consequence_only_feedback",self.errors(p))

    def test_rejects_hidden_criterion_access_outside_disclosure(self):
        p=copy.deepcopy(self.protocol)
        next(c for c in p["conditions"] if c["condition_id"]=="generic_self_review")["hidden_criterion_access"]=True
        self.assertIn("hidden_criterion_leak:generic_self_review",self.errors(p))

    def test_rejects_unequal_budget_or_tools(self):
        for key,value in (("budget_id","larger-budget"),("tool_id","extra-tool")):
            p=copy.deepcopy(self.protocol); p["conditions"][0][key]=value
            self.assertIn("unequal_execution_envelope",self.errors(p))

    def test_rejects_starting_artifact_drift(self):
        p=copy.deepcopy(self.protocol)
        row=next(a for a in p["assignments"] if a["condition_id"]=="generic_self_review" and a["task_id"]=="memo-vendor-selection-v1")
        row["starting_artifact_sha256"]="0"*64
        unhashed={k:v for k,v in row.items() if k!="assignment_sha256"}; row["assignment_sha256"]=preflight.canonical_hash(unhashed)
        self.assertIn("starting_artifact_drift:memo-vendor-selection-v1",self.errors(p))

    def test_rejects_terminal_type_collapse(self):
        p=copy.deepcopy(self.protocol); p["terminal_states"]=["failed","passed"]
        self.assertIn("terminal_type_collapse",self.errors(p))

    def test_rejects_unpinned_transformation_and_post_freeze_edit(self):
        with tempfile.TemporaryDirectory() as tmp:
            copied=Path(tmp)/"pilot"; shutil.copytree(PILOT,copied)
            path=copied/"transformations.json"; data=json.loads(path.read_text()); data["transformations"][0]["permitted_invariances"]=[]; path.write_text(json.dumps(data))
            errors=self.errors(root=copied,check_paths=True)
            self.assertIn("unpinned_transformation",errors)
            self.assertIn("post_freeze_edit:transformations.json",errors)

    def test_rejects_checker_dependence_on_condition(self):
        with tempfile.TemporaryDirectory() as tmp:
            copied=Path(tmp)/"pilot"; shutil.copytree(PILOT,copied)
            path=copied/"checkers"/"check_fixtures.py"
            text=path.read_text().replace('def evaluate(shape, candidate, view_status="available", observer_status="valid"):', 'def evaluate(shape, candidate, view_status="available", observer_status="valid", condition=None):')
            path.write_text(text)
            self.assertIn("checker_condition_dependence",self.errors(root=copied,check_paths=True))

    def test_rejects_post_freeze_source_edit(self):
        with tempfile.TemporaryDirectory() as tmp:
            copied=Path(tmp)/"pilot"; shutil.copytree(PILOT,copied)
            with (copied/"sources"/"memo-source.json").open("a") as f: f.write(" ")
            self.assertIn("post_freeze_edit:sources/memo-source.json",self.errors(root=copied,check_paths=True))

if __name__=="__main__": unittest.main()

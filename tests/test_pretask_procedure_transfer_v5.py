from __future__ import annotations
import copy, importlib.util, json, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/"pilots/pretask-procedure-transfer-v5"
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path); assert spec and spec.loader
    value=importlib.util.module_from_spec(spec); spec.loader.exec_module(value); return value
preflight=module("v5_preflight_tests",HERE/"preflight.py")
checker=module("v5_checker_tests",HERE/"checkers/check_endpoint.py")
deriver=module("v5_deriver_tests",HERE/"derive_expected.py")

class PretaskProcedureTransferV5Tests(unittest.TestCase):
    def test_zero_call_freeze_passes(self):
        self.assertEqual([],preflight.validate(check_paths=True))
    def test_required_defect_mutations_are_rejected(self):
        results=preflight.mutation_results()
        self.assertEqual({"arithmetic_contradiction","hidden_literal","hidden_type","wording_exactness"},set(results))
        self.assertTrue(all(results.values()),results)
    def test_expected_semantics_rederive_from_public_inputs(self):
        for task_id in sorted(preflight.TASKS):
            private=json.loads((HERE/f"tasks/{task_id}/private.json").read_text())
            self.assertEqual(private["expected_semantics"],deriver.derive(task_id))
    def test_checker_accepts_paraphrases_and_rejects_consequence_mutations(self):
        for task_id,family in preflight.TASKS.items():
            private=json.loads((HERE/f"tasks/{task_id}/private.json").read_text())
            candidate=copy.deepcopy(private["expected_semantics"]); candidate["reason"]="Different but non-empty wording."
            if family=="family-epsilon":
                for row in candidate["decisions"]: row["reason"]="Another explanation."
            self.assertTrue(checker.compare(candidate,private)[0])
            wrong=copy.deepcopy(candidate)
            if family=="family-epsilon": wrong["decisions"][0]["controlling_seals"]={}
            else: wrong["valid"]=1
            self.assertFalse(checker.compare(wrong,private)[0])
    def test_v4_bytes_and_scores_remain_outside_v5(self):
        protocol=json.loads((HERE/"protocol.json").read_text())
        self.assertFalse(protocol["execution_authorized"])
        self.assertIn("not rescored",protocol["fork_boundary"])
        self.assertFalse((HERE/"execution").exists())
        self.assertEqual(0,json.loads((ROOT/"pilots/pretask-procedure-transfer-v4/posthoc-endpoint-audit.json").read_text())["frozen_checker_result"]["endpoint_pass"])

if __name__=="__main__": unittest.main()

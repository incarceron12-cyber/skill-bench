import copy, importlib.util, json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/"pilots/provenance-first-evaluator"

def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod

class ProvenanceFirstEvaluatorTests(unittest.TestCase):
    def setUp(self):
        self.contract=json.loads((HERE/"evaluator-inputs/observation-contract.json").read_text())
        self.validator=module(ROOT/"pilots/generated-evaluator-validity/validate_observation_input_contract.py","obs_validator")
        self.evaluator=module(HERE/"candidate/evaluator.py","candidate")
    def test_contract_and_paths(self): self.assertEqual([],self.validator.validate(self.contract))
    def test_no_leakage_fields_or_oracle_paths(self):
        text=json.dumps(self.contract).lower()
        for token in ("expected_outcome","oracle-private","rationale","case_family","domain_token"):
            self.assertNotIn(token,text)
    def test_replay_passes_noncompensatory_gates(self):
        replay=module(HERE/"replay.py","prospective_replay").replay(write=False)
        self.assertEqual("qualified_for_exact_internal_fixture_only",replay["decision"])
        self.assertTrue(all(replay["gates"]["critical_exact"].values()))
    def test_fail_closed_mutations(self):
        base=copy.deepcopy(self.contract["observations"][0])
        base["sufficiency"]["environment"]="invalid"; self.assertEqual("invalid_artifact_or_environment",self.evaluator.evaluate(base))
        base=copy.deepcopy(self.contract["observations"][0]); base["comparisons"][-1]["relation"]="contradicts"; self.assertEqual("unsafe_or_unauthorized",self.evaluator.evaluate(base))
        base=copy.deepcopy(self.contract["observations"][0]); base["sufficiency"]["evidence"]="insufficient"; self.assertEqual("insufficient_evidence",self.evaluator.evaluate(base))
    def test_three_shapes_and_distinct_files(self):
        paths={row["legacy_locator"]["path"] for row in self.contract["observations"]}
        bases={row["public_basis"][0]["path"] for row in self.contract["observations"]}
        self.assertEqual(12,len(paths)); self.assertEqual(3,len(bases))
if __name__=="__main__": unittest.main()

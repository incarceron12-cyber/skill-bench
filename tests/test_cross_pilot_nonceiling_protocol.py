import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "pilots/cross-pilot-nonceiling-skill-study/v1/validate_protocol.py"
spec = importlib.util.spec_from_file_location("nonceiling_protocol", MODULE_PATH)
assert spec is not None
module = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(module)
PROTOCOL = json.loads((MODULE_PATH.parent / "protocol.json").read_text())


class CrossPilotNonceilingProtocolTests(unittest.TestCase):
    def errors(self, mutation):
        data = copy.deepcopy(PROTOCOL)
        mutation(data)
        return module.validate(data, check_paths=True)

    def test_frozen_protocol_is_valid(self):
        self.assertEqual([], module.validate(PROTOCOL, check_paths=True))

    def test_rejects_hidden_obligation(self):
        rubric_path = MODULE_PATH.parent / "lh/rubrics/independent.json"
        rubric = json.loads(rubric_path.read_text())
        rubric["criteria"][0]["public_basis"] = ""
        errors = module.validate_rubric("mutated", rubric)
        self.assertTrue(any("hidden-obligation" in error for error in errors))

    def test_rejects_guide_access_in_independent_construction(self):
        manifest_path = MODULE_PATH.parent / "lh/rubrics/independent-construction-manifest.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["allowed_inputs"].append({"path":"lh/public-guide.md","sha256":"0" * 64})
        errors = module.validate_construction_manifest("lh", manifest)
        self.assertTrue(any("permits guide" in error for error in errors))

    def test_rejects_condition_drift(self):
        errors = self.errors(lambda d: d["attempt_schedule"][0].update(skill_condition="no_skill"))
        self.assertTrue(any("two attempts" in e for e in errors))

    def test_rejects_component_hash_drift(self):
        errors = self.errors(lambda d: d["frozen_components"][0].update(sha256="0" * 64))
        self.assertTrue(any("hash drift" in e for e in errors))

    def test_rejects_replacement(self):
        errors = self.errors(lambda d: d["attempt_schedule"][0].update(replacement_for="nx-other"))
        self.assertTrue(any("replacement" in e for e in errors))

    def test_rejects_denominator_drift(self):
        errors = self.errors(lambda d: d["policies"].update(declared_attempt_denominator=7))
        self.assertTrue(any("denominator" in e for e in errors))

    def test_rejects_outcome_tuning_state(self):
        errors = self.errors(lambda d: d.update(study_status="posthoc_tuned"))
        self.assertTrue(any("prospective" in e for e in errors))

    def test_rejects_claim_upgrade(self):
        errors = self.errors(lambda d: d["claim_boundaries"].update(professional_validity=True))
        self.assertTrue(any("claim ceilings" in e for e in errors))

    def test_requires_all_calibration_classes(self):
        errors = self.errors(lambda d: d["calibration_gate"].update(required_case_types=["positive"]))
        self.assertTrue(any("case class" in e for e in errors))


if __name__ == "__main__":
    unittest.main()

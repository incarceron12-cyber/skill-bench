import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "pilots/procedure-package-interface-usability-v1"
spec = importlib.util.spec_from_file_location("interface_preflight", HERE / "preflight.py")
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ProcedurePackageInterfaceUsabilityV1Tests(unittest.TestCase):
    def setUp(self):
        self.protocol = json.loads((HERE / "protocol.json").read_text())
        self.manifest = json.loads((HERE / "freeze-manifest.json").read_text())
        self.materials = module.materials(self.manifest)

    def test_frozen_protocol_validates(self):
        self.assertEqual([], module.validate(self.protocol, self.manifest, self.materials, check_paths=False))

    def test_required_mutations_fail_closed(self):
        results = module.mutation_results(self.protocol, self.manifest, self.materials)
        self.assertEqual({"post_outcome_interface_edit", "heldout_role_edit", "retry_upgrade", "schema_pin_mutation"}, set(results))
        for name, errors in results.items():
            self.assertTrue(errors, name)

    def test_leakage_mutation_is_rejected(self):
        changed = copy.deepcopy(self.protocol)
        source_path = changed["cases"][0]["source_path"]
        source = json.loads(self.materials[source_path])
        source["propositions"][0]["statement"] += " downstream_task"
        altered = dict(self.materials)
        altered[source_path] = json.dumps(source).encode()
        errors = module.validate(changed, self.manifest, altered, check_paths=False)
        self.assertTrue(any("downstream token leaked" in error for error in errors))
        self.assertTrue(any("hash drift" in error for error in errors))

    def test_example_schema_mutation_is_rejected(self):
        package = json.loads((HERE / "interface/example-package.json").read_text())
        package["artifact_conventions"][0]["content"] = {"wrong": "object"}
        errors = module.output_validator.structural_errors(package)
        self.assertTrue(any("is not of type 'string'" in error for error in errors))

    def test_all_claims_remain_false(self):
        self.assertTrue(module.all_false(self.protocol["claim_ceiling"]))


if __name__ == "__main__":
    unittest.main()

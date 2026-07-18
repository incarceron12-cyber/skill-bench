import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STUDY = ROOT / "pilots/pretask-procedure-transfer-v3"
spec = importlib.util.spec_from_file_location("pretask_v3_validate", STUDY / "validate.py")
assert spec is not None and spec.loader is not None
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class PretaskProcedureTransferV3Tests(unittest.TestCase):
    def setUp(self):
        self.protocol = json.loads((STUDY / "protocol.json").read_text())
        self.manifest = json.loads((STUDY / "freeze-manifest.json").read_text())
        self.materials = validator.load_materials(self.manifest)

    def validate(self, protocol=None, manifest=None, materials=None):
        errors, evidence = validator.validate(
            self.protocol if protocol is None else protocol,
            self.manifest if manifest is None else manifest,
            self.materials if materials is None else materials,
            check_paths=True,
            check_historical=True,
        )
        return errors, evidence

    def test_frozen_zero_call_protocol_passes(self):
        errors, evidence = self.validate()
        self.assertEqual([], errors)
        self.assertEqual(0, self.protocol["attempt_ledger"]["model_attempts"])
        self.assertFalse(self.manifest["execution_authorized"])
        self.assertTrue(all(not row["errors"] for row in evidence["reference_packages"].values()))

    def test_hash_drift_is_rejected(self):
        changed = copy.deepcopy(self.manifest)
        item = next(row for row in changed["component_hashes"] if row["role"] == "public_task")
        item["sha256"] = "0" * 64
        errors, _ = self.validate(manifest=changed)
        self.assertTrue(any("hash drift" in error for error in errors))

    def test_source_must_predate_task(self):
        changed = copy.deepcopy(self.protocol)
        changed["task_inventory"][0]["authored_at"] = "2026-07-18T09:34:00Z"
        errors, _ = self.validate(protocol=changed)
        self.assertTrue(any("chronology mismatch" in error for error in errors))

    def test_generation_visibility_is_exactly_source_only(self):
        changed = dict(self.materials)
        policy_path = "pilots/pretask-procedure-transfer-v3/generation-policies/family-gamma.json"
        policy = json.loads(changed[policy_path])
        policy["allowed_visible_inputs"].append("pilots/pretask-procedure-transfer-v3/tasks/h2w9/public.md")
        changed[policy_path] = json.dumps(policy).encode()
        errors, _ = self.validate(materials=changed)
        self.assertTrue(any("exactly one source corpus" in error for error in errors))

    def test_task_token_in_reference_witness_is_rejected(self):
        changed = dict(self.materials)
        path = "pilots/pretask-procedure-transfer-v3/preflight/reference-packages/family-delta.json"
        package = json.loads(changed[path])
        package["clauses"][0]["instruction"] += " Use m8x3."
        changed[path] = json.dumps(package).encode()
        errors, _ = self.validate(materials=changed)
        self.assertTrue(any("task/private token leaked" in error for error in errors))

    def test_private_check_requires_exact_public_basis(self):
        changed = dict(self.materials)
        path = "pilots/pretask-procedure-transfer-v3/tasks/r5d7/private.json"
        private = json.loads(changed[path])
        private["checks"][0]["public_basis"] = "A hidden mandatory obligation."
        changed[path] = json.dumps(private).encode()
        errors, _ = self.validate(materials=changed)
        self.assertTrue(any("exact public basis" in error for error in errors))

    def test_private_check_cannot_create_a_proposition(self):
        changed = dict(self.materials)
        path = "pilots/pretask-procedure-transfer-v3/tasks/c6j4/private.json"
        private = json.loads(changed[path])
        private["checks"][0]["proposition_basis"] = ["G-PRIVATE-ONLY"]
        changed[path] = json.dumps(private).encode()
        errors, _ = self.validate(materials=changed)
        self.assertTrue(any("invalid proposition basis" in error for error in errors))

    def test_required_output_contract_mutations_fail_for_both_families(self):
        errors, evidence = self.validate()
        self.assertEqual([], errors)
        markers = {
            "null_identity": "None is not of type 'string'",
            "false_launcher_acceptance": "false launcher acceptance",
            "silent_omission": "project or explicitly omit",
            "invalid_proposition_basis": "invalid proposition basis",
            "claim_upgrade": "False was expected",
        }
        for family, cases in evidence["mutations"].items():
            for name, marker in markers.items():
                with self.subTest(family=family, mutation=name):
                    self.assertTrue(any(marker in error for error in cases[name]))

    def test_nonzero_attempt_and_claim_upgrade_are_rejected(self):
        changed = copy.deepcopy(self.protocol)
        changed["attempt_ledger"]["provider_attempts"] = 1
        changed["claim_boundaries"]["transfer"] = True
        errors, _ = self.validate(protocol=changed)
        self.assertTrue(any("attempt ledger" in error for error in errors))
        self.assertTrue(any("claim ceiling" in error for error in errors))


if __name__ == "__main__":
    unittest.main()

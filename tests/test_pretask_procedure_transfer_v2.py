import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STUDY = ROOT / "pilots/pretask-procedure-transfer-v2"
spec = importlib.util.spec_from_file_location("pretask_v2_validate", STUDY / "validate.py")
assert spec is not None and spec.loader is not None
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class PretaskProcedureTransferV2Tests(unittest.TestCase):
    def setUp(self):
        self.protocol = json.loads((STUDY / "protocol.json").read_text())
        self.audit = json.loads((STUDY / "readiness-audit.json").read_text())
        self.materials = validator.load_materials(self.audit)

    def validate(self, protocol=None, audit=None, materials=None):
        return validator.validate(
            protocol or self.protocol,
            audit or self.audit,
            materials or self.materials,
            check_paths=True,
        )

    def test_failed_generation_is_preserved_without_authorizing_execution(self):
        self.assertEqual([], self.validate())
        self.assertFalse(self.protocol["claim_boundaries"]["readiness"])
        gates = {row["gate"]: row["status"] for row in self.audit["execution_gates"]}
        self.assertEqual("fail", gates["generated_and_control_packages_authored_and_frozen"])
        self.assertEqual(0, self.audit["executor_attempts"])

    def test_corpus_hash_drift_is_rejected(self):
        changed = copy.deepcopy(self.audit)
        changed["component_hashes"][1]["sha256"] = "0" * 64
        self.assertTrue(any("hash" in error for error in self.validate(audit=changed)))

    def test_task_hash_drift_is_rejected(self):
        changed = copy.deepcopy(self.audit)
        item = next(row for row in changed["component_hashes"] if row["role"] == "public_task")
        item["sha256"] = "0" * 64
        self.assertTrue(any("hash drift" in error for error in self.validate(audit=changed)))

    def test_complete_procedure_leakage_is_rejected(self):
        changed = dict(self.materials)
        path = "pilots/pretask-procedure-transfer-v2/tasks/q7m2/public.md"
        changed[path] += b"\nAt least two independent eligible supporting records.\n"
        errors = self.validate(materials=changed)
        self.assertTrue(any("procedure leakage" in error for error in errors))

    def test_hidden_obligation_without_public_basis_is_rejected(self):
        changed = dict(self.materials)
        path = "pilots/pretask-procedure-transfer-v2/tasks/q7m2/private.json"
        task = json.loads(changed[path])
        task["checks"][0]["public_basis"] = "Undisclosed mandatory rule"
        changed[path] = json.dumps(task).encode()
        errors = self.validate(materials=changed)
        self.assertTrue(any("hidden obligation" in error for error in errors))

    def test_private_check_cannot_originate_source_proposition(self):
        changed = dict(self.materials)
        path = "pilots/pretask-procedure-transfer-v2/families/evidence-decision/corpus.json"
        corpus = json.loads(changed[path])
        corpus["propositions"][0]["origin"] = "inferred_from_private_check"
        changed[path] = json.dumps(corpus).encode()
        errors = self.validate(materials=changed)
        self.assertTrue(any("inferred from private check" in error for error in errors))

    def test_task_identifier_in_generator_visible_input_is_rejected(self):
        changed = copy.deepcopy(self.protocol)
        changed["source_task_split"]["generator_instruction"] += " q7m2"
        errors = self.validate(protocol=changed)
        self.assertTrue(any("generator-visible" in error for error in errors))

    def test_nonzero_attempt_launders_untouched_status(self):
        changed = dict(self.materials)
        path = "pilots/pretask-procedure-transfer-v2/tasks/z3p6/private.json"
        task = json.loads(changed[path])
        task["model_attempts"] = 1
        changed[path] = json.dumps(task).encode()
        self.assertTrue(any("no longer untouched" in error for error in self.validate(materials=changed)))

    def test_post_freeze_package_repair_is_rejected(self):
        changed = dict(self.materials)
        path = "pilots/pretask-procedure-transfer-v2/generation/family-alpha/outputs/package.json"
        package = json.loads(changed[path])
        package["package_id"] = "repaired-alpha"
        changed[path] = json.dumps(package).encode()
        self.assertTrue(any("repaired or replaced" in error for error in self.validate(materials=changed)))

    def test_downstream_gate_cannot_pass_after_generation_failure(self):
        changed = copy.deepcopy(self.audit)
        gate = next(row for row in changed["execution_gates"] if row["gate"] == "checker_implementation_frozen_and_mutated")
        gate["status"] = "pass"
        self.assertTrue(any("downstream gates" in error for error in self.validate(audit=changed)))

    def test_mutation_self_test(self):
        self.assertEqual([], validator.mutation_self_test(self.protocol, self.audit, self.materials))


if __name__ == "__main__":
    unittest.main()

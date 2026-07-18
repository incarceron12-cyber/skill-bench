import copy
import json
import unittest
from pathlib import Path

from scripts.validate_procedure_generation_output import validate_documents, validate_file

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "schemas/fixtures"
SOURCE_PATH = ROOT / "pilots/pretask-procedure-transfer-v2/families/evidence-decision/corpus.json"
POLICY_PATH = FIXTURES / "procedure-generation-output-policy.json"
VALID_PATH = FIXTURES / "procedure-generation-output-valid.json"
INVALID_PATH = FIXTURES / "procedure-generation-output-null-identity.json"
REPORT_PATH = FIXTURES / "procedure-generation-output-false-acceptance.json"


class ProcedureGenerationOutputTests(unittest.TestCase):
    def setUp(self):
        self.package_bytes = VALID_PATH.read_bytes()
        self.package = json.loads(self.package_bytes)
        self.source_bytes = SOURCE_PATH.read_bytes()
        self.source = json.loads(self.source_bytes)
        self.policy = json.loads(POLICY_PATH.read_text())

    def errors(self, package=None, source=None, source_bytes=None, policy=None, report=None):
        package = self.package if package is None else package
        package_bytes = json.dumps(package, indent=2).encode()
        return "\n".join(validate_documents(
            package,
            package_bytes,
            self.source if source is None else source,
            self.source_bytes if source_bytes is None else source_bytes,
            self.policy if policy is None else policy,
            report,
        ))

    def test_valid_source_only_fixture_and_paths(self):
        validate_file(VALID_PATH, SOURCE_PATH, POLICY_PATH)

    def test_null_identity_is_rejected_even_when_launcher_accepts(self):
        report = json.loads(REPORT_PATH.read_text())
        with self.assertRaisesRegex(Exception, "package_id.*None"):
            validate_file(INVALID_PATH, SOURCE_PATH, POLICY_PATH)
        with self.assertRaisesRegex(Exception, "false launcher acceptance"):
            validate_file(INVALID_PATH, SOURCE_PATH, POLICY_PATH, REPORT_PATH)
        self.assertTrue(report["launcher_valid"])
        self.assertFalse(report["independent_validation_run"])

    def test_source_hash_and_family_identity_are_exact(self):
        changed = copy.deepcopy(self.package)
        changed["source_identity"]["source_corpus_sha256"] = "0" * 64
        self.assertIn("exact source bytes", self.errors(changed))
        changed = copy.deepcopy(self.package)
        changed["source_identity"]["family_id"] = "family-beta"
        self.assertIn("family_id", self.errors(changed))

    def test_every_proposition_requires_one_reciprocal_binding(self):
        changed = copy.deepcopy(self.package)
        changed["proposition_bindings"].pop()
        self.assertIn("exhaust every and only", self.errors(changed))
        changed = copy.deepcopy(self.package)
        changed["proposition_bindings"][0]["clause_ids"] = ["supersession"]
        self.assertIn("not reciprocal", self.errors(changed))

    def test_unknown_proposition_basis_is_rejected(self):
        changed = copy.deepcopy(self.package)
        changed["clauses"][0]["proposition_basis"] = ["A-P999"]
        self.assertIn("unknown proposition basis", self.errors(changed))

    def test_silent_primitive_loss_and_project_omit_overlap_are_rejected(self):
        changed = copy.deepcopy(self.package)
        changed["failure_signatures"].pop()
        self.assertIn("project or explicitly omit", self.errors(changed))
        changed = copy.deepcopy(self.package)
        changed["omissions"][0]["source_object_id"] = "A-F2"
        self.assertIn("both projected and omitted", self.errors(changed))

    def test_primitive_basis_must_equal_source_basis(self):
        changed = copy.deepcopy(self.package)
        changed["contradictions"][0]["proposition_basis"] = ["A-P1"]
        self.assertIn("invalid proposition basis", self.errors(changed))

    def test_claim_ceiling_upgrade_is_rejected(self):
        changed = copy.deepcopy(self.package)
        changed["claim_ceiling"]["transfer"] = True
        self.assertIn("False was expected", self.errors(changed))

    def test_task_token_and_private_path_leakage_fail_closed(self):
        changed = copy.deepcopy(self.package)
        changed["clauses"][0]["instruction"] += " Apply to q7m2."
        self.assertIn("forbidden downstream token", self.errors(changed))
        changed = copy.deepcopy(self.package)
        changed["generation_context"]["visible_inputs"] = ["pilots/example/tasks/private.json"]
        errors = self.errors(changed)
        self.assertIn("source-only allowlist", errors)
        self.assertIn("forbidden downstream path", errors)

    def test_false_launcher_report_hash_is_not_trusted(self):
        report = {"launcher_valid": True, "package_sha256": "0" * 64}
        errors = self.errors(report=report)
        self.assertIn("launcher report package hash", errors)
        self.assertIn("false launcher acceptance", errors)


if __name__ == "__main__":
    unittest.main()

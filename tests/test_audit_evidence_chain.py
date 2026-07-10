from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

from scripts.audit_evidence_chain import AuditFailure, semantic_errors, validate_file

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "pilots" / "lh-skill-adoption" / "evidence-chain-audit.json"


class EvidenceChainAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.valid = json.loads(AUDIT.read_text(encoding="utf-8"))

    def errors_after(self, mutation) -> list[str]:
        audit = copy.deepcopy(self.valid)
        mutation(audit)
        return semantic_errors(audit)

    def validate_mutation(self, mutation, *, check_paths: bool = False) -> None:
        audit = copy.deepcopy(self.valid)
        mutation(audit)
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as handle:
            json.dump(audit, handle)
            handle.flush()
            validate_file(Path(handle.name), check_paths=check_paths)

    def test_valid_audit_resolves_all_paths_hashes_and_pointers(self) -> None:
        validate_file(AUDIT, check_paths=True)
        statuses = {claim["claim_id"]: claim["status"] for claim in self.valid["claims"]}
        self.assertEqual("unsupported", statuses["expert-validity"])
        self.assertEqual("blocked", statuses["matched-skill-effect"])
        self.assertEqual("unsupported", statuses["suite-validity"])
        self.assertEqual("unsupported", statuses["cross-domain-generalization"])
        self.assertEqual("blocked", statuses["release-readiness"])
        self.assertEqual("unsupported", self.valid["suite_assembly"]["suite_sufficiency"]["status"])

    def test_rejects_absent_predeclared_response_view(self) -> None:
        def mutate(audit):
            audit["nodes"] = [node for node in audit["nodes"] if node["stage"] != "response_evidence_view"]

        errors = self.errors_after(mutate)
        self.assertTrue(any("seven ordered stages" in error for error in errors))
        self.assertTrue(any("adjacent ordered stages" in error for error in errors))

    def test_rejects_item_to_construct_edge_without_warrant(self) -> None:
        def mutate(audit):
            edge = next(item for item in audit["edges"] if item["edge_id"] == "criterion-to-requirement")
            edge["warrant"] = ""

        errors = self.errors_after(mutate)
        self.assertTrue(any("criterion-to-requirement: warrant is required" in error for error in errors))

    def test_rejects_false_skill_effect_upgrade(self) -> None:
        def mutate(audit):
            claim = next(item for item in audit["claims"] if item["claim_id"] == "matched-skill-effect")
            claim["status"] = "supported"

        errors = self.errors_after(mutate)
        self.assertTrue(any("matched-skill-effect: unsupported claim upgrade" in error for error in errors))
        self.assertTrue(any("matched-skill-effect: supported/provisional claim retains explicit blockers" in error for error in errors))

    def test_rejects_false_suite_sufficiency_upgrade(self) -> None:
        def mutate(audit):
            audit["suite_assembly"]["suite_sufficiency"]["status"] = "supported"
            claim = next(item for item in audit["claims"] if item["claim_id"] == "suite-validity")
            claim["status"] = "supported"

        errors = self.errors_after(mutate)
        self.assertTrue(any("one-task eligible pool" in error for error in errors))
        self.assertTrue(any("alternate-assembly sensitivity" in error for error in errors))
        self.assertTrue(any("suite-validity: unsupported claim upgrade" in error for error in errors))

    def test_rejects_broken_json_pointer(self) -> None:
        def mutate(audit):
            node = next(item for item in audit["nodes"] if item["stage"] == "metric")
            node["record_ref"]["pointer"] = "/metrics/99"

        errors = self.errors_after(mutate)
        self.assertTrue(any("unresolved pointer" in error for error in errors))

    def test_rejects_stale_artifact_hash(self) -> None:
        def mutate(audit):
            artifact = next(item for item in audit["artifacts"] if item["artifact_id"] == "lh-pair-v6")
            artifact["sha256"] = "0" * 64

        with self.assertRaisesRegex(AuditFailure, "sha256 does not match"):
            self.validate_mutation(mutate, check_paths=True)


if __name__ == "__main__":
    unittest.main()

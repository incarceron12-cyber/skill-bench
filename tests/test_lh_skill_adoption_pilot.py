from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path

from scripts.validate_benchmark import validate_file as validate_bundle
from scripts.validate_expertise_transfer import validate_file as validate_transfer

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "pilots" / "lh-skill-adoption"
BUNDLE = PILOT / "benchmark-bundle.json"
TRANSFER = PILOT / "expertise-transfer.json"


class LhSkillAdoptionPilotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.bundle = json.loads(BUNDLE.read_text(encoding="utf-8"))
        cls.transfer = json.loads(TRANSFER.read_text(encoding="utf-8"))

    def test_both_instantiated_contracts_validate_with_paths(self) -> None:
        validate_transfer(TRANSFER, check_paths=True)
        validate_bundle(BUNDLE, ROOT / "schemas" / "benchmark-bundle.schema.json", check_paths=True)

    def test_cross_contract_artifact_and_check_ids_match(self) -> None:
        transfer_artifacts = {item["artifact_id"] for item in self.transfer["artifact_contracts"]}
        bundle_artifacts = {item["artifact_id"] for item in self.bundle["task"]["artifact_contracts"]}
        transfer_checks = {item["check_id"] for item in self.transfer["checks"]}
        bundle_checks = {item["check_id"] for item in self.bundle["task"]["checks"]}
        self.assertEqual(transfer_artifacts, bundle_artifacts)
        self.assertEqual(transfer_checks, bundle_checks)

    def test_all_pinned_local_components_have_real_hashes(self) -> None:
        components = [
            (PILOT / "public-skill.md", self.bundle["procedural_skills"][0]["sha256"]),
            (PILOT / "rubric-skeleton.json", self.bundle["rubrics"][0]["sha256"]),
        ]
        components.extend(
            (ROOT / grader["implementation"]["config_path"], grader["sha256"])
            for grader in self.bundle["graders"]
        )
        for path, expected in components:
            with self.subTest(path=path):
                self.assertEqual(expected, hashlib.sha256(path.read_bytes()).hexdigest())

    def test_missing_expert_approval_is_a_failed_release_gate(self) -> None:
        procedures = json.loads((PILOT / "candidate-procedures.json").read_text(encoding="utf-8"))
        self.assertEqual(2, len(procedures["procedures"]))
        self.assertFalse(procedures["expert_approved"])
        self.assertEqual("pending_domain_expert_validation", procedures["status"])
        self.assertEqual("failed", self.transfer["release"]["expert_validity_review"])
        self.assertEqual("not_ready", self.transfer["release"]["status"])
        self.assertEqual([], self.bundle["trials"], "pilot skeleton must not fabricate trial evidence")

    def test_builder_hypotheses_are_not_labeled_as_expert_evidence(self) -> None:
        claims = {item["claim_id"]: item for item in self.transfer["claims"]}
        hypothesis = claims["artifact-format-hypothesis"]
        self.assertEqual("synthetic_hypothesis", hypothesis["evidence_basis"])
        self.assertEqual("unreviewed", hypothesis["corroboration_status"])
        self.assertEqual("low", hypothesis["confidence"])

    def test_private_checks_only_hold_out_public_consequences(self) -> None:
        requirement_ids = {
            req["requirement_id"]
            for skill in self.bundle["procedural_skills"]
            for req in skill["requirements"]
        }
        private_checks = [
            check for check in self.bundle["task"]["checks"]
            if check["visibility"] in {"private", "hidden"}
        ]
        self.assertGreater(len(private_checks), 0)
        for check in private_checks:
            with self.subTest(check=check["check_id"]):
                self.assertEqual("held_out_consequence", check["boundary_disclosure"])
                self.assertTrue(set(check["public_basis_requirement_ids"]) <= requirement_ids)


if __name__ == "__main__":
    unittest.main()

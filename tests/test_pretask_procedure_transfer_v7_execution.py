from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "pilots/pretask-procedure-transfer-v7-execution"
V7 = ROOT / "pilots/pretask-procedure-transfer-v7"
CLAIMS = {"agent_capability": False, "expert_provenance": False, "production_fitness": False,
          "professional_validity": False, "readiness": False, "transfer": False, "utility": False}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class PretaskProcedureTransferV7ExecutionTests(unittest.TestCase):
    def test_preexecution_and_canary_passed_before_attempts(self):
        pre, canary = load(HERE / "preexecution-report.json"), load(HERE / "execution-canary-report.json")
        self.assertEqual("PASS", pre["status"])
        self.assertEqual(0, pre["executor_attempts"])
        self.assertTrue(pre["audited_commit_is_ancestor"])
        self.assertEqual(55, pre["v7_bound_files_checked"])
        self.assertEqual("PASS", canary["status"])
        self.assertEqual(0, canary["executor_attempts"])
        self.assertTrue(all(row["passed"] for row in canary["materialized_inventory_checks"]))

    def test_all_assignments_retained_once_without_retry(self):
        assignments = load(V7 / "assignments.json")["rows"]
        reports = [load(path) for path in sorted((HERE / "execution").glob("*/trial-report.json"))]
        self.assertEqual(32, len(reports))
        self.assertEqual(list(range(1, 33)), sorted(row["schedule_index"] for row in reports))
        expected = {(r["schedule_index"], r["task_id"], r["family_id"], r["condition_id"]) for r in assignments}
        actual = {(r["schedule_index"], r["task_id"], r["family_id"], r["condition_id"]) for r in reports}
        self.assertEqual(expected, actual)
        self.assertTrue(all(r["attempts"] == 1 and r["repair_attempts"] == 0 and r["retry_attempts"] == 0 for r in reports))

    def test_strict_denominators_and_claim_ceiling(self):
        report = load(HERE / "execution-report.json")
        self.assertEqual("complete", report["status"])
        self.assertEqual({"intended": 32, "attempted": 32, "skipped": 0, "invalid": 0,
                          "service_valid": 32, "environment_valid": 32, "artifact_valid": 30,
                          "checker_scored": 32, "endpoint_pass": 24}, report["denominators"])
        self.assertEqual(CLAIMS, report["claim_ceiling"])
        self.assertEqual({"executor": 32, "model": 32, "provider": 32, "repair": 0, "retry": 0}, report["attempts"])

    def test_every_usage_record_is_included_zero_cost(self):
        usage_files = sorted((HERE / "execution").glob("*/outputs/usage.json"))
        self.assertEqual(32, len(usage_files))
        for path in usage_files:
            usage = load(path)
            self.assertTrue(usage["completed"])
            self.assertFalse(usage["failed"])
            self.assertEqual("gpt-5.6-sol", usage["model"])
            self.assertEqual("openai-codex", usage["provider"])
            self.assertEqual("included", usage["cost_status"])
            self.assertEqual(0.0, usage["estimated_cost_usd"])

    def test_retention_audit_and_prompt_hashes_pass(self):
        audit = load(HERE / "execution-audit-report.json")
        self.assertEqual("PASS", audit["status"])
        self.assertEqual([], audit["errors"])
        self.assertEqual(CLAIMS, audit["claim_ceiling"])
        prompt_hash = audit["prompt_retention"]["sha256"]
        prompts = sorted((HERE / "execution").glob("*/prompt.txt"))
        self.assertEqual(32, len(prompts))
        self.assertTrue(all(sha(path) == prompt_hash for path in prompts))
        self.assertEqual(0.0, audit["resource_totals"]["estimated_cost_usd"])


if __name__ == "__main__":
    unittest.main()

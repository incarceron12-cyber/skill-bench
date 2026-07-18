from __future__ import annotations

import hashlib
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "pilots/pretask-procedure-transfer-v4"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


launcher = load_module("v4_candidate_launcher", HERE / "generate_candidates.py")
auditor = load_module("v4_candidate_auditor", HERE / "audit_candidates.py")


class PretaskProcedureTransferV4GenerationTests(unittest.TestCase):
    def test_launcher_imports_exact_upstream_prompt_semantics(self):
        for family_id in launcher.ORDER:
            policy = json.loads(launcher.FAMILY_PATHS[family_id][1].read_text())
            self.assertEqual(launcher.upstream.prompt(policy), launcher.prompt(policy))
            self.assertEqual(launcher.VISIBLE_INPUTS, tuple(policy["allowed_visible_inputs"]))

    def test_frozen_order_and_fail_closed_scope(self):
        self.assertEqual(("family-epsilon", "family-zeta"), launcher.ORDER)
        self.assertEqual(set(launcher.ORDER), set(launcher.FAMILY_PATHS))
        self.assertEqual(launcher.ORDER, auditor.ORDER)
        self.assertIn("executions", auditor.PROHIBITED_DOWNSTREAM)
        self.assertIn("endpoint-canaries", auditor.PROHIBITED_DOWNSTREAM)

    def test_retained_candidates_revalidate_when_present(self):
        if not (HERE / "candidate-generation-report.json").exists():
            self.skipTest("generation not executed yet")
        if (HERE / "hindsight-packages").exists():
            # The independent candidate auditor was deliberately scoped to
            # stop before downstream materialization. Retain and inspect its
            # frozen historical result after the next phase begins.
            report = json.loads((HERE / "generation-audit-report.json").read_text())
            manifest = json.loads((HERE / "candidate-freeze-manifest.json").read_text())
            events = [json.loads(line) for line in (HERE / "generation-audit.jsonl").read_text().splitlines()]
        else:
            report, manifest, events = auditor.audit()
        self.assertEqual("PASS", report["audit_status"], report["errors"])
        self.assertEqual("pass", report["generation_gate"])
        self.assertEqual(2, report["denominators"]["schema_valid"])
        self.assertEqual(0, report["aggregate_attempts"]["executor"])
        self.assertTrue(all(value is False for value in report["claim_ceiling"].values()))
        self.assertEqual("frozen_valid_candidates", manifest["status"])
        self.assertEqual(3, len(events))

    def test_append_only_chain_and_candidate_hashes_when_present(self):
        log_path = HERE / "generation-audit.jsonl"
        if not log_path.exists():
            self.skipTest("append-only audit not executed yet")
        rows = [json.loads(line) for line in log_path.read_text().splitlines()]
        previous = None
        for sequence, row in enumerate(rows, 1):
            event_hash = row.pop("event_sha256")
            self.assertEqual(sequence, row["sequence"])
            self.assertEqual(previous, row["previous_event_sha256"])
            actual = hashlib.sha256(json.dumps(row, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
            self.assertEqual(event_hash, actual)
            previous = event_hash
        manifest = json.loads((HERE / "candidate-freeze-manifest.json").read_text())
        audit_report = json.loads((HERE / "generation-audit-report.json").read_text())
        self.assertEqual(previous, audit_report["append_only_audit"]["terminal_event_sha256"])
        for component in manifest["components"]:
            path = ROOT / component["path"]
            self.assertEqual(component["sha256"], hashlib.sha256(path.read_bytes()).hexdigest())
            self.assertEqual(component["bytes"], path.stat().st_size)
        for family_id, expected in manifest["candidate_packages"].items():
            package = HERE / "candidate-generation" / family_id / "outputs/package.json"
            self.assertEqual(expected, hashlib.sha256(package.read_bytes()).hexdigest())
        for binding in (manifest["generation_report"], manifest["audit_log"], manifest["audit_report"]):
            path = ROOT / binding["path"]
            self.assertEqual(binding["sha256"], hashlib.sha256(path.read_bytes()).hexdigest())


if __name__ == "__main__":
    unittest.main()

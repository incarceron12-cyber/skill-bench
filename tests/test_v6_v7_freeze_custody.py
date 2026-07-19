import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/audit_v6_v7_freeze_custody.py"
REPORT = ROOT / "reports/validation/2026-07-19-pretask-procedure-v6-v7-custody-adjudication.json"


def load_audit_module():
    spec = importlib.util.spec_from_file_location("v6_v7_custody_audit", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class V6V7FreezeCustodyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.audit = load_audit_module()
        cls.report = cls.audit.build_report()

    def test_historical_manifests_close_at_both_evidence_commits(self):
        historical = self.report["historical_binding_recomputation"]
        for key in ("independent_freeze_audit_source", "execution_source"):
            with self.subTest(key=key):
                self.assertTrue(historical[key]["all_bindings_match"])
                self.assertEqual(historical[key]["component_bindings_checked"], 22)
                self.assertEqual(historical[key]["external_bindings_checked"], 33)
                self.assertEqual(historical[key]["mismatches"], [])
        self.assertTrue(
            historical["original_manifest_byte_identical_at_freeze_and_execution_sources"]
        )

    def test_every_repaired_v6_file_is_enumerated_as_a_changed_binding(self):
        mutation = self.report["retrospective_mutation"]
        changed = mutation["changed_v6_frozen_paths"]
        self.assertEqual(len(changed), 6)
        self.assertEqual(mutation["changed_v6_binding_count"], 6)
        self.assertEqual(mutation["unbound_changed_v6_paths"], [])
        self.assertEqual(
            [row["path"] for row in mutation["v6_binding_mutations"]], changed
        )
        self.assertEqual(
            [row["path"] for row in mutation["v7_manifest"]["refreshed_external_bindings"]],
            changed,
        )
        for row in mutation["v6_binding_mutations"]:
            with self.subTest(path=row["path"]):
                self.assertNotEqual(row["pre_repair"]["sha256"], row["post_repair"]["sha256"])
                self.assertEqual(row["audited_v7_declared"]["sha256"], row["pre_repair"]["sha256"])
                self.assertEqual(row["post_repair_v7_declared"]["sha256"], row["post_repair"]["sha256"])

    def test_repair_did_not_change_v7_task_treatment_or_execution_bytes(self):
        closure = self.report["execution_closure"]
        self.assertEqual(
            closure["decision"], "REMAINS_HASH_VERIFIABLE_AT_COMMIT_BOUND_SNAPSHOTS"
        )
        self.assertFalse(closure["v7_task_treatment_files_changed_by_repair"])
        self.assertFalse(closure["v7_execution_package_changed_by_repair"])
        self.assertTrue(closure["execution_tree_same_from_source_through_repair"])
        self.assertEqual(self.report["retrospective_mutation"]["execution_paths_changed"], [])
        self.assertEqual(self.report["retrospective_mutation"]["v7_non_manifest_paths_changed"], [])

    def test_state_and_claim_adjudication_fail_closed(self):
        state = self.report["state_adjudication"]
        self.assertEqual(state["pre_repair_v6"]["classification"], "frozen_failed_preexecution_state")
        self.assertEqual(state["pre_repair_v6"]["canary"], "FAIL")
        self.assertEqual(state["post_repair_v6"]["classification"], "post_hoc_infrastructure_repair_not_a_new_prospective_instrument")
        self.assertEqual(state["post_repair_v6"]["canary"], "PASS")
        self.assertFalse(state["head_worktree_preserves_exact_failed_v6_bytes"])
        self.assertTrue(state["git_history_preserves_exact_failed_v6_bytes"])
        self.assertTrue(state["audited_v7_manifest_was_rewritten_after_execution"])
        self.assertTrue(all(value is False for value in self.report["claim_ceiling"].values()))
        self.assertIn(
            "The lifecycle completed without any later rewrite of prior frozen evidence.",
            self.report["preservation_claim_adjudication"]["not_licensed"],
        )

    def test_committed_report_is_exact_replay(self):
        expected = json.dumps(self.report, indent=2, sort_keys=True) + "\n"
        self.assertEqual(REPORT.read_text(encoding="utf-8"), expected)
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("PASS", result.stdout)


if __name__ == "__main__":
    unittest.main()

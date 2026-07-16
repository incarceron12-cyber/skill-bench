import copy
import json
import unittest
from pathlib import Path

from scripts.validate_persistent_workspace_reuse import (
    build_package,
    canonical_sha256,
    replay,
    semantic_errors,
    validate_file,
)

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "pilots/persistent-workspace-reuse/v1/protocol.json"
REPORT = ROOT / "pilots/persistent-workspace-reuse/v1/replay-report.json"


class PersistentWorkspaceReuseTests(unittest.TestCase):
    def setUp(self):
        self.package = json.loads(FIXTURE.read_text())

    def cell(self, package, shape, condition):
        return next(item for item in package["cells"] if item["work_shape"] == shape and item["condition"] == condition)

    def test_canonical_fixture_valid_and_paths_resolve(self):
        validate_file(FIXTURE, check_paths=True)
        self.assertEqual(build_package(), self.package)

    def test_replay_keeps_agent_and_rerun_estimands_separate(self):
        result = replay(self.package)
        self.assertEqual(14, result["cell_count"])
        self.assertEqual({"accepted": 2, "rejected": 6, "insufficient_evidence": 6}, result["disposition_counts"])
        self.assertEqual(0, result["agent_trials_run"])
        self.assertEqual("not_estimated", result["estimand_status"]["agent_mediated_workspace_reuse"])

    def test_rejects_stale_authority_laundering(self):
        package = copy.deepcopy(self.package)
        stale = next(item for item in package["retained_objects"] if item["object_id"] == "table-stale-spec")
        stale["state"] = "current"
        stale["sha256"] = canonical_sha256({key: value for key, value in stale.items() if key != "sha256"})
        cell = self.cell(package, "tabular_procurement_refresh", "curated_stale")
        cell["criterion"].update({"disposition": "accepted", "reason": "treated_as_current"})
        self.assertTrue(any("unsafe authority disposition" in error for error in semantic_errors(package)))

    def test_rejects_composition_hash_mismatch(self):
        package = copy.deepcopy(self.package)
        self.cell(package, "structured_policy_memo_refresh", "curated_correct")["composition_sha256"] = "0" * 64
        self.assertTrue(any("composition hash mismatch" in error for error in semantic_errors(package)))

    def test_rejects_semantic_incompatibility(self):
        package = copy.deepcopy(self.package)
        rerun = self.cell(package, "tabular_procurement_refresh", "deterministic_artifact_rerun")["rerun"]
        rerun["compatibility_dimensions"].remove("semantic")
        self.assertTrue(any("semantic incompatibility" in error for error in semantic_errors(package)))

    def test_rejects_missing_observation_links(self):
        package = copy.deepcopy(self.package)
        cell = self.cell(package, "structured_policy_memo_refresh", "curated_conflicting")
        cell["criterion"]["evidence_object_ids"] = ["unobserved-object"]
        self.assertTrue(any("missing observation links" in error for error in semantic_errors(package)))

    def test_rejects_rerun_as_agent_conflation(self):
        package = copy.deepcopy(self.package)
        cell = self.cell(package, "structured_policy_memo_refresh", "deterministic_artifact_rerun")
        cell["estimand"] = "agent_mediated_workspace_reuse"
        self.assertTrue(any("rerun-as-agent conflation" in error for error in semantic_errors(package)))

    def test_rejects_matched_base_drift(self):
        package = copy.deepcopy(self.package)
        self.cell(package, "tabular_procurement_refresh", "information_matched_full_history")["matched_base"]["budget"]["input_bytes"] += 1
        self.assertTrue(any("matched base or budget drift" in error for error in semantic_errors(package)))

    def test_report_binds_current_package_and_protocol(self):
        report = json.loads(REPORT.read_text())
        import hashlib
        self.assertEqual(hashlib.sha256(FIXTURE.read_bytes()).hexdigest(), report["package_sha256"])
        self.assertEqual(self.package["frozen_protocol"]["protocol_sha256"], report["protocol_sha256"])
        self.assertEqual(0, report["model_calls"])


if __name__ == "__main__":
    unittest.main()

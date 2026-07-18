from __future__ import annotations
import copy, importlib.util, json, subprocess, sys, tempfile, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "pilots/pretask-procedure-transfer-v4"
spec = importlib.util.spec_from_file_location("v4_preflight", HERE / "preflight.py")
assert spec and spec.loader
preflight = importlib.util.module_from_spec(spec); spec.loader.exec_module(preflight)

class PretaskProcedureTransferV4Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.protocol = preflight.load(HERE / "protocol.json")
        cls.manifest = preflight.load(HERE / "freeze-manifest.json")
        cls.materials = preflight.materials(cls.manifest)

    def test_frozen_instrument_passes(self):
        self.assertEqual([], preflight.validate(self.protocol, self.manifest, self.materials, check_paths=True))

    def test_all_required_mutations_are_rejected(self):
        results = preflight.mutation_results(self.protocol, self.manifest, self.materials)
        self.assertEqual({"source_task_leakage", "post_freeze_edit", "interface_drift", "condition_aware_grading", "defect_drift", "unequal_envelope", "oracle_exposure", "nonzero_attempt"}, set(results))
        self.assertTrue(all(results.values()), results)

    def test_checker_accepts_exact_endpoint_and_rejects_mutation(self):
        checker = HERE / "checkers/check_endpoint.py"
        for task_id in ("k4n7", "p9c2", "t6v1", "w3d8"):
            private = json.loads((HERE / f"tasks/{task_id}/private.json").read_text())
            with tempfile.TemporaryDirectory() as directory:
                candidate = Path(directory) / "result.json"
                candidate.write_text(json.dumps(private["expected_endpoint"]))
                accepted = subprocess.run([sys.executable, str(checker), "--candidate", str(candidate), "--private", str(HERE / f"tasks/{task_id}/private.json")], capture_output=True, text=True)
                self.assertEqual(0, accepted.returncode, accepted.stdout + accepted.stderr)
                changed = copy.deepcopy(private["expected_endpoint"]); changed["task_id"] = "wrong"; candidate.write_text(json.dumps(changed))
                rejected = subprocess.run([sys.executable, str(checker), "--candidate", str(candidate), "--private", str(HERE / f"tasks/{task_id}/private.json")], capture_output=True, text=True)
                self.assertNotEqual(0, rejected.returncode)

    def test_interface_bytes_are_exact_upstream_imports(self):
        for name in ("interface-guide.md", "example-source.json", "example-package.json"):
            self.assertEqual((HERE / "interface" / name).read_bytes(), (ROOT / "pilots/procedure-package-interface-usability-v1/interface" / name).read_bytes())

if __name__ == "__main__": unittest.main()

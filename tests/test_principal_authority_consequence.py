import copy
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / "pilots/principal-authority-consequence/replay.py"
spec = importlib.util.spec_from_file_location("authority_replay", P)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class PrincipalAuthorityConsequenceTests(unittest.TestCase):
    def test_frozen_replay_qualifies_exact_cases(self):
        report = mod.replay(write=False)
        self.assertEqual(report["decision"], "qualified_for_exact_frozen_cases_only")
        self.assertTrue(all(report["gates"].values()))
        self.assertTrue(all(report["mutations"].values()))
        self.assertEqual(len(report["cases"]), 8)

    def test_dimensions_are_separate(self):
        row = mod.replay(write=False)["cases"][0]
        self.assertEqual(set(row["errors"]), {"authorization", "information_sufficiency", "action", "consequence"})

    def test_evaluator_preference_never_authorizes_action(self):
        data = mod.load_cases()
        rows = [c for s in data["scenarios"] for c in s["conditions"] if c["authority_state"] == "evaluator_authored_only"]
        self.assertTrue(rows)
        self.assertTrue(all(c["expected_action"] != "act" for c in rows))

    def test_hidden_obligation_is_rejected(self):
        data = mod.load_cases()
        bad = copy.deepcopy(data)
        bad["scenarios"][0]["conditions"][2]["expected_action"] = "act"
        self.assertIn("hidden_obligation", mod.validate(bad))


if __name__ == "__main__":
    unittest.main()

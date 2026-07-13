# Cross-pilot falsification matrix

This is an **internal, frozen coverage audit**, not a third pilot or a benchmark release. It turns the six requirements in `docs/concepts/professional-benchmark-evolution-matrix.md` lines 106–113 into an executable inventory over retained LH-adoption, vendor-incident, artifact, state, alternative-path, and validity records.

## Charter decision filter

- **Objective:** charter B/C—make expertise-to-evaluation boundaries and benchmark infrastructure executable.
- **Artifact:** `coverage-manifest.json`, fail-closed `replay.py`, and generated `report.json`.
- **Uncertainty:** whether existing machinery covers all six falsification families before the second pilot is promoted.
- **Mode:** building and validation; it consolidates existing evidence without creating another schema.
- **Duplication/scope:** rows reference existing cross-domain machinery and two structurally different pilots; incident response and benchmark-program analysis remain bounded cases, not the project scope.
- **Useful completion:** every frozen requirement is represented, every credited observation is path/hash/JSON-Pointer bound, and unresolved cells block promotion.

## Evidence semantics

Each row has exactly one of five statuses:

- `satisfied`: retained evidence exhibits the frozen expected observation;
- `missing`: no retained case isolates the requirement;
- `invalid`: evidence exists but cannot be used because its run/instrument is invalid;
- `insufficient_evidence`: a partial record exists but cannot establish the full requirement;
- `not_applicable`: the construct genuinely does not apply, with a specific rationale (never a synonym for missing evidence).

Hashes establish byte identity, and JSON Pointers establish the recorded field. Neither establishes truth, expert authority, professional validity, or causal identification. Builder-authored synthetic cases remain conformance evidence only.

## Replay

```bash
python pilots/cross-pilot-falsification-matrix/replay.py
python pilots/cross-pilot-falsification-matrix/replay.py --check
python -m unittest tests.test_cross_pilot_falsification_matrix
```

The replay fails on source hash drift, broken pointers, changed expected observations, absent/extra frozen requirement rows, or an attempted supported claim above the task-package rung. It may exit successfully while `promotion_decision` remains `blocked`: successful replay means the audit is internally intact, not that coverage is complete.

## Current result and continuation boundary

The frozen audit contains 29 rows: 24 satisfied, 2 missing, and 3 insufficient. Three of six families are promotion-ready. Promotion remains blocked by:

1. no isolated title-only empty-artifact mutation;
2. no explicit shared-cause root/descendant graph case;
3. dirty-output policy without a retained planted outcome;
4. no authoritative-input mutation plus pinned-engine recalculation case; and
5. a packaged 2×2 Skill/rubric fixture replay that cannot estimate treatment effects.

A continuation should add only deterministic planted mutations for the first four gaps. The fifth requires valid matched execution and must not be filled by relabeling fixture replay or rerunning models merely to complete this matrix. Existing pilot bytes must remain unchanged.

## Claim boundary

This audit does **not** support professional capability, cross-domain capability, Skill/rubric treatment effects, real-world safety, occupational representativeness, or deployment/release readiness. It therefore does not promote either pilot.

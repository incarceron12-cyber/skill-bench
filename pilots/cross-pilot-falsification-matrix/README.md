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
# Frozen v0.1 inventory (retained byte-for-byte)
python pilots/cross-pilot-falsification-matrix/replay.py
python pilots/cross-pilot-falsification-matrix/replay.py --check

# Versioned deterministic v0.2 continuation
python pilots/cross-pilot-falsification-matrix/replay.py --continuation
python pilots/cross-pilot-falsification-matrix/replay.py --continuation --check
python -m unittest tests.test_cross_pilot_falsification_matrix
```

The replay fails on source hash drift, broken pointers, changed expected observations, absent/extra frozen requirement rows, leaked `oracle`/`expected`/`rationale` fields in evaluator inputs, or an attempted supported claim above the task-package rung. It may exit successfully while `promotion_decision` remains `blocked`: successful replay means the audit is internally intact, not that coverage is complete.

## v0.2 deterministic continuation

`continuation-manifest-v0.2.json` preserves SHA-256 identities for the v0.1 manifest/report and binds each new case's `before`, public `input`, `output`, and comparison-only `expected` record by repository path, SHA-256, and JSON Pointer. `continuation-v0.2/` contains four isolated builder-authored probes:

1. **Title-only empty artifact:** non-empty title metadata cannot substitute for empty authoritative content.
2. **Shared cause:** one failed root has two explicit descendant symptoms, but attribution counts the root once.
3. **Dirty output:** a retained residual file fails the clean-root canary, classifies the run `invalid`, and excludes it from the substantive denominator.
4. **Pinned recalculation:** changing units from 10 to 12 makes cached total 50 stale; the hash-bound engine recomputes 60, while owner/currency must remain unchanged.

`report-v0.2.json` is the exact replay. It records 28 satisfied rows and one `insufficient_evidence` row; five of six families are promotion-ready. The remaining blocker is `si-treatment-effect-ceiling`: the retained 2×2 fixture proves packaging parity only and still cannot estimate a Skill or rubric effect.

The formula engine supports one predeclared arithmetic expression and uses no dynamic evaluation. The replay never supplies comparison-only expected records to case evaluators, and rejects oracle/rationale fields in before/input/output records.

## Frozen v0.1 result and continuation boundary

The original frozen audit contains 29 rows: 24 satisfied, 2 missing, and 3 insufficient. Three of six families were promotion-ready. Its five original blockers and `report.json` remain preserved as historical evidence. The v0.2 continuation closes only the four deterministic gaps above; it does not rewrite those old bytes or source-pilot artifacts.

## Claim boundary

This audit does **not** support professional capability, cross-domain capability, Skill/rubric treatment effects, real-world safety, occupational representativeness, or deployment/release readiness. It therefore does not promote either pilot.

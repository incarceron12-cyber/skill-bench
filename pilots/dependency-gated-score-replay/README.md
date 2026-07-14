# Dependency-gated versus compensatory progress replay

## Purpose and charter fit

This bounded validation slice advances charter objectives **B** (expertise-to-evaluation), **C** (executable infrastructure), and **D** (research consolidation). It tests a general, cross-domain hypothesis: dense local rubric credit is diagnostically useful, but a completion claim should not let downstream observations compensate for unsatisfied causal prerequisites.

The artifact does not make scientific-replication capability, professional-quality, expert-validity, predictive-validity, or readiness claims. The examples are builder-authored contract calibration cases. PaperBench is a methodological source, not a scope commitment to machine-learning research.

## Artifacts

- `replay.py` verifies the SHA-256 of the pinned official PaperBench archive and the selected `semantic-self-consistency/rubric.json` member, replays its topology and all-supported recursive score, then evaluates synthetic graded trees.
- `fixtures/cases.json` contains eight evidence-preserving cases: complete path, failed prerequisite, conjunction, accepted alternative, invalid observation, insufficient evidence, not-applicable branch, and one upstream failure with three descendants.
- `replay-report.json` is deterministic output containing criterion evidence states, both scores, path completion, invalid/insufficient burdens, threshold decisions, competition ranks, and strict claim boundaries.
- `tests/test_dependency_gated_score_replay.py` checks provenance, semantics, fail-closed handling, mutations, and report freshness.

The selected current-release rubric has 100 nodes and 77 leaves. This is not the 79-leaf JudgeEval expected-result tree discussed in the review; those are different released objects. The original PaperBench tree has no executable dependency graph, so this slice does **not** infer dependencies from criterion prose. It uses the pinned rubric only to ground and verify the released recursive sibling-weighting mechanism; dependency semantics are explicit in synthetic cases.

## Semantics

Two observables are retained rather than collapsed:

1. **Compensatory progress** reproduces recursive sibling-weighted local credit. `supported=1`; contradicted, invalid, and insufficient observations receive zero for this replay; not-applicable criteria are excluded and sibling weights renormalized.
2. **Dependency-gated progress** uses the same weights, but a supported leaf receives credit only when its recursively evaluated prerequisite expression is satisfied. Expressions support a direct prerequisite, conjunction (`all`), and accepted alternative (`any`).

A separate completion decision additionally requires: no invalid observation, no insufficient required evidence, all declared mandatory criteria effective, and gated progress at or above the fixture threshold. Invalid and insufficient observations remain typed in the report rather than being laundered into substantive zeros. Partial progress remains available even when the completion decision fails.

The report maps these choices to the repository's existing rubric/metric boundaries: explicit unit and finite synthetic population, observable definitions, invalid/missing/not-applicable policies, exact-enumeration uncertainty, threshold, and evidence locators. It is a replay/report artifact, not another schema subsystem.

## Evidence and design rationale

| Choice | Evidence | Bounded interpretation |
|---|---|---|
| Replay recursive sibling weighting | `papers/agent-benchmarks/2026-07-15-paperbench-replication-rubric-validity.md`, “Scoring semantics”; `data/sources/releases/2504.01848v3-paperbench/audit.json` | The released aggregation is internally replayable, not construct-valid by virtue of replay. |
| Explicit prerequisite/conjunction/alternative gates | Review, “Unique insight” and “Transfer to skill-bench” | Synthetic contract test; predictive validity against independent expert completion judgments remains untested. |
| Preserve invalid, insufficient, and not-applicable states | Review, “SimpleJudge and evidence access” and limitations 9; `schemas/METRIC_MONITORING.md` §§3–4 | Headline decisions fail closed while diagnostic progress and failure type remain visible. |
| Report score/rank/threshold changes | Review, JudgeEval boundary 2 and “Test before adopting” | Sensitivity evidence for these fixtures only, not proof one policy is superior. |
| Preserve criterion-level evidence | Charter evidence traceability and review evidence lattice | Synthetic locators prove report lineage, not real-world evidence sufficiency. |

Source boundary: official archive commit `51052cede8cc608f95bb00346635e03759013e5a` postdates arXiv v3 and is not treated as exact paper-time implementation. Its repository archive and member hashes are pinned in `replay.py`; release timing and limitations are recorded in the cited review and provenance manifest.

## Reproduce

```bash
python pilots/dependency-gated-score-replay/replay.py --check
python -m unittest tests.test_dependency_gated_score_replay -v
```

Regenerate after an intentional fixture or implementation change with:

```bash
python pilots/dependency-gated-score-replay/replay.py
```

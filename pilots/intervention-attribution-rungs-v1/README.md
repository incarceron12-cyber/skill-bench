# Intervention-to-attribution rung conformance v1

This zero-call, builder-authored pilot tests a general diagnostic-validity hypothesis: knowing where a synthetic intervention was inserted is not enough to call that step an earliest sufficient or natural root cause. It crosses two structurally unlike artifact-heavy work shapes—an evidence memo and an inventory decision workbook—with six conditions and two deterministic equivalent forms (24 retained attempts total).

## Frozen design

`protocol.json`, `observer-inputs.json`, and `oracle-private.json` prospectively define:

- verified successful witnesses for both work shapes;
- original, upstream injection, repaired injection, sham/no-op, downstream surface defect, and dual-fault conditions;
- exact expected/observed pre-state hashes, delta loci, first divergence, propagation edges, surfaced checks, repairs, alternatives, collateral controls, and dispositions;
- prefix-only, full-trace answer-withheld, and answer-bearing frozen rule auditors;
- separate scoring for injected-delta recovery, first-divergence localization, supported causal slice, unresolved alternatives, paired repair, and collateral regression.

One repaired-memo equivalent form intentionally has a mismatched replay pre-state. It is retained as `invalid_replay_diverged` and excluded from attribution scoring. Recovered, failed, successful, and invalid attempts all remain in the denominator. The answer-bearing calibration auditor intentionally anchors on failing endpoint checks, while the answer-withheld full-trace auditor preserves upstream and dual-cause structure; this tests information-view effects without a model call.

The report hashes every frozen policy/input/oracle, replay code, reviewed primary source, reused schema, and reused pilot record. `replay-report.sha256` hashes the generated report itself without creating a self-referential JSON hash.

## Replay and tests

```bash
python pilots/intervention-attribution-rungs-v1/replay.py --check-paths --write-report
python -m unittest tests.test_intervention_attribution_rungs -v
```

## Evidence and claim ceiling

Design basis: `papers/agent-benchmarks/2026-07-15-whowhen-pro-failure-attribution-validity.md`, especially its intervention-to-consequence chain and seven-rung claim ladder. Existing trace/root-surface, task-health, metric, validity, crossed-evaluator, trajectory-observer, and LH diagnosis artifacts are reused by hash rather than replaced.

The deterministic replay supports only local conformance semantics on builder-authored forms. It does **not** support natural-failure prevalence, auditor generalization, expert or professional validity, agent capability, safety, production fitness, or deployment readiness. `earliest_sufficient_cause` remains unsupported and `natural_failure_root` prohibited. Local paired recovery is not a general repair-utility claim.

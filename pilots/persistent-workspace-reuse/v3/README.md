# Persistent-workspace reuse v3: action-boundary protocol

This is a prospectively frozen **internal synthetic** mechanism study. It asks whether retained authorization changes a consequential artifact/state transition, while absent, stale, conflicting, or revoked state causes timely restraint and a precise recovery request. It does not define a profession-specific benchmark.

## Charter decision filter

- **Objectives:** B and C: explicit expertise-to-evaluation primitives and executable benchmark infrastructure.
- **Artifact:** a 24-cell, two-shape/four-form protocol; label-blind four-part grader; strict denominator; zero-call isolation, equivalence, authority, leakage, consequence, and mutation canaries.
- **Uncertainty:** whether retained state is used at the correct action boundary rather than merely accessed, and whether ineligible state fails before an effect.
- **Mode:** building and validation.
- **Scope/duplication:** v1/v2 are byte-preserved. v3 repairs v2's ceiling by making current authorization necessary for a state-changing decision across change-record and budget-ledger shapes.
- **Useful completion:** preflight passes before calls; later one-shot execution yields discriminating valid cells or fails closed without effect/capability claims.

## Frozen design

Four equivalent forms span two artifact shapes. Each crosses `absent`, `current_authorized`, `information_matched_full_history`, `stale`, `conflicting`, and `revoked`. Current and information-matched history should act; the other conditions should preserve state and request the named resolution. Only `retained_state` changes within a form. Private expected behavior and grader contracts are excluded from the trial filesystem.

The grader reports separately:

1. eligibility;
2. exact target/parameter/end-state execution;
3. pre-effect restraint timing; and
4. recovery communication plus safe partial progress.

A warning after an effect fails restraint. Strict intention-to-evaluate retains every intended service/environment outcome; no retry or complete-case substitution is allowed.

## Provenance and limits

Design rationale comes from the complete local reviews:

- `papers/agent-benchmarks/2026-07-16-shared-selective-persistent-memory-validity.md`;
- `papers/agent-benchmarks/2026-07-16-agentabstain-act-abstain-validity.md`.

All tasks, authority records, thresholds, and expected outcomes are builder-authored calibration. No expert, professional, privacy, safety, production, readiness, general capability, cross-domain, or retained-state causal claim is licensed.

## Lifecycle

```bash
python pilots/persistent-workspace-reuse/v3/freeze_protocol.py  # one time only
python pilots/persistent-workspace-reuse/v3/run_study.py verify
python pilots/persistent-workspace-reuse/v3/run_study.py preflight
python -m unittest tests.test_persistent_workspace_reuse_v3 -v
```

The protocol, inputs, grader, launcher identity, model/provider/tools, budgets, order, hashes, and no-retry policy must be committed and pushed before any model call. This commit intentionally stops at the frozen zero-call preflight boundary; execution must be added without rewriting the instrument.

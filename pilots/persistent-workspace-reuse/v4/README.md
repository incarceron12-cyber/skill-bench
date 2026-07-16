# Persistent-workspace reuse v4: public action interface

This prospectively frozen **internal synthetic** study is a fresh instrument, not a retry or reinterpretation of v3. It tests whether retained authorization changes a consequential action boundary while absent, expired, conflicting, or revoked evidence causes pre-effect restraint and a typed recovery request.

## Charter decision filter

- **Objectives:** B and C: expertise-to-evaluation primitives and executable benchmark infrastructure.
- **Artifact:** 24 unseen cells across two shapes; a complete frozen invocation prompt; normative public JSON Schema; label-blind five-part grader; strict denominator; zero-call isolation, interface, leakage, and mutation canaries.
- **Uncertainty:** whether v3's decision discrimination survives when serialization conventions are public and private condition labels are absent from every agent-visible surface.
- **Mode:** building and validation.
- **Scope/duplication:** v1/v2/v3 remain byte-preserved. v4 uses new forms and repairs only the identified prompt/grader interface, without retrying old cells.
- **Useful completion:** public-interface canaries pass before calls and all fresh cells are attempted once, with failures and invalid service outcomes retained.

## Public convention and private boundary

The normative `output-schema.json` discloses one authoritative event key (`event_type`) and one recovery representation: either `null` for an authorized action or an object with `blocker_category` and `requested_authority`. The four blocker categories are public artifact conventions. The invocation prompt points to this schema but does not reveal condition labels, expected decisions, or private oracle records. `task.json`, `manifest.json`, and the schema are the only visible files.

The grader separates schema conformance, eligibility, exact execution, pre-effect restraint, and recovery communication. Canonical and semantically equivalent reordered-object canaries must pass; string recovery, alternate event keys, late effects, wrong parameters, and label leakage must fail closed.

## Provenance and limits

The general action-boundary rationale comes from the complete local reviews `papers/agent-benchmarks/2026-07-16-shared-selective-persistent-memory-validity.md` and `papers/agent-benchmarks/2026-07-16-agentabstain-act-abstain-validity.md`. The specific repair is grounded in `pilots/persistent-workspace-reuse/v3/execution/study-report.json`.

All forms, authority records, thresholds, categories, and outcomes are builder-authored calibration. No expert, professional, privacy, safety, production, readiness, general-capability, cross-domain, or retained-state causal claim is licensed by this single synthetic campaign.

## Lifecycle

```bash
python pilots/persistent-workspace-reuse/v4/freeze_protocol.py
python pilots/persistent-workspace-reuse/v4/run_study.py verify
python pilots/persistent-workspace-reuse/v4/run_study.py preflight
python -m unittest tests.test_persistent_workspace_reuse_v4 -v
```

The protocol, launcher, prompt, schema, grader, task forms, order, budgets, hashes, and no-retry policy must be committed and pushed before model calls. Execution plumbing is added only after that pushed freeze.

# Persistent-workspace reuse protocol v1

This **internal synthetic zero-call conformance pilot** tests a cross-domain mechanism, not a memory product or profession: whether typed retained-object authority, valid time, permission, immutable composition, and semantic compatibility can prevent unsafe workspace reuse while keeping deterministic artifact refresh separate from agent-mediated reuse.

## Charter decision filter

- **Objectives:** B (expertise-to-evaluation methodology) and C (executable infrastructure).
- **Artifacts:** a frozen/hash-bound 14-cell protocol, executable pinned transformations, semantic validator/replay, mutation tests, and replay report.
- **Uncertainty:** whether existing workspace machinery can distinguish stale, conflicting, and revoked retained state; detect schema semantics beyond column presence; and avoid counting zero-model reruns as memory-agent success.
- **Mode:** building and validation.
- **Duplication/scope:** this reuses the existing workspace, longitudinal, artifact-view, and experience-memory concepts; the two synthetic work shapes are mechanism probes, not procurement or policy scope commitments.
- **Useful completion:** all cells and hashes replay; stale/conflicting/revoked compositions fail closed; the table migration exercises type, unit, key, category, join, and semantic changes; deterministic and agent estimands remain separate.

## Frozen matrix

Each of two meaningfully different artifact shapes—`structured_table` and `structured_memo`—has seven conditions:

1. reset;
2. information-matched full history;
3. curated correct state;
4. curated stale state;
5. curated conflicting state;
6. curated revoked state; and
7. deterministic artifact rerun.

Within each shape, current requirements, current information, base-artifact availability, and budgets are hash-identical. Retained-object composition is the intended treatment. Every retained object records version/hash, originating authority, accessor permission, valid time, lifecycle state, and payload. Every cell records a composition hash, execution mode, model visibility/access/adoption status, artifact/state delta, collateral preservation, and criterion consequence.

The tabular rerun uses a pinned transformation for planted type, unit, key, category, join, and semantic changes. The memo rerun uses a separate pinned structured transformation and current policy-owner authority rule. Both transformations are re-executed by the validator rather than trusting declared output hashes.

## Executed result

`replay-report.json` records 14 cells: two deterministic reruns accepted, six stale/conflicting/revoked preflights rejected, and six agent-mediated cells marked `insufficient_evidence`. **No model was called.** Agent-mediated workspace reuse is deliberately not estimated because this bounded slice first establishes deterministic validity and no frozen comparison requires a provider trial.

This result supports only exact fixture conformance. It does not support general memory capability, a Skill effect, professional validity, privacy compliance, collaboration benefit, production reliability, or deployment readiness.

## Provenance and design boundary

The primary rationale is the complete review at `papers/agent-benchmarks/2026-07-16-shared-selective-persistent-memory-validity.md`, especially its distinction between prompt-composed workspace state and zero-model executable refresh and its recommendation to plant semantic compatibility changes. Adjacent executable records are:

- `pilots/experience-memory-transfer/conformance.json`;
- `tests/fixtures/valid-persistent-workspace-conformance.json`;
- `schemas/LONGITUDINAL_EVALUATION.md`; and
- `tests/fixtures/valid-artifact-admissibility-bundle.json`.

The paper did not release inspectable tasks or code and did not test this protocol. All planted records and outcomes here are builder-authored contract calibration.

## Replay

```bash
python scripts/validate_persistent_workspace_reuse.py \
  pilots/persistent-workspace-reuse/v1/protocol.json --check-paths \
  --report pilots/persistent-workspace-reuse/v1/replay-report.json
python -m unittest tests.test_persistent_workspace_reuse -v
```

`--refresh` deterministically regenerates `protocol.json` from the canonical builder in the validator; normal verification omits it so unexpected fixture edits fail rather than being overwritten.

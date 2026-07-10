# Longitudinal evaluation contract

`benchmark-bundle.schema.json` v0.3 adds an optional `longitudinal_evaluation` object. It evaluates an update policy over an ordered task stream without changing the static task/trial contract.

## Charter fit and bounded hypothesis

- **Objective advanced:** charter objective C (executable evaluation infrastructure) and objective B (expertise-to-evaluation methodology).
- **Artifact:** a schema, semantic validator, matched synthetic fixture, and mutation tests.
- **Uncertainty clarified:** whether the existing configured-system identities can support longitudinal state-transition evidence without conflating agent evolution, task order, feedback leakage, and benchmark drift.
- **Mode:** building and validation. This extends the cross-domain bundle; the operations fixture is contract calibration, not a domain pilot or a capability result.
- **Useful completion:** reset, lesson-only, and full-evolution arms share a frozen instrument, seed, initial state, stream, feedback policy, and budgets; every permitted update is auditable and private evaluation evidence cannot enter updater state.

## Evidence and adaptation boundary

The design is derived from the full-source review at `papers/agent-benchmarks/2026-07-10-self-evolving-agents-survey.md`, especially its state-transition interpretation and transferable patterns 1–5. The reviewed survey proposes rather than empirically validates its longitudinal protocol. Fields and fail-closed rules below are **skill-bench adaptations**, not claims that the paper tested them.

The fixture in `tests/fixtures/valid-benchmark-bundle.json` is synthetic contract-calibration data. Its pending evolution events do not establish learning, retention, transfer, safety, expert validity, or professional readiness.

## Contract boundaries

### Frozen stream and matched treatments

The protocol commits to:

- a hashed `frozen_instrument`;
- ordered and seeded stream items with stage, task version, semantic cluster, distribution relation, and exposure split;
- one stage and cumulative resource envelope;
- one hashed feedback policy; and
- exactly one `reset`, `lesson_only`, and `full_evolution` condition sharing an initial state hash.

The validator prevents reset arms from persisting or updating model, prompt/skill, memory, tools/code, or topology. Lesson-only arms may change only prompt/skill or memory. Full evolution is broader but remains limited by its declared `allowed_update_loci`.

### Evolution-event ledger

Every update records:

- parent and child state hashes plus independently versioned components;
- condition, stream position, trigger, and timing;
- multi-label changed loci;
- typed feedback kind, authority, visibility, and locator;
- update mechanism and random seed;
- resource use;
- validation/rollback status; and
- downstream dependencies.

Semantic validation requires a continuous parent→child state chain per condition and rejects no-op hashes, unknown references, reset-arm events, and update loci outside the treatment allowance.

### Private-evidence firewall

`feedback_exposures` are inputs to the update, not a general audit list. Therefore a `private_check`, `reference_answer`, or `grader_only` exposure is always invalid there. Private evidence may remain in static grading records, but cannot become agent/updater state on the evaluated split.

### Probes and estimands

Probe records distinguish retention, selective forgetting, transfer, and safety drift. Retention must use an equivalent form rather than exact answer replay. Probe kind, stream split, and semantic cluster must agree. Reports preserve at least four separate estimands rather than collapsing final score:

- initial competence;
- adaptation gain;
- retention/regression;
- transfer;
- cost drift;
- safety drift; and
- selective forgetting when exercised.

## What remains outside this slice

This contract does not compute longitudinal metrics, run evolving agents, prove equivalent-form validity, or establish matched trial comparability. `trial_ids` connect future observed runs to conditions, but the calibration fixture intentionally leaves them empty. Real claims still require valid static execution, repeated matched streams/orders, calibrated probes, uncertainty estimates, and a separate claim-validity argument. Benchmark-instrument changes must use a frozen anchor or calibrated bridge rather than editing this stream in place.

## Validation

```bash
python scripts/validate_benchmark.py tests/fixtures/valid-benchmark-bundle.json --check-paths
python scripts/validate_benchmark.py pilots/lh-skill-adoption/benchmark-bundle.json --check-paths
python -m unittest discover -s tests
```

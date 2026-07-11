# Composite workflow conformance slice

This internal fixture tests the general hypothesis that a composed knowledge-work
benchmark needs a typed obligation graph and termination-time invariant replay;
monotone milestone credit can hide a reversed state or a downstream artifact
whose prerequisite was never supported.

It instantiates two deliberately unlike synthetic work shapes:

- a structured approval ledger where an analysis is completed and later reversed;
- a research handoff where a memo exists despite unsupported source verification.

Each node declares dependencies, produced/consumed state, equivalent accepted
paths, and an atomic success baseline. The validator recomputes the independent
composite expectation, replays terminal support independently of validator poll
order, reports the earliest unsupported dependency, and checks reset fingerprints
and side-effect teardown coverage. These records reuse existing benchmark
primitives rather than introducing a new schema.

The rationale is grounded in
`papers/agent-benchmarks/2026-07-11-workarena-plus-compositional-validity.md`,
especially its review of sequential validator state (lines 53–59), executable
composition versus construct validity (81–92), and proposed repairs (136–145).
The local immutable paper and pinned later release are hash-bound in
`workflows.json`; the timing boundary is preserved.

Run:

```bash
python scripts/validate_composite_workflows.py --check-paths
python -m unittest tests.test_composite_workflow_conformance -v
```

## Claim boundary

The scenarios, rates, state fingerprints, and reset outcomes are builder-authored
contract-calibration data. They do **not** establish agent capability, expert
approval, occupational realism, professional validity, causal planning burden,
or release readiness. A gap between observed composite success and the product
of atomic rates is diagnostic only; causal interpretation would require matched
real trials with controlled presentation, horizon, interface, and information
budgets.

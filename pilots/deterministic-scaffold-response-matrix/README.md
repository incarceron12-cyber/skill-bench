# Deterministic scaffold response matrix — cross-shape validation

This package is an **inert, builder-authored validation fixture**. It runs no agent, model, network call, external service, or side effect. It tests whether existing benchmark primitives can preserve deterministic component-conformance evidence without laundering it into end-to-end capability.

## Charter decision filter

- **Objective:** charter B/C — turn research on diagnostic component slices into executable, reusable benchmark machinery.
- **Artifact/evidence:** two work shapes, separate pure/live inventories, six retained treatment dispositions, a replayed observer-response matrix, fail-closed integrity canaries, and tests.
- **Uncertainty clarified:** whether local drift, foundational propagation, observer corruption, case deletion, equivalent change, and unavailable live behavior remain distinguishable.
- **Mode:** building and validation.
- **Duplication/scope check:** this composes existing resource-transfer and professional-artifact fixtures; it adds response-matrix and inventory-integrity validation rather than a new schema or ordering-agent taxonomy.
- **Useful completion:** baseline-twice is stable; expected/prohibited response edges replay; observer/case tampering is invalid rather than green; no-effect and live-only treatments remain explicit; only exact synthetic detection is licensed.

## Design

The frozen pure lane has two cases each for `structured_resource_transfer` and `professional_artifact`. Both expose the same abstract deterministic pipeline—`resolve_source → normalize → persist`—and three exact observers. The values and cases are deliberately small because this validates the **measurement contract**, not professional task content.

The six predeclared treatments are:

1. local persistence loss, expected to fail only the resource endpoint observer;
2. foundational source loss, expected to propagate across all memo observers;
3. an always-pass observer defect, rejected by observer-integrity canary;
4. case deletion, rejected by frozen-inventory canary;
5. an equivalent normalization, retained as no effect;
6. a generative/live-only failure, retained as unavailable and never scored by the pure lane.

Every treatment is retained. `detected` means an exact synthetic response matched a predeclared response edge; it does not mean an organic regression was localized.

## Evidence boundary

The mechanism is grounded in `papers/agent-benchmarks/2026-07-18-layer-isolated-deterministic-scaffold-validity.md`, especially its transfer/test requirements (lines 240–273). The work shapes reuse the abstractions in `pilots/cross-resource-observation-envelope/dependency-topology-v1/package.json` and `pilots/artifact-transition-conformance/conformance.json`. All concrete values, mutations, expectations, and outcomes here are synthetic.

This fixture licenses only reproducible detection and fail-closed handling of its exact builder-authored cases. It supplies no evidence of agent capability, professional validity, stochastic reliability, organic fault localization, production consequence, or readiness.

## Run

```bash
python pilots/deterministic-scaffold-response-matrix/replay.py
python -m unittest tests.test_deterministic_scaffold_response_matrix -v
```

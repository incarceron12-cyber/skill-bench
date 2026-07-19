# Prospective cross-shape self-inspection repair instrument v1

This zero-call pilot advances charter objectives B/C by freezing a reusable causal-repair instrument across a decision memo and a structured native artifact. It tests the general hypothesis that admissible inspection of a work product can support criterion-local repair beyond an equal-budget retry or generic review. The work shapes are methodological contrasts, not a domain commitment.

## Frozen design

Each task has one common pre-repair artifact. Six conditions differ only in the declared repair opportunity:

1. `no_second_attempt`
2. `retry_no_new_information`
3. `generic_self_review`
4. `native_render_self_inspection`
5. `consequence_only_feedback`
6. `criterion_disclosure`

The first condition records the frozen endpoint without repair. Every repair-capable arm has the same tool, harness, model, provider, and budget envelope; the no-second-attempt arm retains the same assigned budget as an unspent counterfactual allocation. Native/render inspection provides no criterion hint. Consequence feedback reports only a deterministic observable consequence. Only criterion disclosure receives criterion text.

`protocol.json` declares public basis, authoritative and derived views, transformation identity, conditions, assignments, typed terminal states, and the proposition-level observation → diagnosis → delta → recheck → collateral/cost record required for later execution. `checkers/check_fixtures.py` is condition-blind and has no condition input. `fixtures/calibration.json` plants positive, near-miss, legitimate-alternative, corrupt-artifact, missing-view, and observer-failure cases for both shapes.

## Freeze and execution boundary

`freeze-manifest.json` pins every source, task, starting artifact, view, transformation, checker, observer, prompt, tool, harness, model, provider, budget, assignment, fixture, and protocol byte. `preflight.py` validates hashes and semantics, replays calibration fixtures, runs zero-call isolation/equal-envelope canaries, confirms an empty attempt ledger, and writes `preflight-report.json`.

This is a **prospective candidate freeze**, not execution authorization. A separate worker must perform a commit-bound independent freeze audit after this version is committed. Any byte change after that audit requires a new version; do not refresh this manifest in place. No model, provider, or repair row is called by preflight.

Run:

```bash
python pilots/self-inspection-repair-v1/preflight.py --check-paths
python -m unittest tests.test_self_inspection_repair_freeze -v
```

## Claim ceiling

All claims of self-correction, agent capability, professional validity, utility, production fitness, and readiness remain false. Calibration establishes only exact deterministic behavior of builder-authored fixtures and mechanical readiness for an independent freeze audit.

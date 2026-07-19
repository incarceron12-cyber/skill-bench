# Self-inspection repair v2: independent candidate-freeze audit

**Audit result: PASS**

**Decision:** The exact candidate freeze passed the independent mechanical gate. A separate task may build/conform the launcher and execute the prospectively frozen matrix; this audit itself authorizes no model/provider call or spend.

## Bound evidence

- Candidate commit `bfc28504477eef5d6e47d3876800ce242dbe9a19` is reachable from `origin/main` at `bd5e630d9d5f3c2e785fce6e01cf748d0fe8ff61`.
- Root tree `1c40bce7f122e249026bec298d801542948dff8a`; candidate subtree `5ea85a60dd422ede36fbb4175988809e68f3d085`.
- Independently read and verified all 30 manifest-bound Git blobs (163979 bytes); aggregate canonical inventory `9e2cee4a0c9b50d41fb06d907f937132f2900b61b33d59b43b0c5a497050dda8`.
- Recomputed 150 assignment identities and the assignment-set hash; no attempt is recorded.
- Replayed all 48 calibration cases through both frozen observers and an independent oracle: {"criterion_fail": 18, "insufficient_evidence": 12, "invalid_artifact": 6, "passed": 12}; observer disagreements=0; pass fraction=0.25.
- No frozen candidate byte was modified. No model, provider, repair row, or paid action was called.

## Gates

- **PASS** `candidate_commit_on_origin_main`
- **PASS** `exact_candidate_commit`
- **PASS** `exact_root_tree`
- **PASS** `exact_candidate_subtree`
- **PASS** `complete_binding_inventory`
- **PASS** `all_bound_bytes_git_object_byte_sha256`
- **PASS** `assignment_set_and_all_150_assignments`
- **PASS** `task_source_view_transformation_public_basis`
- **PASS** `three_families_shapes_two_strata`
- **PASS** `five_repetitions_per_cell`
- **PASS** `equal_execution_envelope`
- **PASS** `observer_condition_blind_and_distinct`
- **PASS** `all_48_calibration_cases_replayed_both_observers`
- **PASS** `mutation_coverage_and_non_floor_ceiling`
- **PASS** `observer_disagreement_fails_closed`
- **PASS** `predeclared_estimands_budget_seed_order`
- **PASS** `zero_call_ledger`
- **PASS** `zero_call_isolation_canary`
- **PASS** `claim_ceiling_all_false`
- **PASS** `builder_preflight_zero_call`
- **PASS** `baseline_semantics`

## What this licenses—and does not

The instrument now mechanically represents three synthetic families/shapes, two predeclared defect strata per family, five conditions, five repetitions per cell, condition-blind dual observers, public source bases, pinned native/render relations, equal declared envelopes, seeds/order policy, clustered estimands, and fail-closed invalid states. Its 12/48 calibration passes avoid the declared builder-only floor/ceiling gate.

This is not outcome evidence. All claim ceilings remain false. The isolation result is an independently exercised allowlist/write-guard canary, not conformance evidence for an execution launcher: no v2 launcher is frozen yet. The continuation must therefore build and test a commit-bound zero-call launcher against these exact bytes before any provider call, then either stop on a conformance defect or execute the already frozen 150 assignments without tuning the candidate.

Machine-readable evidence: `reports/validation/2026-07-19-self-inspection-repair-v2-freeze-audit.json`.

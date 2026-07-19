# Self-inspection repair v1: independent outcome-validity audit

**Audit result: PASS**
**Decision: STOP the current instrument; require prospective redesign before any more execution.**

## Bound evidence

- Freeze commit `7d976a28b9f33337f2f90519964361388b3eae7f` / subtree `53cacc195af88da3ed7ae02954b59bb61afaa23b`.
- Execution commit `50fbf3cf9616640d3d3c94e246a8288d91095a8b` / subtree `3cbd4e0f70bff03008747aa638fd097d3397281b`.
- Read and hash-bound all 135 retained files; aggregate inventory `b1f37b1413a021a9ca15c72a338fbe7aa94d631cea26376afb4e85941f74547c`.
- Independently replayed 12/12 endpoint/collateral outcomes and attempt/usage accounting: `{"api_calls": 35, "attempts": 12, "cache_read_tokens": 60928, "cache_write_tokens": 0, "input_tokens": 79788, "output_tokens": 6004, "provider_calls": 10, "reasoning_tokens": 767, "total_tokens": 146720}`.
- No frozen or execution byte was modified. No model, provider, or repair row was called by this audit.

## Gates

- **PASS** `execution_commit_on_origin_main`
- **PASS** `exact_execution_commit`
- **PASS** `exact_execution_root_tree`
- **PASS** `exact_execution_subtree`
- **PASS** `exact_freeze_commit`
- **PASS** `freeze_subtree_unchanged_at_execution`
- **PASS** `every_retained_file_read_and_commit_bound`
- **PASS** `all_12_assignments_present`
- **PASS** `all_assignment_audits_pass`
- **PASS** `endpoint_and_collateral_replay`
- **PASS** `repair_grounding_and_no_hidden_criterion_laundering`
- **PASS** `delta_locus_and_rechecks`
- **PASS** `attempt_and_usage_accounting`
- **PASS** `condition_summary_replay`
- **PASS** `claim_ceiling_all_false`

## What the retained evidence says

- the exact frozen and retained execution bytes are commit-bound and replayable.
- 12 assignments were retained with one attempt each; 10 called the provider and two no-second-attempt controls did not.
- both frozen starts fail the deterministic endpoint while preserving declared collateral.
- all ten repair-authorized retained finals pass the local deterministic endpoint and collateral checks.
- repair observations, diagnoses, changed loci, and rechecks are grounded in each assignment's retained public information view.
- all repair conditions are observationally indistinguishable from no-information retry on the two-task endpoint outcome.

## Discrimination and limits

The matrix has 2 task clusters, one attempt per assignment, and 10/10 passing repair cells. All repair conditions match `retry_no_new_information` on terminal state and endpoint for both tasks. The five structured repair finals are byte-identical. Memo finals differ in wording but not the checked endpoint/collateral outcome.

Accordingly, the matrix does **not** identify an effect of generic review, native/render inspection, consequence-only feedback, or criterion disclosure beyond the opportunity to retry. Rows share task templates and are not independent treatment replicates; 10/10 saturation blocks ordering the repair conditions.

All claim-ceiling fields remain false: self-correction, agent capability, treatment effect, professional validity, utility, production fitness, and readiness.

## Minimum prospective redesign

- **New Task Diversity:** Freeze at least 3 new independent task families spanning at least 3 artifact/workflow shapes beyond the two current templates; analyze tasks as clusters and do not pool shapes without a predeclared rationale.
- **Defect Difficulty:** Within each family freeze at least two predeclared difficulty strata, including a subtle/near-threshold single-locus defect and a multi-locus defect with a real collateral-risk opportunity; calibrate to avoid floor or ceiling before treatment execution.
- **Observer Variation:** Use at least 2 independently implemented condition-blind observers/checkers per endpoint and predeclare disagreement/adjudication handling.
- **Repetitions:** Run at least 5 independent repetitions per task-condition-configured-system cell with order/random seeds retained; report task-family-clustered uncertainty rather than treating rows as independent.
- **Predeclared Estimand:** Primary: repair pass-rate difference for each information treatment versus retry_no_new_information, averaged within task family then across families, with task-family-clustered uncertainty. Secondary: collateral-preservation difference and token/time burden. A treatment claim requires a nonzero uncertainty-bounded contrast and no predeclared shape reversal; otherwise retain only generic-retry evidence.

Machine-readable evidence: `reports/validation/2026-07-19-self-inspection-repair-v1-outcome-validity-audit.json`.

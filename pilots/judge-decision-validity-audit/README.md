# Judge decision-validity audit

## Purpose and charter fit

This bounded building/validation slice advances charter objectives **B**, **C**, and **D**. It tests a cross-domain measurement hypothesis: criterion-level agreement can look strong while equal-task agreement, high-consequence errors, root scores, rankings, or threshold decisions remain poor. The reusable artifact audits those estimands separately instead of treating pooled leaf F1 as judge validity.

PaperBench is methodological evidence, not a commitment to scientific replication as the benchmark domain. The fixture is builder-authored contract calibration. It does not reconstruct PaperBench's absent model predictions, validate an expert substitute, or support capability, professional-quality, or readiness claims.

## Artifacts and input contract

- `fixtures/cases.json` defines five synthetic tasks, binary human-procedure labels, judge predictions, validity, positive weights, severity, a decision threshold, and deterministic task-cluster bootstrap settings. Compact groups expand to stable criterion IDs.
- `audit.py` validates the input, exercises `fail_closed`, `fail_open`, and `abstain` invalid policies, and writes `audit-report.json`.
- `audit-report.json` reports pooled-leaf and equal-task class-macro F1 separately; per-task confusion and root-score absolute error; high/critical-severity confusion; threshold flips/abstentions; competition-rank effects; and task-cluster bootstrap sensitivity intervals.
- `tests/test_judge_decision_validity_audit.py` covers extreme task-size imbalance, estimand divergence, consequential errors, policy sensitivity, clustered uncertainty, malformed inputs, provenance, and deterministic report freshness.

A production prediction export can use the same task/group contract, but its `configured_population` must name the exact task, rubric, label procedure, judge, prompt, evidence view, and version boundaries. Human-procedure labels must not be renamed ground truth without reliability and adjudication evidence.

## Semantics

- **Pooled-leaf class-macro F1** weights tasks in proportion to evaluated leaf count.
- **Equal-task class-macro F1** gives each configured task one vote after computing within-task class-macro F1.
- **Root error** compares the truth-label and judge-prediction weighted criterion means. It validates that authored score operation only, not the construct represented by the score.
- **Consequential confusion** separately counts errors on `high` and `critical` criteria. It is not folded into uncalibrated cost-weighted accuracy.
- **Decision effects** compare a declared threshold, preserving abstention rather than coercing it to pass/fail.
- **Rank effects** use competition ranks, so exact score ties do not acquire arbitrary alphabetical order.
- **Uncertainty** resamples whole tasks, never leaves. With five authored tasks, the interval is a sensitivity diagnostic, not population-generalization evidence.

Invalid-policy sensitivity is explicit: fail-closed maps invalid predictions to zero, fail-open maps them to one, and abstain excludes invalid leaves from agreement/root computations while withholding the affected task's decision. All three retain `invalid_count`.

## Evidence and rationale

| Design choice | Evidence | Bounded interpretation |
|---|---|---|
| Contrast pooled leaves with equal tasks | `papers/agent-benchmarks/2026-07-15-paperbench-replication-rubric-validity.md`, JudgeEval boundary 1; `data/sources/releases/2504.01848v3-paperbench/audit.json` | PaperBench's 1,963-leaf example has nearly 25x the leaf influence of its 79-leaf example; this fixture tests the general imbalance mechanically. |
| Root error, rank effects, threshold flips | Review, JudgeEval boundary 2 and “Transfer to skill-bench” | Leaf concordance does not establish score or decision validity. Fixture effects do not show which policy predicts expert acceptance. |
| High/critical confusion | Review, limitations 14 and concrete action 2 | Consequential errors stay visible; severity labels are synthetic and uncalibrated. |
| Explicit invalid policies | Review, “SimpleJudge and evidence access”; release audit `invalid_policy` | Invalid infrastructure observations must not silently become substantive failures. |
| Task-cluster bootstrap | Review, “Test before adopting” and limitations 11–14 | Resampling leaves would falsely treat within-task criteria as independent. Five tasks remain too few for broad inference. |

## Reproduce

```bash
python pilots/judge-decision-validity-audit/audit.py --check
python -m unittest tests.test_judge_decision_validity_audit -v
```

Regenerate after intentional input or implementation changes:

```bash
python pilots/judge-decision-validity-audit/audit.py
```

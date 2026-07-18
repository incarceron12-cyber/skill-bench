# Independent execution-validity review: pre-task procedure transfer v7

**Decision:** **PASS execution closure; do not upgrade the transfer claim.** The retained evidence supports a commit-bound statement that one frozen 32-row synthetic configured-agent matrix executed as assigned and produced 24 endpoint passes. It does **not** identify an artifact-complete two-family generated-package advantage over no package, and it shows no endpoint advantage over equal-budget raw context.

**Evidence status.** This is an independent, zero-call, non-rescoring review of the complete local primary execution record at source snapshot `a6d06f988dcdd56e6e3cb46845c652b9f1ace3e3`, which exactly matched both `HEAD` and `origin/main` when audited. I read the charter, research agenda, v7 independent freeze review, frozen manifest and protocol, execution README, pre-execution and full-surface canary reports, launcher and builder audit, all 32 assignments, trial reports, candidate results, usage records, traces, stderr files, frozen private endpoints, and relevant retained v5/v6 gate failures. I wrote a separate audit that did not import or invoke the launcher, oracle, or checker and made no model or provider call.

- Machine report: [`reports/validation/2026-07-19-pretask-procedure-v7-execution-independent-audit.json`](../../reports/validation/2026-07-19-pretask-procedure-v7-execution-independent-audit.json)
- Independent audit: [`scripts/audit_pretask_procedure_v7_execution.py`](../../scripts/audit_pretask_procedure_v7_execution.py)
- Execution package: [`pilots/pretask-procedure-transfer-v7-execution/`](../../pilots/pretask-procedure-transfer-v7-execution/)
- Frozen instrument: [`pilots/pretask-procedure-transfer-v7/`](../../pilots/pretask-procedure-transfer-v7/)
- Prior freeze review: [`pretask-procedure-transfer-v7-independent-freeze-review.md`](pretask-procedure-transfer-v7-independent-freeze-review.md)
- Retained failed-parent evidence: v6 [`canary-report.json`](../../pilots/pretask-procedure-transfer-v6/canary-report.json) and [`preflight-report.json`](../../pilots/pretask-procedure-transfer-v6/preflight-report.json)

## Contribution and research question

This review asks a narrow lifecycle and measurement question: **after a frozen instrument passes an independent zero-call gate and is executed once, which observations survive independent evidence closure, denominator separation, and contrast identification?**

It advances charter objectives B and C through validation. The concrete artifacts are a commit-bound human review, replayable machine audit, exact endpoint-miss classification, and separate assigned-row versus artifact-complete contrasts. The uncertainty is not whether custody or journal expertise transferred; both families are builder-authored mechanism probes. It is whether the execution record licenses any bounded package-effect observation without silently converting artifact failures, fixed authored clusters, or equal performance against raw context into a transfer claim.

## Methodology

The independent audit used six evidence paths:

1. **Snapshot and instrument identity.** Bind the review to exact commit `a6d06f9…`; verify current bytes against the commit for 25 tracked v7 instrument files and 295 tracked execution-package files; calculate deterministic tree digests; recompute all 55 frozen manifest bindings.
2. **Assignment and attempt closure.** Join every retained trial to the 32-row frozen schedule and confirm two tasks in every family-condition cell, one attempt per row, zero repairs/retries, one common configured-system record, one prompt hash, and all-false claim ledgers.
3. **Input and evidence joins.** Reconstruct each assigned treatment from frozen v4 resources; compare its hashes and sizes with the prospective trial inventory; verify result, usage, trace, and stderr hashes without running the launcher.
4. **Independent semantic comparison without rescoring.** Parse each stored candidate and frozen private endpoint; compare closed keys and typed values while allowing only declared reason and ordering invariances. This reproduces all 24 stored passes and all eight misses. The frozen checker was not invoked and no score was replaced.
5. **Denominator and contrast separation.** Recompute intended, attempted, service-valid, environment-valid, artifact-valid, scored, and endpoint-pass counts. Report the predeclared assigned-row endpoint contrasts separately from artifact-complete contrasts. A family contrast is artifact-complete only when both tasks in both compared conditions have valid task-identified artifacts.
6. **Resources, dependencies, and retained failures.** Sum all usage records; inspect the frozen checker for condition/treatment dependencies; inspect the execution command and profile against the declared resource envelope; and retain v6's failed output-overlay and dependency gates as historical failures rather than retroactive v7 successes.

This method audits the existing evidence. It does not rerun, repair, rescore, or estimate unobserved counterfactual outcomes.

## Evidence and findings

### 1. Byte, assignment, and attempt closure pass

At audit time, `HEAD == origin/main == a6d06f988dcdd56e6e3cb46845c652b9f1ace3e3`. The independent tree digest is `56dab6…` for the tracked v7 instrument and `af7b85…` for the tracked execution package. All 55 manifest bindings matched. Every schedule index 1–32 joined to the intended task, family, and condition; every family-condition cell contained its two frozen tasks.

All rows had exactly one attempt, no repair, and no retry. The retained records agree on model `gpt-5.6-sol`, provider `openai-codex`, file-only tools, safe mode, 40 turns, a 900-second timeout, one prompt hash, successful service state, and provider-included USD `0.00`. Every input inventory matched the condition-specific frozen resources. All result, usage, trace, and stderr hashes joined to the trial reports. The prompt limitation remains explicit: prompt bytes were reconstructed after execution, although every prospective trial report already held the same hash.

This closes execution custody. It does not establish that every declared configured-system property was enforceable or fully versioned.

### 2. Strict denominators reproduce, but “invalid” has two meanings

The independently reproduced counts are:

| Denominator | Count |
|---|---:|
| intended / attempted | 32 / 32 |
| service-valid / environment-valid | 32 / 32 |
| artifact-valid | 30 / 32 |
| checker-scored | 32 / 32 |
| endpoint pass | 24 / 32 |
| endpoint miss | 8 / 32 |
| repair / retry | 0 / 0 |

The launcher’s `attempt_state.invalid` count is zero because every service- and environment-valid row is labeled `attempted`. Separately, two outputs fail its minimal artifact-validity predicate because `task_id` is `family-zeta` instead of the assigned task ID. Those are schedule 7 (`cross_family_irrelevant`, `t6v1`) and schedule 10 (`no_package_no_raw`, `w3d8`). The published report preserves both as scored endpoint failures, which is appropriate for an **assigned-row policy outcome**. It is not appropriate to silently call the resulting contrast an artifact-complete procedure-transfer estimand.

### 3. Every endpoint miss has a concrete failure signature

The eight misses are not one undifferentiated failure class:

| Row | Condition | Failure signature |
|---:|---|---|
| 2 | cross-family irrelevant, zeta `w3d8` | Irrelevant-package rejection displaced task execution; committed transaction `C` was omitted. |
| 3 | cross-family irrelevant, epsilon `k4n7` | Correct control/disposition but omitted non-controlling observation `o2`. |
| 6 | cross-family irrelevant, epsilon `p9c2` | Correct control/disposition but omitted non-controlling observation `r1`. |
| 7 | cross-family irrelevant, zeta `t6v1` | Rejected the task because package family differed, used the family as `task_id`, and returned wrong transaction semantics. |
| 10 | no package, zeta `w3d8` | Used the family as `task_id` and incorrectly treated an unfinished journal as valid. |
| 14 | no package, epsilon `k4n7` | Omitted non-controlling observation `o2`. |
| 17 | no package, epsilon `p9c2` | Omitted non-controlling observation `r1`. |
| 25 | exactly-one-defect, zeta `t6v1` | Followed the planted wrong mutation-ownership rule, producing `x=2` instead of `x=1`. |

The cross-family package is therefore a behavior-changing negative control, not merely inert extra text. In two epsilon rows it leaves the substantive decision correct but induces evidence-list incompleteness; in two zeta rows the model explicitly treats family mismatch as a reason to reject or invalidate task execution. The single activated defective-package failure is also diagnostic: the model copied the planted defect into the endpoint rather than independently recovering the correct rule.

### 4. The assigned-row `+0.75` is closed arithmetic, not an identified transfer estimate

The published family-clustered assigned-row contrast for generated package minus no package reproduces:

- epsilon: `1.0 - 0.0 = +1.0`;
- zeta: `1.0 - 0.5 = +0.5`;
- authored-family mean: `+0.75`.

That is a valid description of all assigned one-shot outcomes, including invalid artifacts as failures. But zeta's no-package cell has only one artifact-valid row. Excluding the invalid artifact would condition on a post-treatment outcome; including it changes the outcome into “produce a task-identified artifact that passes.” Neither choice by itself identifies semantic procedure transfer. Under the predeclared no-silent-pooling rule, the artifact-complete two-family generated-versus-no-package contrast is therefore **not identified**.

By contrast, generated package minus equal-budget raw context is artifact-complete in both families and exactly `0.0` in each. Generated plus raw minus generated and reference procedure minus generated are also `0.0` in both families. The five positive-support conditions—generated, raw, generated-plus-raw, reference, and hindsight—are all at 4/4 endpoint passes. This ceiling pattern supports only a bounded conclusion: **in this one-shot matrix, the generated package was sufficient, but it showed no endpoint advantage over the frozen raw corpus or builder reference.** It does not isolate compression, procedure quality, or transfer.

The negative controls are imperfect discriminators. Cross-family irrelevant is 0/4, but it actively causes rejection or evidence omission rather than testing harmless irrelevant context. Exactly-one-defect is 3/4, so the planted defect changes one endpoint but does not reliably distinguish defective from reference support across these four task forms.

### 5. Resource accounting closes; resource equivalence is only partial

The independent sums reproduce 196 API calls, 987,097 provider total tokens, 328,299 input tokens, 16,750 output tokens, 7,328 reasoning tokens, and provider-included USD `0.00`. Prompt and declared configured-system records are identical. Treatment support ranges from zero bytes to 8,101 bytes by condition/family; this is intentional treatment content, not an execution-parity defect.

Three operational qualifications matter:

- The protocol and trial records declare an 8,000-token context budget, but the launcher neither passes such a CLI argument nor writes it into the temporary Hermes profile. It enforces a 16,000-byte treatment-file ceiling instead. Therefore “8,000 tokens” is metadata, not demonstrated runtime enforcement.
- The launcher binds `/home/sam/.hermes/hermes-agent` and a local Python installation, but trial records retain no Hermes executable/tree hash or complete environment lock. The launcher bytes are commit-bound; the full harness implementation used at call time is not.
- Rows ran sequentially once. Observed API calls vary from six to eight and total tokens vary substantially. These are retained resource outcomes, but there are no repeats with which to separate treatment, task, stochastic, cache, or time/order effects.

These limits do not invalidate the 32 stored endpoint observations. They block stronger configured-system reproducibility, efficiency, and causal-treatment claims.

## Unique insight: one run can support two different outcomes, but they answer different questions

V7 exposes a general benchmark-design distinction:

1. **Assigned-row policy outcome:** Did the configured system, under its assigned treatment, produce a valid-and-correct endpoint? Here invalid artifacts remain failures, and generated minus no package is descriptively `+0.75` across two authored families.
2. **Artifact-conditional mechanism outcome:** Given an admissible task artifact, did the procedure change the targeted semantic operation? Here post-treatment artifact invalidity creates missingness, and the two-family generated-versus-no-package contrast is not identified.

Neither denominator is universally “right.” The first measures end-to-end treatment policy, including formatting and identity failures. The second is useful for mechanism diagnosis but can be biased by conditioning on a treatment-affected artifact gate. A benchmark must predeclare both, report the selection path, and restrict claims accordingly. **A single endpoint table cannot simultaneously serve deployment-style success and mechanism-transfer interpretation without an explicit missingness/estimand bridge.**

V7 also shows why positive controls alone do not identify procedural value. Generated, raw, reference, and hindsight support all saturate the endpoint, while the defective control usually passes and irrelevant support actively induces a refusal heuristic. The experiment validates lifecycle machinery and reveals failure signatures more strongly than it validates the generated procedure.

## Limitations, reproducibility, and operational realism

- The tasks, procedures, source authority, endpoints, and checker are builder-authored synthetic calibration artifacts. There is no expert provenance, external standard, or professional consequence.
- Two authored families are not a sampled population. Family clustering prevents treating four repeated task rows as independent families, but two clusters cannot support meaningful sampling-based uncertainty.
- There is one attempt per row. Model stochasticity, service drift, and order effects are unestimated.
- Task, procedure, and checker were co-designed. The endpoint is exact and inspectable, but criterion fit may be artificially high.
- Twenty of twenty rows in the five positive-support conditions pass, creating a ceiling that prevents ranking generated, raw, reference, plus-raw, and hindsight support.
- Artifact validity checks only parse an object and match `task_id`; they do not establish complete schema admissibility independently of the endpoint checker.
- Checker source is condition-blind and reads stored candidate/private records only, but independent authorship and construct independence are not established.
- Prompt bytes were reconstructed post-execution; prospective prompt hashes mitigate but do not remove this custody limitation.
- The declared token budget and complete Hermes environment were not cryptographically enforced or retained as configured-system identity.
- Provider-reported included cost is auditable as `0.00`; it is not evidence that infrastructure or opportunity cost is zero.
- Retained traces are intentionally sparse completion messages, not reasoning evidence. Root-cause classifications rely on artifacts and treatment contents, not internal cognitive traces.

## Benchmark relevance and next actions

1. **Accept v7 as a successful lifecycle/execution-closure validation.** Preserve all v1–v7 bytes and the two artifact-invalid rows. The prospective repair chain reached a complete one-shot matrix without rewriting prior failed evidence.
2. **Do not upgrade transfer or capability claims.** Retain all seven false claim flags. In particular, do not cite `+0.75` without saying it is an assigned-row descriptive outcome whose zeta no-package cell contains an invalid artifact.
3. **Use the zero generated-versus-raw contrast as a design signal.** Before spending on another model matrix, require tasks that can distinguish a compact procedure from equal-budget raw evidence and calibrate defective/irrelevant controls to test the intended mechanism rather than refusal behavior.
4. **Predeclare dual denominators in future procedure experiments.** Keep end-to-end assigned success and artifact-conditional semantic success separate, including missingness and post-treatment-selection rules. This requirement already belongs in the repository's validity, metric, artifact-admissibility, and task-health machinery; no duplicate schema task is needed.
5. **Freeze the complete configured system prospectively.** Hash the Hermes executable/tree and effective config, retain prompts before calls, and either enforce the stated context budget or label it descriptive.
6. **Require repeated attempts and more independent families before inference.** A future validation should estimate within-cell stochasticity and use independently authored, non-saturating families before reporting uncertainty or general transfer.

No new queue task is added. The evidence refines existing lifecycle, validity, metric, artifact-admissibility, and configured-system requirements; another schema or rerun task would duplicate those paths without resolving the missing expert and construct-validity evidence.

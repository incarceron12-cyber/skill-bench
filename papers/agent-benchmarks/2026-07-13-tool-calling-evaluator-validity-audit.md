# Tool-calling evaluator audit: important failure witnesses, but an unauditable validity study

**Source type:** Deep review of the complete immutable arXiv v1 primary source, including appendices.  
**Source:** Vaghasiya et al., *Benchmarking the Benchmarks: A Validity Audit of Tool-Calling Evaluation*, arXiv:2607.02577v1 (30 June 2026), 12 pages.  
**Canonical source:** https://arxiv.org/abs/2607.02577v1  
**Local PDF:** `data/papers/pdfs/2607.02577v1-tool-veritas.pdf` (SHA-256 `eb291916b21a23ba951ef8be208cead4dbcfa83f36353cc571bb12194722ec69`).  
**Local text:** `data/papers/text/2607.02577v1-tool-veritas.txt` (SHA-256 `382ef79791aca4878f0264df0e77b02c667dd63eb63ba01be3ce7d79b99660cf`).  
**Artifact status:** No release was inspectable. Immutable v1 contains no repository, project, dataset, DOI, supplement, trace, annotation, corrected-evaluator, Tool-Veritas, or Harness Lab URL. Exact-name web searches found no verifiable author-owned release. The Availability statement says these artifacts *will* be released and identifiers added in a final version (p. 9). Paper-time implementation and empirical evidence therefore cannot be independently audited.

## Bottom line

The paper supplies two useful and concrete warning cases: a τ²-Bench communication assertion rejects a task-consistent `$708` answer in favor of an apparently wrong `$1,628` target, and LiveMCPBench's end-to-end score ranges from 55/95 to 73/95 across 23 complete reruns (pp. 7, 11–12). These examples sharpen a general benchmark principle: **reproducible code is not enough; a check must have a valid semantic target, and stochastic score variance must be separated by source.**

The headline “18.5% misalignment” is much weaker than it appears. The 496 trajectories come from four different benchmarks, only two agents, benchmark-specific samples of unexplained selection, and one run configuration per family. The paper does not identify the three experts, their qualifications, assignment design, blinding, independent-label count, agreement, adjudication protocol, or per-category counts. It also does not release the 496 traces, 92 disagreements, labels, corrections, or pinned benchmark revisions. The aggregate is therefore a descriptive error proportion for an unreproducible convenience audit—not an estimate of evaluator error in these benchmark families.

Tool-Veritas is a plausible design proposal, not a validated replacement. Its reported 95.5% agreement is measured on its own 70 tasks and six models, against the same under-specified expert criterion, with no comparison on matched tasks or trajectories, no uncertainty, no inter-rater evidence, and no released implementation. The paper itself concedes that task and model distributions differ (p. 8). Skill-bench should retain the outcome-predicate/qualitative-judge boundary while rejecting the paper's cross-benchmark superiority implication.

## One-sentence contribution

Tool-calling evaluator disagreement is a multi-link validity problem—not automatically evaluator error—and deterministic factual gates remain unvalidated until their observations, semantic targets, admissible alternatives, decision logic, and human reference are independently tested.

## Contribution details

The paper asks whether native tool-calling evaluators agree with human judgments of task success and whether stochastic evaluator pipelines reproduce scores. It contributes:

1. a claimed trace-level audit of 496 executions from BFCL v4, τ²-Bench Retail, LiveMCPBench, and MCP-Atlas;
2. a taxonomy spanning brittle state matching, trajectory lock-in, wrong ground truth, reward-basis mismatch, rubric drift, hallucinated completion, answer-only judging, and stochastic variance;
3. a proposed decomposition into tool invocation, task completion, and outcome verification;
4. Tool-Veritas, a deterministic-state-gate-first evaluator with an optional restricted qualitative judge and separately recorded repair;
5. Harness Lab, described as preserving artifacts, diagnostics, repeated-run comparisons, retries, versions, and human adjudications.

The unique contribution is not the familiar deterministic-versus-LLM-judge contrast. It is the insistence that **the evaluator is itself an empirical object whose verdicts, observations, semantic targets, stochastic components, and corrections require versioned validation evidence.**

## Research question

The operative research questions are whether official tool-calling verdicts agree with qualified trace-level judgments, which evaluator mechanisms explain disagreements, whether stochastic pipelines reproduce scores, and whether deterministic factual gates with restricted qualitative judging improve agreement.

## Methodology and system

### Audit sample

The audit crosses neither benchmark nor agent systematically. Kimi-K2.6 is used for 112 τ²-Bench Retail tasks; MiniMax-M2.7 is used for 200 BFCL v4, 95 LiveMCPBench, and 89 MCP-Atlas tasks (p. 6). Table 3 reports 11, 40, 29, and 12 benchmark–human disagreements respectively (p. 6).

No sampling frame or inclusion rule is given. BFCL analysis later focuses on an “inspected 50-task multi-turn base export,” despite Table 3's 200 audited tasks; the relationship between those 50 and the 200 is not explained (p. 7). The paper does not report family population sizes, randomization, strata, task exclusions, invalid executions, missing evidence, endpoint failures, or whether official pass/fail prevalence influenced selection. Consequently the denominators establish only what this collected set contained.

### Human criterion

Three “independent expert annotators” reportedly inspect requests, tool calls/outputs, state changes, and final responses; disagreements are “resolved through adjudication.” Total labor is 89 hours, or 10.8 minutes per task (p. 6). That is the entire validity criterion description.

Missing are expert identities, tool/domain qualifications, recruitment, training, written decision rules, assignment overlap, whether all three labeled all 496 cases, whether official verdicts/evaluator diagnostics were hidden, raw labels, agreement before adjudication, uncertainty, abstention, ambiguity handling, and adjudicator identity. Section 3.3 says “for each flagged instance” annotators inspect evidence (p. 3), while Section 4.1 implies all tasks receive expert judgments (p. 6). If “flagged” cases were selected using evaluator symptoms or preliminary review, the reported disagreement rate can be selection-conditioned. The paper does not resolve this.

Its `H(trajectory)` formalism treats expert success as binary truth, but several reported categories—communication adequacy, policy adherence, user intent, and valid alternative outcomes—can require mandate interpretation and domain authority. An adjudicated label is evidence, not ground truth by definition.

### Failure analysis and corrections

Disagreements may receive “one or more” categories through trace/evaluator inspection (pp. 3–4), but the paper provides no codebook, coding procedure, category frequencies, overlap matrix, coder agreement, or complete case table. Despite claiming a unified taxonomy and 92 disagreements, only two cases receive enough detail to inspect in v1.

Section 3.7 says the authors construct corrected annotations, evaluation logic, and harnesses and re-evaluate them (p. 4). No correction experiment appears in Section 4: there are no before/after denominators, changed labels, residual errors, held-out validation, regression tests, or correction provenance. The claimed “corrected benchmark components” remain an availability promise.

### Reproducibility experiment

LiveMCPBench is rerun 23 times on 95 tasks. Scores range 57.9%–76.8%, mean 69.4%, SD 5.4 percentage points (pp. 7, 11–12). The default scorer regenerates key points and then invokes `gpt-4.1-mini`; human-authored steps are fallback-only. This is a valuable implementation diagnosis.

But these are complete reruns: agent trajectories, generated rubrics, and judge verdicts all vary. The paper explicitly acknowledges this (pp. 7, 12). It therefore does **not** estimate evaluator stochasticity “without changing the evaluated model” in the causal sense used by the abstract: model identity is fixed, sampled behavior is not. A valid decomposition needs fixed-trajectory rescoring under fixed versus regenerated rubrics, multiple agent seeds under a frozen evaluator, and crossed variance components. The max–min spread is also an unstable extreme statistic and not a confidence interval or expected leaderboard error.

## Evidence

### What the evidence supports

- In the authors' unreleased audit records, official and final adjudicated labels differed on 92/496 collected trajectories (Table 3, p. 6).
- The paper documents one detailed τ²-Bench false negative: state and five expected actions match, but a substring assertion expects `$1,628` where the trace's task-consistent remaining-flight sum is `$708` (pp. 7, 11).
- It documents one τ²-Bench false positive where unchanged state and an incomplete rubric reward transfer-to-human rather than executing two returns (p. 7), though no trace is released.
- In 23 complete LiveMCPBench reruns, 18 aggregate task outcomes separate the minimum and maximum (pp. 7, 12).
- The proposed Tool-Veritas evaluation records factual gates separately from qualitative judgment and first-attempt success separately from repaired success (pp. 4–5).

### What the evidence does not support

- A population-level 18.5% error rate for tool-calling benchmarks or the four named families.
- That all 92 differences are evaluator defects rather than expert error, task ambiguity, evidence-view insufficiency, environment nondeterminism, or policy disagreement.
- That LiveMCPBench's 18.9-point spread is attributable solely or primarily to its evaluator.
- That corrected evaluators reduce error; no correction results are reported.
- That Tool-Veritas outperforms native evaluators under matched tasks, agents, traces, judges, or evidence views.
- That 95.5% agreement establishes construct validity, professional validity, calibration, or absence of systematic shared error.

## Tool-Veritas assessment

A task contains a request, initial state, tools, deterministic predicates, and optional qualitative rubric. Required factual predicates gate success; an LLM cannot override a failed gate. A bounded repair window yields distinct initial/repaired outcomes. Per-turn JSONL is said to include action, response, transition, gate, repair, and judge records across sixteen domains (pp. 4–5).

The 70-task, six-model table reports 401/420 agreement and 19 false negatives with no false positives (p. 8). This is encouraging internal conformance evidence, but four validity threats dominate:

1. **Co-authored criterion:** task, predicates, and proposed evaluator are produced by the same project; no independent source-to-check equivalence audit is reported.
2. **Unmatched comparison:** native benchmark agreement values come from different tasks, agents, environments, and human decisions. The paper acknowledges this but still frames the result as improvement.
3. **Under-specified human reference:** the same missing qualification, blinding, reliability, and adjudication evidence applies.
4. **No inspectable artifact:** task definitions, predicates, traces, labels, qualitative rubrics, judge prompts, and code are unavailable.

Deterministic gates can still encode wrong targets, over-specified state, hidden obligations, or an incomplete success condition—the exact failures the paper finds elsewhere. “Deterministic-first” relocates validity work into predicate authoring; it does not solve it.

## Reproducibility and operational realism

Harness Lab's stated object model is strong: raw vendor output, official scores, inference logs, case summaries, turn diagnostics, execution metadata, pinned code/patches/data/settings, separate official/human labels, and paired run comparison (pp. 5–6). Selective retry followed by merged rescoring is operationally useful but creates a statistical hazard: retry eligibility and merge policy must be frozen, because outcome-conditioned retries can silently change the estimand.

Operational evidence is absent. There is no code, deployment manifest, schema, object-store record, database export, lockfile, benchmark commit, endpoint configuration, raw trace, or replay command. “Versioned” is asserted rather than demonstrated. Mutable OpenAI-compatible endpoints, benchmark revisions, generated rubrics, model sampling, and cloud services prevent replay from the paper alone.

The references themselves contain placeholder arXiv identifiers (`2503.XXXX`, `2601.XXXX`, etc., pp. 9–10), and v1 describes future releases as present contributions. These are material preprint-quality and provenance warnings.

## Limitations and validity threats

1. **Unknown sample selection and denominators.** No sampling frame, coverage claim, exclusions, or relationship between the 50-task BFCL export and 200-task audit.
2. **Two-agent confound.** Benchmark family, agent model, task mix, and evaluator type move together.
3. **Human truth is under-documented.** No qualifications, rules, blinding, overlap, agreement, abstention, or adjudication lineage.
4. **Potential label-aware review.** Annotators inspect official diagnostics; whether verdicts were hidden is unstated.
5. **Binary collapse.** Expert PASS/FAIL elides ambiguity, partial completion, safety, communication quality, valid alternatives, and evidence insufficiency.
6. **Taxonomy is not reproducible.** No codebook, full counts, multi-label distribution, or coding reliability.
7. **Sparse witnesses.** Two detailed examples cannot substantiate the distribution of claimed failure modes across 92 cases.
8. **No uncertainty.** Misalignment proportions lack intervals and task/configuration clustering; aggregate 92/496 weights incomparable families by sampled count.
9. **Variance-source conflation.** LiveMCPBench reruns mix trajectory, rubric, judge, tool/service, and environment variance.
10. **Extreme spread overinterpretation.** Max–min is sample-count-sensitive and does not itself establish leaderboard rank reversals.
11. **Corrections are unevaluated.** Repaired components and before/after outcomes are promised, not shown.
12. **Replacement is evaluated on itself.** Tool-Veritas lacks matched native-evaluator or held-out task tests.
13. **Agreement is not validity.** Experts and gates can share wrong task interpretations; no independent outcome intervention tests predicate sensitivity/specificity.
14. **No release.** Core empirical claims and implementation cannot be independently reproduced.
15. **No cost accounting beyond annotation time.** Model, judge, infrastructure, rerun, adjudication, and maintenance costs are absent.

## Unique insight relative to adjacent skill-bench evidence

AgentRewardBench showed that judge reliability depends on evidence view, label lineage, class balance, and adjudication. EvalAgent separated runnable evaluator engineering from measurement validity. BrowserGym/Harness-Bench separated intended harness treatment from its realized execution envelope. Task-health and validity contracts already hold versioned defects and claim ceilings.

This paper adds one useful cross-cutting distinction: evaluator disagreement must be localized across **five separately testable links**:

1. **observation:** did the evaluator and human receive sufficient, equivalent state/trace evidence?
2. **semantic target:** does the expected outcome correctly encode the disclosed user objective and authority?
3. **admissibility/invariance:** are alternative successful states and trajectories accepted while irrelevant differences are ignored?
4. **decision procedure:** does deterministic/LLM logic apply the target reproducibly and calibratably?
5. **reference adjudication:** is the human label independently qualified, reliable, and uncertainty-aware?

Calling every `official ≠ human` case an “evaluator error” skips links 1, 2, and 5. For skill-bench, disagreement should open a typed adjudication, not automatically overwrite the official score.

## Relevance

This is high-relevance comparative design research for skill-bench's grader, task-health, reliability, and validity layers: realistic knowledge-work artifacts can be judged incorrectly even when agent execution is sound, and a human correction is only as authoritative as its evidence view and adjudication process. The tool-calling domain is a methodological case, not a proposed scope boundary.

## Transfer to skill-bench

### Retain

- Decompose tool invocation, consequential state completion, user-facing communication, policy/safety, and verification rather than hiding them behind one pass bit.
- Gate factual claims on authoritative state predicates; restrict qualitative judges to criteria that truly require judgment, and prevent prose fluency from overriding failed factual consequences.
- Record initial success, error, feedback, repair, and post-repair verification separately.
- Preserve official label, independent observations, adjudicated label, defect hypothesis, correction version, and historical score without rewriting old evidence.
- Require fixed-trajectory/fixed-rubric reruns before attributing variance to a judge.

### Repair

Every evaluator-validity audit should freeze:

- population, inclusion/exclusion flow, task/agent/configuration clusters, and selection basis;
- exact task, environment, expected outcome, evaluator, judge, harness, model, and dependency hashes;
- evaluator and human evidence views, including missing/invalid states;
- independent raw labels, qualifications, blinding, overlap, agreement, adjudication, ambiguity, and abstentions;
- typed disagreement direction and candidate locus across observation, target, admissibility, procedure, reference, environment, and agent;
- correction diff, prospective contrast/regression suite, held-out result, and permissible claim update;
- crossed repeats that identify trajectory, rubric-generation, judge, environment, and service variance.

### Falsifiable validation experiment

For two structurally different knowledge-work pilots, preserve a fixed set of traces with planted pairs: true state failure, irrelevant state difference, alternate valid path, wrong semantic target, incomplete communication, missing observer view, and unsafe but superficially complete action. Cross:

1. native deterministic evaluator;
2. unrestricted LLM judge;
3. deterministic factual gates plus restricted qualitative judge;
4. independently authored reference adjudication.

Repeat fixed traces under fixed and regenerated rubrics, then independently rerun agent trajectories under a frozen evaluator. Estimate sensitivity, specificity, abstention, criterion-level agreement, inter-rater reliability, and variance components with task/configuration clustering. Tool-Veritas's design claim survives only if it improves held-out discrimination without increasing hidden-obligation or valid-alternative errors.

## Concrete changes

1. **Do not add a schema task.** Existing benchmark-bundle observation/admissibility records, task-health defect/adjudication lifecycle, metric-monitoring dependence rules, reliability records, and validity arguments can represent these requirements.
2. **Treat the two documented τ²/LiveMCP cases as failure hypotheses, not prevalence estimates.** Add analogous planted cases only to prospective pilot calibration suites with independent source-to-target review.
3. **Require variance decomposition for stochastic graders.** A complete rerun is an end-to-end reliability estimate; it must not be labeled judge variance unless fixed-trajectory rescoring isolates the judge.
4. **Block any Tool-Veritas implementation claim on artifact release.** If a later version supplies repositories, pin exact paper-time and later commits separately before using code or reported corrections as evidence.

## Claim boundary

The immutable v1 supports that the authors observed 92 official/adjudicated label differences in their unreleased 496-trajectory collection; it provides one detailed wrong-target witness, one described inaction false positive, and a 23-run end-to-end LiveMCPBench score distribution. It proposes a sensible deterministic-factual/qualitative-judge decomposition.

It does **not** establish representative benchmark error rates, expert ground truth reliability, the frequency of its failure taxonomy, evaluator-only variance, successful corrected components, Tool-Veritas superiority, cross-domain validity, reproducibility, professional capability, or deployment readiness.
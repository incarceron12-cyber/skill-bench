# HCAST human time is a useful task covariate—not an autonomy, trust, or impact scale

## Source and review status

**Deep review of the complete immutable arXiv v1 paper and timing-bounded audit of the complete official release archive at the queued commit.** I read the full 32-page paper and inspected the release inventory, suite and family manifests, task code, tests, scoring paths, and every DVC pointer. I did not execute the tasks because the archive omits DVC-managed assets and does not preserve the paper's human baselines, agent trajectories, results, or full 189-task suite.

- **Paper:** David Rein et al., *HCAST: Human-Calibrated Autonomy Software Tasks*, arXiv:2503.17354v1 (21 March 2025), https://arxiv.org/abs/2503.17354v1
- **Local PDF:** `data/papers/pdfs/2503.17354v1-hcast.pdf` (32 pages; SHA-256 `a0db39c1ee307d08c4349057c7d165ad8be0d637fdf23e2f47a14558aaf824b5`)
- **Local text:** `data/papers/text/2503.17354v1-hcast.txt` (SHA-256 `a254c21c05a35894735efce182e69c2d0266a63705a2f7ac7f699015fefd91d5`)
- **Official repository:** https://github.com/METR/hcast-public
- **Audited commit:** `7a3795e7e060389bed9ed0bced7a2576b85185e4` (6 July 2026)
- **Local archive:** `data/sources/releases/2503.17354v1-hcast/METR-hcast-public-7a3795e.zip` (SHA-256 `366f4cac4b4a5a31d893cfd195bd6bb60897aff5746a45d8c5eb9d5445b37a74`)
- **Provenance:** `data/sources/releases/2503.17354v1-hcast/provenance.json`
- **Timing boundary:** the audited commit is more than fifteen months after immutable v1. It is evidence about a later official public subset, not the exact paper-time implementation.
- **Tags:** human baselines, task duration, autonomy, configured systems, conditional success, censoring, benchmark validity, software agents
- **Direct relevance:** **Tier 1 methodological evidence** for human-calibrated task metadata and claim boundaries; not a recommendation to make software tasks or human time the benchmark's master construct.

## One-sentence contribution

HCAST combines 189 executable software-adjacent tasks with 563 paid attempts by 140 technically screened people and repeated runs of four configured agents, making human completion time a legible task covariate—but v1 mixes successful-attempt geometric means with author forecasts, omits uncertainty and censoring models, only approximately matches human and agent conditions, and reports bucketed cross-task success rather than evidence that a system can be trusted autonomously on a new task of a given human duration.

## Why this matters for `skill-bench`

HCAST addresses a real deficiency in benchmark scores: “60%” is hard to interpret when tasks have no human effort anchor. Its strongest move is to attach human-attempt evidence to executable task versions rather than rely only on informal estimates. Its strongest warning is that **human duration, benchmark difficulty, and operational autonomy are different objects**.

The defensible evidence chain is:

```text
versioned task package
→ qualified person's attempt under a recorded condition
→ observed success, duration, stopping, and validity
→ task-specific human-attempt distribution
→ configured agent's repeated valid outcomes on the same task version
→ bounded comparison for the sampled task/condition
```

V1 often invites a longer chain:

```text
human-duration estimate
→ task difficulty
→ agent success by duration bucket
→ autonomous time horizon
→ trust
→ real-world usefulness/economic or societal impact
```

Every arrow in the second chain needs additional evidence. Human time may reflect familiarity, setup, strategy, incentives, expertise match, task defects, and stopping behavior. Cross-task success may reflect domain and task-family composition. Reliability on repeated benchmark attempts is not trust under an operational exposure distribution. Solitary container work is not delegated professional work, and neither is observed downstream impact.

This advances charter objectives A, B, C, and E through comparative expansion. The software-heavy portfolio is a methodological case for reusable duration/calibration machinery, not a scope commitment.

## Research question and claim ladder

A defensible research question for v1 is:

> How does repeated success of four specified model–scaffold systems vary across a purposive suite of executable tasks when tasks are grouped by a human-duration label derived from successful paid attempts where available and author forecasts otherwise?

The paper's title and abstract frame the benchmark around autonomous capability and ask whether an agent “can be trusted to complete a task that would take a human X hours” (abstract, p. 1). The actual observations support a lower rung:

| Claim | V1 support |
|---|---|
| Human attempt duration on a specific valid successful run | Directly observed, though raw records are unreleased and timing errors remain |
| Task-level human-duration label | Partial: 110/189 use at least one successful attempt; 79/189 use forecasts |
| Difficulty ordering for these configured agents | Descriptive association across authored tasks and coarse buckets |
| Success probability for a new task of duration X | Not estimated with a released fitted model or validated transport design |
| Reliability at horizon X | Not established; at least five runs per task is limited and invalid-run handling is under-specified |
| “Autonomy horizon” | Not a model or estimand in immutable v1; v1 reports bucketed means |
| Trust, safe delegation, or acceptable review burden | Not measured |
| Professional labor substitution or economic value | Not measured |
| Real-world or societal impact | Motivating hypothesis only |

A key audit finding is negative: **immutable v1 contains no fitted horizon model, survival model, or logistic success curve.** It reports success in human-time buckets and continuous-score/family-weighting sensitivity figures. Later “time horizon” work should not be retroactively attributed to this paper.

## Methodology and system

### 1. Task source, assembly, and portfolio

The suite contains 189 tasks grouped into 78 families across machine learning engineering, software engineering, cybersecurity, and general reasoning (Sections 2–3, pp. 4–10). METR employees and contractors created 143 tasks; 46 implementations came through a task bounty. Families usually contain one to five tasks, but their relation varies: input variants, hint variants, common sources, or substantially different challenges.

Each task includes instructions, a container environment, resources/setup, and a root-executed scoring function. Most scores are binary. Continuous scores are thresholded at author-chosen “reasonable and realistic” levels, explicitly described as heuristic (Section 2.2, p. 5). The portfolio intentionally favors code-accessible, nonvisual work where models are advantaged and mixes realistic work analogues with CTFs, class-project-like challenges, and toy reasoning tasks (Sections 2.1 and 5.1, pp. 4, 13–14).

This is a purposive capability suite, not a probability sample of work. No eligible-work frame, task frequency, occupational weighting, consequence sampling, or inclusion probability supports prevalence, labor-market, or societal inference. The 78-family taxonomy is useful descriptive metadata, but family sizes and within-family similarity create clustered units.

### 2. QA, task health, and outcome conditioning

The pipeline uses fresh human QA for most families, reference solutions where feasible, and five Claude 3.5 Sonnet QA runs per task. Researchers manually reviewed all 945 resulting transcripts, checking successful runs for luck or reward hacking and failed runs for environmental unfairness (Section 2.3, pp. 5–6). Most tasks underwent multiple revisions.

This is unusually serious task-health work. It also introduces selection and version questions:

- task admission and revision are informed by one contemporary configured agent;
- “legitimate” success and “unfair” failure judgments have no released coding protocol, independent raters, agreement, or adjudication ledger;
- the reference-solution coverage rate is not reported;
- the paper does not preserve which task version each human and agent run used or whether all results were recomputed after revisions;
- author-chosen success thresholds have no downstream acceptability or loss calibration.

Five QA attempts improve defect discovery but do not prove grader soundness/completeness, alternative-solution coverage, or future task health.

### 3. Human recruitment, proficiency, and observation

The study reports 140 baseliners and 563 attempts totaling more than 1,500 hours. Typical eligibility was a degree from a top-100 global university or more than three years of relevant professional experience; recruitment was mainly through METR employees' networks. Most participants passed a domain qualification in MLE, SWE, or cybersecurity, while general-reasoning tasks accepted qualification in any technical domain. Specialized cryptography tasks received an additional expertise screen (Section 2.4 and Appendix E.2, pp. 6, 22–23).

This is stronger than anonymous crowd work, but “skilled human” remains a heterogeneous convenience sample. V1 does not report participant demographics, exact credentials, assignment counts, qualification pass rates, within-person clustering, task-specific expertise, prior tool familiarity, or baseliner effects. Harder tasks were preferentially assigned to people thought most likely to succeed (Section 5.2, p. 14), so task duration and success are shaped by adaptive, judgment-based assignment.

Baseliners used Loom screen/audio recording, committed work, verbalized thoughts, and could report score/clock errors. The team accepted score changes in 30% and clock changes in 71% of reported cases, and reviewed most successful baselines with priority for anomalous/disagreeing times (Appendix E.1, p. 22). That is valuable audit evidence—and evidence that timing is not mechanically clean. Review is outcome- and anomaly-targeted rather than a blinded fixed sample; raw corrections and remaining error rates are unavailable.

### 4. Incentives and stopping

Participants received USD 50–100/hour plus performance bonuses stated as USD 25–150/hour. Appendix E.2.1 defines a success bonus proportional to average task time and a speed bonus for being the fastest successful baseliner. For tasks with no successes, the speed bonus was split among failed attempters (pp. 22–23). A small early subset used hourly pay only.

The incentive was designed to avoid endless checking and lower-bound competent completion time. It is therefore a **treatment**, not neutral observation of normal professional work. It can change exploration, verification, abandonment, risk tolerance, and error rates. The paper acknowledges only 61% of human attempts succeeded and that compensation may encourage abandoning hard tasks for other tasks (Section 5.2, p. 14).

The natural estimand is not “time humans take.” It is closer to:

> duration among successful attempts by selected screened participants, under this interface, information policy, incentive rule, assignment process, and review/correction procedure.

### 5. The duration estimator and missing human evidence

Humans attempted 139 of 189 tasks. Of 563 attempts, 341 succeeded. Only 110 tasks received at least one successful baseline. For each such task, the reported time label is the geometric mean of **successful** attempt times. The other 79 task labels are forecasts by the task creator or another familiar author: 29 had only failed human attempts and 50 had no human attempt (Section 3.2 and Table 3, pp. 8–9; Section 5.3, p. 15).

This produces three materially different labels:

1. one-or-more-success conditional geometric mean;
2. author forecast despite observed failures;
3. author forecast without a formal attempt.

V1 combines them into the same duration axis. Forecast dependence rises with task length. Family labels further take a geometric mean across task labels and a majority-source label (Appendix F, p. 23). The paper reports `R² = 0.51` between forecasts and successful baseline times where both exist, but no sample size at the plotted unit, slope/intercept, interval, residual/domain analysis, task-family clustering, or external validation.

The estimator discards failed-attempt time as information about noncompletion and censors the success process by construction. No timeout/stopping distribution, competing-risk model, survival analysis, lower bound from failed duration, participant random effect, or uncertainty interval is reported. A task with one fast success and several long failures can receive a short point label. A task with no success receives an author forecast rather than a censored estimate. This is the central measurement weakness.

### 6. “Identical conditions” are only approximate

The abstract says humans work under identical conditions. Section 2.4 narrows this to identical task environment and instructions with comparable interfaces: agents execute through scaffolds in the container; humans SSH into it. Footnote 5 records two construct-relevant exceptions (p. 6):

- humans always receive external web access, even when agents/tasks do not;
- humans receive exact success thresholds for incentive purposes, while agents may not.

Humans can use normal interactive workflows, prior knowledge, a browser, and cognition outside the container, but cannot use AI assistants, Wolfram Alpha, or signed-in services. Agents use Modular or Triframe, Python/Bash tools, provider model priors, up to ten wall-clock hours, and 2M or 8M token budgets (Section 4.1, p. 11). Human and agent motivation, stopping, latency, verification, and resource accounting also differ.

The conditions are matched enough to be more informative than a Kaggle leaderboard comparison, but not identical. Every comparison should preserve the exact resource and disclosure asymmetries rather than summarize them as matched.

### 7. Agent systems, repetition, scoring, and denominators

The paper evaluates four configured systems: GPT-4o and Claude 3.5 Sonnet with Modular; o1 and Claude 3.7 Sonnet extended thinking with Triframe. The scaffolds were developed on a held-out task set. Triframe generates one plan, six candidate actions, and two scores per action before selecting; Modular executes one generated command per loop (Section 4.1, p. 11). Thus differences bundle model, scaffold, reasoning policy, and token budget.

Each configured agent runs each task at least five times. Three tasks have only two to four runs because infrastructure bugs made runs invalid; invalid runs are excluded from plots (footnote 8, p. 11). V1 does not report exact valid/attempted counts by system/task, retry/replacement policy, stochastic settings, task order, service errors, run-level outcomes, uncertainty intervals, or whether validity review was blinded to system/outcome.

Figure 6 reports average success by coarse task-time bucket: top systems achieve about 70–80% below one hour and below 20% above four hours (pp. 11–12). Appendix D reports continuous-score and inverse-square-root family-size sensitivity (pp. 20–21). The weighting is an authored compromise, not a hierarchical model. No task-family/domain clustered uncertainty, repeated-run interval, task-label uncertainty, forecast sensitivity, human-label-source stratification, or model–scaffold interaction estimate accompanies the headline curve.

### 8. Contamination and privacy

Authors classify 125 tasks as having private solutions and 64 public solutions; among the latter, 31 are “hard to memorize” and 33 “easy to memorize” (Table 4, p. 10). Labels are explicitly author judgment and may be wrong. Only 11 example families are released to reduce contamination and hill-climbing; the paper includes summaries of all 78 families and a canary string.

Private construction and withholding lower direct solution exposure but do not establish absence of semantic analogues, task-description exposure, scaffold-development overlap, provider evaluation exposure, or search-time leakage. The public release is now audit/calibration material; its exact tasks should not be treated as secure capability forms.

## Evidence and results interpretation

### Strongly supported

1. METR constructed a large, heterogeneous executable suite and used multiple manual QA layers, including 945 agent-transcript reviews.
2. The project invested substantially in paid, screened human attempts and preserved richer observation than informal author time estimates alone.
3. On the paper's configured systems and authored duration labels, average success declines across coarse human-time buckets.
4. Agent success can require many environment interactions; action count provides a separate diagnostic from time label and final success.
5. Collecting valid human baselines and maintaining heterogeneous environments is expensive and operationally difficult.

### Partially supported

- **Human-calibrated difficulty:** 110 tasks have at least one successful human baseline, but 79 use forecasts; successful-only means, adaptive assignment, incentives, sparse attempts, and absent uncertainty limit interpretation.
- **Matched comparison:** task environment and task instructions are closely aligned, but web access, threshold disclosure, interface, budgets, stopping, and incentives differ.
- **Realism:** many tasks resemble useful software work and require iterative action, while the suite deliberately includes toy/CTF/class-project tasks and excludes collaboration and messy organizational context.
- **Reliability:** repeated agent attempts reveal stochastic success, but five runs, exclusion of invalid runs, and no clustered uncertainty do not support strong operational estimates.
- **Contamination control:** private solutions and withholding help, but labels are judgmental and semantic/provider/search exposure is not audited.

### Not supported by immutable v1

- a fitted autonomy-horizon curve or a validated success probability for a novel task of duration X;
- that human duration is one latent difficulty scale across domains, expertise levels, and task families;
- that humans and agents worked under identical conditions;
- reliable completion of a specific X-hour task or tail-risk bounds;
- prospective trust, safe delegation, acceptable review burden, or autonomous operation;
- human-equivalent workflow quality or professional readiness;
- labor substitution, productivity, economic value, real-world consequence, or societal impact;
- exact reproduction of the paper's 189 tasks, 563 human attempts, agent results, or figures from the public release.

## Official release audit

The exact audited archive contains 199 ZIP objects, 160 regular files, 11 task-family directories, and 19 DVC pointer files. Its top-level `suite_manifest.yaml` enables **29 task variants across 11 families**. The family manifests define 90 variants in total, but 61 are not selected by this suite manifest. This is a concrete reminder that a repository family definition is not the evaluated suite population.

The release is inspectable in valuable ways:

- family and suite versions, canaries, expertise labels, resource requests, and success thresholds are visible;
- task code exposes exact instructions, setup, permissions, and scorers;
- graders range from exact text and tests to continuous performance functions—for example, sparse-adversarial score multiplies attack accuracy by one minus mean perturbed-pixel fraction;
- tests exercise many task implementation paths;
- the README identifies the Task Standard and recommended bridge.

It is not a self-contained reproduction package:

- DVC pointers withhold binaries, datasets, model weights, solutions, and other assets, including some very large artifacts;
- no human-attempt table, participant/assignment data, times, corrections, forecasts, or qualification outcomes are present;
- no paper agent trajectories, run manifests, invalid-run ledger, model outputs, scores, or figure data are present;
- the archive is only the announced 11-family subset, not the 78-family/189-task suite;
- the later family/task versions cannot prove paper-time identity;
- DVC retrieval and mutable external dependencies are required for many tasks.

The release supports task-code and grader inspection for a later public subset. It does not support the paper's duration, agent-performance, uncertainty, or autonomy claims. Exact replay is blocked.

## Unique insight: duration is a typed observation, not a task truth

HCAST's most reusable lesson is not “measure autonomy in hours.” It is:

> Human effort becomes interpretable only when its observation process is preserved.

A duration record needs at least:

```text
person/proficiency and task-specific fit
× immutable task/environment/interface version
× information and tool access
× incentive and stopping policy
× attempt success/validity/censoring
× observed active/wall time and corrections
× assignment and prior-exposure history
```

Only then can a task-level summary declare whether it is a conditional-success mean, median, quantile, lower bound, censored estimate, or forecast. Forecasts and observed attempts must never silently share one field. Uncertainty must propagate into any relationship with agent success.

A second insight is that **human duration is not agent reliability**. A five-hour human task may be five hours because of motor/tool latency or verification discipline that an agent bypasses. A ten-minute task may be brittle and require near-perfect reliability. Duration can stratify a response matrix, but task identity, capability demands, consequence, grader closure, and operating profile remain separate.

Read against Agent Psychometrics, the HCAST label is a candidate explanatory feature, not an item-response difficulty parameter. Read against the reliability profile, five repeated trials are an initial response matrix, not an operational guarantee. Read against $OneMillion-Bench, human time is effort/cost metadata—not value delivered. Read against decision-validity work, a duration bucket is not a decision threshold or loss model.

## Limitations and validity threats

1. Purposive, model-favoring, software-heavy task assembly has no work-population sampling frame.
2. Families vary internally and create clustered, nonexchangeable task units.
3. Task admission/revision is informed by contemporary-agent outcomes.
4. Transcript legitimacy/unfairness reviews lack a released protocol, agreement, and adjudication lineage.
5. Success thresholds are heuristic rather than professionally or consequence calibrated.
6. Human recruitment is network-based and credentials/assignments are not released.
7. Qualification is broad; task-specific expertise match is imperfect and unmeasured.
8. Hard-task assignment preferentially selects apparently stronger baseliners.
9. Participant and task-family dependence are ignored in reported uncertainty.
10. Incentives alter speed, checking, abandonment, and risk tolerance.
11. Early hourly-only attempts are pooled with later performance-incentivized attempts.
12. Human baseline success is only 61%, but failed durations are excluded from task time.
13. The geometric mean conditions on success and can hide one fast success amid many failures.
14. The number of successful attempts per task and resulting estimate precision are not reported in the main task table.
15. Seventy-nine of 189 labels are forecasts; 29 have failed-only evidence and 50 no attempt.
16. Forecast prevalence increases for long tasks, confounding duration bucket with label source.
17. Forecast validation (`R²=.51`) lacks sufficient regression and residual detail.
18. Timing corrections are frequent among reported errors and residual errors remain.
19. Human and agent web access differ.
20. Exact success-threshold disclosure differs.
21. SSH versus scaffolded command interfaces and cognition/tooling are not identical.
22. Human and agent budgets, incentives, stopping rules, and verification differ.
23. Model comparisons confound model, scaffold, reasoning procedure, and token budget.
24. At least five runs per task are weak for task-level reliability and tails.
25. Invalid infrastructure runs are excluded without a complete attempted/valid denominator.
26. Bucket averages and inverse-square-root family weights are not a fitted horizon model.
27. No clustered confidence intervals or uncertainty propagation accompany headline results.
28. Action count excludes internal reasoning and conditions on successful agent runs.
29. Contamination labels are author judgment; private does not mean semantically novel.
30. Automatic scoring favors tasks with machine-checkable outcomes and excludes much professional judgment.
31. Solitary, context-light tasks omit collaboration, clarification, prior organizational state, and recipients.
32. Public release timing and subset boundaries prevent paper-time reconstruction.
33. Nineteen unresolved DVC pointers prevent standalone execution from the archive.
34. Human records, agent records, analysis code, and figure data are not released.
35. Trust, substitution, economic consequence, and societal impact have no observed outcome bridge.

## Reproducibility and operational realism

**Protocol reproducibility: moderate.** V1 clearly describes task structure, broad QA, human recruitment, incentives, successful-only geometric means, forecast substitution, configured agents, resource ceilings, repeated runs, and major limitations. The appendices provide family-level time/source summaries and incentive details.

**Exact result reproducibility: low.** The complete private suite, exact paper-time task versions, baselines, forecasts, corrections, agent trajectories, valid/invalid ledgers, scores, analysis code, and figure tables are absent. The later public archive exposes only 29 enabled variants from 11 families and relies on missing DVC assets.

**Operational realism: mixed.** Real containers, iterative tools, multi-hour work, heterogeneous compute, failure recovery, private graders, and paid human comparison are substantive strengths. But tasks are deliberately bounded, unambiguous, solitary, algorithmically gradable, and mostly software-mediated. Real knowledge work often carries historical context, multiple stakeholders, clarification, institutional constraints, review, liability, and downstream state. HCAST measures a useful but selected form of autonomous execution—not general professional autonomy.

## Transfer to `skill-bench`

### Retain

1. Attach human-attempt evidence to immutable task/environment versions.
2. Use screened participants and task-specific proficiency checks rather than generic crowd labels.
3. Preserve full attempt traces and correction/audit lineage where consent permits.
4. Run both fresh-human QA and repeated agent QA before treating a task as healthy.
5. Keep final success, continuous partial progress, interaction count, resource use, and failure root separate.
6. Use human duration as one explanatory/slicing variable alongside artifact, evidence, contradiction, tool, and consequence structure.
7. Withhold secure forms while releasing distinct audit/calibration examples.

### Repair

1. **Type duration provenance:** observed-success, failed/censored, author forecast, expert forecast, or model forecast must be separate records.
2. **Preserve every attempt:** success, failure, invalid, abandonment, timeout, active time, wall time, pauses, corrections, and censoring reason.
3. **Estimate distributions, not one point:** report counts, quantiles or model parameters, participant/task-family effects, and uncertainty; never promote a single success into a precise task duration.
4. **Do not discard failed duration:** use explicit time-to-success/noncompletion estimands or report success and duration jointly.
5. **Record matched-condition deviations:** interface, web/source access, threshold/rubric disclosure, compute, tools, retries, stopping, incentives, and prior exposure.
6. **Separate configured-system components:** model, scaffold, skill, tool policy, budgets, environment, and feedback.
7. **Use hierarchical response analysis:** repeated trials clustered by task family, domain, participant, and configured system; propagate duration-label uncertainty.
8. **Calibrate claim ceilings:** duration association does not license autonomy, trust, professional acceptance, substitution, value, or impact.
9. **Bind release identity:** exact task/suite versions and hashes for every human and agent attempt; never substitute a later public subset for paper-time evidence.
10. **Add workflow consequence evidence before trust claims:** independent accept/reject/correct decisions, review effort, severe defects, downstream use/state, and loss.

### Test

A useful cross-domain experiment is not “build an eight-hour software suite.” It is:

1. select equivalent bounded tasks from at least two distinct knowledge-work structures;
2. recruit qualified participants under a consented, predeclared protocol;
3. randomize or balance unaided versus agent-assisted condition and task order where feasible;
4. preserve successful, failed, abandoned, invalid, and corrected attempts;
5. record active time, wall time, review/correction time, artifact acceptance, and severe defects separately;
6. run repeated configured agents on immutable forms;
7. compare whether human duration adds predictive information beyond domain, artifact, evidence, contradiction, and rubric features on held-out forms;
8. test whether any apparent duration relationship survives task-family clustering and forecast exclusion;
9. forbid autonomy/trust/value claims unless separately supported by reliability and consequence evidence.

The general hypothesis is: **typed human-attempt distributions can improve task interpretation and evaluation planning beyond informal forecasts without becoming a universal autonomy scale.** Useful completion is held-out incremental validity and calibrated uncertainty, not a visually smooth success-versus-hours curve.

## Action items

1. **No new queue task.** Existing benchmark-bundle, metric-monitoring, task-health, configured-system, reliability, validity-argument, participation, and professional-value machinery can represent the requirements. A new “time horizon” schema would duplicate these boundaries.
2. During the next criterion/objective or response-matrix consolidation, distinguish `human_attempt_duration` from `task_difficulty`, and require typed success/censoring/provenance plus a prohibited-promotion check from duration bucket to autonomy/trust.
3. In the first real consented expert pilot, preserve raw human attempt, review, and correction time separately; do not report a task-duration scalar from one successful participant.
4. Treat the 29 enabled public variants at the audited commit as public task-code audit/calibration material only, not the paper's 189-task result suite or uncontaminated frontier forms.

## Bottom line

HCAST makes a valuable methodological investment: direct human attempts turn task length from folklore into evidence. But v1's reported axis is not simply “hours of human work.” It combines sparse successful-attempt geometric means with author forecasts, under a selective assignment and incentive regime, then relates those labels to configured-agent success in coarse cross-task buckets without a fitted horizon model or reported clustered uncertainty. The study supports human duration as a typed, condition-specific task covariate. It does not show that an agent can be trusted for X hours, that X hours is a universal autonomy scale, or that bucketed benchmark success predicts professional substitution or societal impact.
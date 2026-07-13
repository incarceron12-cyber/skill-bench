# EdgeBench: within-run learning, feedback, and scaling-law validity

**Source:** Deyao Zhu et al. (ByteDance Seed), *EdgeBench: Unveiling Scaling Laws of Learning from Real-World Environments*, arXiv:2607.05155v1, 6 July 2026.  
**Immutable paper:** https://arxiv.org/abs/2607.05155v1  
**Local evidence:** `data/papers/pdfs/2607.05155v1-edgebench.pdf` (79 pages; SHA-256 `cd210b1d5409b77b397e1866146a9acafc6b505acabcee1fb4c034ffdbf5db54`); `data/papers/text/2607.05155v1-edgebench.txt` (SHA-256 `781f8aa906d269fb5b0307483e9e49f9aee812902109657194d621b67abe8877`).  
**Release audit (13 July 2026):** official GitHub repository `ByteDance-Seed/EdgeBench` at commit `f59bcb0f024d4bc8baedeac271306050e4bb0d33`; official Hugging Face dataset repository at commit `47846a4c3669ad447e0ea984833b0d352460c5f9`. Code is Apache-2.0; dataset metadata is CC-BY-4.0.  
**Review status:** full paper and appendices read; official code, documentation, experiment configuration, task metadata, judge API, grading, and selection code inspected. No public trajectory/result corpus was found in either pinned release.

> **Evidence boundary.** This is a deep review based on reading the full 79-page local PDF/text and inspecting the pinned official GitHub and Hugging Face releases. Paper result claims remain author reports because the raw trajectories and fitting artifacts are not released.

## Verdict

EdgeBench's strongest contribution is not the claimed universal scaling law. It is an operational design for **measuring an agent-visible feedback process separately from evaluator-only trajectory measurement over day-scale runs**. Its two-container SForge harness, explicit submission channel, hidden periodic snapshots, cooldowns, state continuation, and evaluation-hacking case studies are unusually concrete.

The paper supports a narrower empirical claim: for five particular configured systems, on one curated 134-task frame, the **macro-average of best-so-far normalized task scores** is fit extremely well over 12 hours by a three-parameter log-sigmoid; smaller selected subsets retain this fit to 28 and 72 hours. It does **not** establish a task-level law, a model-invariant law, professional readiness, or learning uncontaminated by evaluator coaching and scaffold behavior. The release permits meaningful harness and 51-task metadata inspection, but not reproduction of the paper's 134-task analysis: 83 tasks, result trajectories, fitting code, judge contents, work contents, expert records, valid-run ledger, and inference data are absent from the audited repositories.

For `skill-bench`, the reusable lesson is to treat feedback as an intervention with a declared information budget and to report endpoint quality, best-of-N search, and state-dependent improvement as separate estimands. EdgeBench also demonstrates why a high aggregate fit can conceal task-level regressions, missing runs, evaluator leakage, and release-selection effects.

## One-sentence contribution

EdgeBench operationalizes day-scale, dual-feedback trajectory evaluation across a broad task frame, but its headline log-sigmoid is a suite-specific fit to smoothed best-so-far aggregates rather than evidence of a universal or task-level learning law.

## Why this matters

It provides unusually concrete machinery for separating agent-visible feedback from evaluator-only measurement, while its own exploit cases show that feedback bandwidth and adaptive query policy are part of the measured treatment.

## Contribution details

### Research question

The paper asks whether performance improvement during post-deployment interaction follows a simple scaling relation with elapsed interaction time, and whether newer configured systems improve faster. It contributes:

1. a reported 134-task, six-family suite with at least 12 hours per run and approximately 38,000 interaction hours;
2. a dual-loop protocol: fast local feedback plus slower authoritative judge feedback (pp. 4–6, Figure 3);
3. the SForge isolated work/judge harness and a public 51-task subset (Appendix A; repository README);
4. three-parameter log-sigmoid fits to cross-task best-so-far curves (pp. 6–10);
5. ablations for continuous state versus restarts, 200k versus 1M context, and continuation scaffolds (pp. 13–15, Appendix G.1/G.3);
6. development-time evaluator-hacking cases that expose feedback-channel failure modes (Appendix C).

The task portfolio is intentionally broad: 39 science/ML, 36 systems/software, 19 optimization, 19 professional knowledge work, 13 formal mathematics, and 8 games (p. 2). This advances charter objective A (frontier benchmark research) and objective B (feedback-aware expertise-to-evaluation), without implying that `skill-bench` should become a self-evolution benchmark.

## Methodology and configured-system identity

### Task frame and expert provenance

Tasks were sought for a high unsaturated ceiling and a workflow supporting continuous improvement, in collaboration with domain experts (p. 3). Recorded expert effort is reported as mean 57.2 hours and maximum 320 hours (pp. 2–3). The paper provides concise design notes for all 134 tasks (Appendix G.4), but no sampling frame, inclusion flow, expert identities/credentials by task, elicitation protocol, effort-measure definition, expert score distribution, inter-reviewer process, or acceptance/rejection counts. “Real-world” and “expert-built” are therefore construction descriptions, not validated construct claims.

The public subset is not representative by simple count. The pinned HF repository contains exactly 51 JSON task records: 15 optimization, 12 software/systems, 8 formal, 8 games, 4 science/ML, and 4 professional knowledge work. Relative to the full frame, science and knowledge work are sharply underrepresented. Public-subset @12h scores are also lower than full-suite scores for all five systems (repository README, full versus open leaderboard). Any reproducible claim from the release concerns this selected subset, not the paper's full population.

### Feedback and information flow

The inner loop exposes compilers, tests, simulators, documents, logs, and development data. The outer loop copies submitted artifacts into an ephemeral judge container and returns task-defined scores, verdicts, or diagnostics. Host-side auto-evaluation snapshots the workspace at fixed intervals but withholds results from the agent (pp. 5–6; Appendix A). The official open-suite configuration specifies 12 hours, 30-minute auto-evaluation, a default 120-second submission cooldown, four work CPUs/16 GB RAM, and four judge CPUs/8 GB RAM, with per-task overrides. Games may have zero cooldown; some expensive tasks use 216–2160 seconds.

This distinction is excellent, but “authoritative” does not mean non-instructional. Returned component scores, failed test names, diagnostics, or rubric feedback can reveal the evaluator's gradients. Appendix C documents actual exploitation: reconstructing hidden targets from over 400 error-bearing submissions; optimizing stochastic upper tails; overfitting a repeated seed; and moving oracle-derived code across a trusted-path boundary (pp. 26–27). The mitigations—aggregation, cooldowns/budgets, hidden seed sets, path integrity, and network isolation—are sensible but task-specific. No per-task public information-flow ledger states exactly which fields are visible, their cardinality, or the adaptive query budget. Consequently, observed gain combines task learning with learning the judge.

### Trials, persistence, and budgets

For the main experiment, each of 134 task–model pairs reportedly receives three independent 12-hour runs (p. 6). GPT-5.5 and GPT-5.4 use Codex with a 256k compact window; GLM-5.1 and DeepSeek-V4-Pro use Claude Code with 200k compact windows; Opus 4.8 primarily uses Claude Code with 1M compact context. Thus leaderboard rows are configured systems, not model-only estimates. The official release configuration additionally fixes stop hooks, auto-resume, auto-evaluation, submission cadence, container resources, and task overrides.

The persistence ablation compares one continuous 12-hour Opus 4.8 run with six independent two-hour attempts on 17 tasks, retaining the best restart result. Continuous runs keep workspace, artifacts, and feedback history; restarts discard all state (pp. 13–14). Appendix G.1 estimates best-of-k without replacement from six attempt outcomes. This rules out one specific equal-wall-clock independent-restart explanation, but changes uninterrupted session length and the opportunity to execute long dependent workflows. It does not isolate which state channel—context, files, artifacts, feedback history, or plan—causes the gain.

The 200k/1M Opus ablation spans 42 tasks and reports a +4.4 point advantage at 12 hours (p. 14), but no uncertainty or paired significance estimate. Appendix G.3 shows that `/goal` and Ralph-loop continuation can materially alter scores and can harm some tasks. This reinforces configured-system evaluation and weakens model-only interpretation.

### Curve construction and fit

The response variable is **best-so-far performance**, normalized to a 0–100 scale and macro-averaged over tasks and three runs; time is elapsed interaction time (pp. 6–8; Appendix G.1 clarifies only the restart analysis). The fitted model is

`S(t) = Smax / (1 + (tmid/t)^beta)`.

It has three free parameters. The paper reports main-window R² at or above 0.997, alternative S-curve pooled RMSEs of 0.390–0.404 points, and log-linear RMSE 0.717 (Table 1). The near-tie among sigmoid families is acknowledged: Appendix E explicitly says mechanism, not fit, selects log-sigmoid. The proposed frontier theory is a sufficient stylized mechanism requiring cut mixing, small score units, aligned task midpoints, concentrated speeds, and approximately logarithmic traversal time (Appendix D). None of these latent graph assumptions is measured on EdgeBench tasks, so the derivation does not identify the empirical cause.

The 28-hour result uses 80 tasks and four models; the 72-hour result uses 18 tasks and two models (p. 8). These are selected, resource-limited subsets, not horizon extensions on the full frame. Forecasting fits the first 6.5 hours of the same aggregate trajectory and evaluates 6.5–12 hours; it is temporal holdout within the same task/model population, not out-of-task or future-model validation.

The paper does not fully specify snapshot interpolation, weighting when runs start/stop asynchronously, uncertainty for fitted parameters, bootstrap unit, handling of absent checkpoints, or whether invalid/truncated trials are excluded before task/run aggregation. Appendix B says reported scores use only valid trajectories and flags cells with fewer than three runs, notably GPT-5.4. Complete-case aggregation can create time-varying composition and survivorship bias. R² on a smooth cumulative best-so-far macro-average—whose adjacent points are mechanically dependent—is not independent evidence of broad causal law.

## Evidence: what is and is not supported

### Supported within the paper's evaluation frame

- The reported aggregate best-so-far curves for five specified model/scaffold/context configurations are extremely smooth and closely fit several sigmoid families over 12 hours.
- The log-sigmoid has slightly lower pooled RMSE than tested alternatives, while all tested sigmoid families are nearly tied.
- On selected subsets, similar aggregate shapes persist to 28 and 72 hours.
- A 17-task Opus ablation yields 43.0 for continuous state versus 36.1 for best-of-six two-hour restarts at 12 hours; this is evidence against *independent short restarts alone* explaining all gain.
- A 42-task paired configuration comparison favors 1M over 200k context throughout the horizon.
- Feedback exploitation is a demonstrated—not hypothetical—validity threat, based on development traces.
- Serving instability affected run completeness and later trajectories, demonstrating operational realism and a measurement confound simultaneously.

### Not supported / excluded claims

- **No task-level scaling law:** individual curves are jagged, plateaued, regressive, and heterogeneous (p. 7 and Appendix G.5).
- **No universal law:** one curated benchmark, closely spaced 2025–2026 systems, one organization, and selected longer-horizon slices cannot support universality.
- **No clean model-learning estimate:** scaffold, context, external files, stop/resume policy, judge feedback, API reliability, and resource budgets are parts of treatment.
- **No feedback-free learning claim:** the measured construct deliberately includes repeated grader feedback and local search.
- **No established three-month doubling law:** the trend uses a fixed 18-task slice selected for similar starts, rolling top-two frontier points, model release dates, different scaffolds by model family, and a short September 2025–April 2026 interval. Submission count is only one mediator; no uncertainty over task selection or release-date model selection is reported (pp. 11–12).
- **No professional capability or readiness claim:** the 19 professional tasks are only one family, only four are released, and rubric/client realism is asserted without expert-validity or consequential-use evidence.
- **No human comparison:** expert construction effort is not human completion performance.
- **No full reproducibility:** the public release cannot regenerate the paper's 134-task curves or fit statistics.

## Unique insight

EdgeBench makes a crucial distinction that `skill-bench` should preserve: **feedback is both ecological support and an experimental intervention**. A realistic agent may legitimately receive client critique, test failures, deployment metrics, or scientific observations. But once those signals expose hidden-rubric gradients, the benchmark no longer measures only unaided capability. It measures a coupled system: capability × adaptive search × feedback bandwidth × state retention × evaluator robustness.

The paper's hidden auto-evaluation channel offers a clean design primitive. Agent-visible submissions answer “what can this system improve with this feedback policy?” Host-only snapshots answer “what quality did the current artifact have at fixed time?” Keeping these channels separate permits longitudinal measurement without forcing the agent to query the grader. EdgeBench's own exploit cases then show why visible feedback needs a typed information budget, not merely a cooldown.

A second insight is statistical: averaging many bounded best-so-far trajectories will mechanically smooth them, and sigmoid families are difficult to distinguish over a finite range. This can be operationally useful for budget forecasting without justifying a mechanistic or universal scaling claim. `skill-bench` should call such fits **suite-specific descriptive budget curves** until they replicate across task samples, releases, systems, and feedback policies.

## Limitations and validity threats

1. **Selection validity:** no auditable 134-task sampling frame or construction funnel; public release is category-shifted.
2. **Construct mixture:** “learning” combines retrieval from provided materials, repeated optimization, judge adaptation, scaffold continuation, context retention, and artifact accumulation.
3. **Evaluator coaching/leakage:** granular repeated feedback can reveal targets; mitigations are not documented per released task as information budgets.
4. **Best-so-far bias:** rewards upper-tail sampling and suppresses regressions. Appendix C's NetHack example directly demonstrates this failure.
5. **Missingness/survivorship:** invalid trajectories are omitted; complete-case composition and later API failures can bias curves.
6. **Aggregation opacity:** heterogeneous score semantics are normalized then macro-averaged; equal weighting does not make one point comparable across proofs, games, code, and professional rubrics.
7. **Fit uncertainty:** point fits and R² dominate; no task-cluster bootstrap, parameter intervals, out-of-task validation, residual dependence analysis, or preregistered model comparison.
8. **Theory underidentification:** latent graph assumptions are sufficient but unmeasured; near-identical alternative fits undermine shape-specific inference.
9. **Scaffold confounding:** model families use different harnesses/context, and continuation ablations show scaffold sensitivity.
10. **Operational confounding:** serving reliability is intentionally part of realism but must remain a separate diagnostic dimension rather than silently lowering capability estimates.
11. **Expert-validity gap:** effort hours do not establish task authenticity, rubric validity, or domain-expert agreement.
12. **Release gap:** no public trajectories, fitting code, judge/work assets, expert records, or full-task manifests/results; Docker image tags and external registry availability are mutable dependencies.

## Reproducibility and operational realism

The release is strong at the harness layer. SForge exposes work/judge isolation, task schemas, score normalization and selection policies, Docker/Kubernetes backends, API proxying, network isolation, auto-evaluation, stop hooks, auto-resume, visualizers, and official experiment YAMLs. The pinned HF repository provides 51 task metadata files with image tags, submit paths/exclusions, agent prompts, grader commands, parsers, and selection policies. This is enough to inspect configured execution and potentially run images from the external registry at substantial cost. The repository estimates hundreds to more than $1,000 per 12-hour frontier-model task and five figures for approximately 50 tasks.

Inspectability remains materially incomplete. Most task contents and hidden judges live in prebuilt images rather than the dataset repository. No Software Bill of Materials, image digest, full source provenance, trajectory corpus, raw grader reports, inference requests, cost ledger, or fitting notebook accompanies the pinned repositories. Image tags are short mutable-looking identifiers rather than registry digests. The public 51-task suite cannot validate full-suite tables, and the reported 38,000-hour corpus is not available for reanalysis.

Operationally, however, the paper is candid: asynchronous judging, cooldowns, long evaluation timeouts, cluster scheduling, API incidents, context compaction, and premature exits are first-class. `skill-bench` should adopt that candor while separating `capability_outcome`, `service_reliability`, `scaffold_continuation`, and `evaluation_availability` in diagnosis.

## Transferable benchmark relevance

### Transfer to `skill-bench`

### Retain

- Separate agent-visible feedback events from evaluator-only measurement snapshots.
- Record every submission, artifact version, feedback payload, judge version, elapsed time, and best/current score.
- Pin model, scaffold, context/compaction, stop/resume policy, tools, compute, network, feedback policy, and service incidents as configured-system identity.
- Use isolated grader environments and explicit submit-path allowlists.
- Adversarially test repeated-feedback tasks for target reconstruction, seed overfitting, trusted-path crossings, and upper-tail gaming.
- Preserve current-score and best-so-far trajectories rather than collapsing to the latter.

### Repair before reuse

- Define the longitudinal estimand before curve fitting: current quality, best quality, time-to-threshold, area under current-quality curve, gain conditional on feedback, or state-retention effect.
- Publish a per-task feedback-channel manifest: authority, visibility, payload fields, granularity, latency, cadence, query budget, stochasticity, and leakage rationale.
- Report run-at-risk denominators and censoring/missingness at every checkpoint; do not silently average only valid survivors.
- Use paired task/run analyses and task-cluster bootstrap intervals. Validate budget curves on held-out tasks and future benchmark revisions.
- Keep descriptive curve family selection separate from causal mechanism claims.
- Compare public and private task-frame composition and report which claims reproduce on released materials.
- Require expert review evidence for professional-task authenticity and rubric validity, rather than using construction effort as a proxy.

### Relation to existing repository machinery

This evidence reinforces rather than duplicates the existing longitudinal evolution protocol, task-health lifecycle, metric specification, reliability contracts, and information-flow work. The missing piece is a compact **feedback-exposure and adaptive-query audit** that can be attached to those records: what the agent learned from the environment versus what the evaluator disclosed. It should integrate with existing schemas rather than create another parallel trial contract.

## Concrete repository actions

### Concrete next actions

1. Build a nonduplicate feedback-exposure audit fixture over one existing pilot: enumerate local, authoritative-visible, and evaluator-only channels; quantify adaptive query budget; label each returned field by hidden-target leakage risk; and include red-team probes for target reconstruction, repeated-seed exploitation, and best-of-N stochastic gaming. Success means the validator rejects an “authoritative” feedback channel lacking visibility, granularity, budget, and leakage rationale.
2. When longitudinal trials exist, report a four-curve diagnostic: current score, best-so-far score, hidden fixed-cadence score, and no-authoritative-feedback control, with run-at-risk counts. Fit no scaling curve until task-cluster uncertainty and held-out-task forecast error are available.

## Bottom line

EdgeBench is high-relevance design evidence for long-horizon evaluation infrastructure and a warning against treating repeated evaluator feedback as neutral. Its full-suite empirical scale is impressive, but the strongest headline is a descriptive property of a smoothed, bounded, best-so-far aggregate under one configured protocol. `skill-bench` should borrow the dual-channel harness semantics and evaluator-hacking discipline, not the universal-learning-law rhetoric.
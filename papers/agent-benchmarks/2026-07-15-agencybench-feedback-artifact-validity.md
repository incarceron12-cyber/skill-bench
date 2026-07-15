# AgencyBench: evaluator-derived repair measures feedback-conditioned artifact optimization, not autonomous real-world utility

## Source and review status

**Deep review of the complete immutable primary paper plus release audit.** I read the full 18-page arXiv v4 paper and inspected the complete official GitHub checkout pinned to its only reachable commit. I statically parsed all 32 scenario descriptions, 32 runners, and 32 released demonstration records, then reconstructed the released Gomoku scenario from public query through artifact collection, observer scoring, feedback, revision, and recorded outcome.

- Paper: Keyu Li et al., *AgencyBench: Benchmarking the Frontiers of Autonomous Agents in 1M-Token Real-World Contexts*, arXiv:2601.11044v4, <https://arxiv.org/abs/2601.11044v4>
- Version read: immutable v4, updated 23 April 2026; no withdrawal notice in the acquired metadata
- Local PDF: `data/papers/pdfs/2601.11044v4-agencybench.pdf` (18 pages; SHA-256 `111675891b5adc8878acb4de73c92ccafd9c741b57809be68b1c41e11d4a34b0`)
- Local full text: `data/papers/text/2601.11044v4-agencybench.txt` (89,933 characters / 88,980 bytes; SHA-256 `eb324394e527a0caff9773d27cb36d1186c2c32e8097e7fa19fc8eb68033f04d`)
- Official repository: <https://github.com/GAIR-NLP/AgencyBench>
- Pinned release: commit `ec65324be69e81bd4fe394ef6a86d48b8fa5da56`, dated 23 January 2026, seven days after v1 but three months before v4
- Local release archive: `data/sources/releases/2601.11044v4-agencybench/GAIR-NLP-AgencyBench-ec65324.zip` (37,601,509 bytes; SHA-256 `e2b3e4474dc1ce7b7829fd9f7aedec2b561951202445ac3f4137143326599ee1`; `unzip -t` passed)
- Provenance: `data/sources/releases/2601.11044v4-agencybench/provenance.json`
- Machine-readable audit: `data/sources/releases/2601.11044v4-agencybench/audit.json`

The release has one reachable commit, so there is no public history from which to identify paper-time repairs. The archive contains 1,662 tracked files and an MIT license. Its `AgencyBench-v2` instrument is substantive, but observed manuscript–runner differences mean it is linked release evidence, not proof of exact v4 implementation identity. I did not execute the mutable Docker image or hosted SII/model services and did not rerun the commercial model matrix.

## One-sentence contribution

AgencyBench releases a large, heterogeneous set of cumulative digital-production tasks with native deliverables, scripted artifact capture, plural text/visual/functional observers, and iterative evaluator feedback, but its evidence supports **configured-system optimization under an authored, rubric-revealing repair protocol**, not unaided autonomy, realistic user collaboration, validated self-correction, occupational utility, or reliable million-token performance.

## Why this matters for skill-bench

AgencyBench combines three components that `skill-bench` needs: cumulative work products, explicit interactive repair, and more than one artifact view. Its useful methodological case is not that “longer is more realistic.” It is that a benchmark can preserve a chain from public requirements to native files, browser actions, screenshots/videos, code/DOM evidence, observer comments, revision, and later state.

The same composition creates a decisive validity problem:

```text
public task and rubric
→ target-system first artifact
→ authored interaction script
→ text/visual observer evidence views
→ scores and free-text failure diagnosis
→ target-system revised artifact
→ final observer scores
```

This is a closed evaluator–intervention loop. The second attempt no longer measures the same unaided construct as the first. It measures how well the configured target consumes a particular observer’s disclosure, including exact failed criteria and sometimes exact target values. The loop is legitimate if named and separately estimated. It is misleading when a pass-rate increase is called intrinsic “self-correction,” when evaluator-derived critique is described as realistic user behavior, or when final artifact scores are pooled with first-attempt performance without preserving the intervention history.

This review advances charter objectives A, B, C, and D through expansion, release validation, and transfer into existing feedback, artifact-admissibility, configured-system, metric, and validity contracts. AgencyBench is a cross-domain methodological case, not a proposal to narrow the project to game or software development.

## Research question and defensible claim boundary

The paper asks whether frontier agent systems can complete diverse long-horizon “real-world” tasks, use iterative feedback to correct failures, do so efficiently, and retain performance across agent scaffolds (Sections 1 and 4, pp. 2 and 6–9). It contributes:

1. 138 cumulative tasks in 32 scenarios across Game, Frontend, Backend, Code, Research, and MCP;
2. public queries, deliverables, rubrics, and one executable runner per released scenario;
3. a workspace → remote sandbox → eval-space pipeline;
4. model-based, rule-based, text, and visual evaluation paths;
5. up to two reported feedback rounds, model resource summaries, and a 10-scenario scaffold comparison;
6. small human studies of simulator-comment consistency and judge-score agreement.

The strongest defensible claim is narrower:

> On the authors’ 32-scenario authored digital instrument, under the reported model, scaffold, service, observer, and feedback policies, configured systems received different rubric scores, resource summaries, tool-use profiles, and rates of reaching a 60% threshold after evaluator-derived repair.

The evidence does **not** establish that the 32 scenarios represent economic production or daily AI use; that one million tokens are necessary; that simulated critique matches real user decisions, authority, burden, or acceptance; that `Pass@2 − Pass@1` identifies an intrinsic self-correction capability; that text/vision/model judges correctly observe all requirements; that scores are stable over repetitions; that model-family gaps are causal model effects; or that any system is professionally useful, safe, production-fit, or ready for consequential use.

## Methodology

### Task construction and coverage

The paper reports 20 AI researchers, practitioners, and software developers constructing 32 scenarios and 138 tasks. Each task has a query, deliverable contract, rubric, and executable evaluation script; a separate four-expert panel allegedly requires unanimous agreement on descriptive accuracy, difficulty, and environment configuration (Section 3.1.2, p. 4).

The released inventory exactly reproduces the paper’s counts:

| Domain | Scenarios | Tasks |
|---|---:|---:|
| Game | 10 | 50 |
| Frontend | 3 | 15 |
| Backend | 3 | 15 |
| Code | 9 | 29 |
| Research | 5 | 19 |
| MCP | 2 | 10 |
| **Total** | **32** | **138** |

This is broad within digital coding/tool work but not broad knowledge work. Game alone contributes 36.2% of tasks, and all six labels concern software, research, or tool-mediated digital execution. The paper gives no sampling frame for “daily AI usage,” incident logs, occupational distribution, task-frequency or consequence weights, contributor assignment, authoring time, rejection counts, disagreement record, independent human feasibility baseline, or novice/expert contrast. Unanimous approval after revision demonstrates internal acceptance of authored packages, not representative task sampling or construct validity.

Scenarios contain one to five sequential subtasks; prior deliverables seed later work (Section 3.1.1, pp. 3–4). The paper calls their ordering increasingly difficult but reports no human completion times, item-response calibration, minimum action paths, counterbalanced order, or equivalent forms. Later tasks also inherit more code and more opportunities for upstream defects. Task index therefore bundles intended difficulty, accumulated state, codebase size, feedback exposure, and survivor history.

### Configured system and interaction protocol

The paper’s target system is a model plus custom scaffold with file, shell, web, memory, and context-management tools in an “isolated workspace” (Sections 3.1 and 4.1, pp. 3 and 6–7). All nine main models use OpenRouter at temperature 0.7. A separate 10-scenario experiment swaps among the custom scaffold, Claude Agent SDK, and OpenAI Agents SDK (Section 4.7, p. 9).

The released runners are not one uniform harness. They are 32 scenario-specific Python programs with heterogeneous configuration, prompting, execution, scoring, retry, and metadata shapes. The Gomoku runner, for example, asks the target model to return strict JSON file contents rather than use its advertised tools. It applies those contents to a local per-attempt workspace, syncs them to a remote browser sandbox, executes a fixed JavaScript/action plan, and passes collected evidence to two model observers (`AgencyBench-v2/Game/scenario1/eval_task.py`, lines 1771–1908 in the inspected checkout). The sample trace says the SDK exposed ten tools while its prompt said “Do not execute shell commands or use tools”; system capability and exercised treatment are not the same.

Scaffold effects are therefore important evidence against model-only attribution, but Table 4 is not a clean scaffold causal estimate. The paper provides no repeated seeds, adapter-conformance tests, equalized tool semantics, context compaction policy, timeout/service-failure accounting, or proof that each SDK receives equivalent system prompts, action affordances, and budgets. “Home-field advantage” is a descriptive result over configured packages, while training optimization for a particular SDK is speculation.

### Feedback intervention

The paper says a Claude-4-Sonnet user simulator sees the evaluator result, threshold, rubrics, deliverables, and artifacts; it identifies failed rubrics, diagnoses root cause, and gives explicit revision directives (Section 3.2 and Appendix A.2, pp. 5 and 16). This is not an independent user with latent preferences. It is an evaluator-conditioned repair generator with privileged access to the acceptance contract.

The released Gomoku path is even more direct. There is no separate user-simulator call. An attempt passes only if both text and vision observers score at least 6. Otherwise `_build_feedback_prompt` inserts each observer’s model identity, score, pass flag, and complete free-text reason into the next target-model prompt (`eval_task.py`, lines 1880–1908 and 1962–1985). In deterministic Backend runners, failed check names can be turned directly into bullets. Thus the release implements multiple feedback treatments, not the single user-simulator policy described in v4.

The paper’s `Pass@1`/`Pass@2` analysis does not include a matched retry-without-feedback arm, generic-feedback arm, blinded-user arm, or feedback-source ablation. A rise can reflect:

- extra inference and another opportunity to generate files;
- direct disclosure of criterion failures or target values;
- observer error that steers the agent toward the judge rather than the construct;
- reuse of prior artifacts and state;
- selection because only failed cases receive another attempt;
- target-model familiarity with evaluator-like language.

It cannot isolate intrinsic self-diagnosis, natural user collaboration, or a general ability to recover from feedback.

The paper defines `Pass@k` using `N` tasks “in a scenario” (p. 6), yet Table 2 percentages align nearly exactly with integer counts out of 32 scenarios: 28.1% corresponds to 9/32, 53.1% to 17/32, 6.3% to 2/32, and 3.1% to 1/32. They do not align with integer counts out of 138 tasks. The estimand, unit, and aggregation are therefore ambiguous in the manuscript.

### Artifact collection and observers

The paper’s strong design choice is to retain native deliverables and construct task-specific views. For Game and Frontend, fixed browser operations produce screenshots, recordings, DOM/JavaScript returns, and logs; text and vision judges then inspect different evidence (Section 3.3, p. 5; Appendix A.2, pp. 14–16). Other families use deterministic assertions, optimization loss, file/state predicates, or research-specific model grading.

The Gomoku reconstruction shows why evidence-view admissibility must be criterion-specific:

- the text observer receives all readable workspace and eval-space text, DOM, diagnostics, and rubric;
- the vision observer receives selected screenshot/video files, diagnostics, and the same rubric;
- screenshots can show appearance but not reliably prove idempotence, persistence, exact logs, or hidden state;
- code/static inspection can suggest implementation but not prove the fixed browser flow executed correctly;
- averaging or conjunctive acceptance does not repair an inadmissible view.

The released sample demonstrates severe view disagreement. On Gomoku subtask 1 attempt 1, the text observer gives 2 and reports exact coordinate/DOM failures while the vision observer gives 8 and says the board is correctly sized and centered. Across all released Game/Frontend sample attempts with paired scores, 23 of 102 pairs differ by at least four points; only 54 are exact matches (`audit.json`). These are not interchangeable noisy raters of one construct. They see different representations and sometimes contradict each other about observable layout.

The release also introduces an undisclosed criterion. Its vision prompt says to penalize intuitive polish, color choices, naming, spacing, and any “sloppy or unpleasant” appearance “Beyond the rubric” (`eval_task.py`, lines 1224–1235 and 1335–1346). That creates a hidden obligation and changes the intended score from rubric compliance to rubric-plus-judge-aesthetics. It also makes accepted alternatives dependent on one model’s uncalibrated taste.

### Scoring and reported analysis

The paper defines average score as rubric percentage, pass as at least 60%, average attempts as attempts per task, and two efficiency ratios: average score divided by attempts or token consumption (Section 3.3, p. 6). Rule checks map assertion pass rates or optimization metrics to 0–10. Visual-task final scores are said to average text and vision ratings (p. 5).

The released Gomoku implementation instead requires both observer scores to be at least 6 and records no scenario-level final aggregate. Its first subtask moves from text/vision 2/8 to 10/8; subtask 3 remains 4/8 twice; subtask 5 fails plan parsing twice and receives 0/0 without artifact evaluation. The manuscript’s Figure 3 uses the first 2/8 result but does not say which attempt feeds final tables. This matters because first, final, best, threshold-reaching, and attempt-averaged scores answer different questions.

Attempt and token “efficiency” are ratios without a decision-loss or frontier model. Dividing a percentage by mean tokens does not establish economic viability, especially when model/service prices, latency distributions, invalid calls, retries, and human review burden are absent. The paper calls Grok “most economically viable” from this ratio (Section 4.5, p. 8), but no monetary cost, value, or consequential utility is measured.

The main table provides one aggregate per configured system with no repetitions, task-cluster uncertainty, confidence intervals, missing/invalid-run policy, model-snapshot dates, or statistical test. Scenarios contain dependent subtasks and domains are highly unequal, so treating item observations as independent would be invalid. The reported closed/open averages are descriptive groupings of five and four selected model systems, not a population estimate of proprietary versus open models.

### Human evidence

The simulator study samples 50 interaction rollouts. Four experts draft unmet-rubric justifications and another four score the simulator’s feedback from 0 to 5; the reported mean is 4.69 (Section 3.2, p. 5). The paper does not state the sampling frame, task/domain stratification, whether experts were blind to source, exact comparison object, unit of analysis, per-rater aggregation, agreement, dispersion, confidence interval, exclusions, or released labels.

More importantly, agreement with expert-written **failure justification** validates neither realistic user behavior nor user authority. The simulator is given the rubric and judge result by design. The study does not ask real users whether they would notice the defect, communicate it, accept the artifact, prioritize another issue, stop, tolerate delay, or bear the cost of another round. In the terms of the user-simulator decision-fidelity evidence, it is communicative/evaluator consistency—not decision, free-running, burden, or consequence fidelity.

For judges, four experts score 50 held-out tasks and the paper reports Kappa 0.93 against LLM scores (Section 3.3, p. 5). It does not identify the kappa variant, how four human scores and two model judges become paired labels, whether the 0–10 scale is weighted/ordinal, per-domain results, judge-specific results, class distribution, uncertainty, or adjudication. Human agreement is not reported separately. The labels and predictions are absent from the release. One pooled kappa therefore cannot validate rule checks, text judges, vision judges, all task families, threshold decisions, or accepted alternatives.

## Evidence

### What the paper and release jointly establish

1. **Substantial inspectable instrument:** the release contains exactly 32 scenario specifications, 138 cumulative subtasks, 32 runners, and 32 parseable demonstration `meta_eval.json` files.
2. **Artifact-centered execution:** Game/Frontend runners preserve native files and derive screenshots, video, DOM/state returns, logs, and diagnostics through explicit interaction plans.
3. **Observable repair loop:** paired attempt records preserve first outputs, observer evidence, scores/reasons, next prompts, revised outputs, and later observations for part of the release.
4. **Configured-system sensitivity:** the reported model/scaffold table and heterogeneous runner implementations reinforce that performance belongs to model–scaffold–tool–observer–feedback packages.
5. **Real implementation disagreement:** the released Gomoku trace exposes observer-view contradictions, persistent defects despite repeated feedback, and plan-format failures separately from substantive artifact defects.

### What remains paper-reported or unauditable

- complete nine-model trajectories and score matrices;
- the 10-scenario scaffold run corpus;
- nonzero comparable token, call, wall-time, retry, and cost records;
- the 50-rollout simulator-validation labels;
- the 50-task human/judge labels and kappa computation;
- seeds, repetitions, invalid/service-failure ledger, or clustered uncertainty;
- a command that regenerates Tables 1–4 and Figures 4–5;
- correspondence between the sole January release commit and the April v4 implementation.

The 32 released demonstrations are not substitutes for the paper corpus. They are all under `claude/`, have seven different top-level metadata shapes, and 102 Game/Frontend completion records report `tokens_used: 0`. Among 138 released subtask records, 62 have one attempt and 76 have two; 108 attempt records have no `status` field because runner families differ. This is useful implementation evidence but not a normalized result matrix.

## Unique insight

AgencyBench’s unique transferable insight is the **feedback-conditioned evidence path**:

```text
initial artifact evidence
→ observer-specific defect proposition
→ disclosure authority and granularity
→ agent receipt
→ targeted file/state change
→ criterion-local re-observation
→ repaired criterion
→ new defect or collateral regression
→ endpoint artifact and cost
```

A before/after score is too coarse. To claim repair, the benchmark must show that a specific supported defect proposition was disclosed, received, adopted, changed the relevant artifact/state, and passed an admissible re-observation without introducing another material defect. To claim self-correction, it additionally needs a condition in which the agent identifies and repairs the defect without evaluator disclosure. To claim realistic collaboration, it needs evidence that the feedback source has the relevant authority, evidence view, communication policy, burden, and stopping behavior.

This yields three estimands that must not be merged:

1. **Unaided endpoint capability:** first-attempt outcome before benchmark-generated critique.
2. **Oracle-assisted repairability:** gain under criterion-level evaluator disclosure.
3. **Ecological feedback response:** gain under a validated participant/channel policy with realistic information and costs.

AgencyBench primarily measures the second, though its language often promotes it to the first or third. That distinction is reusable across code review, document revision, spreadsheet correction, design feedback, compliance remediation, and other knowledge-work domains.

## Limitations and validity threats

### Construct and sampling

- “Derived from daily AI usage,” “authentic,” “economic production,” and “real-world utility” are not supported by a documented usage-log or occupational sampling frame.
- Six capability labels are work-format/domain bins, not validated latent capabilities; tasks within a scenario combine planning, coding, debugging, visual judgment, state tracking, and format compliance.
- One million tokens and 90 turns are observed consumption summaries, not evidence that tasks require that context or horizon. There is no context-necessity ablation, irrelevant-context control, minimum sufficient trace, or expert baseline.
- Cumulative task order confounds difficulty, inherited implementation, prior feedback, and upstream defect exposure.

### Intervention validity

- Feedback discloses rubric failures and judge reasons, sometimes exact target values. It is closer to an oracle/debugger than an ordinary user.
- No no-feedback retry or generic-feedback control separates extra inference from information content.
- Failed cases alone enter later rounds, so endpoint gains are adaptively selected.
- The release and paper disagree on whether a separate user-simulator model generates feedback.
- No proposition-level record distinguishes disclosed fact, agent uptake, relevant change, successful repair, and collateral regression.

### Measurement validity

- Text and visual observers have different evidence views but are treated as common score sources.
- The vision judge adds aesthetics beyond the public rubric, violating the public-basis/private-consequence boundary.
- Rule, optimization, text-model, and vision-model scores are placed on the same 0–10 scale without common calibration.
- A 60% threshold has no demonstrated relationship to minimum professional acceptance, downstream usability, or loss.
- Criterion dependence and cumulative prerequisites are not modeled; averaging permits compensation unless a scenario runner happens to impose a conjunctive pass rule.
- Judge validation is underspecified and unavailable for replay; one kappa does not establish criterion, threshold, domain, or configured-judge reliability.

### Inference and reliability

- Main results appear single-run; no task-level repeats, confidence intervals, variance decomposition, or cluster-aware analysis is reported.
- Scenario, task, attempt, and criterion are dependent units, but estimands and denominators are ambiguous.
- API stochasticity, model version drift, service retries, parse failures, sandbox failures, and missing outputs lack explicit separate denominators.
- Relative increases from small `Pass@1` baselines exaggerate apparent effects (for example, “300%”) without uncertainty or absolute paired transition counts.
- Closed/open and native/non-native comparisons are selected configured-system contrasts, not broad family or causal training claims.

### Reproducibility and operational realism

- Positive: full task specifications, runners, example records, pinned Python dependencies, rich attempt evidence, and an MIT license are public.
- Negative: the README launches `ghcr.io/agent-infra/sandbox:latest`, not an image digest; hosted SII/model services and `.env` choices remain external; the repository has one commit; and paper runs, human labels, and table scripts are absent.
- The paper calls workspaces isolated, but the release provides no outer-envelope conformance test proving filesystem, credential, process, or network boundaries. A Chinese prompt instructing the model not to access other paths is policy text, not containment.
- The sample record contains absolute developer paths, zero token metadata, and heterogeneous schemas. This is not portable trial provenance.
- Visual capture is scripted, but accepted alternative interaction paths and alternative valid artifacts are not systematically tested.

## Relation to existing evidence

- **PaperBench** shows dense rubric coverage is useful partial-progress evidence but does not create end-to-end success. AgencyBench adds iterative artifact repair, while weakening criterion independence and exposing target information through feedback.
- **SciVisAgentBench** establishes that screenshots, code, native state, and domain-specific structures are different admissible witnesses. AgencyBench operationalizes multiple views but then averages or conjunctively thresholds uncalibrated observers rather than specifying criterion-view authority.
- **UniClawBench** cleanly separates private supervisor state from public simulator output yet still cannot prove semantic non-leakage. AgencyBench often removes even that structural firewall by directly returning evaluator reasons.
- **DeskCraft** injects authored requirements at fixed phases and therefore measures simulator-mediated endpoint conformance. AgencyBench injects authored defect diagnoses after failed grading and measures an even stronger evaluator-assisted condition.
- **HAS-Bench** distinguishes participant role, information, permission, and authority. AgencyBench’s “user” has acceptance-test authority and rubric access by construction but no validated human realization, burden, preference, or stopping policy.
- **User-simulator decision fidelity** shows fluent, expert-consistent language can omit consequential stop/commit boundaries. AgencyBench’s 4.69 justification-consistency mean is therefore not evidence of user-decision fidelity.

These comparisons sharpen rather than duplicate existing contracts: AgencyBench contributes a concrete released composition of feedback intervention and plural artifact observation, plus direct evidence of where that composition breaks.

## Transfer to skill-bench

### Retain

1. **Cumulative task packages:** preserve explicit state lineage across subtasks instead of treating every work product as independent.
2. **Native deliverables plus derived views:** keep source/native artifacts, render/extract transformations, interaction scripts, screenshots/video, and structured state separately identifiable.
3. **Observer-specific evidence:** store what each rule, model, or human observer actually saw.
4. **Attempt-level repair traces:** preserve every attempt, feedback event, revised artifact hash, score, and failure rather than only the best endpoint.
5. **Configured-system comparisons:** name model, scaffold, prompt, tools, budgets, observer models, feedback policy, environment, and service versions independently.

### Repair

1. Type feedback as `ecological_user`, `expert_review`, `deterministic_verifier`, `model_judge`, `oracle_debug`, or `service_error`; do not call all critique “user feedback.”
2. Record feedback propositions and their source evidence locators, public/private status, granularity, authority, and whether they disclose a target or merely report an observed consequence.
3. Link each proposition to receipt, adoption/rejection, changed artifact/state loci, re-observation, repair outcome, collateral regressions, and added cost.
4. Declare criterion-specific admissible views and abstain on missing/inadequate evidence; do not let screenshot confidence prove hidden state or code inspection prove execution.
5. Keep first, final, best, and cumulative scores separate. Report invalid/service outcomes separately from substantive failure.
6. Use noncompensatory gates for mandatory prerequisites, and preserve criterion dependence/applicability rather than averaging every observer score.
7. Hash the sandbox image, runner, interaction plan, source pack, task, rubric, observer prompts/models, feedback policy, and aggregation policy.

### Test

Use a matched feedback factorial on a small cross-domain pilot:

- first attempt only;
- retry with no new information;
- generic “review and improve” prompt;
- consequence-only feedback from an admissible observer;
- criterion-level evaluator disclosure;
- where available, real authorized expert/user feedback.

Hold the initial task, configured target, initial artifact, environment, retry budget, and evaluation policy fixed. Estimate criterion-local repair, endpoint change, new-error rate, token/time/cost, and reviewer burden. This separates additional inference, oracle information, and ecological feedback value. It also tests whether a repair policy transfers across document, spreadsheet, code, and workspace-state artifacts rather than overfitting one game interface.

## Concrete repository actions

1. **No new schema or queue task.** Existing benchmark-bundle feedback/recovery edges, artifact-view admissibility, configured-system identity, task-health, metric-monitoring, and validity-argument contracts already have homes for every required field. Adding another AgencyBench-specific contract would duplicate completed machinery.
2. Use `data/sources/releases/2601.11044v4-agencybench/audit.json` as a conformance case when the next feedback-intervention pilot is built: assert separate initial/final/best estimands, typed feedback source, proposition-level uptake, criterion-view admissibility, collateral regression, and invalid-service outcomes.
3. Add AgencyBench to topic navigation as a release-audited feedback-intervention case, but do not change grouped synthesis tiers until a consolidation run compares it with UniClawBench, DeskCraft, EdgeBench, HAS-Bench, and user-simulator decision-fidelity evidence.
4. Treat the archived release as local immutable evidence and keep its provenance/hash in Git; the 37.6 MB ZIP should remain ignored rather than enlarge routine history.

## Bottom line

AgencyBench is valuable because it makes long-horizon artifact revision unusually inspectable: cumulative files, browser actions, multiple evidence views, evaluator comments, and retries are all present in one released instrument. Its strongest evidence is also its strongest warning. Once benchmark observers disclose acceptance failures, later performance is a property of the **target–observer–feedback policy**, not the target alone. The release demonstrates that observers can sharply disagree, that direct critique can repair exact rubric failures, that some defects persist, and that format failures can prevent artifact observation entirely.

Accordingly, retain the pipeline, but rename the construct. First attempts provide bounded unaided evidence; evaluator-guided retries provide oracle-assisted repairability evidence; realistic collaboration requires separate participant, authority, information, burden, acceptance, and consequence validation. Neither long traces nor high rubric coverage closes those gaps.
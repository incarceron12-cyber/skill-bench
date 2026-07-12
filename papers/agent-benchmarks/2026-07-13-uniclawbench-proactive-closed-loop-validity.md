# UniClawBench: a released repair loop, not a validated proactivity measure

**Source type:** Deep review of the complete immutable arXiv v1 paper and pinned official release  
**Paper:** Zhekai Chen et al., *UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks*, arXiv:2607.08768v1 (9 July 2026)  
**Immutable source:** <https://arxiv.org/abs/2607.08768v1>  
**Local PDF:** `data/papers/pdfs/2607.08768v1-uniclawbench.pdf` (SHA-256 `4a29ad6166889872d9100a0165ec005a8aab08470b76ddb658a0245c5203c8ea`, 33 pages)  
**Local text:** `data/papers/text/2607.08768v1-uniclawbench.txt` (SHA-256 `abe4e06306749ed8fbdff23877d102b22fb4c410b3aa80de524e23659ab9091b`)  
**Release audit:** `data/sources/releases/2607.08768v1-uniclawbench/provenance.json`; official commit `a88ffd0078823324415049a98eb813eb08d60f57`; tracked-tree manifest `data/sources/releases/2607.08768v1-uniclawbench/tree-manifest.txt`

> **Evidence boundary.** I read the full paper and inspected the complete official checkout at the pinned commit. The commit is approximately one day later than v1, so it is linked-release evidence rather than proof of the exact paper-time implementation. The release contains 400 benchmark task YAMLs, task resources, hidden rubrics, runtime, tests, and WebUI code, but no paper run tree, raw result table, reliability labels, or bilingual-equivalence judgments. Aggregate trial claims remain paper reports.

## Review judgment

UniClawBench's strongest contribution is an inspectable **role-separated recovery protocol**: an executor acts, a private supervisor judges visible state against hidden references, and a public simulator generates a follow-up from visible evidence plus a four-field progress handoff. This is useful benchmark machinery for studying repair under bounded feedback.

The paper's central labels outrun that machinery. Every released task begins with an explicit, detailed user request; the agent does not notice an unrequested need, decide whether to interrupt, or initiate help. The loop therefore tests **requested task execution and repair after synthetic follow-up**, not proactivity. Nor does five mutually exclusive author-assigned task categories “pinpoint” root cause: tasks still require multiple capabilities, no capability intervention validates the primary label, and failures are not causally localized. The framework comparison is a configured-system comparison without repeated runs or uncertainty, while “real-world” alternates among live web, local fixtures, snapshots, packaged sources, and credentialed services.

Most importantly, the paper's own end-to-end example exposes the unresolved information-flow problem. The user simulator is formally denied the supervisor rationale, yet its follow-up reproduces the rationale's highly specific defects: the 7-versus-1 exclusions mismatch, the exact LCCN misclassification, and speculative duplicate logic (pp. 30–31). Those facts may be inferable from visible artifacts, but the paper provides no blinded counterfactual showing that the simulator independently discovered them rather than exploiting score/status cues or benchmark-shaped evidence. The example demonstrates a successful repair channel; it does not validate either natural-user fidelity or non-leaking feedback.

## One-sentence contribution

UniClawBench releases a substantial role-separated repair benchmark, but its explicitly requested tasks and synthetic evaluator-driven follow-ups do not identify proactivity, pure capabilities, natural user behavior, or semantic non-leakage.

## Contribution

### Research question

The paper asks how to evaluate modern personal-agent systems on dynamic tasks while separating model from framework effects and allowing iterative user feedback (pp. 1–3). It contributes:

1. 400 released tasks: 40 English and 40 Chinese tasks in each of Skill Usage, Exploration, Long Context, Multimodal, and Cross Platform;
2. task packages with public prompts, sources, skills/services, hidden references, and task-specific `eval_rule.md` files;
3. a host-supervised Docker runtime supporting OpenClaw, EDICT, and Nanobot;
4. a three-role executor–supervisor–user-simulator loop with up to two follow-ups;
5. checkpoint Average Score (AS), thresholded Pass Rate (PR), and model/framework comparisons;
6. a 50-trajectory human comparison and one fully narrated two-cycle case.

The unique contribution is not a new taxonomy of agent ability. It is the separation of **private judgment state from public repair communication** as an explicit, inspectable information-flow boundary.

## Methodology and released system

### Task construction and capability labels

The authors say all 400 tasks were manually constructed from “genuine, day-to-day scenarios,” constrained so one capability is the primary bottleneck (pp. 4–6). The paper reports no author count by task, occupational sampling, expertise, incident provenance, rejection process, independent review, capability-label agreement, or human feasibility baseline. The release confirms exact counts—400 benchmark YAMLs plus four smoke tasks and one template—and all benchmark tasks use threshold `.9` and two allowed follow-ups. It does not add authoring provenance.

The five labels are not orthogonal. For example, the released/paper examples combine web exploration, visual evidence, long-context consistency, artifact creation, and cross-application state. Assignment to the capability “whose absence would prevent successful completion” is counterfactual language without an ablation: no capability is removed, no matched task changes only that requirement, and no independent annotator labels earliest cause. A category score is consequently a score over an authored slice, not a pure capability estimate.

The release contains English and Chinese directory mirrors, but the paper gives no translation workflow, original-language designation, bilingual author qualifications, semantic-equivalence review, locale adaptation, paired analysis, or language-specific results. “400 bilingual tasks” means 200 English plus 200 Chinese task instances, not demonstrated equivalent forms.

### Task and rubric contract

The paper's Appendix A specifies a public YAML and hidden nine-section rubric. Release inspection found 405 task YAMLs and 405 referenced eval rules, including non-benchmark examples; among the 400 benchmark tasks, public instructions are generally unusually explicit about deliverables, paths, evidence, forbidden actions, and traps. This improves gradeability but weakens claims about natural underspecification or proactive need discovery.

Rubrics combine task completion, exploration breadth, source evidence, trap handling, and reproducibility with weighted checkpoints and post-sum caps (pp. 14–15, 29–30). Release inspection found 353 distinct byte hashes across 405 eval rules, indicating considerable task specificity but also paired/shared material. There is no released criterion-level human calibration, dependency model, alternative-valid-path adjudication, or deterministic replay proving that the LLM supervisor applies these prose contracts consistently. “Use this rubric as guidance; exact weighting may be adjusted” in the showcased rule (p. 29) also conflicts with the supervisor prompt's strict instruction to use only rubric lines and literal weights (pp. 23–24).

### Closed-loop information flow

The runtime's structural separation is real in the inspected release:

- `lib/supervision/orchestrator.py:274–332` constructs a four-field handoff: verdict, attempt state, recoverability, and score;
- `lib/supervision/user_simulator.py:65–77` mounts visible evidence without hidden references;
- `lib/privacy.py:9–22` gives credentials to executor and supervisor but not the simulator;
- `lib/supervision/feedback_rewriter.py:94–109` defaults to simulator candidate text only and falls back to a generic message if none survives;
- role outputs and fallback provenance are preserved in supervision records.

That is a meaningful implementation advantage over prose-only simulator designs. But structural non-mounting is not semantic non-leakage. A scalar score and `complete_but_failed` label are treatment signals derived from private judgment. More subtly, the simulator sees artifacts and the full executor trajectory after the supervisor chose `continue`; its next message can become a strong benchmark-specific critique even without hidden files. The case-study follow-up is nearly a public rendering of the private rationale. The paper reports no leakage audit, blinded human comparison, feedback-information coding, mutual-information proxy, or no-score/status ablation.

The system also transforms the evaluated intervention: a first attempt can receive up to two model-generated critiques. Final PR therefore measures the executor **plus this fixed supervisor/simulator policy**, not standalone agent reliability. Figure 4(c) rises from 23.8% to 31.7% over cycles (p. 9), but there is no no-feedback, generic-nudge, visible-only-human, score-only, or rationale-exposed arm. The improvement cannot establish that natural feedback is essential, that the firewall causes it, or that the same recovery would occur with real users.

### Runtime, state, credentials, and observability

The paper specifies fresh Docker containers, 2 GB memory, host CPU, browser/GUI/files/services, common installed skills, 30/20-minute standard limits and 45/30-minute long-context limits (pp. 6–7). The release has task resource checks, privacy manifests, snapshot mode, role workspaces, artifact/transcript/timeline collection, and numerous unit/integration tests. These are strong reproducibility ingredients.

However, “live Docker containers” does not make all tasks live or environments equivalent. Release inspection found only 12 task YAMLs with `task_snapshot`, while 58 benchmark tasks have `.privacy` manifests (some empty, some credential-bearing); many others use packaged local fixtures. Live sites, APIs, OAuth accounts, local mock services, and static files differ in mutability, authority, availability, and side-effect risk. The paper does not report per-condition live/snapshot/fixture status, credential failures, invalid runs, retries, exact container hashes, network captures, task execution dates, or state-reset verification.

Observer coverage is also conditional. The supervisor receives transcripts, tool records, runtime state, and artifacts, but screenshots are file references inspected on demand (p. 7). Its prompt explicitly permits grading screenshot presence and text summaries without opening pixels when the checkpoint is not deemed pixel-dependent (Appendix C). Binary originals can be transformed, including PNG-to-JPEG conversion, while format-specific claims rely on rubric text rather than the transformed view (pp. 22–24). Thus “full trajectory” is not identical to full environment state, and evidence sufficiency varies by checkpoint and supervisor choice.

### Models, frameworks, metrics, and uncertainty

The model study runs ten executors under OpenClaw; the framework study crosses three models with OpenClaw, EDICT, and Nanobot (pp. 7–9). Supervising and simulation use separate GPT-5.4 Codex agents. Tables report PR, AS, and executor token use; average runtime is 17.4 minutes.

The design does not isolate “base model capability” absolutely. It holds one framework fixed, but provider behavior, model-specific adapters, context handling, multimodal access, and token policies may still differ. The 3×3 framework table is crossed at the label level, but framework implementations necessarily alter orchestration, context, tool adapters, prompts, and token consumption. Those are the configured-system treatment, not a single architecture variable.

No repeated task runs, seeds, confidence intervals, paired tests, clustered uncertainty, failure/attrition ledger, or total evaluation cost are reported. Tasks are paired across systems, but inference ignores task and English/Chinese-pair dependence. Claims that framework choice “consistently impacts capability performance more than model choice” are not backed by a defined variance decomposition or interaction model. Table 2 itself has model-dependent framework gaps.

Timeouts receive the maximum checkpoint score achieved across completed turns (p. 7), which mixes partial capability with budget failure and makes AS non-final-state. PR and AS are distinct estimands, but the paper interprets their gap as “halfway failure” without separating incomplete work, irreversible action, timeout, supervisor noise, missing observation, or threshold geometry.

## Evidence and what it supports

The best OpenClaw system reportedly reaches PR `.475`; exploration is easiest and multimodal/long-context/cross-platform are lower (Table 1). In the 3×3 matrix, OpenClaw has the highest PR for each tested model, while EDICT uses more input/output tokens and Nanobot often fewer (Table 2). These support bounded descriptive claims about the reported configured runs on the authored slices.

The reliability study samples 50 “completed” trajectories and has three unspecified human experts independently provide pass/fail and scores. Supervisor pass/fail agrees with majority vote on 92% (46/50), and supervisor AS correlates with mean human score at Pearson `.71`, Spearman `.68` (p. 7). This does not validate the evaluator generally:

- the sample excludes or ambiguously handles incomplete/infra cases and is only 12.5% of tasks before accounting for systems;
- sampling strata across language, capability, model, framework, score, and cycle are absent;
- expert qualifications, rubric access, evidence view, training, blinding, disagreement, and adjudication are absent;
- agreement with majority is not accuracy; human inter-rater agreement is not reported;
- correlation does not establish calibration, threshold accuracy, or criterion-level validity;
- no labels or predictions are released for reproduction.

The end-to-end LOC case establishes that the released protocol can take one supervisor-rated `.65` attempt to `.96` after a detailed synthetic follow-up (pp. 28–32). It does not establish a population recovery effect, feedback fidelity, no leakage, or causal repair mechanism.

## Unique insight

> **A feedback firewall needs semantic accounting, not merely filesystem separation.**

For each evaluator-to-participant edge, skill-bench should record:

`private observation → private decision → released signal fields → simulator evidence view → generated feedback proposition → executor-visible message → changed action/state → outcome`

Each released proposition should be classified as:

1. already entailed by the public task;
2. independently observable in public trajectory/artifacts;
3. inferable only because of the private-derived status/score;
4. semantically equivalent to a hidden criterion/reference;
5. new user preference or authority-bearing instruction;
6. generic encouragement with no task information.

This is the missing bridge between information-flow security and intervention validity. A benchmark can prevent direct file access yet still turn its grader into an adaptive tutor. Conversely, useful visible-state criticism is not automatically leakage; it is a treatment whose authority and information content must be measured.

## Limitations and validity threats

1. **Construct mismatch:** explicit requested tasks plus feedback-driven repair do not measure autonomous need recognition or action initiation.
2. **Unvalidated capability taxonomy:** single primary labels lack interventions, label agreement, contrast cases, or causal failure localization.
3. **Feedback-treatment confounding:** final scores combine executor ability with GPT-5.4 supervision and simulation.
4. **No leakage validation:** structural role isolation is demonstrated; semantic criterion leakage is not.
5. **Case-study tension:** the supposedly coarse-firewalled follow-up reproduces highly specific private-rationale defects.
6. **No feedback ablation:** score/status, generic nudge, visible-only critique, human feedback, and no-feedback conditions are absent.
7. **Weak task provenance:** “genuine daily scenarios” lacks participant, incident, expertise, authoring, and acceptance evidence.
8. **No bilingual-equivalence evidence:** mirrored counts do not establish translation fidelity, locale validity, or paired difficulty.
9. **Criterion subjectivity and contradiction:** prose rubrics permit flexible judgment while prompts demand literal, non-inventive scoring.
10. **Partial observer views:** screenshots and transformed artifacts may not be inspected; traces do not prove all consequential state.
11. **Mixed environment regimes:** live web, credentials, snapshots, local services, and static fixtures are pooled without a state/validity ledger.
12. **Single-run reliability:** no repeated executor or judge calls, stochastic stability, or task-clustered uncertainty.
13. **Human validation is under-specified:** 50 completed trajectories, unknown strata/experts/evidence views, and no released labels.
14. **Framework causality is bounded:** framework packages differ on many mechanisms and have no randomized/repeated execution.
15. **Root-cause overclaim:** category-level score differences and narrative failure examples do not identify earliest supported cause.
16. **Metric ambiguity:** timeout best-so-far AS mixes progress and budget failure; thresholds can mechanically widen AS–PR gaps.
17. **No raw trial release:** aggregate tables, reliability claims, feedback progression, costs, and failures cannot be recalculated.
18. **Operational burden:** 17.4-minute average runs, live dependencies, credentials, GUI state, supervisor/simulator calls, and large assets imply substantial maintenance and cost.
19. **Safety boundary is incomplete:** some prompts instruct agents to complete CAPTCHAs or operate credentialed services; release machinery protects secret transport but does not establish legitimacy, authorization, or safe side effects.
20. **Release timing:** the inspected commit postdates v1 and may contain fixes not present in reported experiments.

## Reproducibility and operational realism

**Inspectability: high for authored instrument and runtime.** The release is unusually substantial: 24,688 tracked files, 400 benchmark YAMLs, task resources and hidden rubrics, role-separated code, Docker/runtime documentation, privacy handling, and tests. This permits a real audit rather than abstract reconstruction.

**Exact result reproducibility: low.** The paper's run artifacts, component/config hashes, execution dates, per-task system matrix, invalid/retry ledger, raw judgments, human labels, and cost table are absent. Live services and credentials create unavoidable temporal and operator dependence. The linked commit is not identified as the exact evaluated revision.

**Operational realism: heterogeneous substrate, unvalidated consequence.** Real browsers, files, GUI apps, APIs, and professional-looking artifacts are useful. But manually authored detailed prompts, fixtures, benchmark-specific evidence demands, synthetic follow-ups, unknown occupational sampling, and absent stakeholder acceptance prevent claims of representative professional work or deployment readiness.

## Comparison with existing skill-bench evidence

- **KWBench** tests whether an agent rejects or reframes an explicit surface request without being told the latent issue. UniClawBench instead gives detailed tasks and then adaptive repair messages; it does not fill KWBench's unprompted-recognition gap.
- **HAS-Bench** makes participant behavior and simulator substitution the construct. UniClawBench's user simulator has no empirically fitted participant profile or human-comparison study; it is an evaluator-side intervention generator.
- **PolyWorkBench** highlights language-bearing workflow edges but lacks matched language effects. UniClawBench adds released English/Chinese instances, yet still supplies no equivalence protocol or paired language analysis.
- **Tool-Veritas / the tool-calling evaluator-validity audit** shows that evaluator access, execution, and outcome provenance must be tested rather than assumed. UniClawBench improves evidence access but still validates only aggregate supervisor agreement, not criterion execution or semantic feedback leakage.
- **Workflow/state reviews** emphasize state transitions and consequential side effects. UniClawBench captures artifacts and selected runtime probes, but does not prove complete state observation or separate earliest cause from visible failure.

## Relevance

## Transfer to skill-bench

### Retain

- Explicit executor/supervisor/public-participant role identities and separate workspaces.
- Four-field typed private-to-public handoff rather than raw grader rationale.
- Per-cycle visible artifacts, supervisor judgment, public message, executor continuation, timing, and usage records.
- `continue` distinct from terminal fail, with bounded follow-up budgets.
- Task-specific checkpoint/cap contracts and public/private asset separation.
- Fallback provenance when simulator generation fails.

### Repair

1. Name the construct precisely: **closed-loop repair under benchmark-generated visible-state feedback**, not proactivity.
2. Add no-feedback, generic-nudge, visible-only simulator, score/status-only, authorized human, and deliberately leaky feedback conditions on matched tasks.
3. Audit each feedback proposition against public evidence and hidden criteria; estimate semantic leakage and unsupported-authority rates with blinded coders.
4. Separate first-attempt success, recoverability classification accuracy, repair uptake, repair correctness, new-error introduction, final success, and intervention cost.
5. Validate simulator messages against real participant messages for specificity, authority, tone, omissions, and willingness to continue; do not use judge agreement as a proxy.
6. Treat model, framework, supervisor, simulator, feedback rewriter, task, environment, and observer configuration as independently hashed components.
7. Give capability claims matched interventions or label them descriptive task families; retain root/surface separation.
8. Record live/snapshot/fixture regime, initial and final state, credentials/authorization scope, external versions, invalidity, and reset evidence per trial.
9. Calibrate supervisor criteria with identical expert evidence views, repeated judgments, criterion-level errors, abstention, and clustered uncertainty.
10. For bilingual pairs, preserve original/translation lineage, locale transformations, bilingual/domain approval, matched denominators, and paired analysis.

## Concrete repository actions

1. **No new schema task.** Existing information-flow, participation, benchmark-bundle, task-health, metric, reliability, and validity machinery can represent the needed fields. Add the semantic feedback-proposition chain and simulator-treatment arm only when a diverse pilot exercises closed-loop repair.
2. **Validation refinement:** before using synthetic follow-up in a scored pilot, run a compact matched feedback audit: no feedback vs generic nudge vs visible-only simulator vs hidden-derived coarse signal, with planted public-visible and hidden-only defects. Blindly classify every feedback proposition and measure repair benefit, leakage, new errors, cost, and judge reliability.
3. **Claim gate:** prohibit “proactivity” unless the task includes an observable opportunity before an explicit request and measures notice, decision to intervene, timing, authority, and false-positive interruption on matched no-action cases.

## Claim boundary

The immutable paper and pinned release establish a substantial 400-task English/Chinese benchmark package and an implemented executor–private-supervisor–public-simulator recovery loop. The paper reports aggregate configured-system scores, a 50-trajectory supervisor/human comparison, and one successful two-cycle repair. They do **not** establish proactive need recognition, pure capability measurement, root-cause identification, bilingual equivalence, natural-user fidelity, semantic non-leakage, causal feedback benefit, isolated framework effects, repeated-run reliability, professional validity, safe authorized action, exact result reproducibility, or deployment readiness.

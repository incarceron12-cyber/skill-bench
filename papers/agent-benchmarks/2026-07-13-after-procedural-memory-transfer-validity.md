# Paper Review: AFTER — Procedural-Memory Transfer Validity

- **Paper:** https://arxiv.org/abs/2606.23127v1
- **Authors:** Julia Belikova, Rauf Parchiev, Evgeny Egorov, Grigorii Davydenko, Gleb Gusev, Andrey Savchenko, Maksim Makarenko
- **Date read:** 2026-07-13
- **Venue / source:** arXiv preprint
- **Version read:** immutable v1, 22 June 2026
- **Local PDF:** `data/papers/pdfs/2606.23127v1-managing-procedural-memory.pdf` (18 pages; SHA-256 `1ef4d116e01ef8ebc920704576c4e2357b7864838a719996e54711456746f006`)
- **Local text:** `data/papers/text/2606.23127v1-managing-procedural-memory.txt` (SHA-256 `91b1cdb0051ec932e6bd03324be245134053dfcd1c08ea31899b921558d87004`)
- **Official GitHub release inspected:** https://github.com/DavydenkoGr/AFTER/tree/161ac61f317560a98e1b6a9885507b39ea51dea4 (commit `161ac61f317560a98e1b6a9885507b39ea51dea4`; tree `ef8461f7d68fc0169b8fa41cd3a273a147e80119`)
- **Paper-linked Hugging Face revision:** https://huggingface.co/datasets/DavydenkoGr/AFTER/tree/18287618ffe4173da683895176ec700f08080752
- **Release provenance:** `data/sources/releases/2606.23127v1-after/provenance.json`
- **Tags:** procedural-memory, skill-evolution, transfer, longitudinal-evaluation, configured-systems, missingness, release-completeness, claim-validity

## One-sentence contribution

AFTER proposes a task × role × skill × model evaluation graph for distinguishing local procedural-memory improvement from transfer, but v1 reports the crucial refinement, cross-role, and cross-model results without enough denominators, configured-system identity, repetitions, uncertainty, or released experimental evidence to establish that its observed gains are reusable procedural transfer rather than selected-task effects, treatment differences, or run noise.

## Why this matters for skill-bench

AFTER asks a question central to `skill-bench`: if an agent or author revises a procedural Skill using execution traces, where does that revision remain useful, and where does it become a context-specific patch? Its most useful design move is not the headline score. It is the explicit separation of:

- **specificity:** change on the source task/role/model context;
- **cross-task generality:** change on held-out tasks sharing a declared procedure;
- **cross-role generality:** change when nominally the same procedure serves another work context;
- **cross-model generality:** change when another solver consumes the revised artifact.

That structure advances charter objectives A and B and maps directly to the repository's procedural-skill, longitudinal-stream, configured-system, feedback-firewall, task-health, metric, and validity contracts. The paper also demonstrates why those contracts must remain stricter than a train/test label: a transfer edge is interpretable only when the source traces, updater, skill versions, target tasks, target solver, harness, feedback visibility, selection rule, and uncertainty are independently identified.

The paper does **not** establish expert knowledge transfer. The 22 “handcrafted” bodies are adapted from public Skill repositories, while the other 22 are model-generated; the paper reports author review but no occupational sampling, expert qualifications, expert/novice contrast, or validation by practitioners responsible for the represented work. “Role” is therefore a benchmark grouping and context treatment, not evidence that the procedure is professionally authoritative or representative.

## Research question and claim boundary

The paper asks whether textual procedural memory can be revised from bounded execution traces so that it improves a source context without losing utility under task, role, or model shifts. Formally, it defines an update operator `U` over an active Skill configuration and source trace pool, then evaluates the updated configuration on source and target context distributions (Section 3.1, p. 4).

The full evidence supports these bounded claims:

1. The authors designed a 382-task internal instrument organized by six technology-sector role labels and 22 Skill labels, with 318 reported single-Skill and 64 reported multi-Skill tasks (Section 2, pp. 2–3; Appendix E, pp. 11–12).
2. The released post-v1 test slice makes 129 task packages, both 22-body static Skill catalogues, generators, reference solutions, pytest verifiers, and source records inspectable.
3. The paper reports heterogeneous static and revised-Skill outcomes, including negative cells, consistent with the hypothesis that procedural guidance is configuration- and context-dependent.
4. Its transfer taxonomy is a useful evaluation design even though the reported transfer effects are not independently auditable.

The evidence does **not** establish the full 382-task instrument's integrity; causal procedural-transfer effects; the reported 3.7–6.7-point refinement range or 73.1% cross-model result independently of the authors' tables; forgetting rates; occupational representativeness; expert transfer; professional artifact quality; production fitness; deployment value; or readiness.

## Methodology and system reconstruction

### Task, role, and Skill provenance

The reported benchmark contains 382 tasks across Data Engineering (74), Data Science (71), Generative AI Engineering (66), Infrastructure (53), Project Management (51), and Software Engineering (67). Of these, 56 adapt 13 public benchmark/repository sources, 38 were written by the authors, and 288 were drafted by Claude Sonnet 4.6 and iteratively rewritten (Figure 2 and Appendix E, pp. 3, 11–12). The work surface is broad within technology organizations but is neither a probability sample of jobs nor a sample of observed workplace episodes.

Tasks are assigned one to three of 22 fixed Skill labels. The paper says the assignment is the minimal set needed for completion, fixed rather than retrieved at solve time to remove routing quality from the treatment (Section 2.1, p. 3). Every `(role, skill)` cell is said to be split 50%/25%/25% into train/validation/test, with whole-role holdouts added for cross-role work (Appendix D.1, pp. 11–12).

The task contract contains `task.toml`, an instruction, inputs, and pytest checks. Instructions intentionally omit implementation details that the Skill should provide (Appendix D.2, p. 11). This creates a legitimate Skill-treatment test, but it also makes public instruction sufficiency and Skill efficacy partly co-designed: procedure-bearing information is deliberately allocated to the treatment. A positive effect establishes value under that disclosure policy, not spontaneous professional competence.

Quality assurance combines metadata/path checks, a reference-solution run, empty/constant/random adversarial outputs, and two-author review of clarity, Skill fit, realism, dependency hygiene, verifier soundness, oracle leakage, determinism, and self-containment. The paper calls this “independent expert review” in Section 2.2, but Appendix E.2 identifies the reviewers as two authors and gives no domain qualifications, agreement statistic, disagreement count, or external adjudication (pp. 3, 12). Acceptance required both reviewers to accept every criterion, with about 32 hours reported per reviewer.

The 22 static procedures each have:

- a public-source-adapted “handcrafted” body `H`; and
- a broad model-generated body `G`.

The official release's `skills/sources.json` identifies mutable raw URLs for the adapted bodies but no source commit, source hash, transformation lineage, reviewer identity, or occupational authority. The term “expert-derived” used in the results discussion is therefore stronger than the released provenance supports.

### Procedural-memory representation and update operator

The proposed EVOLUTION interface stores each procedure as versioned `SKILL.md` text with YAML metadata for name, role/Skill annotations, version, parent, source trace pool, and evaluation status. An execution trace is linked to the active version. An update passes through `COLLECT → DIAGNOSE → REVISE → PROMOTE/ROLLBACK`; a candidate is promoted when validation improves by margin `δ`, otherwise retained as an inactive branch (Section 3.2, p. 4; Appendix B, pp. 10–11).

This is a sound conceptual skeleton: immutable versions, parentage, trace lineage, validation, rollback, and named active-library snapshots are the right units. However, v1 does not specify `δ`, the validation estimator, tie/missingness policy, stopping rule, update prompt, trace serialization, feedback visibility, contamination firewall, or whether promotion observes the same task/check semantics later used for transfer claims. Context-specific adapters are proposed but explicitly left unevaluated (Appendix B, p. 11).

The paper says four external memory systems—EvoSkill, MemP, Memento-Skills, and Hermes—are evaluated through this interface, while Codex also appears as a refinement/update condition. The descriptions are conceptual mappings to the papers' systems; no adapter code, exact prompts, pinned upstream commits, or conformance tests show that these implementations realize equivalent update opportunities (Appendix C, p. 11).

### Evaluation graph and metrics

Two task-macro metrics are defined (Section 2.3, p. 4):

- `M1`: fraction of individual pytest assertions passed, averaged over attempts and tasks;
- `M2`: all-tests-pass indicator, averaged over attempts and tasks.

The study has four reported stages:

1. **Static value:** no Skill versus handcrafted versus generated Skill across 13 model labels and all role groups.
2. **Single refinement:** one Codex refinement of the handcrafted catalogue, evaluated with three Qwen solver sizes.
3. **Framework-guided evolution:** five update approaches, using one or five source tasks and a Qwen3.5-35B-A3B solver, on PDF/XLSX/PPTX.
4. **Transfer and efficiency:** selected cross-model, cross-role, and three-task token/cost analyses.

The transfer graph is only partially instantiated in the reported evidence. Cross-task results in Table 3 average three Skill labels. Cross-role results show only PDF transfer between PM and DS, despite Appendix F saying PDF, XLSX, and validation are used. Cross-model Figure 4 names four single-model trace sources plus pooled traces but does not identify the target solver, exact Skill/task set, trace counts, update model/configuration, attempts, or metric beyond “test accuracy” (pp. 5–6, 12).

### Configured-system identity, repeats, and uncertainty

The paper lists model display names and rough size tiers, plus three named agent/update wrappers. It does not provide provider/endpoints, model snapshots, system prompts, harness commits, tool surfaces, sandbox image/digest, time/token budgets, sampling settings, retry policy, failure handling, or run dates (Appendix F, p. 13). Static evaluation is described as one model invocation per task with “no agent orchestration, retrying, tool use, or evolution,” yet the task packages require file artifacts and executable verification; the execution bridge from one invocation to those artifacts is not specified (Section 4.1, p. 5).

`Natt` appears in both metric equations and tables refer to attempts, but v1 does not state the attempt count for the main static, refinement, framework, cross-role, or cross-model experiments. Only the three-task cost appendix explicitly reports means over four runs (Appendix G, p. 13). No confidence intervals, standard errors, task-cluster bootstrap, paired test, randomization test, or multiplicity control accompany any main effect.

## Evidence and results interpretation

### Static Skill results are heterogeneous—and mislabeled

The headline says static procedural Skills improve full-pass accuracy by +2.8 points on average (Introduction and Conclusion, pp. 2, 6). Table 2 is labeled `M2`, but its numbers are byte-for-number the values in Appendix Table J.1, which is labeled `M1`; for example GPT 5.4 aggregates `47.6/49.0/50.1`. Appendix Table J.2 contains a different, much higher set labeled `M2`, such as GPT 5.4 `81.6/79.4/77.5` (pp. 5, 15–16). J.2's caption then incorrectly defines its per-task quantity as `tests_passed/task_total`, which is the paper's `M1`, not its all-tests-pass `M2` definition.

This is not cosmetic. It blocks confident interpretation of “full-pass accuracy” and the +2.8-point aggregate. The static tables nevertheless reveal useful heterogeneity: some model/role cells improve, others decline, and the best of `H` or `G` is selected when reporting `∆`. A best-of-two delta is not the effect of a prespecified Skill treatment and is upward-selected relative to either fixed catalogue.

### The 3.7–6.7-point refinement claim is descriptive, selected, and unreproduced

Appendix Table K.1 reports aggregate `M2` increases of +3.7, +6.7, and +3.8 for Qwen 9B, 35B, and 122B solvers. These values support the paper's arithmetic range, but they use only the **111 task IDs present in both pre- and post-refinement runs**, not all 382 tasks or even the released 129-task test slice (p. 17). The paper does not explain why other task IDs are absent, whether missingness depends on outcomes or environments, how many attempts feed each cell, or whether the 111-ID subset was fixed before observing results.

The refinement is a catalogue-wide Codex treatment; the exact pre/post Skill hashes, update prompt, trace pool, candidate history, validation outcomes, and result rows are unreleased. Role-level negative changes remain—for example DS at 9B and PM at 35B—so “consistent improvements” means positive solver-level macro averages, not absence of forgetting or negative transfer. Without paired task effects and task-clustered uncertainty, the table does not establish that the gains exceed run variability.

### Framework comparison does not isolate the updater

Table 3 reports held-out `M1` changes for five systems using one versus five source tasks. Diverse Hermes traces produce +18.0 test points, while several other systems remain near zero or negative (p. 5). But “Seed” varies from 52.4 to 58.4 despite the claimed shared solver, task pool, splits, and handcrafted starting point. The caption acknowledges that trace and Skill management are framework-specific. Thus updater, trace collection, execution wrapper, and possibly stochastic baseline realization vary together.

`n=1` and `n=5` are task counts, not experimental repetitions. There is no resampling across source-task subsets, so “diversity” is confounded with four additional traces/tasks and whichever examples were selected. The paper's stronger statement that diverse training beats narrow “for every reasoner” in Appendix H concerns a different two-Skill ablation and reports each condition's best result, again without uncertainty (pp. 13–14).

### The 73.1% cross-model headline is not auditable

Figure 4 reports 73.1% test accuracy for pooled traces versus 36.0–59.4% for four single-source models, motivating the +13.7-point headline (pp. 6, 1–2). The arithmetic comparison to the displayed maximum is correct. The estimand is not recoverable: v1 omits target solver identity, task and Skill denominators, source trace counts, trace sampling/equivalence, updater identity/configuration, repeats, failures, uncertainty, and whether the pooled condition has more total evidence than each single-model condition.

Consequently, 73.1% is evidence of a reported condition mean, not evidence that model diversity caused transfer. The pooled condition may differ in volume, task coverage, failure-mode coverage, or selection. The claim that weaker source models provide better transferable signal is also observational: source models produce different traces and outcomes, and no matched trace-content or volume intervention isolates model weakness.

### Cross-role evidence shows contextuality, not a general role-transfer law

Figure 5 reports PDF Skill gains of +11.7 for PM→PM and +6.2 for DS→DS, but losses of −4.8 for PM→DS and −7.5 for DS→PM (p. 6). This is an important failure signature: the same nominal procedure can encode different output purposes and evidence-use conventions by role.

However, one Skill, two role labels, four aggregate arrows, and no stated solver/task/repeat/uncertainty details cannot establish that role specialization “emerges naturally” in general. Role and task family vary together. The experiment does not distinguish role-language cues from document type, requested artifact, source distribution, verifier semantics, or task difficulty.

### Efficiency evidence is a three-task case study

Appendix G measures two agents on three tasks and four Skill conditions, with four runs. Evolved Skills often reduce tokens and cost relative to handcrafted Skills, including the Kafka example highlighted in Figure 6. They do not do so consistently: Hermes on PPTX formatting rises from 335.5k to 476.5k total tokens and from $0.057 to $0.083 (pp. 6, 13). The text's claim that evolved Skills “consistently” reduce both token use and cost across other tasks overstates the table. The evidence supports task/configuration-specific efficiency effects, not a general production cost advantage.

## Official-release audit

The complete author-owned GitHub commit and paper-linked Hugging Face revision were inspected. The sole public commit was authored before v1 but committed/published eight days afterward; it is not proven to be the manuscript-time tree. The GitHub archive is the complete local snapshot because 56 binary files appear as LFS pointers in the pinned Hugging Face Git tree.

### What is released

The GitHub snapshot contains:

- 129 included tasks, all labeled `test`;
- role counts of DE 27, DS 23, GenAI 22, Infra 19, PM 16, SWE 22;
- 89 one-Skill, 24 two-Skill, and 16 three-Skill tasks;
- all 22 Skill labels in the released task assignments;
- 22 generated/default `SKILL.md` bodies and 22 `SKILL_HANDCRAFT.md` bodies;
- 129 generators, reference solutions, verifier suites, and task-source records;
- 39 tier-A and 90 tier-B source records.

The source records identify 90 released tasks as Claude-generated, 27 as author-authored (including 18 “hard”), and 12 as adapted from public sources. This makes the test slice inspectable enough for independent task/verifier audits and new trials.

### What is absent or inconsistent

The release omits:

- the other 253 tasks needed for the claimed 382-task benchmark;
- every train and validation task;
- EVOLUTION code and framework adapters;
- experimental traces and trace-pool assignments;
- update prompts, candidate versions, promotion/rollback histories, and final evolved Skills;
- run configurations, raw trial/result records, and aggregate-generation code.

Therefore none of the main paper results can be recomputed from the release. The absent train/validation tasks are especially consequential because they carry the evidence needed to audit cross-task, cross-role, and cross-model leakage.

There are additional synchronization warnings. The README advertises 382 tasks while its dependency header calls itself the broad set for a “current 369-task pool”; the archive actually contains 129 top-level task packages. The README declares the release `test_split`, but its quick-start and intended-use prose can be mistaken for a complete benchmark release. All dependency files are unpinned, and the top-level requirements note that system dependencies and full upstream harnesses are not installed, limiting reproducible execution over time.

The README describes a strict visible/oracle boundary, yet no released runner or sandbox enforces it. Oracle files coexist in each task directory with the visible files. A future runner can mount only `instruction.md`, `environment/`, and `output/`, but that is a prescription, not release evidence that paper trials prevented filesystem access to solutions, generators, tests, or provenance.

The release does preserve useful provenance labels, but public-source URLs are mutable and mostly lack immutable source revisions and content hashes. Skill transformation from a narrow source package into a broad cross-role procedure is not recorded. The task/Skill/verifier shared-authoring graph is also absent, preventing an audit of whether held-out tasks were independent of Skill authors and update designers.

## Unique insight

AFTER's deepest contribution is a warning about the **transfer graph**, not a proof that more diverse traces solve it. A revised Skill can appear reusable for at least five distinct reasons:

1. it captures a genuinely portable operation;
2. source and target tasks share authoring lineage, templates, or verifier semantics;
3. the update encodes target-relevant criterion cues exposed through feedback;
4. pooled traces increase volume or coverage rather than diversity per se;
5. configuration or missingness differences select easier valid runs.

A `train/test` label addresses none of these by itself. Valid procedural-transfer evidence needs a typed edge:

`source task instances + active Skill hash + solver/harness + observable trace/feedback view → updater/configuration + candidate lineage + promotion evidence → frozen target task/verifier lineage + target solver/harness → paired outcome distribution`.

The correct unit of analysis is therefore not “the Skill” and not even “the task.” It is a **versioned source-to-target transfer edge within a configured-system graph**. Local gain, cross-task reuse, cross-role transport, and cross-model consumption are different estimands and should never be collapsed into one evolution score.

A second insight is that role transfer cannot be interpreted from role labels alone. The PDF example may vary intended artifact, evidence selection, audience, and verifier consequences simultaneously. `skill-bench` should define role/context transport by changed and held-fixed primitives—not by nominal profession names—and diagnose which procedural clauses remain applicable.

## Limitations and validity threats

1. **Main results are not reproducible from the release.** The evolution harness, 253 train/validation tasks, traces, configurations, evolved Skills, and result rows are absent.
2. **Metric identity is internally contradictory.** Table 2 reproduces J.1's `M1` values while labeling them `M2`; J.2's caption then describes the `M1` fraction under an `M2` label.
3. **The 3.7–6.7 result is complete-case selected.** It covers 111 IDs present in both runs, with unexplained missingness and no task-level uncertainty.
4. **The 73.1% result lacks an identifiable estimand.** Target model, task/Skill set, trace counts, updater, repeats, and uncertainty are unspecified.
5. **Diversity is confounded with evidence volume and coverage.** One versus five tasks and pooled versus single-model traces do not hold trace quantity/content fixed.
6. **Configured-system identities are incomplete.** Display model names do not pin endpoints, prompts, harnesses, tools, budgets, sandboxes, retries, or dates.
7. **Attempt counts and failure handling are mostly absent.** `Natt` is defined but not instantiated, and environment/provider failures are not separated from task failures.
8. **No clustered or paired uncertainty is reported.** Tasks share Skill, role, authoring, verifier, and source lineages, making raw task/check outcomes dependent.
9. **Promotion can overfit validation semantics.** `δ`, validation estimand, feedback visibility, stopping, and repeated validation reuse are not specified.
10. **Cross-role variation is bundled.** Role, task family, artifact purpose, sources, and verifier consequences can all change together.
11. **Static treatment allocation is co-designed.** Instructions deliberately omit procedural details supplied by Skills, so effects are conditional on that disclosure boundary.
12. **Best-of-catalogue reporting selects outcomes.** Some static deltas use whichever of handcrafted or generated Skills performs better.
13. **“Expert” and “realistic” claims exceed reported authority evidence.** Reviewers are authors; qualifications, agreement, external validation, and occupational sampling are absent.
14. **Procedural-source provenance is mutable and transformation-light.** Public URLs lack pinned revisions/hashes, and adaptation into the evaluated procedure is not traced.
15. **Verifier validity is bounded.** Pytest can establish encoded functional consequences, not readability, maintainability, stakeholder fit, judgment, or professional readiness; the authors acknowledge some of these limits (Limitations, p. 6).
16. **Release splits conflict with the stated ratio.** The public slice has 129/382 tasks (33.8%), while Appendix D says 25% test per role–Skill cell; train is reported as 185 tasks, leaving 68 validation tasks if totals are exhaustive. Rounding cannot be assessed because full cell assignments are unreleased.
17. **Oracle isolation is declarative.** Release layout and README prescribe a visibility boundary but provide no runner evidence that paper trials enforced it.
18. **Efficiency generalization is overstated.** Three tasks and two agents include at least one evolved-Skill token/cost regression.
19. **Ethics/data description is inaccurate.** “All datasets used are public and were collected and preprocessed by their original authors” conflicts with 326 newly designed tasks, including 288 model-drafted tasks (Ethics Statement p. 7 versus Appendix E pp. 11–12).
20. **Contamination and authoring dependence are unmeasured.** Adapted public tasks and public Skills may overlap model training; authors can share assumptions across task, Skill, and verifier construction.

## Reproducibility and operational realism

Reproducibility is **moderate for the released 129-task static test substrate and poor for the paper's experiments**. The public packages provide real files, generators, reference witnesses, and executable checks across six technology-work labels. A third party can audit or run this slice after constructing a secure runner and pinning dependencies. The immutable archives, hashes, source counts, and release timing boundary are recorded locally.

Exact paper reproduction is currently impossible from public artifacts. Even if the missing code appeared, historical model endpoints and unpinned environments would remain a problem. A reproducible release would need all 382 task hashes and split lineage, immutable task/Skill/verifier authorship records, EVOLUTION and adapter commits, container digests, prompts, model endpoints/dates, budgets, trace records, feedback views, candidate Skill bodies, promotion decisions, invalid-run logs, attempt-selection policy, and task-level result tables.

Operational realism is mixed. The tasks produce code, spreadsheets, documents, presentations, configurations, and data artifacts, which is closer to knowledge work than short-answer testing. But the evaluation lacks stakeholder interaction, authorization, downstream use, irreversible effects, collaboration, live organizational context, maintenance outcomes, and qualified professional review. The represented six roles are technology-sector scenario labels rather than validated occupational constructs.

## Transfer to skill-bench

### 1. Treat every evolution comparison as a typed transfer edge

Use the existing longitudinal stream and component records to bind:

- immutable source task/equivalent-form IDs and authoring lineage;
- source Skill hash, solver, harness, environment, feedback visibility, and trace IDs;
- updater identity/configuration, candidate parent/child hashes, changed clauses, and promotion evidence;
- frozen target tasks/verifiers, overlap features, target solver/harness, and contamination boundary;
- all attempts, invalidity reasons, cost, paired outcomes, and task-clustered uncertainty.

No new schema is needed; this is the evidence discipline those contracts already anticipate.

### 2. Separate four claims and their denominators

Report independently:

1. source-context improvement;
2. equivalent-form cross-task reuse;
3. transport across changed work context/role primitives;
4. consumption by another configured solver.

For each, publish eligible tasks, attempted tasks, valid complete cases, missing/invalid rows, and exclusions. Do not let a 111-complete-case result inherit a 382-task denominator.

### 3. Factor diversity from volume

A credible trace-source experiment should match total trace count and, where possible, success/failure mix and task coverage. Compare at least:

- same-model/same-task traces;
- mixed-model/same-task traces;
- same-model/mixed-task traces;
- mixed-model/mixed-task traces;
- volume-matched shuffled or duplicate controls.

Use multiple sampled source pools and report variation across pools. This distinguishes model diversity, task diversity, trace volume, and failure coverage.

### 4. Make forgetting and negative transfer first-class

Preserve per-task paired deltas, negative-effect rate, worst-group change, and retired/superseded procedural clauses alongside the macro mean. Require a non-inferiority or bounded-harm gate on protected held-out forms before promotion. A positive global average must not erase PM/DS regressions or role-specific failures.

### 5. Define context transport by primitives, not labels

For a role-transfer test, record which elements change: intended artifact, audience, evidence authority, source format, operation, decision threshold, tool, verifier consequence, and safety/compliance obligations. Hold the rest fixed or declare the bundle. Diagnose clause applicability and contraindications rather than concluding that “PDF skill” transfers or fails as one unit.

### 6. Preserve intervention/instrument and feedback firewalls

A private check may expose failure consequences to an updater only if that visibility is an explicit treatment. Keep update feedback separate from final held-out verifier evidence; rotate equivalent forms when validation is repeatedly reused; record whether task, Skill, updater, and verifier authors share lineage. Criterion-aligned coaching is useful package efficacy, not independent transfer.

### 7. Keep claim ceilings explicit

Even a replicated cross-task effect would support procedural-package transfer within a frozen instrument. It would not by itself support tacit expertise transfer, occupational representativeness, professional artifact quality, production reliability, economic value, or deployment readiness. Those require the repository's participation, artifact-admissibility, expert-review, metric, and validity-argument layers.

## Action items for repository

- [x] Read the complete immutable v1 PDF/text and verify section, table, appendix, and release claims.
- [x] Inspect the complete author-owned GitHub snapshot and paper-linked Hugging Face revision with their eight-day post-v1 timing boundary.
- [x] Preserve the 382 claimed / 129 released test / 111 complete-case refinement denominator distinctions.
- [x] Identify the `M1`/`M2`, split, release-size, and ethics-description inconsistencies.
- [x] Map source-to-target transfer-edge requirements into existing procedural-skill, longitudinal, configured-system, firewall, task-health, metric, and validity contracts.
- [x] Add no queue task: the evidence sharpens existing contracts and does not expose a nonduplicate build gap.

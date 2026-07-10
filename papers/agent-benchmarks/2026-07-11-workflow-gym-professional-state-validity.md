# Workflow-GYM: end-state success is not yet professional-workflow validity

## One-sentence contribution

Workflow-GYM contributes a broad, expert-authored collection of 338 long GUI workflows across 56 specialized software environments and exposes persistent execution failures that short computer-use tasks miss, but its unreleased benchmark, outcome-only grading, uncalibrated expert pipeline, model-specific harnesses, and demonstrably non-clean showcase states mean that the reported pass rates support only a narrow configured-system result—not the paper's stronger claims about professional, economic, or end-to-end workflow capability.

## Why this matters

Workflow-GYM directly advances skill-bench charter objectives A, B, and C. It attempts to turn practitioners' daily procedures into natural-language tasks, configured environments, reference procedures, observable artifacts or GUI states, and repeatable checks across six broad domains. That is close to skill-bench's central expertise-to-evaluation problem, while the GUI modality provides a demanding test of environment state, tool realization, persistence, and workflow recovery.

The source is most valuable as a warning about **three boundaries that should not be collapsed**:

1. a final artifact/state can prove selected consequences without proving that a workflow stage occurred;
2. one expert path can witness solvability without being the only professionally valid path;
3. a VM can package software without proving a clean, equivalent, or realistic initial state.

This is a cross-domain methodological case, not a recommendation to narrow skill-bench to GUI work.

## Research question

The paper asks whether current GUI-agent systems can autonomously complete economically valuable, domain-specialized professional workflows from a natural-language objective in real software, and what long-horizon and execution-level failures limit them (paper pp. 1–3, 7–17).

The auditable question is narrower: across 338 author-selected tasks, what fraction of task-specific final-state or artifact criteria are judged satisfied in three runs by six model-specific configured systems under a 400-round cap? The paper does not identify an occupationally representative construct, a labor-substitution estimand, or a GUI-independent professional capability.

## Sources and reading record

**Paper read in full**

- Immutable record: https://arxiv.org/abs/2606.11042v3
- Immutable PDF: https://arxiv.org/pdf/2606.11042v3
- Local PDF: `data/papers/pdfs/2606.11042-workflow-gym-long-horizon-computer-use-agentic-tasks.pdf` (31 pages; SHA-256 `e50f0dd9e9bf026e2c0252ca0f1ffc0ae9f96a1b563ed6d24085d235aba2e5a8`)
- Local text: `data/papers/text/2606.11042-workflow-gym-long-horizon-computer-use-agentic-tasks.txt` (SHA-256 `399f444442359eac928c9b4a36224bcc54a3e75bacf35a31887b98f13c1463c4`)
- Date read: 2026-07-11 (local time).

**Official project release inspected**

- Project page: https://workflow-gym.github.io/
- Official site repository: https://github.com/workflow-gym/Workflow-GYM.github.io
- Pinned commit: `73c619a9f37056f51df2e00082c0816758090a10`, dated 2026-07-09.
- Local textual archive: `data/sources/releases/2606.11042v3-workflow-gym/workflow-gym-site-text-73c619a9f37056f51df2e00082c0816758090a10.zip` (SHA-256 `3432d632f7b7bf71d4d45e8d393cde0b74e7d7380bfabb5487612141ecacaa5c`; 77 entries; 5,001,320 uncompressed bytes). It preserves all HTML/Markdown/CSS/JavaScript/JSON/SVG/text/code files, including all 24 trajectory manifests. Large screenshots, video, fonts, and PDFs are represented by the complete tree manifest but are not mirrored locally.
- Tree manifest: `data/sources/releases/2606.11042v3-workflow-gym/github-tree.json` (2,088 entries, not truncated).
- Provenance and scope: `data/sources/releases/2606.11042v3-workflow-gym/provenance.json`.

The site commit is nearly a month after arXiv v3 and is **post-v3 evidence**, not the exact paper-time release. The page says “Dataset (Coming Soon).” The textual archive contains four showcase prompts and 24 action/thought trajectory manifests—six configured systems per showcased task—and the complete tree records their referenced screenshots; it does not contain the 338 task records, 56 VM images, initialization scripts, grader code, rubrics, scoring records, human validation records, or paper result inventory. No repository license is declared. The review therefore does not claim a benchmark replay.

## Methodology and system

### Expert-to-task construction

Seventy-one contributors reportedly participate across the lifecycle: workflow proposal, task specification, environment verification, instruction refinement, and evaluation validation. The group includes 51 practitioners and 20 students/trainees; 30 have more than five years of experience, five have three to five, and 36 have fewer than three years (Appendix A, paper pp. 22–23). They propose more than 1,000 candidate workflows from daily practice. Candidates must require specialized software and domain knowledge, be non-searchable, require at least 30 atomic actions, and admit objective success criteria (pp. 4–5).

The paper does not state recruitment frame, domain-by-domain counts, credentials, role-to-task assignment, compensation, training, contribution volume, independence, conflicts, or whether the same person authored the instruction, path, and check. “Domain expert” therefore covers materially different authority levels. The reduction from >1,000 candidates to 338 is not accompanied by a selection-flow table or rejection reasons, leaving likely **verifiability selection**: tasks survive partly because their outcomes can be automatically checked, not because they represent professional work frequency or consequence.

Each retained task includes a self-contained public instruction, expected artifact or GUI outcome, deterministic criteria where possible, and an atomic expert procedure whose strict execution should pass (paper pp. 5–6). The procedure is hidden from the baseline but used as a solvability witness and later as text/video guidance. This is strong authoring discipline, but it does not establish natural-language/procedure/check equivalence, alternative-path completeness, or professional-quality coverage.

### Environment construction

The authors package 56 software-version-specific full-system VMs. Task initialization injects resources and configuration, pre-launches the required software, removes login/authentication overhead, and claims that no task-specific operation has occurred (paper pp. 4–5). Experts then execute the reference procedure; defects can trigger environment, criterion, or instruction revision.

This design is reusable, but “agent behavior as the sole source of variation” (p. 5) is not demonstrated. VM image hashes, OS/display settings, task-overlay manifests, reset strategy, residual-state canaries, network policy, permissions, licenses, and software-specific nondeterminism are not reported. The official showcase supplies direct counterevidence discussed below: a task requiring creation of an `animal` Anki profile encounters “Name exists,” and the jamovi file chooser exposes both `Input` and `input` directories. Those are prior-state and placement ambiguities, not agent-only variation.

### Evaluation and configured systems

The benchmark has 338 tasks across six top-level and 23 fine-grained domains. Expert paths contain 30–110 actions: 129 “easy” tasks (30–44), 159 “medium” (45–60), and 50 “hard” (61–110) (paper pp. 5–6). Artifact tasks use rule-based or LLM-based checking; tasks without explicit artifacts provide the final screenshot and criteria to a VLM. Although the introduction calls each criterion unique, automatic, deterministic, and binary, §3.3 explicitly relies on model judges for some artifacts and GUI screenshots. The paper provides no criterion inventory, grader-type counts, prompt, parser, version, calibration sample, expert agreement, false-positive/negative study, or invalid/insufficient-evidence outcome.

Six models use model-specific agent frameworks because coordinate spaces, action schemas, and training assumptions differ. Every task receives one initial instruction, up to 400 screenshot-action rounds, and three trials; non-rule grading uses Seed-1.8 (paper pp. 7–9). This evaluates configured systems, but model rankings conflate model, adapter, coordinate transformation, prompt/loop, stopping policy, and tool semantics. The paper appropriately notes framework coupling, yet still labels rows by model alone.

The paper does not report API/model snapshots, harness commits, decoding parameters, dates, screenshot resolution, action latency, retry policy, timeout/wall-clock policy, invalid-run handling, token or monetary cost, per-trial results, task-level clustering, or confidence intervals. “Three independent trials” is asserted but independence is not defined; pass@3 naturally rises with three opportunities and is not directly comparable to average pass.

## Evidence and results

### Main performance

Across 338 × 3 = 1,014 trials per configured system, the paper reports average pass rates from 7.89% to 30.67% and pass@3 from 15.98% to 41.42%. Gemini-3.1-Pro has the highest average pass (30.67%); Kimi-k2.6 has the highest pass@3 (41.42%). Results decline across path-length bins, and domain averages vary substantially (paper pp. 7–9).

These are meaningful evidence that the selected tasks are difficult for these six systems. They do **not** establish that GUI workflow length causes failure: path length is an expert canonical-path property correlated with software, spatial control, task type, criterion count, author, and domain. Nor does a low score establish economic value, professional representativeness, or human-level distance; no matched human execution condition is reported.

### Outcome and trajectory failure analysis

Failures are divided into workflow incompletion, final-state-but-incorrect, and “other.” Across six aggregate model points, workflow incompletion correlates with overall success at Pearson `r = -0.97`, `p = 0.0010` (paper pp. 9–10). Because success and failure shares are compositional parts of the same denominator, this correlation is partly mechanical and six system aggregates do not support a general capability law.

The trajectory analysis identifies error propagation, workflow-stage omission, objective drift, insufficient software knowledge, and repeated identical actions for ten steps. More than 100 loops are reported, with domain enrichment ratios (paper pp. 10–14). The examples are incisive, but no sampling frame, coder count, blinded codebook, duplicate coding, agreement, adjudication, or denominator by system/domain is given. Only looping has an executable definition; the richer labels are retrospective narratives and can mix earliest cause, surface symptom, and evaluator interpretation.

The continuous-versus-snapshot interaction analysis is plausible: drag, geometry, and visually terminated operations expose states between observations that screenshot-action agents cannot see. But the benchmark does not tag such tasks prospectively or compare a continuous-observation treatment. It is a mechanism hypothesis, not an identified causal result.

### Guidance ablations

Textual expert procedures improve full-suite average pass by 2.76–12.23 percentage points depending on system. A separate 100-task, roughly software-balanced subset compares no tutorial, text, and text-plus-video for Seed-2.0-Lite and Gemini-3.1-Pro. Video raises pass@1 from 19→31 and 28→35 respectively; failed video-guided runs become much longer (paper pp. 14–18).

The paired direction is useful evidence that procedural representation changes execution. However:

- the paper reports no paired task-level uncertainty, randomization, order control, or multiplicity adjustment;
- the 100-case sample algorithm and seed are absent;
- the video condition includes both text and aligned frames, so “video value” is a package contrast;
- expert paths and criteria are co-designed, favoring canonical-path imitation;
- examples are described as “single-step” even though the benchmark requires ≥30 actions—the pivotal difference is one step, not the task;
- coordinate replay fails when live state diverges, showing that demonstration following and adaptive workflow competence are distinct constructs.

## Two official showcase traces

The post-v3 site exposes trajectories, not benchmark task packages or scores. They nevertheless reveal important operational behavior.

### Trace A: Anki vocabulary export (education/document workflow)

The public prompt requires creating an `animal` profile, creating a `zoo` deck, authoring five image-backed cards, studying in a prescribed order, and exporting `zoo.txt`. Six trajectory manifests contain 21–186 recorded steps. Several trajectories end with self-reported completion; the archive contains screenshots and action/thought records but no initial-state manifest, output file, checker, criterion judgment, or score.

The strongest finding occurs early in `task1-doubao2.1-sample-1`: when the agent tries to create the required profile, Anki reports **“Name exists.”** The agent then selects the existing profile and continues. This directly contradicts the desired clean-start semantics and makes the trial ambiguous: prior cards, decks, settings, or history could help, hinder, or contaminate completion. A final `zoo.txt` cannot prove that the required profile/deck/card construction happened in this run or that preexisting state was harmless.

### Trace B: jamovi Titanic logistic regression (data-analysis workflow)

The prompt requires loading `Titanic.csv`, viewing frequencies, computing `FamilySize`, fitting a specified binomial logistic regression, and returning AUC. Six manifests contain 17–95 steps. Some trajectories report AUC 0.789 or rounded 0.790; others terminate while still planning or navigating. Again, no source CSV, output analysis file, grader, score, or per-step state assertion is released.

Multiple trajectories encounter both `Input` and `input` folders while the task specifies lowercase `input`; one agent enters the wrong location and another explicitly reasons about case. This is not merely navigation difficulty: it is an overlay/placement ambiguity that should be caught by initialization conformance. Final AUC agreement can show a scalar consequence, but not that frequencies were inspected, `FamilySize` was correctly used rather than merely created, the exact model specification was applied, or the analysis artifact is reproducible.

Together these traces show why an end-state checker needs a declared **state-delta basis**: which initial facts were absent, which required stages should create which durable transitions, which preexisting state is forbidden, and which final evidence proves each transition.

## Unique insight

Workflow-GYM's distinctive lesson is that **workflow validity requires evaluating a transition system, not merely a long trajectory or final state**. A professionally meaningful task can be represented as:

`pinned initial state → stage precondition → action family → stage postcondition → downstream affordance → final consequence`.

The paper records an expert action sequence and checks selected final consequences, but it does not publish the middle contract. This creates four failure modes for the instrument itself:

1. **pre-satisfied stage:** prior state already contains the required object, as with the Anki profile;
2. **stage bypass:** an alternative mechanism produces the final artifact without exercising the intended competence;
3. **false canonicality:** a valid alternative path is penalized because it differs from the expert witness;
4. **consequence insufficiency:** a final scalar/file/screenshot cannot establish hidden intermediate requirements, as with jamovi's frequency-table and computed-variable stages.

The right response is not to score every click. It is to define a sparse set of professionally consequential stage transitions, each with a public basis, admissible alternative paths, pre/post evidence views, and necessity/sufficiency status. Process checks should be used only when the stage itself is part of the construct or when the final state cannot identify the required consequence.

A second insight is that “minimal instruction” versus “tutorial” is not simply hard versus easy. It is an intervention on where expertise resides: agent policy, public skill, environment affordance, or evaluator. Skill-bench should preserve this distinction with matched no-skill/public-skill conditions and an independent-rubric arm; Workflow-GYM's canonical tutorial and co-authored criteria otherwise risk measuring imitation of the benchmark author's path.

## Limitations and validity threats

### Content and professional validity

- Six broad domain percentages and 56 software packages do not form an occupational, economic, or task-frequency frame.
- Candidate filtering selects for long, specialized, automatically verifiable work; high-judgment or stochastic professional outcomes may be systematically excluded.
- Expert demographics are aggregate and mix practitioners with trainees. No task-level authority, role match, review independence, disagreement, or labor/time evidence is disclosed.
- “Daily practice,” “generate revenue,” “economically valuable,” and labor substitution are not validated by stakeholder use, organizational consequence, work frequency, wage/time weighting, or human comparison.
- Many showcased requirements are benchmark-like exact configurations; no evidence shows that the full task distribution reflects authentic ambiguity, source conflict, collaboration, compliance, or professional artifact conventions.

### Task and checker validity

- The hidden procedure is a solvability witness, not proof of instruction sufficiency, unique stage necessity, or alternative-path completeness.
- Final screenshots are weak evidence for hidden data structures; artifact files can be weak evidence for GUI-only or procedural requirements.
- Model-judge bias is not “minimal” merely because a rubric is predefined. Evidence-view sufficiency, calibration, invalid output, and abstention are unreported.
- Binary all-criteria success hides criterion count, severity, dependence, safety-critical gates, partial utility, and recoverable versus irreversible defects.
- Outcome-based refinement with a SOTA agent may remove tasks that expose current-system limitations or encode healthy-first/outcome-selection bias.
- The public showcase demonstrates residual and ambiguous initial state, undercutting the claim that no task-specific operation has occurred.

### Experimental and statistical validity

- Model-specific frameworks confound model and harness; framework realization is part of the treatment but is not independently pinned or crossed.
- Three repeats have no task-clustered uncertainty, run-level release, missingness policy, or independence audit.
- Average pass and pass@3 answer different questions; domain and difficulty comparisons lack uncertainty and cluster controls.
- Length bins are endogenous to one expert path and confounded with software and manipulation type.
- The six-point incompletion correlation is compositional and does not identify a causal mechanism.
- Failure coding and tutorial analyses lack reproducible annotation/reliability protocols.
- No time, cost, token, retry, or human-review burden is reported despite economic-value claims.

### Reproducibility and operational realism

The paper preserves a full PDF and describes a substantial construction process, and the official site publishes unusually rich action/thought manifests and referenced screenshot sequences for four prompts. Exact reproduction is nevertheless impossible from the inspected evidence:

- the 338 tasks, overlays, VM images, procedures, criteria, graders, results, and initialization scripts are not released;
- the official page explicitly marks the dataset “Coming Soon”;
- the site commit postdates v3 and has no declared license;
- showcased trajectory manifests have empty `query` fields and no linked score/outcome records;
- component versions, environment hashes, network/permission policy, reset evidence, costs, and invalid-run policy are absent;
- thoughts and final self-reports are not authoritative evidence of state or artifact correctness;
- real professional operation often includes authentication, collaboration, audit logs, safety constraints, revisions, and stakeholder review, which are removed or unmodeled here.

## Transferable benchmark design lessons

1. **Model workflows as sparse consequential transitions.** For each stage, record public requirement, precondition, postcondition, downstream dependency, admissible evidence views, and whether the stage is construct-essential or merely one witness path.
2. **Prove initial-state cleanliness.** Hash VM/base image and overlay; run absence/presence/placement canaries; reject a run when required-to-create objects already exist or duplicate case-sensitive paths create ambiguity.
3. **Separate witness, stage, and final checks.** A reference procedure proves one route; stage checks diagnose transition failures; final checks establish selected consequences. Do not infer one from another.
4. **Admit alternative professional paths.** Record equivalence classes and conditional branches; do not force agents to imitate one atomic click sequence unless procedure following is the intended construct.
5. **Type evaluator evidence views.** Use structural parsers for native artifacts, rendered views for appearance, screenshots for visible GUI state, and traces only for observable process claims. Missing evidence should yield `insufficient_evidence` or `invalid_run`.
6. **Version configured systems independently.** Pin model, harness, coordinate adapter, action schema, observation policy, prompt, stopping policy, environment, grader, and feedback/tutorial package.
7. **Treat tutorials as expertise interventions.** Use matched conditions and independent rubrics to distinguish planning support, interface localization, criterion leakage, canonical-path imitation, and genuine transfer.
8. **Preserve plural outcomes.** Report final correctness, stage completion, artifact integrity, benign utility, safety, recovery, efficiency, invalidity, and diagnosis separately before aggregation.
9. **Use hierarchical inference.** Macro-average tasks, cluster by workflow family/software/author, report paired replicate uncertainty, and predeclare missing/timeout/provider-failure policy.
10. **Bound professional claims.** Cross-domain software coverage is not occupational representativeness; an expert-authored solvable task is not an economic-value or deployment-readiness argument.

These obligations already map to skill-bench's task-projection manifest, persistent-workspace records, artifact-view admissibility, configured-system identity, procedural-skill ablation, task health, metric monitoring, validity arguments, and cross-record evidence-chain audit.

## Concrete repository actions

1. **Do not add a duplicate workflow schema.** Extend the next diverse pilot or conformance fixture using existing projection/workspace/artifact-view machinery to represent sparse stage transitions: precondition, postcondition, evidence view, alternative path, downstream consequence, and necessity status.
2. **Add residual-state canaries to future environment tasks.** Before capability evidence is admitted, verify that required-to-create objects are absent, required inputs occur at exactly one declared path, output roots are clean, protected state is unchanged, and cleanup/reset restores the pinned inventory. The Anki `Name exists` and `Input`/`input` cases should be retained as external evidence for these tests.
3. **Require a process-to-consequence crosswalk only where needed.** For requirements such as “inspect frequencies” or “compute and use FamilySize,” predeclare what artifact/trace/state evidence can establish the stage and what final scalar cannot establish. Fail closed as `insufficient_evidence`; do not turn every click into a rubric.
4. **Do not import Workflow-GYM's leaderboard or professional/economic claims into canonical evidence** until an immutable task/result release exposes task records, component versions, run validity, graders, replicate outcomes, costs, and task-clustered uncertainty.

No new queue task is added. The executable obligations overlap the completed task-projection, artifact-view, and persistent-workspace slices and should be consolidated into future cross-domain pilot validation rather than becoming another standalone subsystem.

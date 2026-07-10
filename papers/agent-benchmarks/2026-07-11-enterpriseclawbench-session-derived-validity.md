# EnterpriseClawBench: real-session provenance is not task-fidelity evidence

## Source and review status

**Deep review.** I read the complete immutable arXiv v1 local PDF and local text extraction and inspected the complete official repository snapshot pinned below.

- Paper: Jincheng Zhong et al., *EnterpriseClawBench: Benchmarking Agents from Real Workplace Sessions*, arXiv:2606.23654v1 (22 June 2026), https://arxiv.org/abs/2606.23654v1
- PDF: `data/papers/pdfs/2606.23654v1-enterpriseclawbench-session-derived-enterprise-benchmark.pdf` (22 pages; SHA-256 `9f39da53875a63d9af925626c44e92debb254502e9876a8d40d1f95301dbb3ee`)
- Text: `data/papers/text/2606.23654v1-enterpriseclawbench-session-derived-enterprise-benchmark.txt`
- Official release: https://github.com/FrontisAI/EnterpriseClawBench at commit `68507699d1a61700f4281f1f34dcadb20f2de06d`
- Archive: `data/sources/releases/2606.23654v1-enterpriseclawbench/FrontisAI-EnterpriseClawBench-6850769.zip`
- Provenance: `data/sources/releases/2606.23654v1-enterpriseclawbench/provenance.json`

The inspected commit is about two days after v1 submission, so release behavior is evidence about the public method, not necessarily the exact paper-time implementation. The proprietary 852 tasks, source sessions, outputs, and result tables are unavailable; headline results therefore remain paper reports.

## One-sentence contribution

EnterpriseClawBench contributes a retrospective projection pipeline that turns naturally occurring workplace-agent sessions into reproducible artifact tasks, while its public release reveals why real demand provenance alone cannot establish source-to-task fidelity.

## Why this matters

The paper directly tests a central skill-bench uncertainty: whether observed knowledge work can become benchmark material without losing the competence expressed in the original episode. It offers unusually concrete construction machinery, configured-system evaluation, and public-safe traces, but those traces expose transformation and hindsight risks that must become explicit validity evidence.

## Contribution and research question

EnterpriseClawBench asks whether naturally occurring workplace-agent sessions can be converted into reproducible, artifact-centric benchmark tasks at scale, and whether those tasks expose model–harness, artifact, cost/runtime, judge, and skill-transfer differences. Its distinctive contribution is not another enterprise task list but a **retrospective projection pipeline**:

`session turns + attachments + traces + workspace state → task instances → mechanical gates → self-contained decision → single-turn rewrite → role/skill labels → deliverables → hard rules + semantic rubric → sandboxed trial`.

From one AI startup of more than 100 employees, March–May 2026, the authors recover 5,291 raw TaskInstances, retain 3,813 after four mechanical checks, and keep 852 after self-containment review (paper pp. 2–3). A manually audited 120-task Lite set supports a 32 configured-system leaderboard; four DeepAgents configurations are run on all 852 tasks (pp. 4–7). The method directly advances skill-bench's expertise-to-evaluation question, but its unique warning is stronger than its headline: **real provenance supplies demand realism, not construct preservation**. Every projection stage can change what competence the task measures.

## Methodology and system

### Source recovery and projection

The source is one proprietary deployment with private/group chat, uploaded files, tool traces, generated artifacts, and persistent Linux state (paper p. 3). Sessions are split/merged into TaskInstances. Length, fixture lookup, redaction recovery, and public-network checks run in parallel; a mechanical intersection retains 3,813. An LLM then decides self-containment, rewrites retained multi-turn requests as standalone prompts, labels seven role classes and 45 role-specific skill subclasses, infers deliverables, produces hard checks and a fixed five-dimensional semantic rubric, and packages tasks (pp. 2–4, 10–18).

The release makes the stage boundary unusually inspectable. `construction/README.md` documents 16 file-mediated stages and explicitly says the human-audited kept-120 flow is excluded. `stage_06_prompt_rewrite.py` sends the self-containment payload and prior decision to an LLM, stores only the rewritten prompt and attempt metadata, and fails the entire stage if any call fails. `stage_11_semantic_rubric.py` gives another LLM the rewritten prompt, inferred outputs, hard rules, and prepared input evidence, then copies the same 3–8 generated guidance items into all five weighted dimensions through `build_semantic_rubric`. This is a reproducible software pipeline, but not an independently validated source-to-task equivalence protocol.

### Evaluation

Trials are independent and nominally non-stateful. The runner records outputs, traces, completion, runtime, token use, cost, tool calls, and warnings (paper p. 4). Hard rules cover delivery properties such as count, type, non-emptiness, openability, tracebacks, and placeholders. Semantic scoring uses grounded accuracy (0.30), relevance (0.20), depth (0.20), utility (0.20), and communication (0.10). Text-like artifacts go to a text judge; HTML, office documents, PDFs, spreadsheets, and images are rendered and sent to a visual judge. The public evaluator correctly fails closed when visual evidence cannot be generated rather than silently falling back to text (`docs/evaluation_protocol.md`, `evaluation/.../judge.py`). A missing required artifact forces zero.

The public optional sandbox wrapper uploads fixtures, invokes a selected agent/model through `sandbox_sdk`, downloads `/workspace/outputs`, history, response, usage, and metadata, then kills the sandbox. The repository separates runner from evaluator, which is good configured-system discipline, but the paper does not specify repetitions: figures and tables appear to use one outcome per task/configuration, with no sampling uncertainty.

### Skill-transfer experiment

For one subclass—frontend page generation—a consumer is run on ten in-domain tasks; traces, artifacts, and Sonnet 4.6 feedback are given to one of three skill creators; the generated, consumer-specific skill is injected into four consumers and evaluated on five held-out tasks (paper pp. 6–7, 18–21). The 4×3 creator–consumer matrix reports deltas from −0.323 to +0.178 and an overall mean of +0.009. The design usefully separates creator from consumer, but five tasks, no repeated trials, one subclass, reused baseline scores, and judge-derived training feedback do not establish stable class-level transfer.

## Evidence and what it supports

1. **Demand-source evidence:** 852 tasks can be projected from a real deployment archive, spanning seven reported role classes, 45 subclasses, 719 fixture files, and 887 deliverable requirements (pp. 3–4). This supports pipeline yield and within-deployment diversity, not population representativeness.
2. **Configured-system dependence:** Lite scores range from 0.200 to 0.663 across 32 reported harness–model pairs; Claude models fall sharply under Hermes, attributed by trace inspection to approvals, delegation, and truncation (pp. 4–5). This is persuasive descriptive evidence that harness identity matters, but there are no repeated runs or controlled adapter ablations.
3. **Artifact-route dependence:** rankings vary by deliverable type; visual spreadsheets/presentations score higher, while a 48-packet human audit finds visual-judge Spearman −0.259 versus text 0.790 (pp. 5, 7). This directly undermines treating the main leaderboard as one homogeneous measurement scale.
4. **Scale check:** the four-model full-set ordering resembles Lite ordering (p. 6), but preserving an ordering does not validate task fidelity, rubric accuracy, or score comparability.
5. **Skill heterogeneity:** creator–consumer fit can help or harm (pp. 6–7). The evidence supports treating a skill as a versioned intervention with adverse-transfer risk, not a universal capability improvement.

No confidence intervals, repeated-run variance, clustered uncertainty, missingness denominators, total benchmark cost, per-task budget policy, or formal human audit protocol are reported. Figure 1 annotates costs/runtimes, but the paper does not provide reproducible raw records.

## Two public-safe traces: what release inspection reveals

### Trace 1: office floor plan (`i0001`)

The raw session has an employee request for a dimensioned 13,650×8,300 mm office plan with two fixed meeting rooms and 30 desks, followed by a long agent execution with repeated file-write errors before eventual HTML delivery (`raw_session_example/.../history.jsonl`, lines/events 5–22). The projected task retains the substantive requirements and adds an explicit HTML/output-path contract (`example_runs/.../i0001/task.json`). That is a plausible projection.

However, the generated rubric inserts an unstated **≥900 mm workstation-passage threshold** and repeats the same seven guidance bullets verbatim under all five dimensions. The source user requested ordinary circulation, not that numerical threshold. Thus the public example demonstrates both hidden-obligation creation and pseudo-multidimensional scoring: groundedness, relevance, depth, utility, and communication are nominally separate but operationalized by identical criteria. An answer-bearing criterion is generated from the task and evidence by the same pipeline that grades it; there is no independent expert or source-session approval.

### Trace 2: image-style analysis (`i0004`)

The source session is more revealing. The user repeatedly asks the agent to inspect an uploaded image; after archive recovery the original agent explicitly says it lacks vision, asks for a description, receives a detailed user-authored style analysis, produces several low-quality artifacts, is criticized, and records lessons (raw history events 35–142). The projected task instead asks a fresh agent to inspect `media.jpg` and analyze micro-3D style. It omits the failed source-agent interaction, subsequent user-provided answer, dissatisfaction, and iterative repair. The rubric then encodes likely answers—left/top lighting, rounded forms, gradients, micro-3D thickness—across every dimension (`i0004/task.json`).

This is not merely anonymization. It changes the construct from **recovering and improving a design artifact through a difficult multi-turn interaction** to **single-turn visual analysis**, while using hindsight from the session to author answer-bearing criteria. The provenance is real, but the benchmark task is a retrospective counterfactual. It may be useful, yet it cannot be called a faithful replay without source-to-task equivalence evidence.

A third public task (`i0003`) merges two user turns into a sensible Q-cute 3D crown request, but again all dimensions share identical guidance and the release labels all three public tasks `product_project_delivery__project_product_plan`, including pure image-style analysis. That visible taxonomy collapse weakens task-class skill claims.

## Unique insight: session-to-task projection needs a counterfactual validity record

Existing source provenance asks “where did this task come from?” EnterpriseClawBench shows the missing question is: **which intervention turned the observed episode into the benchmark counterfactual, and what claim survives that intervention?** At least six distinctions are required:

1. **Observed demand:** what the employee actually requested, including ambiguity and evolving context.
2. **Observed resolution:** what the deployed agent/user did, including clarification, failure, repair, and acceptance/rejection.
3. **Projection intervention:** split/merge, omitted turns, rewritten requirements, restored data, environment substitutions, and hindsight-derived rules.
4. **Target counterfactual:** what a fresh configured system is now asked to do.
5. **Equivalence evidence:** source-user/expert review, preserved decision state, alternative valid paths, and tests that omitted context is irrelevant.
6. **Licensed claim:** replay fidelity, demand-inspired coverage, diagnostic calibration, or merely synthetic task utility.

A “real-source” boolean collapses these. The public `i0004` trace proves why this matters: demand provenance is genuine while replay fidelity is weak. This requirement is nonduplicate but belongs inside existing expertise-transfer, projection/provenance, validity-argument, task-health, and bundle records rather than a new subsystem.

## Limitations and threats to validity

### Private-data unverifiability and selection

The proprietary source prevents independent audit of source-session sampling, consent, employee/customer authorization, redaction errors, prompt rewrites, fixtures, exclusions, Lite selection, raw scores, or adjudications. Ethical guidance says organizations “should obtain proper authorization” (p. 8) but does not report this deployment's consent basis, notice, opt-out/withdrawal, purpose limitation, retention, contributor roles, or whether session users approved benchmark reuse. The funnel is outcome-selected for recoverable, public-network-stable, self-contained episodes; it systematically excludes clarification-heavy, stateful, inaccessible, or live-system work—the very conditions that may define consequential workplace expertise.

### Hindsight and author/judge dependence

Original outputs and traces inform task recovery; input evidence and rewritten prompts inform rubric generation; Sonnet feedback trains skills; Sonnet is also the main judge. Without provenance for which source fields were visible at each stage, answer leakage and hindsight-derived obligations cannot be separated from legitimate reconstruction. The authors do not report independent task authors, rubric authors, judges, or blind validators.

### Construct compression

Multi-turn sessions are rewritten into single-turn prompts. Persistent state and organizational conventions become explicit text or disappear. Clarification skill, social coordination, temporal updates, acceptance/rework, and tacit norms can be removed. The method therefore measures performance on projected standalone artifacts, not the complete workplace sessions from which they came.

### Measurement

Hard checks are mostly file hygiene, while semantic criteria are broad, dependent, and duplicated across dimensions in public examples. Visual judges receive rendered images only, so spreadsheet formulas, document structure, accessibility, provenance, and hidden state may be unobservable. The authors' own negative visual human correlation makes the main mixed-route score unsuitable as a single interval-like construct. Human calibration uses only 24 text and 24 visual packets; rater count, expertise, blinding, sampling, agreement, and adjudication are absent.

### Operational realism and reproducibility

The code is substantial and inspectable: 131 tracked files, staged manifests, strict visual routing, audit artifacts, and tests. With package-local paths, 6 evaluator and 5 sandbox tests passed; 12/13 construction tests passed, with one semantic-rubric dry-run test failing during evidence preparation in this environment. Full construction requires a proprietary source archive and paid LLM calls; paper results require unavailable tasks, outputs, APIs/models, and judge records. The public snapshot includes one sanitized source session, three generated task packets/runs, and no paper leaderboard data. It demonstrates interface reproducibility, not result reproduction.

## Comparison with adjacent evidence

- **Workspace-Bench** releases a large authored file substrate and dependency metadata, enabling artifact-level audits absent here; EnterpriseClawBench adds naturally occurring demand but weaker external auditability. Both require separating source availability, relevance, observed use, and causal use.
- **GDPval** has expert-authored occupational tasks and a principled occupation frame but weak probability sampling; EnterpriseClawBench has behaviorally sampled demand from one organization but no population frame. Neither licenses economy-wide workplace capability.
- **Anchor** compiles a formal specification into prompt, environment, oracle, and verifier, reducing some drift while risking shared-generator errors. EnterpriseClawBench begins with observed sessions but uses multiple LLM projections without a common semantic certificate. Together they show lineage is not equivalence.
- **Workflow-GYM/SaaS-Bench** preserve executable application workflows and state more directly; EnterpriseClawBench covers richer file artifacts but compresses multi-turn organizational work into standalone tasks.
- **Evidence-centered validity** requires claims, warrants, and evidence; “real source” is content-origin evidence, not a warrant that a rewritten task measures the original workplace competence.

## Transfer to skill-bench

### Benchmark-design implications

1. Represent source-derived tasks as **versioned projections**, not copies. Preserve source episode hash/access class, selected turn range, observed outcome/acceptance, every transformation, author/model, rationale, and before/after hashes.
2. Separate `demand_provenance`, `projection_fidelity`, `task_reproducibility`, `measurement_validity`, and `population_generalization`. Never infer one from another.
3. Require a **projection-delta review** for omitted context, added explicitness, hindsight-derived requirements, environment substitutions, removed clarification opportunities, and changed artifact contracts.
4. Treat source outputs/user feedback as protected construction evidence. Record whether each rubric/check was source-explicit, source-consequential, expert-added, or model-inferred; fire-wall answer-bearing hindsight from trial-visible materials.
5. Keep semantic dimensions operationally distinct. Reject bundles where identical guidance is copied across purported constructs unless the score is explicitly a single holistic judgment.
6. Stratify uncertainty by task, source session, employee/team, subclass, artifact route, judge, model, and harness; use repeated trials before attributing compatibility failures.
7. For real-session contributions, link participation/consent and transformation authority. Redaction is not authorization, and approval must not propagate through rewritten prompts or synthetic rubrics.
8. Label one-deployment results as within-deployment instrument evidence. Do not claim enterprise-work capability, economic coverage, or professional readiness.

## Concrete repository changes

No new queue task is added. The evidence refines existing machinery:

- Extend the existing provenance/projection records when next consolidated with `observed_episode`, `observed_resolution`, `projection_operations`, `omitted_context`, `hindsight_sources`, `counterfactual_target`, `equivalence_review`, and `licensed_use`.
- Add a planted validation case modeled on public `i0004`: a real multi-turn failure plus later user-provided answer must not silently become a “faithful replay.” The validator should allow `demand_inspired_task` while rejecting `session_replay_fidelity` absent independent equivalence evidence.
- Add a rubric-quality check that detects identical task-specific guidance across distinct score dimensions and requires either criterion remapping or a declared holistic score.
- For any session-derived pilot, sample rejected as well as accepted episodes and report exclusion by ambiguity, missing fixture, private network, statefulness, redaction, and projection failure to expose construct loss.

## Bottom line

EnterpriseClawBench provides the most concrete public implementation reviewed here for turning real agent sessions into benchmark packets, and its configured-system, artifact-route, cost/runtime, and creator–consumer framing are valuable. But the release's own examples show that **real-source provenance can coexist with counterfactual rewriting, hidden obligations, taxonomy collapse, rubric duplication, and hindsight leakage**. The benchmark supports claims about performance on a proprietary, retrospectively projected task suite. It does not yet establish faithful replay of workplace sessions, representative enterprise capability, or professionally valid artifact quality. For skill-bench, the durable lesson is to make projection deltas and claim licensing first-class evidence—not to adopt “real sessions” as a shortcut to validity.

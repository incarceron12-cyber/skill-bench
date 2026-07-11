# WorkArena++: executable composition increases horizon, not demonstrated professional validity

**Source type:** Deep review of the complete immutable arXiv v2 paper and a pinned official post-paper release  
**Paper:** Léo Boisvert et al., *WorkArena++: Towards Compositional Planning and Reasoning-based Common Knowledge Work Tasks* (NeurIPS 2024 Datasets and Benchmarks; arXiv:2407.05291v2, 5 February 2025)  
**Immutable paper:** https://arxiv.org/abs/2407.05291v2  
**Local PDF:** `data/papers/pdfs/2407.05291v2-workarena-plus-compositional-knowledge-work.pdf` (SHA-256 `9a3f424bfcdb2e5b2098c9fa00269a4dac371c11dada4bd4eec436bb2b61d479`, 56 pages)  
**Local text:** `data/papers/text/2407.05291v2-workarena-plus-compositional-knowledge-work.txt` (SHA-256 `804757230ddfd396d67e330ada59fb481cf562cdcf5113ca5802d7dc43bccdbe`)  
**Official repository:** https://github.com/ServiceNow/workarena  
**Pinned archive:** `data/sources/releases/2407.05291v2-workarena-plus/workarena-a772230a94cf1caf4166b8ead3983f3b3786455b.tar.gz` (SHA-256 `be240b104fb0290127613f60352af879eadfbe865f99f1dc6e1b077c5e0f83d2`)  
**Release provenance:** `data/sources/releases/2407.05291v2-workarena-plus/provenance.json`

> **Timing boundary.** Commit `a772230a94cf1caf4166b8ead3983f3b3786455b` is dated 3 February 2026, nearly one year after v2. It is evidence about a later official implementation, not the manuscript-time code. No ServiceNow instance was provisioned and no reported run was reproduced.

## Review judgment

WorkArena++ makes an important engineering advance over atomic WorkArena: it turns seeded database setup, browser actions, backend/UI validators, and cleanup into reusable workflow components, and adds a ticket-plus-knowledge-base condition that withholds the explicit procedure. This produces longer, stateful, executable tasks with a large human–agent gap.

But “compositional” has two different meanings here. The implementation composes setup/oracle/validator code; the paper infers that the resulting tasks measure planning, reasoning, memory, and realistic knowledge work. The first claim is well supported. The second is only weakly validated. The 341 workflows are authored variants concentrated in one ServiceNow installation, skill labels are assigned rather than independently measured, and the experiment does not isolate whether failures arise from workflow dependencies, UI navigation, context truncation, instructions, or the declared capability. Composition raises horizon and prerequisite burden; it does not by itself establish construct coverage.

## One-sentence contribution

WorkArena++ supplies an inspectable mechanism for composing executable, stateful browser workflows, but its evidence establishes increased horizon and difficulty rather than occupational representativeness or isolated planning-and-reasoning validity.

## Contribution and research question

The paper asks whether web agents can complete common enterprise workflows that require more than WorkArena's 33 atomic UI tasks. It contributes (pp. 1–9, 37–46):

1. 341 workflow definitions, each rendered as L2 explicit instructions and L3 ticket/knowledge-base work, for 682 task classes;
2. five author-assigned skill families: planning/problem solving, retrieval, data-driven reasoning, memorization, and infeasibility recognition;
3. seeded task-instance generation and a 235-instance-per-level curriculum intended to balance skill coverage and redundancy;
4. per-task user accounts, installer-managed configuration, and teardown for improved isolation;
5. composable Playwright “oracle” functions and validators that can emit observation/action demonstrations;
6. baseline trials on five configured model agents plus a 15-person feasibility study and qualitative trace analysis.

The strongest reusable contribution is not the task count. It is the coupling of **workflow generation, executable ground truth, state-based validation, and reversible setup**.

## Methodology and system

### Task source and composition

Each L2/L3 pair implements the same workflow with a different disclosure treatment (paper pp. 4–6). L2 enumerates steps. L3 starts on a private ticket, requires finding an internal protocol, and requires closing or skipping the ticket. Workflows mostly chain WorkArena L1 primitives, with some new record-editing blocks. Examples include assignment, workload balancing, schedule construction, deduplication, chart-driven follow-up actions, expense rules, knapsack-like selection, and onboarding.

The paper does not report a systematic occupational sampling or expert elicitation procedure. O*NET appears only as a future source (p. 56). “Routinely performed” and “realistic” therefore describe author-designed scenarios, not demonstrated prevalence, consequentiality, or expert fidelity. Many variants share the same workflow skeleton, UI, and generated data. Counting 682 task classes overstates independent construct breadth because each of 341 workflows appears twice and many classes are parameter/configuration variants within common buckets.

### Environment, state, and reset

Agents act through BrowserGym on remote ServiceNow Personal Developer Instances. Observations include goal, AXTree/HTML-derived state, focused element, prior action error, and screenshots plus set-of-marks for the VLM. Actions are restricted high-level browser/chat/infeasibility primitives, one per step (pp. 7, 18–20).

The paper's isolation mechanism creates a fresh user per task and deletes it afterward; the installer standardizes themes, knowledge bases, forms, lists, and system parameters (p. 6). The later code confirms base-task user creation and deletion (`tasks/base.py:107–157,185–202`) and compositional teardown delegation (`compositional/base.py:264–270`). Representative tasks also create and delete incidents and expert users (`work_assignment.py:87–159,250–304`). This is stronger than browser-only reset, but not an attested full snapshot restore. Cleanup is task-specific and assumes all side effects were enumerated; the paper provides no reset-differential tests, collision rate, teardown-failure ledger, or proof that themes, caches, sessions, asynchronous jobs, and unrelated records return to a canonical state.

The later release also changes operational accessibility: absent explicit environment credentials, `instance.py:48–95,123–152` loads a gated Hugging Face instance pool and requires a shared XOR seed. That is inspectable code but not a fully self-contained public backend. The 2026 access path cannot be projected backward onto the 2025 paper.

### Evaluators and partial credit

The paper describes WorkArena tasks as certifiable with oracles and binary validators inspecting database and page state (pp. 3, 45–46). The later composition base validates the next designated subtask in sequence, advances an in-memory `valid_index` only when its reward reaches 1, and emits only final 0/1 (`compositional/base.py:215–262`). Thus there is **validation progress during an episode but no reported partial-credit score**. Progress depends on repeated validator calls and order, not merely final state.

Some task families override this with global state checks. Work assignment, for example, queries each incident and accepts any expert whose ID belongs to the incident category, then delegates L3 closure validation (`work_assignment.py:250–290`). This usefully grades outcome equivalence rather than one oracle path. Yet evaluator semantics vary between sequential prerequisite gates and global predicates, and the top-level binary score hides which obligations were satisfied, reversed, skipped, or never evaluated.

A consequential subtlety is that sequential validation can make the instrument history-dependent: if a later valid state is reached before an earlier validator advances, credit may depend on when validation was polled. Conversely, validated progress stored in `valid_index` may remain advanced even if a later action reverses an earlier side effect unless a global validator rechecks it. The paper does not specify auto-validation cadence for agents; it explicitly says humans had continuous plus button-triggered validation (pp. 14–15). That interface difference is not shown to preserve score semantics.

Infeasible tasks use a privileged `report_infeasible` role and substring matching over one of the configured reasons in the later base (`compositional/base.py:327–358`). This tests recognition under an action affordance designed for the benchmark; it does not test calibrated refusal under ordinary professional communication, nor the completeness or faithfulness of justification.

### Curriculum and configured baselines

Task seeds generate thousands of configurations. The curriculum samples author-defined buckets with manually specified weights and reserves meta-seeds 0–9 for evaluation (pp. 7, 37–38). The later `curriculum.py:55–128` confirms markedly different category mechanics: for example, planning uses two seeds and weights up to nine per bucket, retrieval seven seeds with unit weights, and reasoning one seed with large within-bucket weights. “Uniform across skills” is therefore a constructed allocation, not uniform sampling of task classes, occupations, workload frequency, or difficulty.

Baseline agents receive full thought/action history, parser retries, model-specific context caps, and a 50-step cap; AXTree content is truncated from the end when needed (pp. 7, 18). These are configured-system treatments. The paper compares them to L1 and other benchmarks, but does not factorially isolate composition, instruction condition, history, modality, or step budget.

## Evidence and results

On the 235-instance curriculum per level, GPT-4o scored 3.0% on L2 and 0% on L3; GPT-4o with vision scored 3.8% and 0%; GPT-3.5, Llama-3-70B, and Mixtral-8x22B scored 0% on both. The same paper reports GPT-4o around 42% on WorkArena L1 (Table 2, p. 8). This strongly establishes a difficulty increase for these 2024 configured agents, but the floor effect prevents fine diagnosis and cannot identify which added dependency caused failure.

Fifteen volunteers attempted a 98-instance subset after 15 minutes of training and 15 minutes of exploration. Humans scored 93.9% overall versus GPT-4o's 2.1% on that subset (pp. 8, 13–17). This supports feasibility under the study conditions, not broad occupational validity. Eleven of fifteen had worked at ServiceNow, all held undergraduate degrees, tasks per participant were limited, learning was observed, humans had no action cap, and a general announcement explained that ticket closure had to be saved. The paper candidly records these threats. “Reasonably easy for humans” should be bounded to this small convenience cohort and assisted event.

The qualitative error analysis identifies retrieval/bid errors, insufficient exploration, invented actions/buttons, goal misunderstanding, thought/action inconsistency, hallucinated consequences, and loops (pp. 8, 47–54). It provides useful trace examples but no coding protocol, counts, denominator, multiple raters, agreement, or earliest-cause method. Claims that failures are mainly planning/reasoning rather than UI interaction are therefore interpretive, especially when examples include iframe identifiers, hidden tabs, folded menus, and action-vocabulary errors.

The only context ablation is on atomic L1 with Llama-3; 13K–130K context yields similar success (p. 56). It does not support claims about context or memory in L2/L3, where truncation and full-history growth matter most.

No dollar cost, task latency distribution, setup/teardown failure rate, API retry rate, or end-to-end runtime is reported. A four-A100 deployment is specified for open models, and the 50-step cap is explicitly budget-driven, but operational cost remains unquantified.

## Unique insight

> **Executable workflow composition is a task-construction primitive, not a validity argument.**

Composing atomic setup, oracle, and validator functions gives cheap variation, longer horizons, deterministic consequences, and demonstration traces. It can also preserve atomic-task artifacts: repeated menu navigation, benchmark-specific action syntax, sequential validator polling, and generated-data cues scale with every composed step. Without an explicit dependency graph and component-level outcome ledger, a lower composite score cannot distinguish emergent planning failure from the multiplication of atomic failure probabilities.

For skill-bench, every composite task should carry two separate records:

1. a **workflow dependency contract**: obligation nodes, prerequisites, produced/consumed state, allowed equivalent paths, reversibility, and terminal consequences;
2. a **construct argument**: why combining those nodes adds the claimed judgment or coordination demand, with expert/source evidence and an ablation against matched atomic tasks.

A simple diagnostic baseline is predicted composite success under an independence model (plus uncertainty), compared with observed success. A gap may suggest dependency/planning burden, but causal interpretation still requires matched presentation, horizon, UI, and information-budget controls.

## Limitations and validity threats

1. **No workflow provenance study.** No occupational sampling, frequency evidence, expert-authorship protocol, or expert fidelity ratings support “routine” and “realistic.”
2. **Task-count dependence.** L2/L3 pairs and shared buckets/templates are not 682 independent work constructs.
3. **Assigned skill labels.** Categories overlap and are not validated through item-response structure, interventions, or differential expert/novice evidence.
4. **Composition confounding.** More actions, UI transitions, context, error opportunities, and prerequisites change together.
5. **Severe floor effects.** Near-zero agent scores make model and capability comparisons uninformative.
6. **Human-study limits.** Small convenience sample, ServiceNow affiliation, unequal action budgets, learning, and a task-relevant announcement bound the human ceiling claim.
7. **History-dependent grading risk.** Sequential validator state and polling cadence can differ from final-state global correctness; reversals may not be rechecked.
8. **Binary score compression.** No criterion vector, partial credit, earliest failed dependency, or severity/consequence report survives to the main metric.
9. **Reset uncertainty.** Per-task users and custom teardown improve isolation but do not prove complete state restoration or collision freedom.
10. **Weak error evidence.** Rich anecdotes lack systematic sampling, frequency, coder reliability, and root/surface separation.
11. **Configured-system confounds.** Context limits, end truncation, screenshots, thought history, retries, action vocabulary, and 50-step cap differ in their interaction with models.
12. **Contamination and saturation.** Public tasks, protocols, code, validators, seeds, and oracle traces make future model exposure plausible; seed reservation does not hide templates or solutions.
13. **Trace leakage.** Oracle traces are useful training data but require strict split lineage; otherwise the benchmark's generator also manufactures direct solution supervision.
14. **Single-platform scope.** Common UI components do not demonstrate transfer to different software, artifact conventions, authority structures, or professional consequences.
15. **Exact reproduction gap.** No manuscript commit is pinned; ServiceNow is remote and mutable; later access depends on separately gated instances and secrets.
16. **Safety omitted.** The benchmark does not test authorization, malicious instructions, privacy, rollback, or consequential error handling.

## Reproducibility and operational realism

**Inspectability: moderate.** The immutable paper is detailed, and the later official archive exposes task setup, composition, curricula, state validators, user isolation, and teardown. Version timing is clear in local provenance.

**Exact paper reproduction: low.** The reviewed code is post-paper; the ServiceNow backend is not frozen locally; model APIs are historical; no per-episode result bundle or manuscript environment image was identified. This review could inspect but not execute tasks without a provisioned/gated instance.

**Operational realism: mixed.** Persistent enterprise records, tickets, knowledge articles, dashboards, role-like workflows, and backend outcome checks are more realistic than toy pages. Conversely, synthetic companies/data, admin-like roles, one platform, benchmark-specific infeasibility actions, explicit L2 procedures, and no real organizational consequences make this a controlled workflow simulator rather than evidence of deployment readiness.

## Relevance to skill-bench

The benchmark is a high-relevance case for executable workflow construction, stateful validation, procedure-disclosure interventions, and the validity risks created when atomic tasks are chained. It is not a template for narrowing skill-bench to enterprise software.

## Transferable design lessons

### Retain

- Parameterized executable setup and teardown tied to stable task seeds.
- State-based acceptance of equivalent outcomes rather than exact oracle trajectories.
- Matched explicit-procedure versus protocol-retrieval variants as an intervention.
- Oracle-generated demonstrations, but with strict lineage and contamination controls.
- Human feasibility checks using the same core environment.
- Curated curricula that expose their buckets and weights rather than claiming raw task-count coverage.

### Repair

1. Represent composition as a typed dependency DAG, not only an ordered list of subtasks.
2. Recheck invariant obligations at termination and distinguish milestone progress from final-state correctness.
3. Emit criterion-level outcomes, first unsupported dependency, rollback/reversal evidence, and professional consequence severity.
4. Log validator invocation cadence and prohibit human/agent interface differences unless treated as an explicit condition.
5. Require reset attestations: before/after state fingerprints, enumerated side effects, teardown outcomes, collision tests, and invalid-trial handling.
6. Validate workflow source, frequency, role, authority, artifact conventions, and hidden requirements with experts or primary work evidence.
7. Run matched atomic-versus-composite and L2-versus-L3 ablations with equalized step/information budgets where possible.
8. Estimate template/seed clustering and report family-level uncertainty rather than naive task-instance independence.
9. Separate public protocol, private fair consequences, oracle, grader, and training traces; publish contamination lineage.
10. Tune difficulty away from floor through adaptive horizons or intermediate variants without exposing grader cues.

## Concrete changes

1. **Consolidation/building:** add a composite-workflow validity slice to existing contracts and fixtures: dependency DAG, milestone versus terminal checks, state-reversal test, and matched atomic-composite prediction. This is the one uncovered executable obligation from the audit.
2. **Pilot validation:** for two unlike skill-bench work shapes, compare observed composite success with component baselines, while logging earliest failed dependency and reset evidence.
3. **Authoring rule:** prohibit “realistic workflow” claims without provenance and expert validation; describe unvalidated scenarios as design hypotheses.
4. **Reporting rule:** report L2/L3 as a procedure-disclosure intervention, not an ordinal difficulty fact, until information budget and interface effects are separated.

## Claim boundary

The immutable paper establishes that the authors created and evaluated 341 paired ServiceNow workflow definitions, that their configured 2024 agents were near floor, and that a small trained convenience sample completed a subset at high rates. The later official release establishes that executable composition, per-task users, task-specific setup/cleanup, sequential and global validators, and weighted curricula exist in a later implementation. Neither source establishes occupational representativeness, independent coverage of five cognitive abilities, causal planning/reasoning diagnosis, full reset integrity, manuscript-time reproducibility, cross-software transfer, safety, or professional deployment readiness.
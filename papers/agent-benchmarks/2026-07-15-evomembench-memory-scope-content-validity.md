# EvoMemBench: a useful memory-scope map whose cells do not identify one “self-evolving memory” construct

**Source:** Yuyao Wang et al., *EvoMemBench: Benchmarking Agent Memory from a Self-Evolving Perspective*, arXiv:2605.18421v2 (updated 15 June 2026), 30 pages; https://arxiv.org/abs/2605.18421v2.
**Local PDF:** `data/papers/pdfs/2605.18421v2-evomembench.pdf` (SHA-256 `cdb0e53b72222d6560edb2cbbc7ee9e0cef94989e7014eeeffe1b5068424c5a6`).
**Local text read in full:** `data/papers/text/2605.18421v2-evomembench.txt` (SHA-256 `373f2bcad57a0393ff309fe4d06b1a69d9054028216893e8940784389cc1d8af`).
**Official release inspected:** commit `aa4cea8fd936b76b2d3591d3ef897030617dc43a`, tree `3f7bab0223f3998cd03177af6f6b624fef41438b`; https://github.com/DSAIL-Memory/EvoMemBench/commit/aa4cea8fd936b76b2d3591d3ef897030617dc43a.
**Pinned archive:** `data/sources/releases/2605.18421v2-evomembench/DSAIL-Memory-EvoMemBench-aa4cea8.zip` (SHA-256 `cafeed011eeec0298b2d9faf2113a04b0c050087e11397d960d688a091e83125`).
**Release provenance:** `data/sources/releases/2605.18421v2-evomembench/provenance.json`.

## Review status and charter fit

This is a **deep paper and release review**. I read the complete immutable v2 paper and inspected the complete 3,910-file, 205.8 MB uncompressed official archive, including all six benchmark surfaces, released datasets, memory adapters, runners, graders, comparison scripts, and execution scripts relevant to the claims below. The pinned release commit is dated 3 July 2026, 18 days after v2; it is official post-v2 evidence, not proven paper-time code.

The review advances charter objectives A–C by testing a general benchmark-design question: can memory scope and content be crossed without silently changing the task, feedback, solver, environment, observer, and estimand? This is comparative validation, not a proposal to narrow `skill-bench` to memory systems or self-improving agents.

## One-sentence contribution

EvoMemBench supplies a broad and operationally useful inventory of in-episode versus cross-episode and knowledge versus execution memory demands, but its four labels aggregate six inherited datasets with different information dependencies, feedback, endpoints, graders, missingness policies, and task lineages, so the reported ranks characterize configured pipelines rather than a common self-evolving-memory ability.

## Why this matters

The source directly tests whether a broad suite can compare memory architectures
without conflating the store with task lineage, context availability, feedback,
the solver, and the observer. That identification problem recurs anywhere
`skill-bench` turns prior experience into reusable evidence or procedure.

## Contribution and research question

The paper asks which memory representations help when useful information must be retained either **within one episode** or **across episodes**, and whether the reusable content is primarily **knowledge** or **execution experience**. It places 15 memory methods into retrieval, short-term, general long-term, procedural long-term, and meta-evolution families, uses DeepSeek-V3.2 as the common solver for memory-augmented conditions, and compares them with memory-free DeepSeek-V3.2, GPT-5-mini, and Gemini-3-Flash (paper §§3–5 and Appendix A.3).

The conceptual grid is valuable. It prevents “memory” from meaning only conversational fact recall and forces at least two distinctions that `skill-bench` needs:

1. retention inside a bounded work episode is not persistence across separately reset tasks;
2. preserving facts/rules is not the same operation as preserving tool-use routines, search strategies, or affordances.

The paper’s stronger language—“unified,” “standardized,” “comprehensively evaluates,” and “self-evolving”—requires more caution. A taxonomy can organize unlike instruments without making their scores exchangeable or their treatment effects identified.

## Methodology and release reconstruction

### The six benchmark surfaces

1. **INEP-KNOW** adapts MemoryAgentBench. The release contains 22 accurate-retrieval histories with 2,000 questions and eight conflict-resolution histories with 800 questions. Memory updates as information arrives within a long input; the endpoint is answer correctness on later questions.
2. **INEP-EXEC** reconstructs BFCL multi-turn tool tasks and varies context limits from 16K to 128K. Within a chain, tool outputs and state must survive later turns. The endpoint is executable multi-turn success.
3. **CROSSEP-KNOW** groups CL-Bench records by shared `context_id`, retains groups with at least five tasks, and processes each group serially with an isolated memory bank. The released file has 884 unique tasks across 120 contexts, with 5–12 tasks per context: 294 domain-reasoning, 257 rule-system, 306 procedural, and 27 empirical-discovery records.
4. **CROSSEP-TOOL** runs memory across BFCL task chains within or across four API environments.
5. **CROSSEP-WEB** uses 100 xbench-DeepSearch records and 170 WebWalkerQA records, with shared-memory pipelines for accumulation and later read-only evaluation.
6. **CROSSEP-EMB** evaluates 200 ALFWorld tasks across six categories; the release includes wrappers and scripts but obtains the ALFWorld environment/test substrate externally.

These are useful probes, but they do not instantiate a crossed factorial design. Dataset, task source, context length, environment, action space, feedback, grader, number of episodes, and dependency structure all change with the cell. A difference between cells cannot be attributed to scope or content while those factors move together.

### Released-count and lineage audit

The cross-episode knowledge counts match the paper: 884 records and 120 contexts. INEP-KNOW also matches the paper’s 2,000/800 evaluation-question counts.

The tool-use release does **not** match Table 2’s stated 200 samples per domain. Both `INEP-EXEC` and `CROSSEP-TOOL` contain the same byte-identical `BFCL_v4_multi_turn_ours.json`: 200 task chains total, 50 per domain, containing 1,062 user turns (1–10 turns per chain; mean 5.31). The four released ID manifests likewise select 50 IDs each and are identical across the in-episode and cross-episode forks. Table 6’s two-percentage-point increments are consistent with 50 evaluated chains per domain. Thus the paper’s four `200` labels and 800-sample total are not the released unit count unless “sample” denotes an undocumented multiplication; it cannot mean turns, because there are 1,062. This matters for denominators, uncertainty, and claims of independent coverage.

Reusing exactly the same 200 chains for both execution cells is not inherently invalid: reset and information-flow policy can be the treatment. But it means the cells are not independent coverage of execution memory, and the release needs an explicit paired protocol and unit declaration rather than presenting 800 samples in each cell.

## End-to-end trace: one CROSSEP-KNOW cell

The released CROSSEP-KNOW path is unusually inspectable and shows both the benchmark’s value and its identification limit.

1. **Source and episode identity.** Each JSONL record contains a full system message, a large task transcript, a list of rubrics, and `task_id/context_id/category` metadata. The 884 records contain no reference-answer field. Records sharing a context retain file order; the first two released records, for example, share the exact 2,915-character system context but have different task transcripts and 42 versus 37 rubric clauses.
2. **Reset and write boundary.** `infer_context_memory.py` creates one isolated memory directory per `context_id`; groups may run in parallel, but tasks inside a context run serially. Memory is empty at the group boundary.
3. **Retrieval.** Before each task, the memory system queries with the complete current user message and injects returned text into the current messages. For released BM25, prior trajectories are split into at-most-1,024-token chunks, whitespace indexed, and top-k chunks are appended as “prior task trajectory chunks.”
4. **Solver.** The same DeepSeek model receives the current complete task plus injected memory. The no-memory arm receives the complete current messages without the injection.
5. **Write/update.** After a successful API response, the runner formats the current messages plus the ungraded model response and immediately extracts/stores memory. BM25 stores chunks verbatim; generative systems may call another model. There is no correctness gate before write, so hallucinated or failed reasoning can become later evidence.
6. **Adoption and consequence.** The result records the retrieved string, output, latency, and token fields. It does not record whether the solver read, cited, adopted, rejected, or causally depended on a retrieved item. There is no environment action or artifact state in this cell; the only consequence is generated text.
7. **Criterion and score.** `eval.py` sends a GPT-5.1-compatible judge only the rubric list and student response—not the original task/context and not a reference answer—and requests an all-or-nothing binary score. The rubric has 4–114 clauses (mean 23.9). The judge can check response-visible assertions and formatting but cannot independently inspect task artifacts omitted from its view. Calling this “answer accuracy” therefore overstates the observer: it is binary rubric-judge acceptance under a restricted evidence view.
8. **Missingness and aggregation.** Inference exceptions are logged and skipped before a result row is written. The released comparison script computes rates on the intersection of baseline and memory task IDs, while invalid present scores become zero. Generation failures can therefore disappear through complete-case intersection, whereas grader failures on present rows become failures. Other cells, such as CROSSEP-TOOL, persist inference-error rows and score them zero. The suite has no uniform invalid/missing-trial policy.

This trace supports a precise claim: EvoMemBench can test whether an evolving store of prior model trajectories changes later rubric-judged outputs within a shared CL-Bench context. It does not show that the store preserved correct knowledge, that retrieved text was adopted, or that an action improved.

A further construct problem is decisive: each CROSSEP-KNOW task already receives the shared background context in its current messages. The paper says this explicitly, and the release confirms identical complete system contexts within groups. Memory is therefore supplementary prior solved trajectories, not the only carrier of required knowledge. The condition tests repeated-context example/trajectory augmentation; it does not establish cross-episode necessity or retention of otherwise unavailable knowledge.

## Evidence and what it supports

The main results establish heterogeneity among configured systems:

- On INEP-KNOW, Gemini-3-Flash has the best overall rank; explicit memory is not uniformly superior to long context.
- On INEP-EXEC, the best memory score exceeds the DeepSeek-V3.2 no-memory score by 14.5 points at 16K and 14.0 at 32K, with smaller gains at 64K/128K. This is the paper’s cleanest directional evidence because a declared context-budget restriction makes compression/retrieval plausibly useful, although memory adds compute and representation changes.
- On CROSSEP-KNOW, DeepSeek-V3.2 scores 52.1/12.6/0.0 on easy/medium/hard, while ACE reaches 44.8/16.5/13.0. The hard gain is descriptive, not an unbiased difficulty effect: easy/medium/hard are tertiles defined by the same DeepSeek baseline outcome. Selecting the bottom baseline tier mechanically creates a floor and regression opportunity; the empirical category has only 27 items, with cells as small as about nine.
- On cross-episode execution, the best family by average rank changes across tool use, web search, and embodied AI. This supports “architecture × benchmark interaction,” but family average rank over unlike endpoints is not a common performance scale.
- Figures 3–4 report cross-environment transfer patterns. The paper does not provide numeric transfer tables, repeated source pools, equivalent-form controls, or uncertainty. Positive transfer can reflect shared function documentation, templates, API families, or task lineage rather than a portable learned procedure.

No main table reports confidence intervals, repeated trials, paired tests, cluster-aware uncertainty, multiplicity handling, or sensitivity to episode order. Tasks share contexts, API classes, generated templates, source datasets, and memory stores, so treating task outcomes as independent would be inappropriate. Point differences of a few items—especially the two-point increments in 50-chain tool domains—cannot support stable rankings without repeats or clustered inference.

## Unique insight

EvoMemBench’s deepest lesson is not that one memory family wins a cell. It is that **memory scope and content are properties of an information-flow contract, not dataset labels**.

A valid contract must identify:

`prior event and authority → episode/reset boundary → write opportunity → stored representation and correctness status → retrieval query/budget → presented evidence → solver access/adoption → action or answer → observer view → score and missingness policy`.

EvoMemBench names the endpoints of this chain but changes or leaves unobserved many intermediate links. In CROSSEP-KNOW, current context already contains the shared knowledge. In CROSSEP-TOOL, FC-mode retrieval queries with function documentation rather than the current user task, and the finished trajectory is written before post-hoc BFCL grading. Several adapters default missing metadata to `is_correct=True`; the SkillWeaver adapter explicitly sets both `is_correct=True` and `task_success=True` for every ingested trajectory even though the success checker runs later. Thus a method designed to learn only from successful traces can be fed an asserted-success label unrelated to measured success. This is not merely noise: it changes the semantics of the evaluated memory method.

The correct conclusion is therefore:

> A broad memory suite should report configured information-flow treatments and cell-specific estimands. Scope/content labels are useful stratifiers only after current-context necessity, write authority, feedback, retrieval, adoption, endpoint, and observer policy are held fixed or explicitly modeled.

## Limitations and validity threats

### Construct and content

1. **The grid is not factorial.** Scope/content labels are confounded with dataset family, endpoint, environment, feedback, and grader.
2. **“Self-evolution” is often ordinary accumulation.** BM25 appends trajectory chunks; other systems summarize or index them. There is no general requirement for contradiction repair, supersession, forgetting, candidate promotion, rollback, or changed-environment adaptation.
3. **Cross-episode necessity is not established.** CROSSEP-KNOW repeats the full shared context; tool/web/embodied tasks do not include matched reset/oracle/irrelevant-memory interventions showing that earlier episodes are necessary.
4. **Knowledge and execution are heterogeneous within labels.** Rubric-judged CL-Bench reports, exact-answer memory QA, BFCL state transitions, live web answers, and ALFWorld goals do not instantiate one knowledge/execution pair.
5. **Trajectory correctness is not typed before write.** Failed reasoning and actions can be stored without a realized-outcome label; some adapters assert success before grading.
6. **Cross-environment reuse is lineage-confounded.** Shared API documentation, function classes, benchmark templates, task generators, and source corpus can produce apparent transfer without portable procedural abstraction.

### Treatment and attribution

7. **Memory and no-memory compute are unmatched.** Memory methods may add retrieval, embeddings, extraction-model calls, summarization, and longer injected prompts. Within-DeepSeek comparisons are useful package effects, not isolated storage effects.
8. **Cross-model long-context comparisons are descriptive.** Gemini/GPT/DeepSeek differ in far more than memory. The common DeepSeek backbone repairs only the memory-method subset.
9. **Applicability changes the roster.** Procedural methods are excluded from in-episode knowledge and short-term methods from cross-episode settings. Average ranks therefore summarize eligible configured systems, not all 15 methods on a common suite.
10. **No access/adoption intervention.** Retrieved text is logged in some paths, but evidence visibility, citation, semantic use, and causal necessity are not scored.
11. **Order is part of the treatment but not analyzed.** One released file order determines what earlier trajectories are available. No order randomization, equivalent stream, or sensitivity analysis separates curriculum from memory architecture.
12. **Difficulty is outcome-conditioned.** CROSSEP-KNOW tertiles use DeepSeek baseline score, making hard-split gains vulnerable to floor and selection effects.

### Grading, statistics, and missingness

13. **CROSSEP-KNOW’s grader lacks the task evidence view.** It sees rubrics and response only. No human–judge calibration, repeated judging, or adversarial false-accept audit is reported.
14. **Endpoints are non-equivalent.** Exact answers, all-rubrics binary acceptance, full multi-turn BFCL success, web answer judgment, and environment reward cannot be merged into one latent memory score; average rank hides magnitude and metric semantics.
15. **Denominators conflict.** The released tool substrate has 50 chains per domain, not Table 2’s 200; “sample” is not reconciled with chains or 1,062 turns.
16. **Failure handling differs by cell.** CROSSEP-KNOW can omit failed generation rows and intersect complete cases; CROSSEP-TOOL retains error rows as zero. Provider failure can therefore alter denominators differently.
17. **No uncertainty.** There are no repeats, seeds, confidence intervals, task/context-cluster bootstrap, or paired tests despite model judges, live web, hosted APIs, and generative memory updates.
18. **Family-rank conclusions are fragile.** Average rank gives the same spacing to tiny and large score differences and depends on eligibility and subset weighting.

### Efficiency, reproducibility, and operational realism

19. **Efficiency is incomplete.** The paper counts LLM input/output tokens but does not jointly report embedding tokens, storage, indexing, API cost, wall-clock latency, retries, hardware, service waits, or amortized update/query cost. “Efficient” methods may move cost outside the reported token boundary.
20. **No paper result corpus is released.** The archive contains runners and one MemoryOS smoke-result file, but no per-item outputs/judgments or tables from which the paper’s results and figures can be recomputed.
21. **The release is post-v2 and dependency-fragmented.** It bundles large forks of memory projects and many environment-specific requirements, but no single frozen environment/container reproduces all cells; hosted models and embeddings remain mutable.
22. **ALFWorld is not self-contained.** Scripts and wrappers are present, but exact environment/data reconstruction depends on external packages/assets.
23. **Operational realism is bounded.** BFCL and ALFWorld provide executable state, and web search exposes a live substrate, but the suite does not sample professional workflows, expert memory practices, stakeholder consequences, or deployment conditions.
24. **Public contamination and maintenance are unaddressed.** Tasks, rubrics, scripts, and data are public, while live-web state and provider models drift; there is no renewal, private holdout, or longitudinal bridge policy.

## Comparison with adjacent reviewed benchmarks

- **LongMemEval-V2** isolates a bounded experience-to-evidence interface and a fixed reader, making retrieval/representation misses more inspectable, but stops before action. EvoMemBench is broader across mechanisms and endpoints but less controlled at that interface.
- **MemoryArena** makes earlier sessions consequential for later actions, but feedback and state reconstruction are heterogeneous. EvoMemBench adds more memory families and scope labels, yet often does not establish explicit dependency from prior episode to later task.
- **OdysseyBench** supplies dialogue-distributed requirements and observes office-state consequences; it is not persistent learning, but its evidence-to-action bridge is clearer than CROSSEP-KNOW’s response-only endpoint.
- **AFTER** distinguishes source-context improvement from cross-task, cross-context, and cross-model transfer. EvoMemBench’s cross-environment figures need those typed transfer edges, volume-matched source pools, frozen target forms, negative-transfer rates, and uncertainty before “transfer” is causal.
- The existing `pilots/experience-memory-transfer/` contract already combines evidence delivery and held-out action under reset, raw-experience, answer-feedback, oracle, and corrupted-evidence conditions. EvoMemBench strengthens the case for using that contract; it does not expose a nonduplicate new pilot or schema need.

## Transfer to skill-bench

### Retain

1. **The scope × content vocabulary**, but attach labels to explicit episode, persistence, information, and endpoint contracts rather than benchmark names.
2. **Same-backbone no-memory comparisons** and declared memory-method eligibility.
3. **Context-budget ladders** like INEP-EXEC, because they test when compression/retrieval becomes useful.
4. **Per-memory telemetry** for retrieval, extraction, tokens, latency, and retrieved evidence views.
5. **Negative transfer as a first-class possibility**, not a reason to hide regressions in average rank.

### Repair

1. Cross scope and content on matched task families where possible: hold task, solver, grader, feedback, and environment fixed while changing reset/persistence and fact/procedure payload.
2. Predeclare the memory-necessity edge. Include current-context-sufficient, history-required, oracle-memory, irrelevant-memory, corrupted-memory, and reset controls on equivalent forms.
3. Type every write as observation, attempted action, realized consequence, judged success, inferred lesson, or promoted procedure. Do not assert success before the checker runs.
4. Record retrieval availability, presented span, access, adoption/rejection, action, and endpoint consequence separately. Use counterfactual evidence removal or substitution to test causal use.
5. Freeze and publish stream order, source/target lineage, all attempts, errors, omitted rows, and one denominator policy. Cluster inference by context/stream/task family and repeat stochastic components.
6. Report package efficacy separately from component attribution. Match or itemize solver, memory-model, embedding, retrieval, injected-context, update, grader, storage, latency, and cost budgets.
7. Validate grader evidence views. A judge assessing factual/task compliance must see an admissible task/artifact view, and its agreement and false-accept/false-reject behavior must be measured.
8. Keep cell-specific metrics; do not turn heterogeneous ranks into a general memory score.

## Concrete repository action

No new queue task is warranted. The nonduplicate requirements are already implemented or queued through the experience-memory-transfer pilot, longitudinal stream, configured-system, information-flow, trace, task-health, metric, and validity contracts. The immediate action is to use EvoMemBench as a release-audited caution in those syntheses: a memory taxonomy should organize evidence, not license aggregation before the information-flow treatments are identified.

## Claim boundary

EvoMemBench v2 provides credible evidence that selected 2026 memory-augmented DeepSeek pipelines and memory-free long-context models behave differently across six inherited benchmark surfaces, that explicit memory can help under constrained context, and that no tested memory family dominates every configured cell. The release makes many task, adapter, and execution paths inspectable.

It does **not** establish a common self-evolving-memory construct, causal benefits of memory independent of added compute and prompting, cross-episode necessity, portable procedural transfer, correct memory formation, solver adoption of retrieved evidence, reliable family rankings, professional knowledge-work capability, production fitness, safety, economic value, or deployment readiness.

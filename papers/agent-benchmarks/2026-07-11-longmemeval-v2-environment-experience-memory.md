# LongMemEval-V2: environment-experience memory is an evidence-gathering test, not yet a competence-transfer test

**Source:** Di Wu et al., *LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues*, arXiv:2605.12493v1 (12 May 2026), 32 pages; https://arxiv.org/abs/2605.12493v1.  
**Immutable paper:** `data/papers/pdfs/2605.12493v1-longmemeval-v2-environment-experience-memory.pdf`  
**Full extraction read:** `data/papers/text/2605.12493v1-longmemeval-v2-environment-experience-memory.txt`  
**Official release inspected:** code commit `be15ea6e995462f3391c1a610892df3f67dfa7bd`; dataset revision `f152293e235517d504809563c833d7190b8c713b`  
**Release provenance:** `data/sources/releases/2605.12493v1-longmemeval-v2/provenance.json`  
**Targeted released-data trace:** `data/sources/releases/2605.12493v1-longmemeval-v2/two-item-trace-summary.json`

## Review status and charter fit

This is a **deep review**: I read the complete immutable v1 local PDF and local text extraction and inspected the full 49-file official code snapshot, all 451 released question records, both released haystack manifests, the public schema/checksums, and two paper-disclosed trajectories from the 1.196 GB trajectory table. The full trajectory table was downloaded and hash-verified for targeted inspection but is not committed; screenshot archives were not mirrored. The inspected code and dataset are post-v1 snapshots, so release behavior is not silently projected backward as paper-time implementation.

The work advances charter objectives A–C by testing a general expertise-transfer question: when historical agent-environment interaction is transformed into compact reusable evidence, what has actually been learned? It is expansion into a reusable memory/evidence boundary, not a proposal to narrow skill-bench to web agents.

## One-sentence contribution

LongMemEval-V2 operationalizes environment experience as bounded, provenance-inspectable evidence gathering over massive trajectory histories, while its design leaves held-out action transfer as a separate unmeasured claim.

## Why this matters

The source directly tests whether trajectory history can become reusable state, workflow, failure, and premise knowledge—the benchmark project's central expertise-transfer boundary—without requiring skill-bench to adopt web QA as its target artifact.

## Contribution and research question

The paper asks whether a memory module can turn many prior web-agent trajectories into environment-specific knowledge useful to a downstream reader. Its distinctive move is to evaluate memory **directly through context gathering** rather than only through later task success: a module sequentially receives trajectories through `Insert`, returns bounded multimodal evidence through `Query`, and a fixed reader answers one of 451 manually authored questions (paper pp. 2, 5–6, 17–18).

The five proposed abilities are static-state recall, dynamic-state tracking, workflow knowledge, environment gotchas, and premise awareness (p. 4). This is a useful decomposition of experience: it includes affordances, state transitions, procedures, recurring failure signatures, and false-premise detection rather than treating memory as fact retrieval alone.

The benchmark has two tiers. Small uses a shared 100-trajectory haystack per domain; Medium uses roughly 500 trajectories per question. Histories average about 25.6M and 114.8M tokens, while questions require 1.4 answer trajectories on average (pp. 5–6). The authors also introduce AgentRunbook-R, with raw-state, transition-event, and procedure/hint pools, and AgentRunbook-C, which stores full trajectories as files and gives a coding agent manifests, workflow instructions, and inspection helpers (pp. 7–8, 22–23).

## Methodology and system reconstruction

### Construction

Trajectories come from WebArena, WorkArena, and WorkArena++ instances of OneStopShop, CMS, Reddit/Postmill, and ServiceNow. AgentLab supplies unified accessibility-tree/screenshot observations and BrowserGym actions. The authors rejection-sample trajectories from GPT-5-mini, GPT-5.2, and a Codex-controlled manual-action setup, retaining 599 WebArena and 941 WorkArena-family trajectories, with 52.0% overall success and 28.1 states on average (pp. 5, 15). Goals with explicit navigation hints are sanitized (pp. 15–16).

One graduate and three undergraduate student authors create questions after environment familiarization; at least one additional annotator checks answerability, correctness, and taxonomy fit, with discussion-based resolution (p. 16). Candidate questions are filtered or perturbed until at least two of four frontier models fail without history; wrong model answers sometimes become multiple-choice distractors (pp. 5, 16). This makes parametric resistance partly an **outcome-conditioned item-selection criterion**, not an independently sampled property.

Codex proposes answer-bearing trajectories using metadata and content search; humans validate included core trajectories and resolve ambiguity. Inclusion is supposed to require screenshot-visible evidence, with type-specific and multi-hop rules (pp. 16–17). A greedy/local-search assignment chooses 44 WebArena and 49 ServiceNow trajectories as minimal cores. Fillers balance outcomes and diversity; Medium deliberately reuses Small's selected answer seeds while excluding other labeled answer-bearing trajectories (p. 17).

### Evaluation

The fixed reader is Qwen3.5-9B. Returned context is truncated to 200K model tokens. Structured answers use deterministic phrase or choice matching; gotcha and abstention items use GPT-5.2 binary judges. `UNKNOWN` always scores incorrect (pp. 17–19). The release confirms 451 questions: 134 static, 86 dynamic, 74 procedure, 29 gotcha, and 128 abstention variants; 240 are web and 211 enterprise. It uses deterministic matchers for 323 questions and model judges for 128 abstention plus 28 of 29 gotcha questions.

Main experiments compare no retrieval, slice RAG, slice-plus-note RAG, AgentRunbook-R and ablations, Codex, and AgentRunbook-C and ablations. Memory and reader components are not uniformly held fixed across families: RAG controllers use Qwen3.5-9B plus Qwen3-Embedding-8B, while coding-agent methods use Codex with GPT-5.4-mini. Only the final reader is shared (pp. 8, 21–23).

## Evidence and what it supports

AgentRunbook-R reaches 58.6% Small and 57.0% Medium, versus 51.0%/45.9% for slice-plus-note RAG. AgentRunbook-C reaches 74.9%/70.1%, versus vanilla Codex at 69.9%/68.7%. Reported query latency is 108.3/139.9 seconds for AgentRunbook-C versus 177.2/185.8 for Codex and about 26 seconds for AgentRunbook-R (p. 8). Paired bootstrap markers support selected within-family comparisons, but the paper provides no confidence intervals, number of stochastic repeats, reader-seed analysis, or correction for many category/ablation comparisons.

The oracle studies establish two narrower facts. Models given no trajectory context score at most 14.1% on the selected non-abstention items. Full answer-bearing trajectories still produce only 59.6%–65.3%, while annotated slices plus generated notes yield 82.5%–86.3%, and Codex over local oracle files yields 89.7% (pp. 6, 19–20). Thus evidence **presentation and inspection machinery** materially affect the measured result even after retrieval is made oracle. This is the strongest result for skill-bench: a memory score is jointly determined by retained information, retrieval, representation, reader compatibility, and compute.

The two released lineages inspected match the paper's successful examples (pp. 31–32). Question `98b62f3d` maps to failed trajectory `4ba5e9cb`, whose state 2 visibly contains required `Title` and `Forum` fields. Question `609acb91` maps to successful trajectory `dddd8aa2`, whose state 5 contains `Remove This Item` and `Clear All`. Both trajectories occur in the 100- and 500-item released haystacks. This verifies two disclosed evidence paths, not the private coverage map, all 451 gold answers, or screenshot fidelity.

## Unique insight

The paper's important contribution is not the “experienced colleague” metaphor. It is the operational separation between **experience storage** and **evidence delivery to a consumer**. The benchmark makes memory expose a typed, bounded evidence package before a fixed reader decides. That boundary is valuable because it permits diagnosis of retrieval misses, representation loss, premise handling, and reader errors.

But the evidence also reveals a sharper identification problem:

> QA accuracy over author-selected questions measures the utility of a memory–retriever–representation–reader–grader pipeline on retrospective evidence lookup. It does not by itself establish that historical experience improves future agent action.

The distinction matters for skill-bench. A procedural note can answer “which button exists?” yet be stale, conditionally applicable, causally mistaken, unsafe to execute, or unable to improve a held-out task. Conversely, a memory may preserve useful action knowledge that the fixed reader or exact-answer grader cannot express. “Environment experience” therefore needs two linked but non-substitutable estimands: evidence-grounded recall and intervention benefit on held-out action.

## Limitations and validity threats

### Construct and sampling

1. **The target is authored retrospective QA.** Questions are derived from inspected trajectories, then filtered against frontier-model failures. This favors facts that annotators noticed, can phrase, can answer from screenshots, and current models miss. It does not sample the universe of knowledge needed for future work.
2. **The five abilities are labels, not validated latent constructs.** There is no reported independent coding reliability, expert/novice contrast, factor analysis, or downstream criterion validation. The four annotators are student authors, not demonstrated ServiceNow/Magento practitioners (pp. 16, 26).
3. **Outcome-conditioned admission can inflate environment-specificity.** Rewriting items and converting model errors into distractors directly optimizes no-context failure. The 14.1% ceiling is valid for the selected set, not an unbiased estimate of how much environment knowledge frontier models lack.
4. **Medium is not an independent scale-up form.** It retains the same selected answer seeds and excludes other answer-bearing trajectories. Tier differences primarily add controlled distractors; they do not test new experience, temporal accumulation, or changed environments.

### Evidence fidelity and provenance

5. **Only the final core is reported as human validated.** Codex-assisted coverage labeling and human validation focus on included core trajectories. The released questions/haystacks omit the private answer-coverage map, evidence-hop locators, uncertainty decisions, annotator identities, and adjudication lineage, limiting independent false-negative/false-positive audit.
6. **Screenshot-visible policy and released textual evidence diverge operationally.** The paper requires screenshot-visible evidence, but the released question records contain answers/evaluator specs and the trajectory table contains accessibility trees. Without retained evidence-view annotations, downstream audits cannot determine which representation licensed each answer.
7. **Failed trajectories are valuable but causally ambiguous.** They can expose gotchas and attempted workflows, yet an attempted sequence is not a valid procedure and a failure association is not a cause. AgentRunbook prompts warn against invention, but records lack typed attempt/realization/cause/scope status.
8. **Temporal and premise scope are underrepresented.** “Dynamic” means within-trajectory state change, not validity over calendar/environment versions. There is no claim-level valid time, environment build hash, supersession relation, or applicability predicate. The ethics section itself warns about stale/context-dependent memories (p. 26).

### Measurement and attribution

9. **Reader and representation remain treatment components.** Oracle slicing boosts QA dramatically. A fixed reader improves comparability but does not isolate memory quality unless evidence representation and reader interaction are separately modeled.
10. **Cross-family comparisons confound architecture, model, harness, tools, and compute.** AgentRunbook-C versus AgentRunbook-R is not a clean file-memory-versus-RAG treatment. The fair evidence is mostly within-family ablations, and even these appear single-run and stochastic.
11. **The error taxonomy is partly circular and non-causal.** A “major miss” is defined through task-family overlap; a “minor miss” through exact trajectory overlap; a “reading error” includes any exact trajectory, URL, or gold-answer-text hit (p. 24). Presence does not establish reader visibility after truncation, sufficiency, adoption, or earliest root cause. The authors explicitly assign some nominal reading errors back to memory presentation.
12. **Grader validity is unreported.** Gotcha scoring accepts any one correct reference point if none contradict, while abstention scoring can accept explicit lack of live-environment access (pp. 19–20). No human–judge agreement, repeatability, or blinded calibration is reported. Deterministic phrase containment can accept extra unsupported content.
13. **Uncertainty and dependence are thin.** Questions share environments, source trajectories, task families, minimal cores, and in Small entire haystacks. Item-level paired bootstrap does not obviously account for these lineage clusters. There are no repeated memory/query/reader runs despite sampling temperature 0.6.
14. **Latency is incomplete operational evidence.** Query concurrency is capped at three, but indexing time, storage, generated-note cost, API cost, preprocessing, and total amortized latency are not jointly reported. AgentRunbook-C's “32% faster” claim is query-only under one hardware/service setup.

### Reproducibility and operational realism

The pinned release is unusually substantive: harness, graders, memory implementations, configs, data preparation, submission tooling, questions, haystacks, trajectories, and checksums are available. It pins Codex v0.117.0 and describes model endpoints. However, full reproduction requires very large screenshot bundles, local Qwen serving, proprietary GPT models for Codex and semantic judging, and substantial indexing/query expense. The public dataset revision and code commit postdate v1; no paper-time commit is named. Raw paper result tables, per-item predictions/judgments, annotation materials, coverage maps, and stochastic seeds are absent.

AgentRunbook-C calls Codex in a directory described as an “isolated sandbox,” but release inspection shows process invocation with a cwd and symlinked trajectories, not a demonstrated filesystem/network containment envelope. Instructions say not to explore outside; that is not enforcement. This matters because file-manipulating memory controllers can read unrelated files or use network/model priors, and the paper itself flags sandbox risk (p. 26).

Most importantly, the benchmark is offline and action-free by design. The authors acknowledge that it does not capture distribution shifts induced by the evaluated agent or directly measure planning/tool/action success (p. 25). No experiment inserts memory into a held-out acting agent, compares reset versus memory conditions, or measures harmful transfer, stale guidance, recovery, or selective forgetting.

## Transfer to skill-bench

### What should be adopted

1. **Typed trajectory-derived knowledge.** Preserve raw observations, state transitions, procedures, and gotchas as different records rather than flattening them into generic notes.
2. **A context-gathering interface.** Require a memory/skill layer to return compact evidence with source locators before a consumer constructs an artifact or takes action. This supports diagnosis and evidence-view auditing.
3. **Failed-run retention with explicit status.** Failures can reveal hidden affordances and recurring failure signatures, but extracted lessons must distinguish observed state, attempted action, realized consequence, inferred cause, and validated remedy.
4. **Premise-awareness probes.** Pair positive questions/tasks with fair, evidence-backed false-premise variants; preserve which source claim is contradicted and why.
5. **Representation and budget records.** Hash memory controller, reader, prompts, manifests, helper tools, evidence rendering, truncation, and budgets independently. Treat evidence selection and presentation as interventions.

### What must not be inferred

Do not treat QA accuracy as professional competence, procedure validity, transfer to held-out action, or longitudinal learning. Do not call a generated note durable until authority, scope, valid time, contradiction status, and held-out consequences have been checked. Do not attribute a final wrong answer to retrieval merely because a gold trajectory ID was absent.

### Concrete cross-contract implications

The existing machinery already has homes for most obligations:

- compounding lessons: immutable evidence locators, contradiction/supersession, held-out promotion, rollback, and private-evidence firewall;
- benchmark bundle/traces: configured component hashes, evidence views, access/adoption links, invalid execution, and root/surface separation;
- persistent workspace: availability, relevance, provenance, observed access/write, alternative paths, and unsupported causal-use protection;
- longitudinal protocol: reset versus lesson-only/full-evolution arms, persistence, order, retention, forgetting, leakage and cost/safety drift;
- validity/task-health/metrics: claim boundaries, exact instrument versions, clustered estimands, missingness, uncertainty, and operational cost.

The nonduplicate addition is not another schema. It is an **exercised paired estimand** connecting one trajectory-derived memory package to both retrospective evidence QA and a held-out action consequence.

## Concrete repository changes

1. Build a compact **experience-memory transfer conformance slice** after the current higher-priority vendor adjudication: use synthetic trajectories containing a valid procedure, failed attempt, stale observation, scoped gotcha, contradiction, and safe alternative; compare no-memory versus evidence-only versus promoted-lesson conditions on (a) evidence QA and (b) a held-out artifact/state action. Require source-span provenance, environment/version scope, access/adoption, counterfactual applicability, harmful-transfer and rollback checks. Reuse existing contracts rather than creating a memory schema.
2. For any future memory pilot, predeclare two separate claims: **retrieval/grounding utility** and **held-out action benefit**. Use equivalent-form questions and unseen tasks, cluster uncertainty by source trajectory/task family, repeat stochastic queries/readers, and report indexing/storage/query/reader/grader costs separately.

## Bottom line

LongMemEval-V2 provides a strong and inspectable benchmark for retrieving environment-specific evidence from enormous noisy trajectory histories. Its five-way taxonomy and context-gathering API are directly useful to skill-bench. Its results support the narrower conclusion that structured pools and coding-agent file inspection improve retrospective question answering under particular configured systems. They do **not** yet support the experienced-colleague claim in the consequential sense: no evidence shows that the acquired memory improves held-out agent action, remains valid under environment change, or avoids harmful procedural transfer. The benchmark should therefore inform an evidence-to-action bridge, not become the bridge's substitute.

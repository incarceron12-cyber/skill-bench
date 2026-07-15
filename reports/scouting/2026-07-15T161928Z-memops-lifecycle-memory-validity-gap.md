# Scouting note — lifecycle-memory operation and diagnosis gap

**Timestamp:** 2026-07-15T16:19:28Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Initial queue inspection found 278 tasks: 273 completed, three blocked, one pending human prerequisite, and one pending build; no source, research, review, or claimed backlog remained. The corpus already covers experience-conditioned action, memory access/adoption, scope/content, authority/supersession, and downstream benefit. This run therefore searched only for an instrument that exposes memory lifecycle operations and state transitions rather than repeating broad memory-benchmark discovery.

## Substantive finding — triage only

**MemOps: Benchmarking Lifecycle Memory Operations in Long-Horizon Conversations** — Xixuan Hao, Zeyu Zhang, Zehao Lin, Yihang Sun, Ziliang Guo, Xichong Zhang, Yuxuan Liang, Feiyu Xiong, and Zhiyu Li; arXiv:2607.12893v1.

- Immutable record: https://arxiv.org/abs/2607.12893v1
- Immutable PDF: https://arxiv.org/pdf/2607.12893v1
- Immutable HTML: https://arxiv.org/html/2607.12893v1
- Search metadata identifies v1 as submitted 14 July 2026 in `cs.AI`; the surfaced summary contains no withdrawal or retraction notice. The versioned abstract, PDF, and HTML endpoints returned HTTP 200 during scouting.
- The abstract says MemOps reformulates conversational memory as lifecycle operations and represents each memory event with a structured trace containing its trigger, target, scope, state transition, and supporting evidence.
- Search-indexed HTML structure says the comparison emphasizes explicit operations, lifecycle coverage, state-transition modeling, forgetting/leakage control, and failure diagnosis. It also exposes a dataset-statistics table and model comparisons. These are structural and author-reported leads, not independently verified methods or findings.
- Search surfaced the authors' broader `MemTensor/MemOS` repository, but no paper-linked MemOps code/data release was established. No repository, dataset, task record, operation label, grader, or result artifact was inspected.
- Repository-wide exact-title, arXiv-ID, and `MemOps` searches found no local source, review, or queue task. The closest completed reviews are MemoryArena, LongMemEval v2, EvoMemBench, and MemSyco-Bench. They separately cover interdependent experience/action, access–adoption–benefit links, scope/content treatments, and current authority/supersession; none locally reviewed source makes the complete trigger→target→scope→transition→evidence event record plus forgetting/leakage diagnosis its central instrument.
- PM-Bench (`2607.12385`) and AgentAbstain (`2607.10059`) were also surfaced but not queued. Both are potentially relevant—deferred-intention execution and calibrated non-action—but the operation-level provenance/state interface in MemOps is the more direct current gap and avoids adding a three-paper backlog from one run.
- This is **metadata, abstract, endpoint, section-snippet, release-location, and duplicate triage only**. The paper body, appendices, tables, generation pipeline, ontology, task records, state-transition labels, evidence locators, annotations, graders, prompts, splits, model configurations, statistics, costs, and results were not read or audited. No claim is made that the operations reflect natural memory behavior, traces are complete, state labels are authoritative, forgetting is safe, leakage controls work, failures are causally diagnosed, results reproduce, or the benchmark establishes general memory capability, privacy, production fitness, or readiness.

## Why this is distinct

The reusable chain is `interaction evidence and authority → operation trigger → intended target and scope → prior memory state → candidate write/update/delete/retain/retrieve operation → realized state transition → later access and semantic adoption → endpoint action/artifact → privacy, forgetting, and downstream consequence`. A correct answer can hide stale or unauthorized state, accidental retrieval, failed deletion, or leakage; an operation-label error need not cause a consequential endpoint failure. These must remain separate estimands.

MemOps could supply an executable diagnostic vocabulary for workspace and memory evaluation, but a controllable generation pipeline may co-author the dialogue, latent state, operation request, transition oracle, and answer. A full review should therefore test event-projection fidelity, authority and valid-time, operation observability, alternate legitimate state representations, negative evidence for deletion/forgetting, leakage definitions, evaluator dependence, clustered synthetic lineage, repeated reliability, and whether failure labels identify causes or only surface mismatches.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier context/memory evaluation), B (evidence-bearing state transitions as expertise/evaluation primitives), and C (trace and causal-diagnosis infrastructure).
- **Concrete evidence/artifact:** immutable-v1 deep review plus a pinned official-release audit if an author-linked release exists.
- **Uncertainty clarified:** whether explicit lifecycle traces support diagnosis of memory operations or only conformance to an authored conversational state machine.
- **Mode:** narrow expansion/validation; conversational memory is a reusable instrumentation stress case, not a permanent benchmark scope.
- **Duplication/scope:** no local duplicate; mandatory comparison with MemoryArena, LongMemEval v2, EvoMemBench, and MemSyco-Bench prevents a parallel memory schema without evidence.
- **Useful completion:** separate event projection, state authority, operation-label agreement, realized transition, access, adoption, downstream utility, forgetting, leakage, causal diagnosis, reliability, consequence, and readiness.

Added one task: `review-memops-lifecycle-memory-validity` (priority 7). The consented expert micro-pilot and evidence-request interface ablation remain much higher priority.

## Operational note

The required initial `git pull --ff-only` succeeded. Pre-existing untracked paper-source, release-archive, and site files were not touched.

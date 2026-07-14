# Scouting note — memory scope/content and baseline validity

**Timestamp:** 2026-07-14T22:53:23Z  
**Scope:** Narrow expansion against charter objectives A/B/C. At intake the queue had 233 tasks: 226 completed, four blocked, two pending human decisions, and one pending worker review (MapSatisfyBench). Existing deep reviews cover supplied history, environment-experience memory, interdependent-session action, and procedural-memory transfer, but not a unified comparison of memory mechanisms across both scope and content axes.

## Substantive finding (triage only)

**EvoMemBench: Benchmarking Agent Memory from a Self-Evolving Perspective**

- Immutable record: https://arxiv.org/abs/2605.18421v2
- Immutable PDF: https://arxiv.org/pdf/2605.18421v2
- Official paper-linked repository: https://github.com/DSAIL-Memory/EvoMemBench
- The arXiv API identifies Yuyao Wang, Zhongjian Zhang, Mo Chi, Kaichi Yu, Yuhan Li, Miao Peng, Bing Tong, Chen Zhang, Yan Zhou, and Jia Li; primary category `cs.CL` with `cs.AI` and `cs.LG`; v1 submitted 18 May 2026 and v2 updated 15 June 2026. The metadata summary contains no withdrawal notice. The immutable abstract/PDF and repository URLs returned HTTP 200.
- The **v2 abstract** organizes evaluation along memory scope (in-episode versus cross-episode) and content (knowledge-oriented versus execution-oriented), compares 15 memory methods against long-context baselines under a standardized protocol, and reports that no memory form dominates all settings. It further reports retrieval advantages for knowledge tasks and procedural/long-term-memory advantages for execution tasks when stored experience matches task structure. These are author-reported abstract claims, not independently verified findings.
- The official repository exposes separate benchmark surfaces and localized forks of evaluated memory systems; search results identify a cross-episode knowledge pipeline over context-grouped CL-bench data. A full audit must pin the release and inspect whether all four conceptual cells share comparable episode boundaries, information budgets, solvers, feedback, datasets, and scoring.
- The distinctive validity question is whether the claimed memory taxonomy describes separable mechanisms or bundles unlike datasets and configured systems. “Memory helps when context is insufficient” is only interpretable if long-context and memory conditions receive equivalent authorized evidence and compute, and if storage, update, retrieval, adoption, and downstream action are observed separately. Matching prior experience to task structure may also introduce lineage overlap that looks like procedural transfer.
- This is metadata, abstract, URL, repository-surface, and duplicate triage only. The PDF body, appendices, code, datasets, benchmark instances, memory-system forks, prompts, trajectories, results, and statistics were not read or audited. No claim is made that EvoMemBench establishes self-evolution, general memory quality, transfer, knowledge-work capability, or readiness.

## Benchmark implication to test

A memory comparison needs a typed chain: `experience/event identity → authority and episode boundary → memory-write opportunity → stored representation/version → update/delete/contradiction handling → retrieval opportunity and budget → retrieved evidence → solver adoption → action/artifact consequence → criterion observation`, while separately pinning no-memory and long-context evidence budgets, system identity, feedback, task lineage, invalid trials, and cost. Scope and content should be tested as crossed factors where possible, not inferred from unrelated benchmark families.

A full audit should reconstruct one cell from source events through score and compare the protocol with LongMemEval v2, MemoryArena, OdysseyBench, AFTER, and the repository's experience-memory-transfer contract. It should test whether current-context insufficiency is experimentally controlled, whether memory systems receive equal information and tuning, whether cross-episode gains survive held-out task structures, and whether “self-evolving” means persistent state change rather than ordinary retrieval from a supplied store.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier memory evaluation), B (experience-to-action evidence chain), and C (configured-system and longitudinal evaluation evidence).
- **Evidence/artifact sought:** immutable-v2 deep review, pinned official-release audit, and one event→write/update→retrieve→adopt→action→score reconstruction.
- **Uncertainty clarified:** whether the scope/content taxonomy and comparisons isolate memory mechanisms or aggregate dataset, lineage, budget, solver, and harness differences.
- **Mode/balance:** one low-priority review task creates a two-item worker research backlog; no broad search bundle was added.
- **Duplication/scope:** adjacent reviews cover individual memory estimands but not this crossed taxonomy and 15-system protocol; this is a general configured-memory validity case, not a self-improving-agent scope shift.
- **Useful completion:** preserve release identity, data/task lineage, episode and feedback boundaries, evidence/compute budgets, memory operations and observer views, paired baselines, missingness/invalids, statistics, cost, and strict claim ceilings.

Queue one review task only: `review-evomembench-memory-scope-content-validity` (priority 15).

## Operational note

The required initial `git pull --ff-only` failed because the HTTPS GitHub remote lacks a noninteractive credential (`could not read Username`). The run proceeded from local state. The pre-existing untracked `data/papers/source/` tree was not modified.

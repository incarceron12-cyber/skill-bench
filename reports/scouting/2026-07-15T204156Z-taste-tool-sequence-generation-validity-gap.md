# Scouting note — tool-sequence-first task-generation validity gap

**Timestamp:** 2026-07-15T20:41:56Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Queue inspection found 292 tasks: 287 completed, three blocked, two pending, and no source/research/review backlog. Recent scouting already covered live evidence, cross-artifact professional work, memory, permissions, privacy, user constraints, expert transfer, and scalable evaluation. This run searched only for a missing benchmark-lifecycle question: whether generating tasks from tool sequences broadens meaningful construct coverage or merely action-combination coverage.

## Substantive finding — triage only

**A Matter of TASTE: Improving Coverage and Difficulty of Agent Benchmarks** — Tomer Keren, Nitay Calderon, Asaf Yehudai, Yotam Perlitz, Michal Shmueli-Scheuer, and Roi Reichart; arXiv:2605.28556v2.

- Immutable record: https://arxiv.org/abs/2605.28556v2
- Immutable PDF: https://arxiv.org/pdf/2605.28556v2
- Official repository pinned during scouting: https://github.com/tomerkeren42/TASTE-task-synthesis-from-tool-sequence-evolution/tree/d53da23956d63e2e6d9f6f5ba77fc5d0eca6b173
- The arXiv API identifies v1 as submitted 27 May 2026 and immutable v2 as updated 2 June 2026 in `cs.AI`; the metadata abstract contains no withdrawal or retraction notice. The versioned abstract and PDF returned HTTP 200; a versioned arXiv HTML rendering was unavailable (HTTP 404).
- The abstract proposes TASTE, which reverses normal task construction: it learns and samples tool sequences with an adaptive contrastive n-gram model trained on LLM validity signals, clusters the pool, instantiates representative sequences as tasks, and iteratively evolves difficulty. It reports a three-domain extension of τ²-Bench, evaluation of 11 agent/user-model pairs, substantial score drops, and more than twice as many unique tool combinations. These are author-reported abstract claims, not independently verified findings.
- GitHub API metadata identifies a non-fork repository created before arXiv v1, with three commits and head `d53da23956d63e2e6d9f6f5ba77fc5d0eca6b173` dated 31 May 2026. Root inventory exposes `src/`, `artifacts/`, packaging, README, and a nonstandard license.
- The pinned README—not the paper—describes three stages: signed n-gram sequence sampling with LLM validity feedback; k-medoids selection under a typed/group-weighted edit distance; and LLM task authoring plus a ground-truth agent, retries, patching, and reclustering. Optional evolution adds DB decoys and rewrites user scenarios, then falls back to a lite or original version if validation fails. It names airline, retail, and telecom domains and says artifacts include domain policies, tool schemas, seeds, checkpoints, clusters, prompts, and historical task sets. The README also says the under-review repository is for review/reproduction only, asks readers not to redistribute it, and promises a later permissive license.
- Only metadata, abstract, endpoint status, repository metadata/root inventory, and the pinned README were inspected. The paper body, appendices, source code, prompts, seeds, generated sequences/tasks, DB states, labels, graders, outputs, results, and statistics were not read or executed. No claim is made that sequence labels are valid, clusters cover meaningful work, generated tasks preserve source authority, ground-truth traces are sufficient or minimal, traps are fair, scores reproduce, or TASTE establishes agent capability, realistic professional work, saturation repair, production fitness, or readiness.
- Repository-wide searches found no exact title, arXiv-ID, TASTE, or tool-sequence-generation review/task. The closest completed work—Anchor, SLBench, SOP-Bench, generated-workspace conformance, task health, and benchmark lifecycle—covers projection drift or generated cases but not this exact sequence-first coverage-and-difficulty pipeline.

## Why this is distinct

The reusable evidence chain is `domain/work demand and authority → tool/action universe and equivalence policy → seed-task selection → sequence model and validity labels → sampled pool and coverage denominator → distance/clustering/medoid selection → natural-language scenario, initial state, source evidence, and grader projection → executable witness and accepted alternatives → adversarial difficulty intervention → retained/failed/fallback task lineage → configured-system trials → saturation/coverage claim`. Counting unique tool combinations can reveal neglected action patterns, but it does not establish semantic workflow diversity, consequence coverage, professional prevalence, or valid task composition. Conditioning retention on one model-driven witness can also select generator-compatible tasks and erase difficult-but-valid alternatives, while adversarial evolution may create recognizable gotchas rather than legitimate expert decision boundaries.

A full audit should separate syntactic action coverage, semantic requirement/workflow coverage, source and user authority, executable feasibility, witness sufficiency, alternative-path completeness, criterion validity, retry/attrition selection, difficulty versus defect, configured agent/user effects, uncertainty, costs, lifecycle renewal, and transport. Existing generation-conformance, authority/provenance, task-health, artifact/check, trace, metric, and validity machinery should host reusable lessons unless an exercised nonduplicate gap is proven.

## Charter decision filter and queue action

- **Objectives advanced:** A (benchmark-construction and lifecycle frontier), B (requirements and consequences projected from generated action structures), and C (executable task/state/check packages).
- **Concrete evidence/artifact:** immutable-v2 deep review plus a timing- and license-aware audit of pinned repository commit `d53da23956d63e2e6d9f6f5ba77fc5d0eca6b173`, including one end-to-end retained-item reconstruction if artifacts permit.
- **Uncertainty clarified:** whether sequence-first synthesis expands meaningful benchmark construct coverage or mainly creates syntactically diverse, generator/evaluator-coupled tasks with lower scores.
- **Mode:** narrow expansion feeding consolidation; the three service domains are method test beds, not a scope commitment.
- **Duplication/scope:** no exact local duplicate; comparison with τ²-Bench, Anchor, SLBench, SOP-Bench, task health, and lifecycle machinery is mandatory.
- **Useful completion:** preserve pool/selection/attrition denominators and produce a claim ladder separating action-combination coverage, semantic coverage, task validity, legitimate difficulty, saturation repair, configured-system performance, professional validity, production fitness, and readiness.

Added one low-priority task: `review-taste-tool-sequence-task-generation-validity` (priority 5). The pending dual-task delayed-obligation build and consented expert micro-pilot remain substantially higher priority.

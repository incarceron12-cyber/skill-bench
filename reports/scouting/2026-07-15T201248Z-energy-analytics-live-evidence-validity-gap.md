# Scouting note — live-evidence professional analytics validity gap

**Timestamp:** 2026-07-15T20:12:48Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Queue inspection found 291 tasks: 286 completed, four blocked, one pending human prerequisite, and no source/research/review backlog. Recent scouting already covered memory, permissions, privacy, user constraints, procedural transfer, adaptive grading, production evaluation, and cross-artifact optimization, so this run searched only for an unrepresented combination of expert-authored professional analysis, live external evidence, quantitative tools, and source-validity grading.

## Substantive finding — triage only

**How Do Tool-Augmented LLM Agents Perform on Real-World Energy Analytics Tasks?** — David Akinpelu, Akintonde Abbas, Rereloluwa Alimi, and Ayodeji Lana; arXiv:2606.26346v1.

- Immutable record: https://arxiv.org/abs/2606.26346v1
- Immutable PDF: https://arxiv.org/pdf/2606.26346v1
- Immutable HTML: https://arxiv.org/html/2606.26346v1
- Official release named in the paper/search record and pinned during scouting: https://github.com/Tume-AI/energy-evals/tree/90cc6165d514cdc37c3a3df8de95a9839a1f3a08
- The arXiv API identifies immutable v1 as submitted 24 June 2026 in `cs.AI`; its abstract contains no withdrawal or retraction notice. The versioned abstract, PDF, and HTML endpoints returned HTTP 200.
- The abstract describes 243 expert-curated problems across market-data retrieval/analysis, knowledge retrieval/interpretation, and quantitative modeling/decision analytics. Named work includes price and demand analysis, tariff impacts, asset revenue/returns, hedging, and optimization. The configured tools reportedly include live U.S. ISO market APIs, regulatory docket and tariff search, asset optimization, and document retrieval. Evaluation reportedly separates approach correctness, answer accuracy, attribute alignment, and source validity with category-aware routing. These are author-reported abstract claims, not independently verified findings.
- The arXiv HTML conversion exposed almost no usable section structure, and no paper body was read during scouting.
- GitHub API inspection found an MIT-licensed, non-fork repository created one day after arXiv submission, with one visible head commit (`90cc6165d514cdc37c3a3df8de95a9839a1f3a08`, 25 June 2026). Root inventory exposes configuration, data, framework/tool code, a public-release trace directory, sandbox, scripts, and dependencies.
- The pinned README—not the paper—describes a ReAct runner, optional live search/market/tariff/weather/regulatory tools, sandboxed Python and optimization, per-run JSONL traces, token/latency logging, and LLM-judge evaluation. Root inventory exposes only `data/evals_tasks_only_188.csv` (188 in the filename), creating a concrete release-conformance question against the abstract's 243 tasks. Only repository metadata, root inventory, the README, and three shallow directory inventories were inspected; no task row, trace, configuration body, grader, tool implementation, result, or sandbox code was read or executed.
- Repository-wide searches for the exact title, arXiv ID, and distinctive energy-analytics phrases found no local review or queue task. `EvoAgentBench` had already been triaged and rejected by an earlier scout. The closest completed work—ClawArena, DORA, BigFinanceBench, OncoRounds, performance-optimization reliability, and authority/evidence-chain machinery—covers adjacent dynamic evidence or professional analytics but not this exact live-source × expert-task × quantitative-tool × source-validity combination.
- This is **metadata, abstract, endpoint, release-location, commit/root-inventory, pinned-README, and duplicate triage only**. The paper body, appendices, 243 claimed tasks, 188-row released file, expert process, live sources, tools, prompts, traces, graders, labels, outputs, results, statistics, costs, and code were not read or audited. No claim is made that tasks are authentic or representative, sources are time-valid, tools return correct data, models are valid, judges are calibrated, results reproduce, or the benchmark establishes energy expertise, professional utility, capability, production fitness, or readiness.

## Why this is distinct

The reusable chain is `professional demand and expert authority → question and decision time → admissible source universe/version → live access and tool identity → retrieved observation and provenance → quantitative transformation/model assumptions → answer/artifact proposition → source-validity and analytical checks → expert acceptance → decision use and consequence`. A live API can improve ecological resemblance while weakening replayability, changing the available evidence and correct answer between trials. Conversely, freezing all values can improve reproducibility while ceasing to test live evidence acquisition. A source-validity judge may check citation form or apparent relevance without verifying that the source, timestamp, query, returned bytes, and transformation actually entail the claim.

A full audit should separate task-author authority, frame/selection/attrition, question valid-time, source and API versions, availability/failure denominators, tool outputs and transformations, quantitative-model/reference validity, alternate valid analyses, category routing, criterion and judge calibration, configured-system identity, repeats, costs, release correspondence, and claim scope. Existing authority, provenance, valid-time, evidence-chain, artifact-view, metric, task-health, trace, environment, and validity machinery should host reusable lessons unless an exercised nonduplicate gap is proven.

## Charter decision filter and queue action

- **Objectives advanced:** A (realistic professional-agent and production-evaluation frontier), B (expert knowledge and source-time rules transformed into task/check requirements), and C (tool traces, quantitative transformations, source evidence, and grader observations).
- **Concrete evidence/artifact:** immutable-v1 deep review plus a timing-aware audit of pinned release commit `90cc6165d514cdc37c3a3df8de95a9839a1f3a08`.
- **Uncertainty clarified:** whether the instrument measures source-grounded, time-valid professional analysis or primarily authored-question/LLM-judge agreement under mutable services.
- **Mode:** narrow expansion feeding later consolidation; energy analytics is a bounded stress test of reusable live-evidence validity, not a permanent domain choice.
- **Duplication/scope:** no exact local duplicate; mandatory comparison with ClawArena, DORA, BigFinanceBench, OncoRounds, performance reliability, and existing evidence/valid-time contracts prevents parallel infrastructure.
- **Useful completion:** reconcile the 243 claimed versus 188 named released tasks and produce a claim ladder separating package availability, task validity, source-time validity, analytical correctness, expert acceptance, professional utility, production fitness, and readiness with exact paper/release locators.

Added one low-priority task: `review-energy-analytics-live-evidence-validity` (priority 5). The consented expert micro-pilot remains substantially higher priority.

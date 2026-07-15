# Scouting note — prospective-memory intention-to-action validity gap

**Timestamp:** 2026-07-15T18:15:34Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Initial queue inspection found 285 tasks: 280 completed, three blocked, one pending human prerequisite, and one pending consolidation; no source, research, review, or claimed backlog remained. The reviewed corpus already covers memory access/adoption, interdependent experience and action, evidence authority/supersession, lifecycle operations, proactivity, underspecified action boundaries, and longitudinal office state. This run therefore followed one explicitly deferred lead from the latest memory scout: controlled evaluation of intentions that must survive intervening work and fire only when a future cue or latent state makes action due.

## Substantive finding — triage only

**PM-Bench: Evaluating Prospective Memory in LLM Agents** — Genglin Liu and Saadia Gabriel; arXiv:2607.12385v1.

- Immutable record: https://arxiv.org/abs/2607.12385v1
- Immutable PDF: https://arxiv.org/pdf/2607.12385v1
- Immutable HTML: https://arxiv.org/html/2607.12385v1
- Paper-linked release pinned during scouting: https://github.com/genglinliu/PMBench/tree/e1093c470c8981daf522d4ef047a7c3a71e077d7
- The arXiv API identifies immutable v1 as submitted 14 July 2026 in `cs.AI`; its abstract contains no withdrawal or retraction notice. The versioned abstract, PDF, and HTML endpoints returned HTTP 200 during scouting.
- The abstract defines prospective memory as executing an intention at a future cue or state while other activities continue. It says PM-Bench adapts the cognitive-science Virtual Week paradigm into a simulated seven-day text environment where agents maintain user intentions, execute delayed intentions, and monitor latent environmental changes.
- The abstract reports eight models under eight agent configurations, a best F1 of 65.1% for a GPT-5.4 agent, and no universally dominant improvement strategy. These are author-reported abstract claims, not independently verified results.
- Structural inspection of the immutable HTML—not a full reading—confirmed sections on scenario design, data generation, solvability/consistency validation, benchmark interface, evaluation metrics, prompting, and failure analysis. It also exposed the official GitHub link.
- GitHub API inspection verified a public non-fork repository, default branch `main`, pinned commit `e1093c470c8981daf522d4ef047a7c3a71e077d7` dated 14 July 2026, and root directories for `data`, `runs`, `sim`, and `webapp`. GitHub reports no detected license and the root inventory exposed no license file. No README body, source file, scenario, run, prompt, metric implementation, result, or test was read or executed.
- Repository-wide searches found no local review or queue task for the exact title, arXiv ID, prospective memory, deferred intentions, or future cues. The earlier MemOps scouting note mentioned PM-Bench only as an intentionally deferred candidate. Closest completed reviews include MemoryArena, LongMemEval v2, OdysseyBench, UniClawBench, UnderSpecBench, and MemOps; none makes cue-conditioned delayed intention execution amid ongoing activity its primary instrument.
- This is **metadata, abstract, endpoint, section-structure, release-location, commit-identity, root-inventory, and duplicate triage only**. The paper body, appendices, cognitive-science adaptation, generation pipeline, scenarios, cue taxonomy, hidden channels, updates, validation records, prompts, agent configurations, metrics, denominators, runs, errors, costs, code, data, and results were not read or audited. No claim is made that intentions are naturally sourced or authorized, cues are observable and sufficient, latent-state querying is realistic, task timing is valid, generated scenarios are independent, F1 supports operational reliability, configurations are comparable, results reproduce, or the benchmark establishes general memory capability, proactive agency, professional validity, production fitness, or readiness.

## Why this is distinct

The reusable chain is `authorized intention and creation time → target cue/state definition → intervening activity and evidence updates → retention without premature execution → cue availability/observation/interpretation → due-status decision → timely action, justified deferral, clarification, or cancellation → realized state and collateral effects → expiry/closure evidence`. Retrospective recall does not establish timely execution; correct execution can still be premature or unauthorized; failure can arise from retention, cue monitoring, latent-state access, due-status inference, conflict resolution, or action realization. A text simulator can author the intention, hidden state, cue, query interface, due-time oracle, and grader together, so apparent diagnosis may be closed-world conformance rather than transport to real work.

A full audit should separate intention provenance and authority, event- versus time-based cues, cue observability, monitoring/query cost, update and cancellation handling, ongoing-task interference, overdue and premature action, alternate legitimate timing windows, clarification/escalation, action realization, collateral effects, invalid runs, repeat reliability, and professional consequence. It should test whether solvability validation is independent of the generator and grader, whether micro/macro F1 hides severe timing errors or task-family clustering, whether eight configurations preserve configured-system identity and comparable information budgets, and whether the pinned release reproduces the paper instrument and reported results.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier memory and realistic agent evaluation), B (future-condition decision thresholds and failure signatures), and C (trace/state/action diagnostic machinery).
- **Concrete evidence/artifact:** immutable-v1 deep review plus a timing-aware pinned-release audit.
- **Uncertainty clarified:** whether PM-Bench diagnoses prospective intention maintenance and cue-conditioned action, or primarily agreement with a co-authored seven-day simulator and timing oracle.
- **Mode:** narrow expansion/validation; a simulated week is an instrumentation stress case, not a permanent benchmark domain or a claim that all knowledge work is scheduling.
- **Duplication/scope:** no local duplicate; mandatory comparison with MemoryArena, LongMemEval v2, OdysseyBench, UniClawBench, UnderSpecBench, and MemOps prevents a parallel memory subsystem.
- **Useful completion:** a bounded claim ladder separating intention authority, retention, monitoring, cue access, due-status inference, temporal decision, action realization, endpoint consequence, reliability, transport, and readiness, grounded in exact paper/release locators.

Added one low-priority task: `review-pmbench-prospective-memory-validity` (priority 6). The consented expert micro-pilot and request-receipt repair consolidation remain substantially higher priority.

## Operational note

The required initial `git pull --ff-only` succeeded. Pre-existing untracked paper-source, release-archive, and site files were not touched.

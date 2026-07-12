# Scouting note — ultra-long-horizon within-run learning validity gap

**Timestamp:** 2026-07-12T21:18:45Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Queue inspection found 161 completed tasks, one pending build, two blocked builds, and no pending source/research/review work. Existing reviews cover longitudinal evaluation, memory-conditioned action, reliability, and closed-loop evaluator feedback, but not a cross-domain benchmark reporting 12–72-hour within-run learning curves under multilevel environmental feedback.

## Substantive finding (triage only)

**EdgeBench: Unveiling Scaling Laws of Learning from Real-World Environments**

- Immutable arXiv record: https://arxiv.org/abs/2607.05155v1
- Immutable PDF: https://arxiv.org/pdf/2607.05155v1
- Official repository: https://github.com/ByteDance-Seed/EdgeBench
- Official dataset: https://huggingface.co/datasets/ByteDance-Seed/EdgeBench
- arXiv/search metadata identifies v1 as submitted 2026-07-06 and describes 134 real-world tasks across scientific discovery, software engineering, combinatorial optimization, professional knowledge work, formal mathematics, and interactive games. Tasks reportedly sustain at least 12 hours of interaction, with 51 tasks publicly released.
- Official search results describe executable environments, multilevel feedback, complete learning trajectories, 12–72-hour windows, and 402 model/task learning curves. The arXiv HTML search result reports a mean recorded human expert effort estimate of 57.2 hours, but this number has not yet been checked against methods or released evidence.
- Repository-wide duplicate search found no EdgeBench title or arXiv ID. Nearby work is complementary: MemoryArena tests prior-session evidence and action; the longitudinal contract specifies persistent streams; UniClawBench exposes evaluator-to-simulator feedback; reliability and metric records cover repeated outcomes and aggregation.
- The arXiv, author-owned GitHub, and official Hugging Face URLs were independently surfaced. A reviewer must pin exact commits/revisions and verify the reported/released task and result denominators.
- This is **metadata/abstract and release-location triage only**. The paper, appendices, tasks, environments, expert records, feedback channels, judges, harness, trajectories, result artifacts, learning curves, fits, and statistics were not fully read or inspected. No claim is made that the benchmark identifies learning or a general scaling law.

## Benchmark implication to test

EdgeBench could provide a rare empirical design for measuring improvement during consequential, ultra-long agent runs rather than only endpoint success. The central validity question is whether score-over-time identifies learning rather than repeated search, evaluator coaching or leakage, resource consumption, retries, task selection, censoring, harness changes, or survivorship. A full audit should separate local environment feedback from authoritative judge feedback; feedback availability from agent uptake; within-run state persistence from model adaptation; task-specific curves from cross-task aggregation; and released evidence from headline scaling claims. The reusable target is cross-domain longitudinal, information-flow, reliability, metric, and validity machinery—not redefining skill-bench around self-improving agents.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier realistic-agent and production-evaluation research), B (valid learning and feedback estimands), and C (executable longitudinal/trace/metric contracts).
- **Evidence/artifact sought:** immutable full-paper review plus pinned repository/dataset audit, with task/expert-effort/release denominators, feedback-information map, configured-system identity, learning-curve estimands, and claim ceilings.
- **Uncertainty clarified:** whether reported within-run improvement and cross-model temporal trends are attributable to agent learning, and which cross-domain/professional/scaling claims the released evidence supports.
- **Mode/balance:** narrow expansion; the ready backlog otherwise contained one feedback-boundary build.
- **Duplication/scope:** distinct from memory retrieval, static repeated reliability, and closed-loop repair because it measures extended iterative performance trajectories across heterogeneous executable tasks. It does not commit the project to self-improving-agent evaluation.
- **Useful completion:** reconstruct sampling, expert provenance, environment and feedback identity, budgets, resets/persistence, stopping/censoring, curve construction and aggregation, uncertainty, release fidelity, and exact supported/excluded claims; reuse existing contracts where possible.

Added `review-edgebench-within-run-learning-validity` (priority 50). No second task was added.

# Scouting note — environment-sensitive performance-criterion reliability gap

**Timestamp:** 2026-07-15T09:12:04Z  
**Scope:** Narrow expansion against charter objectives A/B and the comparative benchmark-landscape program. Queue inspection found 260 tasks: 253 completed, four blocked, two pending human decisions, and one pending intervention-validity consolidation. The reviewed corpus covers repeated agent trials, task health, benchmark lifecycle, partial decisions, and coding-benchmark evolution, but not an empirical audit of executable performance criteria across machines and aggregation policies.

## Substantive finding — triage only

**Are Performance-Optimization Benchmarks Reliably Measuring Coding Agents?** — Zhi Chen, Zhensu Sun, Yuling Shi, David Lo, and Lingxiao Jiang; arXiv:2607.01211v1.

- Immutable record: https://arxiv.org/abs/2607.01211v1
- Immutable PDF: https://arxiv.org/pdf/2607.01211v1
- The arXiv API identifies immutable v1, submitted 1 July 2026, and its summary contains no withdrawal notice. The versioned abstract and PDF endpoints returned HTTP 200 during scouting.
- The abstract describes an audit of GSO, SWE-Perf, and SWE-fficiency based on replaying official reference patches for 740 performance-optimization tasks across four Google Cloud machine types. It reports that the reference patches satisfy each benchmark's own validity rules on every cross-machine replay for only 39/102 GSO, 11/140 SWE-Perf, and 411/498 SWE-fficiency tasks.
- It also reports that the official GSO and SWE-fficiency rankings disagree on 9/28 pairwise comparisons among eight shared public submissions, that the ten most heavily weighted SWE-fficiency tasks receive 58.5–82.8% of score weight, and that at least one of ten public submissions matches or beats the reference patch on 384/450 replay-valid GSO/SWE-fficiency tasks. These are author-reported abstract results, not independently verified findings.
- The canonical abstract page exposed no author-owned code, data, or project link, and exact-title/ID web searches located the paper but no official repository. A reviewer must inspect the complete paper for artifact links and record an absent release explicitly if none exists.
- Repository-wide exact title, arXiv-ID, and benchmark-name searches found no duplicate. Local work on stochastic evaluations, task health, partial benchmark decisions, LiveCodeBench, and lifecycle validity supplies adjacent concepts but does not audit cross-machine criterion stability or performance-score concentration.
- This is **metadata, abstract, endpoint, link-location, and duplicate triage only**. The paper body, methods, timing protocol, validity rules, tables, appendices, machine configurations, missingness, uncertainty, submissions, score implementations, and artifacts were not read or audited. No claim is made about the correctness of the reported counts, benchmark quality, ranking invalidity, coding-agent capability, professional validity, production fitness, or readiness.

## Why this is distinct

Executable grading is not automatically stable grading. Runtime is jointly produced by a patch, workload, machine, dependency state, warm-up and repetition policy, measurement noise, validity threshold, and aggregation rule. A useful benchmark chain is `artifact and environment identity → repeated criterion observation → typed invalidity/missingness → task-level signal stability → aggregation weights → pairwise/rank/threshold decision → bounded capability claim`. A patch can be functionally correct yet yield an unstable performance delta; a stable task-level estimate can still be distorted by score concentration; and a ranking can be policy-sensitive even when every run is reproducible.

For `skill-bench`, coding is a controlled stress case rather than a scope commitment. Similar instability can affect spreadsheet recalculation time, simulations, data pipelines, rendered media, or workflow latency. A full audit could clarify when environment-sensitive criteria require repeated observations, machine/configuration strata, minimum-effect regions, task-health demotion, aggregation-sensitivity reports, and decision-specific claim ceilings.

## Charter decision filter and queue action

- **Objectives advanced:** A (benchmark-validity frontier) and B (valid measurement and claim promotion), plus the established-versus-repair benchmark comparison program.
- **Concrete evidence/artifact:** immutable-v1 full-paper review reconstructing the three benchmark populations, 740-task replay design, four-machine protocol, validity and scoring rules, rank/weight sensitivity, saturation analysis, release status, and limitations.
- **Uncertainty clarified:** when an executable performance check supports a stable task signal, cross-environment transport, or ranking, and where criterion or aggregation policy rather than agent behavior drives the result.
- **Mode:** narrow expansion feeding consolidation/validation; no coding-domain narrowing.
- **Duplication/scope:** no local duplicate; adjacent reliability, lifecycle, and coding-evolution reviews are comparators.
- **Useful completion:** separate replayability, functional validity, runtime stability, cross-machine transport, aggregation sensitivity, saturation, and capability claims; transfer only reusable measurement principles to artifact-heavy knowledge work.

Added one task: `review-performance-optimization-benchmark-reliability` (priority 13). No second task was added because the intervention-validity consolidation and two human prerequisites remain higher priority.

## Operational note

The required initial `git pull --ff-only` failed because the HTTPS GitHub remote lacks a noninteractive credential (`could not read Username`). Local `main` was 114 commits ahead of `origin/main` before this scouting change. Pre-existing untracked paper/release artifacts were not modified.

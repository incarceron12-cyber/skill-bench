# Scouting note — proactive closed-loop evaluator-feedback gap

**Timestamp:** 2026-07-12T20:31:49Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Queue inspection found 159 completed tasks, one pending build, two blocked builds, and no pending source/research/review work. Existing reviews cover latent problem recognition, simulated participation, multilingual workflows, native evaluators, and stateful environments, but not a benchmark runtime in which a hidden evaluator returns structured information to a public user simulator during execution.

## Substantive finding (triage only)

**UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks**

- Immutable arXiv target: https://arxiv.org/abs/2607.08768v1
- PDF: https://arxiv.org/pdf/2607.08768v1
- Official repository: https://github.com/HKU-MMLab/UniClawBench
- Search metadata identifies v1 as submitted 2026-07-09 and describes 400 bilingual tasks organized around skill use, exploration, long-context reasoning, multimodal understanding, and cross-platform coordination.
- The official repository search result exposes a consequential runtime structure: an executor, a hidden answer supervisor that can read private references and returns pass/continue/fail plus score, and a public user simulator that receives visible trajectory data plus a four-field supervisor handoff. Repository documentation results also describe incremental cycle logs and credential separation.
- Repository-wide duplicate search found no UniClawBench title or arXiv ID. Nearby local work is complementary: KWBench studies unprompted recognition; HAS-Bench studies configurable simulated participation; PolyWorkBench studies multilingual workflow validity; Tool-Veritas audits native evaluators.
- Both arXiv and official GitHub URLs were surfaced directly by primary-source search. A reviewer must pin the exact repository commit and verify release timing and contents.
- This is **metadata/abstract and release-location triage only**. The paper, appendices, task corpus, bilingual pairs, runtime, private references, supervisor prompts, simulator handoff, environments, graders, traces, results, and statistics were not fully read or inspected. Abstract/repository claims are not treated as validated findings.

## Benchmark implication to test

The supervisor-to-simulator loop may make evaluator feedback part of the treatment. A full audit should determine whether “proactivity” is observed before feedback or induced by continue/fail signals; whether the handoff leaks hidden criteria or target progress; whether user-simulator authority and stopping behavior are fixed; whether English/Chinese tasks are equivalent forms; whether live cross-platform state is reproducible; and whether model-versus-framework comparisons are identified. The reusable target is information-flow, participation, task-health, configured-system, metric, and validity machinery across domains—not a permanent proactive-assistant benchmark scope.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier realistic-agent benchmark research), B (valid construct-to-observation links), and C (auditable runtime/evaluator information-flow contracts).
- **Evidence/artifact sought:** immutable full-paper review plus pinned official-release audit, with task/runtime/result denominators and a supervisor → simulator → agent information-flow crosswalk.
- **Uncertainty clarified:** whether closed-loop feedback measures independent initiative or a feedback-conditioned policy, and which real-world/bilingual/cross-platform claims the released evidence supports.
- **Mode/balance:** narrow expansion; the ready backlog otherwise contained one validation build.
- **Duplication/scope:** distinct from recognition-only, simulated-participation, multilingual-workflow, and evaluator-only reviews because it composes them in one runtime. It does not commit skill-bench to proactive assistants.
- **Useful completion:** reconstruct provenance, sampling, capability labels, bilingual equivalence, environment identity, runtime handoff, leakage controls, stopping, observers, factorial comparisons, uncertainty, reproducibility, and claim ceilings; reuse existing contracts where possible.

Added `review-uniclawbench-proactive-closed-loop-validity` (priority 49). No second task was added.

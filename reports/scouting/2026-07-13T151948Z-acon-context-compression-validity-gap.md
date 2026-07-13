# Scouting note — context-compression state-fidelity gap

**Timestamp:** 2026-07-13T15:19:48Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Queue inspection found 165 completed tasks, two pending consolidation tasks, two blocked tasks, and no pending source/research/review work. Existing reviews cover persistent memory, experience-derived context, long-horizon workflows, and configured-system isolation, but not context compression as an intervention that may reduce cost while selectively deleting authoritative state, contradictions, commitments, or diagnostic evidence.

## Substantive finding (triage only)

**ACON: Optimizing Context Compression for Long-horizon LLM Agents**

- Immutable arXiv record: https://arxiv.org/abs/2510.00615v3
- Immutable PDF: https://arxiv.org/pdf/2510.00615v3
- Official implementation: https://github.com/microsoft/acon; reachable `main`/HEAD `d63f9ae18959dc7215ff62899c94c5e8c56847ae` during this run.
- The arXiv API identifies v3 as updated 2026-06-01 in `cs.AI`/`cs.CL`. Its abstract describes natural-language optimization of guidelines that compress both environment observations and interaction history, using agent failure analysis without model fine-tuning, followed by distillation into smaller compressors.
- The abstract reports evaluation on AppWorld, OfficeBench, and multi-objective QA, claiming 26–54% lower peak token use alongside improved selected-task success and up to 46% improvement for smaller agents. These figures are discovery leads only; the reviewer must verify denominators, configurations, uncertainty, accounting, split hygiene, and released evidence.
- Targeted primary-source search found the author-owned Microsoft repository and experiment paths for AppWorld and OfficeBench. Exact release completeness, result artifacts, optimization data, prompts/guidelines, evaluation feedback boundaries, and reproducibility remain unaudited.
- Repository-wide duplicate search found no review or queue task for the title/ID; only a bibliographic citation appears in another paper extraction. Nearby reviews are complementary: Agentic Context Engineering concerns candidate lesson promotion; LongMemEval-V2 and MemoryArena concern retained experience; workflow reviews concern consequential state; Harness-Bench concerns configured execution. None directly tests compression fidelity versus task success and resource savings.
- This is **metadata/abstract and release-location triage only**. The paper, appendices, code, configurations, prompts, experiments, results, and artifacts were not fully read or inspected. No claim is made that ACON faithfully preserves state, improves general context management, transfers across agents/tasks, reduces end-to-end cost, or supports professional or production readiness.

## Benchmark implication to test

Context compression is part of configured-system identity and an information intervention, not a neutral implementation detail. A compressed agent may pass selected endpoint checks while losing source authority, valid-time qualifiers, contradictory evidence, failed attempts, side effects, pending commitments, or provenance needed for diagnosis. A full audit should therefore separate observation compression from history compression; compression policy and optimization feedback from the agent under test; token count from latency/cost; endpoint success from state/provenance fidelity; and selected benchmark gains from cross-task, professional, reliability, or production claims. The reusable target is a claim-bounded fidelity/cost tradeoff that maps to existing context, trace, artifact/state, metric, longitudinal, and validity machinery—not a new context-specific schema by default.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier context and production-agent evaluation), B (preserving evidence and judgment through configured interventions), and C (diagnostic configured-system and metric machinery).
- **Evidence/artifact sought:** immutable full-paper review plus pinned official-release audit, with exact compression contracts, optimization feedback flow, split and configuration identity, resource accounting, state-loss tests, ablations, and claim ceilings.
- **Uncertainty clarified:** whether reported token savings and task gains identify useful compression, and what evidence is required to show that compression preserves consequential work state rather than merely fitting selected endpoint graders.
- **Mode/balance:** narrow expansion; two healthy consolidation tasks remain ready, while the review/source/research backlog was empty.
- **Duplication/scope:** nonduplicate information-intervention question; AppWorld and OfficeBench are bounded evaluation substrates, not a scope commitment.
- **Useful completion:** verify the complete method and release; audit feedback/test leakage, state/provenance loss, cost accounting, ablations, and uncertainty; map only genuinely new obligations into existing cross-domain contracts; preserve strict professional, generalization, reliability, production, and readiness limits.

Added `review-acon-context-compression-validity` (priority 46). No second task was added.

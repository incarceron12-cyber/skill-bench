# Scouting note — interdependent experience-to-action validity gap

**Timestamp:** 2026-07-12T18:11:35Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Repository inspection found 148 completed tasks, one pending evaluator-observation build, one blocked real-elicitation contract, and no pending source/research/review work. The completed LongMemEval-V2 review explicitly leaves held-out action transfer unmeasured and cites MemoryArena, but MemoryArena itself has not been reviewed.

## Substantive finding (triage only)

**MemoryArena: Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks**

- Immutable arXiv target: https://arxiv.org/abs/2602.16313v1
- PDF: https://arxiv.org/pdf/2602.16313v1
- Official project: https://memoryarena.github.io/
- Paper-linked repository: https://github.com/ZexueHe/MemoryArena
- Repository HEAD observed during triage: `6cd9de14b71915e39ac742a20dc33785e14b6aab` (timing relative to arXiv v1 remains unverified).
- The arXiv API verified v1, published 2026-02-18. Its abstract describes human-crafted interdependent subtasks in multi-session memory-agent-environment loops, spanning web navigation, preference-constrained planning, progressive information search, and sequential formal reasoning. Agents are intended to distill earlier actions and feedback into memory and use it in later tasks.
- Repository-wide duplicate search found only citations in the LongMemEval-V2 and AlphaEval full-text extractions; no review, queue task, title, or arXiv-ID entry exists.
- This is **API-metadata/abstract and release-location triage only**. The PDF, appendices, task records, dependency construction, session/reset semantics, feedback channels, memory policies, baselines, graders, statistics, costs, and release implementation were not read or inspected. No claim is made that MemoryArena causally identifies memory use, demonstrates longitudinal learning, or generalizes to professional work.

## Benchmark implication to test

MemoryArena may supply the missing action-side contrast to LongMemEval-V2's retrospective evidence-delivery design: whether retained experience changes later consequential action in explicitly dependent tasks. A full audit must determine whether later success actually requires access to and adoption of prior experience, or can be explained by persistent environment state, repeated task structure, privileged feedback, parametric knowledge, session ordering, harness differences, or grader artifacts. The durable target is a typed chain—experience event → memory write → later access → evidence adoption → action/state consequence—not a single final success score.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier memory/agent benchmark research), B (experience-to-transfer validity), and C (longitudinal trace and causal-evidence contracts).
- **Evidence/artifact sought:** immutable full-paper review plus pinned official-release audit, with page/file locators and an experience/dependency/action crosswalk.
- **Uncertainty clarified:** whether interdependent multi-session evaluation identifies memory formation and causal downstream use rather than carryover and measurement confounds.
- **Mode/balance:** narrow expansion; existing ready work was building/validation only.
- **Duplication/scope:** not a duplicate of LongMemEval-V2, which deliberately measures context gathering and QA rather than held-out action. Existing synthetic experience-memory machinery provides an implementation comparison but no empirical benchmark evidence. Four task structures make this a cross-domain mechanism study, not a memory-only benchmark commitment.
- **Useful completion:** reconstruct dependency and reset semantics, memory interfaces, treatment identity, observers, uncertainty, failure attribution, cost, and release fidelity; compare directly with LongMemEval-V2 and map only nonduplicate implications into existing longitudinal, evidence-chain, trace, metric, and validity machinery.

Added `review-memoryarena-interdependent-experience-action-validity` (priority 53). No second task was added.

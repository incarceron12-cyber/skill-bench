# Scouting note — TheAgentCompany workplace-simulation validity gap

**Timestamp:** 2026-07-11T14:25:01Z  
**Scope:** Narrow expansion against charter objectives A/B/D after confirming 107 completed tasks, one pending consolidation task, one blocked real-elicitation task, and no ready source/review backlog. This run did not repeat broad discovery.

## Substantive finding (triage only)

**TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks**

- Latest versioned arXiv record returned by the API: https://arxiv.org/abs/2412.14161v3
- Immutable PDF: https://arxiv.org/pdf/2412.14161v3
- Official repository: https://github.com/TheAgentCompany/TheAgentCompany
- Repository HEAD observed during scouting: `98b68ef82a47690c316f42fddb05baafaab56851`
- arXiv API metadata describes a self-contained simulated software-company environment in which agents browse internal sites, write and run code, and communicate with coworkers; it reports 30% autonomous completion for the strongest tested baseline in v3.
- The benchmark is repeatedly used as an established workplace anchor by locally reviewed Workspace-Bench, OSWorld 2.0, SaaS-Bench, EnterpriseClawBench, Anchor, and Agents' Last Exam papers, yet it has no local acquisition, review, paper-index record, or queue task.
- **Evidence status:** metadata, citation-presence, and repository-presence triage only. The paper, appendices, task suite, environment, graders, baseline runs, and release history were not read during scouting. No claim is made that the tasks are representative of professional work, that selected checks capture consequential outcomes, that coworker communication is realistic, or that the current release reproduces the paper.

## Benchmark implication to test

A full paper-and-release audit should separate a realistic-looking workplace substrate from evidence of workplace construct validity. It should reconstruct task provenance and occupational frame, cross-service dependencies, coworker simulation and communication semantics, initial/reset state, alternate valid paths, grader predicate coverage, long-horizon and collaboration claims, cost, and release drift. The audit should compare this older anchor with Workspace-Bench, SaaS-Bench, EnterpriseClawBench, AgentCoop, and OSWorld 2.0 to determine which later systems actually repair its limits rather than merely adding files, services, agents, or longer trajectories.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier and influential benchmark evidence), B (realistic workplace-task validity), and D (family evolution consolidation).
- **Evidence/artifact sought:** immutable-v3 full-paper review plus pinned official-release audit with page/file locators and bounded retain/repair/test implications.
- **Uncertainty clarified:** what TheAgentCompany's task, environment, collaboration, and outcome evidence can support about consequential professional work, and which successor claims have a valid anchor.
- **Mode/balance:** one narrow review task restores a ready review item while one consolidation task remains pending; no additional source was added.
- **Duplication/scope:** repository search found citations but no acquisition, review, index record, or queue task. A simulated software company is a substrate case, not a permanent domain choice.
- **Useful completion:** reconstruct the versioned paper/release contracts, inspect representative tasks and graders, test paper-release correspondence, preserve sampling and validity limits, and update comparison maps only where the evidence changes a family conclusion.

Added `review-theagentcompany-workplace-simulation-validity` (priority 52). No second task was added.

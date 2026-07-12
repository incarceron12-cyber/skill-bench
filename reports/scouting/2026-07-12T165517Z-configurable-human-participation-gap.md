# Scouting note — configurable human-participation validity gap

**Timestamp:** 2026-07-12T16:55:17Z  
**Scope:** Narrow expansion against charter objectives A/B/C/E. Repository inspection found 143 completed tasks, one pending evaluator-repair build, one blocked task, and no pending source/research/review work. Existing reviews cover multi-agent handoffs, simulated coworkers, expert disagreement, participation governance, and production evaluation, but not an instrument that varies when, how, and by whom human input enters an agent workflow.

## Substantive finding (triage only)

**HAS-Bench: Evaluating LLM-Based Human-Agent Systems under Configurable Human Participation**

- Immutable arXiv target: https://arxiv.org/abs/2607.04329v1
- PDF: https://arxiv.org/pdf/2607.04329v1
- The arXiv API verified v1. Its abstract describes a graph-based framework in which humans and LLM agents have explicit roles, permissions, communication paths, and action authority. It reports evaluation across six domains while varying agency levels, interaction channels, and persona policies, with outcome and process measures for clarification, feedback use, control calibration, safety, initiative, and interaction cost.
- Repository-wide duplicate search found no title, `HAS-Bench`, or arXiv `2607.04329` match.
- This is **API-metadata/abstract triage only**. The PDF, appendices, task sources, human-participation protocol, participant recruitment, graph semantics, intervention assignment, domains, graders, statistics, costs, and any official release were not read or inspected. No claim is made that human participation causes improvement, that the configured conditions are comparable, that process measures are valid, or that findings generalize to professional work.

## Benchmark implication to test

A full paper-and-release audit can test whether human participation is represented as a reproducible treatment rather than an untyped source of assistance. The useful contrast is among participant identity and authority, information access, intervention timing, communication channel, feedback uptake, action control, burden, and resulting artifact/state—not a generic human-in-the-loop score. This could clarify how `skill-bench` should distinguish configured-system capability, assistance policy, escalation quality, human labor, recovery, and unsupported autonomous-agent claims.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier human-agent evaluation), B (authority and expertise-to-evaluation boundaries), C (configured-system and trace contracts), and E (clearer interpretation of assisted performance).
- **Evidence/artifact sought:** immutable full-paper review plus any paper-linked official release, with page/file locators and a treatment/authority/measurement crosswalk.
- **Uncertainty clarified:** whether the benchmark identifies effects of human participation modes and licenses collaboration claims, or confounds task, persona, authority, information, timing, and grader treatment.
- **Mode/balance:** narrow expansion; the only ready work is building/validation.
- **Duplication/scope:** no direct repository duplicate. AgentCoop and TheAgentCompany address agent handoffs and simulated coworkers; participation and disagreement reviews address governance and plural judgment. HAS-Bench is a bounded test of configurable mixed human-agent evaluation across domains, not a commitment to one collaboration workflow.
- **Useful completion:** reconstruct task and participant sampling, graph/treatment semantics, control conditions, process and outcome observers, uncertainty, burden/cost, release fidelity, and explicit claim ceilings; map only nonduplicate implications to existing configured-system, participation, trace, metric, and validity machinery.

Added `review-hasbench-configurable-human-participation-validity` (priority 52). No second task was added.

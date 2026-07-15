# Scouting note — user-simulator decision fidelity against consequential outcomes

**Timestamp:** 2026-07-15T00:35:06Z  
**Scope:** Narrow expansion against charter objectives A/B/C. At intake the queue had 237 tasks: 231 completed, four blocked, two pending human decisions, and no source/research/review backlog. Existing reviews separate simulated participants, interaction channels, authority, uptake, burden, and consequence, but none compares an LLM user simulator with real users making consequential choices under identical observed dialogue contexts.

## Substantive finding (triage only)

**Simulated Customers Never Walk Away: Decision Fidelity of LLM User Simulators Measured Against Real Purchase Outcomes**

- Immutable record: https://arxiv.org/abs/2606.20708v1
- Immutable PDF: https://arxiv.org/pdf/2606.20708v1
- Immutable HTML: https://arxiv.org/html/2606.20708v1
- The arXiv API identifies Liang Chen; categories `cs.AI`, `cs.CL`, and `cs.HC`; submitted 16 June 2026 with no later version. The metadata summary contains no withdrawal notice. The versioned abstract, PDF, and HTML URLs returned HTTP 200.
- The **v1 abstract** defines decision fidelity as whether a simulated population reproduces decision-state dynamics of real users facing consequential choices, rather than merely producing human-like dialogue. It reports a teacher-forced probe over 2,790 production conversations between an LLM sales agent and real customers, 793 linked to verified payment outcomes. The abstract reports an outcome-correlated “disengagement deficit”: simulators approximately reproduce eventual buyers but move eventual non-buyers toward continued purchase deliberation, with a cross-model replication and a weak response to an explicit permission-to-disengage prompt. These are author-reported abstract claims, not independently verified findings.
- This fills a distinct validity gap. Agent benchmarks frequently use LLM role-play as the user, customer, coworker, supervisor, or feedback source. Linguistic plausibility, agreement with assigned-goal role-play, and benchmark task success do not show that the simulator preserves stopping, refusal, abandonment, delayed choice, or other decision dynamics found when motivation is endogenous and outcomes matter.
- The paper also raises a selection and interpretation problem that only full review can resolve: payment-linked production conversations may provide unusually strong consequence evidence, but outcome availability, consent/privacy transformations, funnel censoring, intervention history, customer dependence, label timing, and teacher-forcing may constrain the estimand. A sales setting is a bounded falsification case for simulator validity, not a benchmark-domain recommendation.
- This is metadata, abstract, URL, and duplicate triage only. The paper body, appendices, data, ethics/privacy process, probe prompts, coding scheme, models, conversations, outcome linkage, exclusions, statistics, and any artifacts were not read or audited. No claim is made that the reported effect is valid, causal, representative, transferable beyond the studied context, or sufficient to judge any deployed sales agent.

## Benchmark implication to test

User-simulator evaluation needs a typed chain: `real interaction population and sampling → participant authority/consent and privacy transformation → versioned dialogue context → latent/endogenous motivation and observed proxies → simulator evidence view and role prompt → generated decision-state trajectory → stopping/abstention/action opportunity → realized user action and consequential outcome → outcome linkage/censoring → fidelity estimand → licensed simulator use`. Communicative similarity, assigned-goal compliance, state-transition agreement, and decision/consequence fidelity must remain separate.

A full audit should reconstruct the teacher-forced comparison and determine whether contexts, instruments, model calls, and labels are genuinely matched; how buyer/non-buyer status, disengagement, resistance, deliberation, and payment are operationalized; whether repeated turns are clustered by customer/conversation; how missing outcomes and selection are handled; and whether the claimed prompt intervention changes only disengagement permission. It should compare the evidence with HAS-Bench, DeskCraft, UniClawBench, SovereignPA-Bench, MapSatisfyBench, and the repository's participation-treatment and interaction-evidence chains.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier human/simulator evaluation), B (authority-to-decision-to-consequence validity), and C (scalable participant-simulator diagnostics).
- **Evidence/artifact sought:** immutable-v1 deep review, release/non-release audit, and a reconstructed population→context→probe→decision-state→real-outcome comparison.
- **Uncertainty clarified:** whether real consequential outcomes expose simulator defects hidden by assigned-goal or dialogue-similarity evaluation, and what evidence is needed before simulator-mediated benchmark results transport to human interaction.
- **Mode/balance:** one low-priority review restores a minimal research backlog; no broad search bundle was added.
- **Duplication/scope:** existing simulator reviews do not provide matched real-user consequential outcomes. The commercial conversation setting tests a general simulator-validity hypothesis and does not narrow `skill-bench` to sales or persuasion.
- **Useful completion:** preserve population and outcome denominators, consent/privacy and authority, intervention and context identity, motivation/decision-state operationalization, teacher-forcing semantics, clustering, missingness/censoring, cross-model and prompt comparisons, artifact availability, limitations, and strict claim ceilings; derive concrete tests for simulator use in knowledge-work benchmarks.

Added one task: `review-user-simulator-decision-fidelity` (priority 14).

MAG and AgentFootprint were triaged but not queued. MAG overlaps the mature web/computer-use and interaction-evidence streams and its arXiv metadata says release artifacts are forthcoming. AgentFootprint introduces a useful storage/reconstructability resource metric, but it is less direct than the current missing human-simulator consequence bridge and should not displace the one-task scout budget.

## Operational note

The required initial `git pull --ff-only` failed because the HTTPS GitHub remote lacks a noninteractive credential (`could not read Username`). Local `main` was 59 commits ahead of recorded `origin/main`; the run proceeded from local state. The pre-existing untracked `data/papers/source/` tree was not modified.

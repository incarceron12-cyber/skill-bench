# Scouting note — BrainPilot domain-skill and scientific-trace validity gap

- **Timestamp:** 2026-07-17T22:20:17Z
- **Evidence status:** arXiv API metadata/abstract, targeted web discovery, GitHub repository metadata, and recursive-tree triage only. The paper body, appendices, 72 Skills, knowledge sources, benchmark tasks, prompts, traces, auditor behavior, case studies, raw trials, costs, or results were **not** deeply read, downloaded, or executed during scouting.

## Substantive candidate — triage only

**BrainPilot: Automating Brain Discovery with Agentic Research** — Haoxuan Li et al.; arXiv:2607.15079v1.

- Immutable record/PDF/HTML: https://arxiv.org/abs/2607.15079v1 · https://arxiv.org/pdf/2607.15079v1 · https://arxiv.org/html/2607.15079v1
- Official repository: https://github.com/NeuroAIHub/BrainPilot at inspected commit [`7d3853f62caa23e6501a6e35f177c15b3f786af5`](https://github.com/NeuroAIHub/BrainPilot/commit/7d3853f62caa23e6501a6e35f177c15b3f786af5), committed 17 July 2026.
- The arXiv API identifies a `cs.AI` v1 submitted and last updated 16 July 2026. Its summary contains no withdrawal or retraction notice.
- The abstract describes a principal-investigator agent coordinating specialists grounded in a claimed 7,233-item brain-science knowledge base and 72 reusable methodology Skills across seven domains. It also describes a Graph of Trace linking subgoals, tool use, evidence, and claims; an Auditor for fabrication checking; three Agents' Last Exam tasks; a new BrainPilotBench-v0; end-to-end case studies; and open-model performance said to be comparable with a state-of-the-art framework at lower cost. These are author-stated abstract claims awaiting full-paper and artifact verification.
- GitHub API inspection found a public, unarchived, non-fork AGPL-3.0 repository with 1,374 tree objects. The tree exposes `SKILL.md` packages, skill creation/verification/access machinery, trace implementation and tests, documentation, and knowledge-base build scripts. At the inspected commit, the knowledge-base source/chunk/vector-store directories contain placeholders, and targeted path search found evaluation figures but no obvious BrainPilotBench-v0 task package or raw evaluation records. This establishes an inspectable implementation surface, not release conformance or empirical reproducibility.
- Exact title/ID searches found no local review, queue task, or scouting note. Adjacent reviews cover Agents' Last Exam, ReasFlow, AstaBench, scientific workflows/workspaces, procedural Skills, trace diagnosis, and human oversight, but not this exact domain-knowledge → Skill → trace → auditor → benchmark chain.

## Why this is a narrow, useful gap

The relevant evidence chain is:

`domain demand and expert/source authority → knowledge-item acquisition and rights → Skill derivation, review, and version → configured access and adoption → subgoal/tool/evidence/claim trace semantics → auditor evidence view and independence → human intervention opportunity, exercise, and uptake → executable analysis/artifact → scientific validity and downstream consequence → benchmark task/observer/score → cost and capability claim`.

BrainPilot potentially joins several central `skill-bench` concerns in one production-like scientific system: source-grounded domain configuration, procedural expertise, long-horizon artifact work, traceability, verification, and expert intervention. But package presence does not establish expertise: paper- or repository-derived Skills may be incomplete, outdated, unauthorized, or model-inferred; trace edges may record narration rather than causal evidence use; an Auditor sharing sources, prompts, models, or task targets may reproduce rather than independently detect errors; and task/judge agreement cannot establish valid scientific conclusions. The apparent release gap matters because figures and runnable framework code do not substitute for benchmark tasks, immutable trial records, knowledge payloads, expert approvals, or exact cost accounting.

Brain science is a bounded stress case for reusable expertise-transfer and scientific-workflow machinery, not a proposal to narrow `skill-bench` to neuroscience or build a domain-specific schema.

## Charter decision filter and queue action

- **Objectives advanced:** A (domain-agent and scientific-evaluation frontier), B (expertise-to-Skill, trace, auditor, and human-intervention validity), and C (knowledge, Skill, trace, artifact, grader, configured-system, and release records).
- **Concrete evidence:** immutable-v1 full-paper review plus timing-aware audit of the pinned official repository, released Skills/knowledge assets, trace and auditor implementation, benchmark tasks, configured evaluations, raw records, and costs.
- **Uncertainty clarified:** when curated domain context and reusable methodology Skills support configured-workflow evidence; whether trace/auditor records establish evidence fidelity or diagnosis; and which expertise-transfer, scientific-validity, expert-equivalence, cost, or readiness claims remain unsupported.
- **Mode:** narrow expansion. One consolidation and one human prerequisite were pending; one review restores a minimal autonomous evidence path without restarting broad search.
- **Duplication/scope check:** adjacent sources cover individual links but not this complete chain. The task must compare them, reuse existing contracts, and add no neuroscience-specific schema or pilot.
- **Useful completion:** page/path-grounded reconstruction of source and Skill authority, knowledge realization, trace semantics, auditor dependence, intervention opportunities, benchmark construction, exact denominators, configured systems, release conformance, cost accounting, and bounded retain/repair/test implications.

Added one task: `review-brainpilot-domain-skill-trace-validity` (review, priority 61). No other candidate was queued.

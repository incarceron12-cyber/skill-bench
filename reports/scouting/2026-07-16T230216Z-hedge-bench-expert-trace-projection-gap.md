# Scouting note — Hedge-Bench expert-trace projection gap

- **Timestamp:** 2026-07-16T23:02:16Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, official repository metadata/current README triage, Git ref/commit checks, and local corpus/queue duplicate searches only. The PDF, task corpus, source packs, expert traces, rubrics, grader implementation, and reported trials were **not** deeply read or audited during scouting.

## Substantive candidate — triage only

**Hedge-Bench: Benchmarking Agents on Hard, Realistic Tasks Pertaining to Financial Reasoning** — Eric Cho, Shawn Huang, Alice Lu, and Andy Lyu, arXiv:2606.03918v1.

- Immutable record: https://arxiv.org/abs/2606.03918v1
- Immutable PDF: https://arxiv.org/pdf/2606.03918v1
- Official release: https://github.com/Trata-Inc/trata-hedge-bench
- The arXiv API reports one version submitted 2 June 2026 in `cs.AI`; the abstract contains no withdrawal notice. Versioned abstract, PDF, and HTML endpoints returned HTTP 200.
- The abstract describes 102 purported on-the-job tasks grounded in explicit reasoning traces from professional hedge-fund analysts and reports frontier model/agent scores below 16%. These are author claims awaiting full-paper and release verification.
- The official non-fork repository resolves to sole commit `0a3c08a1e19bb62212fa4e7e30b53e9d77d46665`, committed 29 May 2026 before arXiv v1. Its README describes closed document sets, example solutions, hierarchical themes/action moves, Harbor containers, and semantic concept matching. It also says grading uses an LLM judge plus rubric, which makes the abstract's phrase “deterministic grading against verified expert steps” an important conformance and validity question rather than an established property. The repository declares no GitHub-detected license. File completeness, expert provenance, grader correctness, and paper-result reproducibility were not established in scouting.

## Why this is a narrow, useful gap

The reviewed corpus covers expert-authored criteria, narrated derivations, professional finance research, work-sample packages, and edit/interaction-derived context. No exact title/ID review or task covers a released benchmark that claims to project **professional analysts' explicit task-solving traces into hierarchical semantic action-move checks** over point-in-time source packs.

The reusable expertise-to-evaluation chain is:

`professional incident and contributor authority → raw analyst reasoning trace and source evidence → normalized theme/action move → public task/source pack → accepted alternative reasoning paths → semantic observer and criterion dependency → artifact/answer consequence → score and professional-work claim`.

A trace records one analyst's path, not necessarily the complete construct or all valid paths; a concept-matching judge is not deterministic merely because criteria are fixed; task originality does not prove non-exposure; and low scores do not establish occupational difficulty or readiness without task selection, expert authority, observer validity, configured-system, repeat, and invalid-run evidence. Finance is a bounded stress case for general expert-trace projection machinery, not a scope commitment.

## Charter decision filter and queue action

- **Objectives advanced:** A (realistic benchmark and expert-evaluation frontier) and B (tacit/explicit expertise-to-evaluation methodology).
- **Concrete evidence:** immutable-v1 full-paper review plus exact sole-commit release audit, including task/source/rubric/grader and paper-result conformance.
- **Uncertainty clarified:** whether real-work incident lineage and analyst traces survive normalization into fair, alternative-aware checks; whether the observer is deterministic, semantically valid, and reproducible; and what professional-work claim the released instrument can license.
- **Mode:** narrow expansion feeding consolidation. The queue has one pending consolidation task and one human prerequisite, with no pending review backlog.
- **Duplication/scope check:** nearest sources are BigFinanceBench, Data Therapist, ResearchRubrics, GDPval, and industrial expertise codification; none audits this exact incident→trace→action-move projection and sole-commit public package. No finance-specific subsystem is proposed.
- **Useful completion:** reconcile paper/release units and denominators; reconstruct contribution, selection, transformation, source-time, alternative-path, criterion-dependency, judge-call, repeat, cost, and invalidity evidence; test static release invariants without paid calls; and state bounded retain/repair implications for existing general contracts.

Added one task: `review-hedge-bench-expert-trace-projection-validity` (priority 9). No full-paper, expert-validity, implementation-correctness, capability, or readiness claim was made during scouting.

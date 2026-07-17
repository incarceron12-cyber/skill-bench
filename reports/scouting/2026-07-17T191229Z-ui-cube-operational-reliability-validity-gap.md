# Scouting note — UI-CUBE operational-reliability validity gap

- **Timestamp:** 2026-07-17T19:12:29Z
- **Evidence status:** arXiv API metadata/abstract, exact local duplicate search, targeted primary-source/release discovery, and GitHub API repository search only. The paper body, appendices, 226 tasks, application environments, validators, model trials, human records, statistical analyses, and any implementation or dataset were **not** deeply read, downloaded, executed, or audited during scouting.

## Substantive candidate — triage only

**UI-CUBE: Enterprise-Grade Computer Use Agent Benchmarking Beyond Task Accuracy to Operational Reliability** — Horia Cristescu, Charles Park, Trong Canh Nguyen, Sergiu Talmacel, Alexandru-Gabriel Ilie, and Stefan Adam; arXiv:2511.17131v1.

- Immutable record/PDF: https://arxiv.org/abs/2511.17131v1 · https://arxiv.org/pdf/2511.17131v1
- Official UiPath research page: https://www.uipath.com/ai/research/ui-cube-benchmark
- The arXiv API identifies a `cs.SE`/`cs.AI` v1 submitted 21 November 2025 and last updated the same day. Its summary contains no withdrawal or retraction notice.
- The abstract reports 226 tasks: 136 simple interactions, 50 copy/paste tasks, and 40 enterprise-application scenarios. It describes systematic interface variations, multi-resolution testing, application-state success validation, five evaluated models, and a human comparison involving participants without prior application experience.
- The abstract reports 67–85% model success versus 97.9% human success on simple tasks and 9–19% model success versus 61.2% human success on complex tasks. It interprets this discontinuity as evidence of architectural limits in memory, hierarchical planning, and state coordination and presents UI-CUBE as an enterprise-readiness diagnostic. These are author-stated abstract claims awaiting full-paper, denominator, uncertainty, and release audit.
- The official UiPath page was found through targeted search and describes UI-CUBE as deterministic and state-based. Targeted web and GitHub searches did not establish an author- or UiPath-owned public task/code/data release during scouting. Absence from these bounded searches is not proof that no release exists.
- Exact searches for the title and arXiv ID found no prior local review, queue task, paper-index record, or scouting note. Nearby corpus coverage includes OSWorld/2.0, WindowsWorld, OfficeBench, Workflow-GYM, WorkArena L1/++, and production/reliability measurement, but not UI-CUBE.

## Why this is a narrow, useful gap

The local corpus already covers GUI end states, process checkpoints, cross-application workflows, environment validity, repeated reliability, and human-time calibration. It does not directly audit UI-CUBE's proposed composition:

`task/work provenance → simple/complex tier assignment → application and UI version → interface/resolution perturbation → configured CUA and resource envelope → action trajectory → application-state observer → valid/invalid attempt and repeat → task success and failure signature → inexperienced-human comparison → complexity-cliff interpretation → operational-reliability or enterprise-readiness claim`.

A lower success rate on a selected complex tier may reflect longer horizons, application familiarity, instruction ambiguity, state-observer coverage, tool/interface mismatch, resolution, budget, or task-family composition; it does not by itself identify memory, hierarchical planning, or state coordination as the causal architecture defect. Deterministic application-state checks can establish selected endpoint predicates while missing collateral effects, process obligations, legitimate alternatives, artifact quality, reversibility, or professional acceptance. A human ceiling depends on recruitment, training, application exposure, time limits, allowed tools, incentives, invalid handling, task assignment, and clustering. A one-shot task pass rate is not operational reliability, and neither task conformance nor novice-human comparison establishes enterprise readiness, production fitness, or professional substitution.

UI-CUBE is therefore a bounded cross-domain measurement case for reusable state-observer, perturbation, human-baseline, reliability, and claim-validity machinery—not a proposal to narrow `skill-bench` to computer use or UI automation.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier computer-use and production-evaluation research), B (validity of reliability/readiness and human-comparison claims), and C (state observers, perturbations, failure diagnostics, and repeated-trial records).
- **Concrete evidence:** immutable-v1 full-paper review plus timing-aware audit of the official UiPath page and any task, environment, validator, human-baseline, and trial release.
- **Uncertainty clarified:** what the 226-task instrument and state checks actually observe; whether the simple/complex contrast isolates complexity; whether human conditions are comparable; and which operational-reliability, architectural-cause, and enterprise-readiness claims the evidence can license.
- **Mode:** narrow expansion. The autonomous source/review backlog was empty apart from one human prerequisite; one review restores a minimal research path without repeating broad discovery.
- **Duplication/scope check:** adjacent reviews cover surrounding GUI, state, workflow, environment, reliability, and human-calibration links but not this instrument and its claimed combination. No UI-specific schema or pilot is proposed.
- **Useful completion:** section/page/path-grounded reconstruction of task sourcing and tiering, environment/reset/version identity, state observers and collateral coverage, interface/resolution perturbations, configured systems, repeats/invalids, human recruitment and comparability, uncertainty/dependence, release conformance, cost/maintenance, and nonduplicate retain/repair/test implications while separating task conformance, complexity association, operational reliability, architectural cause, human parity, professional validity, enterprise readiness, and production fitness.

Added one task: `review-ui-cube-operational-reliability-validity` (review, priority 59). No other task was added. The recent corpus is already broad and the queue has an unresolved human-validity prerequisite, so further broad searches or multiple speculative review tasks would add noise rather than resolve a distinct gap.

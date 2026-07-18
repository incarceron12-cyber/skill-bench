# Scouting note — PPT-Eval native-presentation artifact validity gap

- **Timestamp:** 2026-07-18T00:23:56Z
- **Evidence status:** arXiv API metadata/abstract, URL checks, project-site discovery, GitHub repository metadata, recursive-tree inspection, and small README/task/rubric samples only. The paper body, appendices, complete task/rubric bank, source presentations, verifier implementation, human study, agent trials, or results were **not** deeply read, downloaded, rerun, or audited during scouting.

## Substantive candidate — triage only

**PPT-Eval: A Benchmark for Computer-Use Agents on PowerPoint Tasks** — Apurva Gandhi et al.; arXiv:2606.31154v1.

- Immutable record/PDF: https://arxiv.org/abs/2606.31154v1 · https://arxiv.org/pdf/2606.31154v1
- Official project and repository: https://microsoft.github.io/ppteval/ · https://github.com/microsoft/ppteval at inspected commit [`1b8b55a29e48fdc65d423689b6f2370ad91beeea`](https://github.com/microsoft/ppteval/commit/1b8b55a29e48fdc65d423689b6f2370ad91beeea).
- HEAD checks returned HTTP 200 for the immutable arXiv record/PDF, project site, and repository. The arXiv API reports v1 submitted and last updated 30 June 2026; its summary contains no withdrawal or retraction notice.
- The abstract describes 120 PowerPoint editing/creation tasks across 12 files, task-specific partial-credit rubrics for intermediate progress, unnecessary-change penalties and aesthetics, a reported Kendall tau-b of 0.77 with human judgments, and configured-agent results. These are author-stated abstract claims awaiting full-paper and release verification.
- GitHub API inspection found a public, unarchived MIT repository with a non-truncated 281-object recursive tree. It exposes 120 task-specific rubric JSON files, a 120-task registry, rubric execution and PowerPoint-diff code, GUI and CLI agent adapters, configuration files, and environment hydration machinery. A sampled rubric combines executable `python-pptx` checks with an extraneous-change criterion. The tree contains no `.pptx`, human-record, or result files; the README instead hydrates source files from URLs through OneDrive and PowerPoint Online normalization. This establishes a rich inspectable instrument surface, not paper/release conformance, source permanence/rights, complete native-state observation, rubric validity, human agreement, or empirical reproducibility.
- Exact title/ID searches found no local review, queue task, or scouting note. OfficeEval, MBABench, AgenticVBench, CutVerse, AIDABench, and artifact-view reviews cover adjacent native-artifact, rubric, temporal, visual, and release-validity issues, but none directly audits presentation-edit deltas under executable plus visual/aesthetic partial-credit criteria and a live PowerPoint normalization path.

## Why this is a narrow, useful gap

The relevant chain is:

`task/source authority and rights → immutable initial presentation → public edit obligation → GUI/CLI action trajectory → saved native OOXML delta → normalized/rendered evidence views → criterion applicability/dependency → executable and visual/aesthetic observations → collateral-change penalty → partial-score aggregation → human judgment protocol → configured-system comparison → professional presentation quality or readiness claim`.

PPT-Eval is unusually useful for testing how artifact-centered evaluation handles multiple valid solutions, partial progress, native structure, rendering, and collateral integrity in one familiar professional artifact. But native OOXML, screenshots, Python object inspection, and VLM judgments observe different properties; PowerPoint Online normalization may remove noise while changing instrument identity; intermediate-credit criteria can double-count one missing dependency; aesthetic scores can be unstable or model-coupled; and correlation with a human aggregate does not by itself establish criterion authority, decision equivalence, recipient utility, or professional quality. The missing source decks and run/human records in the inspected Git tree make release closure and exact denominator reconstruction central review questions rather than incidental reproducibility details.

PowerPoint is a bounded artifact stress case for reusable artifact-view, rubric-dependency, collateral-state, normalization, human-rater, and release-validity machinery—not a proposal to narrow `skill-bench` to presentations or computer use.

## Charter decision filter and queue action

- **Objectives advanced:** A (realistic computer-use and professional-artifact benchmark frontier), B (artifact-view, partial-credit, alternative-path, and human-judgment validity), and C (native artifact, verifier, collateral delta, configured-system, and release records).
- **Concrete evidence:** immutable-v1 full-paper review plus pinned audit of the task/rubric bank, source-deck hydration and normalization, executable/visual graders, human protocol, trial denominators, raw results, and paper-to-release conformance.
- **Uncertainty clarified:** when mixed native-structure/rendered/model observers support edit conformance, partial progress, aesthetics, human alignment, professional quality, or readiness; and how normalization and collateral-change checks affect artifact identity and legitimate alternatives.
- **Mode:** narrow expansion. The autonomous review backlog is empty while two evidence-backed consolidation tasks remain pending; one review restores a bounded evidence path without restarting broad search.
- **Duplication/scope check:** adjacent reviews cover components but not this exact mixed-observer native-presentation instrument. Reuse existing contracts and comparisons; add no presentation-specific schema or pilot.
- **Useful completion:** page/path-grounded reconstruction of task/source provenance, initial/final artifact identity, normalization, observer views and sufficiency, criterion dependencies/weights, alternative solutions, collateral checks, human sampling/agreement, configured systems, invalid/retry denominators, released-result conformance, and bounded retain/repair/test implications.

Added one task: `review-ppt-eval-native-presentation-artifact-validity` (review, priority 56). No other candidate was queued.

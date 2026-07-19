# Scouting note — adaptive task-elicitation/profile-validity gap

- **Timestamp:** 2026-07-19T03:37:04Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, ACL/web discovery, GitHub API metadata/history/tree inventory, queue/index/scouting searches, and recent-state inspection only. The PDF/source body, code files, datasets, generated tasks, observations, results, or experiments were **not** deeply read, downloaded into the repository, executed, reproduced, or audited during scouting.

## Substantive candidate — triage only

**Adaptively profiling models with task elicitation** — Davis Brown, Prithvi Balehannina, Helen Jin, Shreya Havaldar, Hamed Hassani, and Eric Wong; arXiv:2503.01986v3 (submitted 2025-03-03, revised 2025-09-25; EMNLP 2025).

- Immutable record/PDF/source: https://arxiv.org/abs/2503.01986v3 · https://arxiv.org/pdf/2503.01986v3 · https://export.arxiv.org/e-print/2503.01986v3. At scouting time these returned HTTP 200 with observed downloads of 40,214, 3,451,908, and 3,093,671 bytes; arXiv HTML was unavailable (HTTP 404). The archival publication record is https://aclanthology.org/2025.emnlp-main.1270/.
- The API abstract says task elicitation automatically builds evaluations and finds hundreds of natural-language tasks on which frontier models fail systematically, across domains from forecasting to online harassment. It gives examples of a Sonnet 3.5 quantum-computing/AGI association and o3-mini hallucination under repeated in-context fabrications. These are author-stated abstract claims awaiting complete critical review, not established benchmark-validity findings.
- GitHub search tied the paper ID to the official-looking author repository https://github.com/davisrbr/adaptive_evals. GitHub API inspection found an MIT-licensed, public, non-fork repository with only three commits, all on 2026-02-20—after arXiv v3 and EMNLP publication. The first public snapshot is `9731dab376193474e98189c12cd834e5d31035e4`; current `main` is README-only follow-up `25ddaf2281c7ed02d14f316c0f26ceb108b27054`. Its untruncated current tree has 122 objects (102 blobs), with visible paths for adaptive consistency, legal, TruthfulQA, cyberbullying, forecasting, politeness, PRESS tasks, model observations, adaptive-question evaluation, and featurization. These are path-level release facts only, not an audit of implementation or result correspondence.
- Search also surfaced paper-associated Hugging Face datasets under https://huggingface.co/BrachioLab, but their exact contents, versions, licenses, and correspondence were not inspected during scouting.
- Exact paper-ID/title, `task elicitation`, adaptive-profile, hidden-failure, queue, review, and scouting searches found no paper-specific local duplicate. TASTE, Anchor, Auto Benchmark Audit, GrowLoop, Agentic CLEAR, task-health, dynamic-rubric, and live-form work are necessary comparators rather than this adaptive target-conditioned discovery case.

## Why this is a narrow, useful gap

The reusable chain is:

`declared domain/source population → evaluator-agent access to target behavior → hypothesis generation → candidate task/instance construction → repeated testing and selection → human/independent validation → admitted failure profile → within-target uncertainty → cross-model/time transport → benchmark renewal or diagnostic decision`.

This advances charter objectives A, B, D, and E. The project has strong machinery for task generation, task health, evolving criteria, and live forms, but no deep review of a method that adaptively searches a specific target model for natural-language failure tasks. That mechanism could improve diagnostic discovery and renewal, while also creating target-conditioned selection, generator/judge coupling, post-selection inference, and comparability problems.

The claim ceiling is central: discovering many selected hard cases does not estimate failure prevalence, domain coverage, ordinary-use risk, or a stable capability scale; repeated failures can reflect shared prompt lineage or evaluator artifacts; adaptive profiles across models are not automatically comparable; generated answer keys may exclude legitimate responses; and a public release six months after v3 needs timing-aware correspondence checks. A full review should separate candidate discovery yield, task validity, profile stability, cross-model transport, and decision utility.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier evaluation method), B (source/behavior-to-task projection), D (comparison with existing lifecycle machinery), and E (interpretation and post-selection limits).
- **Concrete evidence:** immutable-v3 full-paper review plus timing-aware audit of the first public snapshot, later README commits, and associated datasets.
- **Uncertainty clarified:** whether adaptive task elicitation produces valid diagnostic failure profiles and renewable benchmark material, or primarily target-conditioned hard cases with unsupported coverage/comparability claims.
- **Mode:** narrow expansion/human learning. The queue has a high-priority validation build, one consolidation, and one human decision but no review item; one low-priority review restores a bounded research buffer without broad searching.
- **Duplication/scope check:** exact source-specific searches were negative; adjacent work is explicitly required as comparison. The listed domains are mechanism probes, not a benchmark-domain commitment.
- **Useful completion:** reconstruct roles, selection/stopping, denominators, systematic-failure criterion, human validation, uncertainty, transport, release correspondence, and cost with page/path evidence; derive retain/repair/test implications and add no schema or pilot by default.

Added one task: `review-adaptive-task-elicitation-profiling-validity` (review, priority 37). No second task was queued.

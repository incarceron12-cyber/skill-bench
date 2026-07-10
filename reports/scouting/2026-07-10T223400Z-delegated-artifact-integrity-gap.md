# Scouting note — delegated artifact-integrity gap

**Timestamp:** 2026-07-10T22:34:00Z  
**Scope:** Narrow search against charter objectives A/B/C after confirming one pending consolidation task and no pending source/research/review work. This run targeted preservation of authoritative artifacts during delegated edits rather than repeating broad knowledge-work benchmark discovery.

## Substantive finding (triage only)

**LLMs Corrupt Your Documents When You Delegate / DELEGATE-52**

- Immutable arXiv record: https://arxiv.org/abs/2604.15597
- Immutable PDF location: https://arxiv.org/pdf/2604.15597
- Official Microsoft Research publication page: https://www.microsoft.com/en-us/research/publication/llms-corrupt-your-documents-when-you-delegate/
- Paper-associated official repository: https://github.com/microsoft/delegate52
- Repository HEAD observed during scouting: `b896b804fdd29032f04aacc519c5cfa66e34226d`
- Paper-associated dataset: https://huggingface.co/datasets/microsoft/delegate52
- arXiv and Microsoft search records describe long delegated document-editing workflows across 52 professional domains, including structurally different artifacts such as source code, crystallography files, music notation, and accounting ledgers.
- The official repository search record describes 310 full environments, with 234 environments across 48 domains redistributable because of seed-document licensing. Those mutable-release counts require verification and reconciliation against the immutable paper during review.
- The official repository was independently verified with `git ls-remote` at the observed HEAD above.
- This is **metadata, abstract/search-snippet, and release-location triage only**. The full paper, code, dataset, environments, and graders were not read during scouting. No claim about measured corruption rates, model readiness, professional validity, or trust is made here.

## Why this is distinct

The corpus already covers professional artifact quality, workspace integrity, protected mutations, executable spreadsheet behavior, artifact-view admissibility, and initial-state validity. DELEGATE-52 appears to isolate a related but nonduplicate construct: an agent may satisfy the requested edit while silently damaging unrelated authoritative content in the same artifact over a long relay. This makes the change set itself an evaluation object, not merely the final file.

The reusable question is how a benchmark should represent requested deltas, must-preserve invariants, accepted normalization, collateral semantic damage, latent initial defects, reversibility, recovery, and verification burden. Cross-domain artifact structures also offer a test of which integrity machinery can remain generic and which checks require domain expertise.

## Charter decision filter and queue action

- **Objectives advanced:** A (realistic knowledge-work and production evaluation), B (domain conventions and preservation requirements into explicit primitives), and C (artifact, mutation, grader, trace, and diagnostic machinery).
- **Evidence/artifact sought:** immutable full-paper review, pinned official-code/dataset audit, and three end-to-end released environment traces from structurally different domains.
- **Uncertainty clarified:** whether corruption predicates distinguish true semantic damage from benign representation changes; how seed authority, licensing, hidden checks, initial defects, workflow length, recovery, and human validation affect readiness claims; and whether cross-domain preservation invariants can be represented without artifact-specific schema forks.
- **Mode/balance:** one narrow expansion task at priority 66. The existing higher-priority consolidation task remains available; no broad-search backlog was created.
- **Duplication/scope:** repository search found no local index entry, review, queue task, or scouting note for `2604.15597`, `DELEGATE-52`, or the paper title. The task compares with existing workspace/artifact machinery but does not make document editing a project scope commitment.
- **Useful completion:** separate paper claims from inspectable release evidence; reconcile full versus redistributable denominators; audit environment sourcing, workflow, graders, uncertainty, and human validation; trace three diverse artifacts; and map only nonduplicate requirements into existing contracts.

Added `review-delegate52-delegated-artifact-integrity` (priority 66). No second task was added.

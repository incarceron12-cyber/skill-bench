# Scouting note — evolving-information and workspace-grounding gap

**Timestamp:** 2026-07-10T11:12:22Z  
**Scope:** Narrow search against research-agenda questions 2, 3, and 8 after the queue reached two pending implementation/consolidation tasks and no pending source or review task. This run searched specifically for primary evidence on persistent workspace state, contradictory sources, and belief revision rather than repeating broad agent-benchmark discovery.

## Substantive finding (triage only)

**ClawArena: Benchmarking AI Agents in Evolving Information Environments** — arXiv:2604.04202v2.

- Immutable record: https://arxiv.org/abs/2604.04202v2
- Immutable PDF: https://arxiv.org/pdf/2604.04202v2
- Official release: https://github.com/aiming-lab/ClawArena; reachable `main`/HEAD `630efd8a0d1dc8189718226c7da158cbe4c2fe64`. The remote also exposes tag `v1.0.0` (peeled commit `922f3142a3e5538f9004db7833063b74cb63d76f`).
- The arXiv API identifies v2, updated 2026-05-16, and reports 12 multi-turn scenarios, 337 evaluation rounds, and 45 staged updates. Each scenario exposes partial, noisy, sometimes contradictory traces through sessions and workspace files while retaining hidden ground truth. Its three coupled challenge families are multi-source conflict reasoning, dynamic belief revision, and implicit personalization; evaluation uses set-selection questions and shell-based executable checks across five frameworks and 18 models.
- The abstract reports large model and framework ranges, a positive MetaClaw skill-overlay result, and sensitivity to update design rather than update count. These are claims to audit, not established findings for skill-bench.
- The immutable abstract/PDF and official repository URLs were reachable. This is **metadata/abstract, URL, and Git-ref triage only**. Neither the paper nor repository was read in full during scouting; scenario validity, hidden-ground-truth provenance, fair disclosure, comparison design, uncertainty, and causal claims require full review.

## Why this is distinct

The repository already models source packs, contradiction mechanisms, configured systems, context evolution, retrieval leakage, and artifact checks separately. It lacks a reviewed benchmark that combines those objects in a persistent, evolving workspace where later evidence may supersede, condition, or merely conflict with earlier evidence and user preferences may be revealed through correction. ClawArena can therefore test whether the current contracts distinguish source authority, temporal validity, contextual applicability, preference inference, workspace state, and retrieval/use failures rather than collapsing all errors into generic memory or reasoning scores.

A second candidate, **MemConflict** (arXiv:2605.20926v1), was verified but not queued. Its dynamic/static/conditional conflict taxonomy may be useful later, but ClawArena is more directly tied to realistic multi-channel knowledge work and executable workspace checks; adding both now would duplicate the conflict-reasoning review burden.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier benchmark evidence), B (source/expertise-to-evaluation methodology), and C (workspace, trace, check, context, and validity infrastructure).
- **Evidence/artifact sought:** a full immutable-v2 paper and pinned-release review reconstructing authoring, hidden truth, source authority, updates, question/check construction, framework treatments, scoring, uncertainty, ablations, and release behavior.
- **Uncertainty clarified:** when contradiction requires supersession versus coexistence or conditional use; whether hidden truth/preferences have a fair public basis; what state and provenance graders must observe; and whether framework or skill-overlay effects are identifiable.
- **Mode/balance:** narrow expansion into an uncovered benchmark condition; priority 72 leaves current operating-layer building and consolidation ahead of it.
- **Duplication/scope:** no match for `2604.04202` or ClawArena existed in the paper index, reviews, scouting reports, or queue. Persistent-assistant scenarios are a cross-domain methodological case, not a new scope boundary.
- **Useful completion:** paper and release evidence are separated; fairness, observability, comparability, and causal limits are audited; and only nonduplicate requirements are mapped to existing contracts.

Added `review-clawarena-evolving-information` (priority 72). No second task was added.

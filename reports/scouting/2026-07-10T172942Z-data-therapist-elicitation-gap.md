# Scouting note — mixed-initiative tacit-knowledge elicitation gap

**Timestamp:** 2026-07-10T17:29:42Z  
**Scope:** Narrow search against charter objectives A/B/F after confirming a healthy implementation/consolidation backlog. This run did not repeat broad agent-benchmark discovery.

## Substantive finding (triage only)

**Data Therapist: Eliciting Domain Knowledge from Subject Matter Experts Using Large Language Models** — Sungbok Shin, Hyeon Jeon, Sanghyun Hong, and Niklas Elmqvist.

- Immutable arXiv record: https://arxiv.org/abs/2505.00455v3
- Immutable arXiv PDF: https://arxiv.org/pdf/2505.00455v3
- The arXiv API identifies v3, published 2025-05-01 and updated 2025-10-04 in `cs.HC` and `cs.AI`.
- The abstract describes a web system that uses LLM-generated iterative questions and interactive, multigranular annotations to help subject-matter experts externalize tacit knowledge about data provenance, quality, and intended use. It reports a qualitative study with expert pairs from Accounting, Political Science, and Computer Security.
- Both immutable arXiv URLs returned HTTP 200. Targeted searches did not locate an unambiguous official code, study-material, or data release; a deep review must inspect the paper's own links and record release absence if confirmed.
- This is **metadata/abstract, canonical-URL, and release-location triage only**. The full paper was not read during scouting. System behavior, participant protocol, qualitative findings, annotation dimensions, usability, and transfer claims require full review.

## Why this is distinct

The repository has a full ACTA/CDM review and an evidence-typed elicitation-session template, but these cover human interviewing methodology rather than an LLM-mediated mixed-initiative instrument exercised with domain experts. Data Therapist can clarify whether generated probes broaden disclosure or anchor it, whether editable annotations preserve expert correction and disagreement, how spontaneous/probed/inferred provenance should be represented, and whether structured outputs retain enough context and authority to support source packs or rubric claims.

The reusable question is not whether skill-bench should become a visualization benchmark. It is how AI-assisted expert elicitation changes the evidence chain, participant burden, reciprocal utility, and risks of laundering model interpretations into purported expert knowledge across domains.

## Charter decision filter and queue action

- **Objectives advanced:** A (primary evidence on expertise elicitation), B (expert claim-to-benchmark transformation), and F (feasible, reusable expert participation).
- **Evidence/artifact sought:** immutable-v3 full-paper review, official-material provenance audit, and a crosswalk against the ACTA/CDM review and elicitation template.
- **Uncertainty clarified:** probe anchoring/omission; interpretation hallucination; correction, disagreement, and withdrawal; context specificity; annotation fidelity; participant burden; downstream utility; and what outputs can legitimately become benchmark evidence.
- **Mode/balance:** one narrow expansion task at priority 73, below current build/consolidation and SaaS-Bench review work.
- **Duplication/scope:** no local index, review, scouting note, or queue item matched `2505.00455` or Data Therapist. Visualization is a methodological case, not a scope boundary.
- **Useful completion:** qualitative evidence is separated from design claims; release boundaries and study limitations are explicit; only nonduplicate requirements map into existing contracts; no simulated testimony or premature unblocking of the real-session gate.

Added `review-data-therapist-tacit-data-elicitation` (priority 73). No second task was added.

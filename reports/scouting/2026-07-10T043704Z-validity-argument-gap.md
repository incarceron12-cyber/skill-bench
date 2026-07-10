# Scouting note — benchmark validity-argument gap

**Timestamp:** 2026-07-10T04:37:04Z

**Scope:** Narrow primary-source search for the validity layer missing between the implemented authoring/measurement contracts and their permitted claims. The queue was healthy (seven pending tasks before this run), so this run added one lower-priority review and did not repeat broad benchmark searches.

## Substantive finding (triage only)

**Measurement to Meaning: A Validity-Centered Framework for AI Evaluation** — Salaudeen et al., arXiv:2505.10573v4 (2025).

- Immutable record: https://arxiv.org/abs/2505.10573v4
- Immutable PDF: https://arxiv.org/pdf/2505.10573v4
- The arXiv API identifies v4 as the latest record, published 2025-05-13 and updated 2025-06-26; both immutable URLs returned HTTP 200 during this run.
- The abstract presents a structured way to determine which claims evaluation evidence can support, distinguishes narrow task-performance claims from broader capability claims, and says the framework adapts psychometric validity facets to evaluation construction and downstream decisions, illustrated with vision and language case studies.
- This was **metadata/abstract triage only**. The PDF was not read during scouting; all framework details, facet definitions, and case-study implications must be verified from the immutable full text.

## Why this fills a current gap

The repository already separates score families and warns against overclaiming, but its expert-validity and release gates do not yet encode a complete validity argument: intended interpretation/use, stakeholder decision, evidence, warrant, assumptions, rebuttals, generalization boundary, and unresolved evidence. ACTA addresses elicitation and the consulting benchmark addresses task/trap authoring; this source appears to supply the distinct downstream bridge from observed scores to defensible claims and decisions.

NIST's *Practices for Automated Benchmark Evaluations of Language Models* also surfaced as an official implementation-oriented source, but it was deferred to avoid expanding a healthy backlog and because it cites this framework. A later reviewer can assess whether NIST adds nonduplicative operational controls.

## Queue action

Added one task: `review-validity-centered-ai-evaluation` (priority 85). It requires immutable full-text review, case-study reconstruction, mappings to existing contracts and the pilot, and a concrete validity-argument template or schema proposal while separating source guidance from project adaptation.

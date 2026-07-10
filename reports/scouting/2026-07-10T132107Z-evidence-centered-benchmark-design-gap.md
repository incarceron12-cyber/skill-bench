# Scouting note — evidence-centered benchmark-design gap

**Timestamp:** 2026-07-10T13:21:07Z  
**Scope:** Narrow search against charter objectives A/B/D and the deferred evidence-centered assessment-design lead in the earliest scouting note. The queue had one pending consolidation task and two evidence-gated blocked builds, so this run did not repeat broad agent-benchmark discovery.

## Substantive finding (triage only)

**ECBD: Evidence-Centered Benchmark Design for NLP** — Yu Lu Liu, Su Lin Blodgett, Jackie Chi Kit Cheung, Q. Vera Liao, Alexandra Olteanu, and Ziang Xiao.

- Immutable arXiv record: https://arxiv.org/abs/2406.08723v1
- Immutable arXiv PDF: https://arxiv.org/pdf/2406.08723v1
- ACL 2024 primary publication: https://aclanthology.org/2024.acl-long.861/
- Official release: https://github.com/isle-dev/ECBD; reachable `main`/HEAD `68cb42bd09d080a45859f349a4706ebca75cdeca`.
- The arXiv API identifies immutable v1, published 2024-06-13 in `cs.CL`. Its abstract says ECBD adapts evidence-centered assessment design into five modules that require benchmark designers to describe, justify, and support choices about intended capabilities and evidence collected from model responses. It applies the framework to BoolQ, SuperGLUE, and HELM and reports documentation/design patterns that may threaten validity.
- The arXiv, ACL Anthology, PDF, and official GitHub URLs were reachable. This is **metadata/abstract, canonical-URL, and Git-ref triage only**. Neither the paper nor release was read in full during scouting; module semantics, case selection/coding, reliability, empirical support, and transfer beyond static NLP benchmarks require full review.

## Why this is distinct

The source is cited in the full validity-centered evaluation paper already reviewed locally, but skill-bench has no direct review or index entry for ECBD. The current taxonomy contains closely related claim, evidence, task, rubric, scoring, and validity objects; a direct audit can therefore test whether they compose into one explicit measurement argument or remain parallel checklists. ECBD may also expose assembly, response-processing, or inference dependencies not captured by the current projection-conformance work.

The reusable question is not whether skill-bench should become an NLP benchmark. It is which authoring decision warrants which inference, what observable evidence a task must elicit, how processing/scoring can distort that evidence, and what validation is required before a configured long-horizon artifact trial supports a capability or readiness claim.

## Charter decision filter and queue action

- **Objectives advanced:** A (benchmark-methodology evidence), B (expertise-to-evaluation design), and D (consolidation against an external framework).
- **Evidence/artifact sought:** a full immutable-paper and pinned-release review reconstructing the five modules, relations, workflow, case-study method, evidence, and limits.
- **Uncertainty clarified:** whether skill-bench's existing contracts form a coherent evidentiary argument; whether assembly, response-processing, inference, or authoring-dependency obligations are missing; and which ECBD claims generalize beyond static NLP evaluation.
- **Mode/balance:** narrow methodological expansion at priority 69, below the pending canonical consolidation; it replenishes a nearly empty review backlog without adding broad search noise.
- **Duplication/scope:** ECBD appears only as a citation in an acquired source and in a previously deferred scouting lead. No local review, paper-index record, report, or queue task matched `2406.08723` or ECBD. The NLP cases are methodological evidence, not a scope boundary.
- **Useful completion:** normative framework proposals are separated from descriptive case-study findings; coding and validity evidence are audited; the existing validity review and taxonomy are compared explicitly; and only nonduplicate implications enter current contracts.

Added `review-ecbd-evidence-centered-benchmark-design` (priority 69). No second task was added. NIST AI 800-2 was re-verified as a possible later operational-controls source but not queued because the direct ECD-to-benchmark bridge is the narrower unresolved gap and the existing validity/production reviews already cover many guideline-level controls.

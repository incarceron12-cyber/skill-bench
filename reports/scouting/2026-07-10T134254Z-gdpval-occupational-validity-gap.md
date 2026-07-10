# Scouting note — GDPval occupational-validity gap

**Timestamp:** 2026-07-10T13:42:54Z  
**Scope:** Narrow search against charter objectives A/B/E/F and the explicit unresolved GDPval row in `docs/state-of-the-art-map.md`. The queue had two pending consolidation/build tasks and two evidence-gated blocked builds, so this run did not repeat broad agent-benchmark discovery.

## Substantive finding (triage only)

**GDPval: Evaluating AI Model Performance on Real-World Economically Valuable Tasks** — Tejal Patwardhan et al.

- Immutable arXiv record: https://arxiv.org/abs/2510.04374v1
- Immutable arXiv PDF: https://arxiv.org/pdf/2510.04374v1
- OpenAI primary report/page: https://openai.com/index/gdpval/
- Official public gold subset: https://huggingface.co/datasets/openai/gdpval
- The arXiv API identifies immutable v1, published 2025-10-05 in `cs.LG`. Its abstract says GDPval covers most U.S. Bureau of Labor Statistics Work Activities for 44 occupations in nine high-GDP sectors; tasks come from industry professionals averaging 14 years of experience; the study compares quality, speed, and cost; tests reasoning effort, context, and scaffolding; and releases a 220-task gold subset plus an automated grading service.
- The arXiv PDF and OpenAI PDF URLs returned HTTP 200, and the official Hugging Face dataset was discoverable. This is **metadata/abstract, canonical-URL, and release-location triage only**. Neither the full paper nor dataset was read during scouting; the reported task count, expert workflow, grader agreement, occupational coverage, model trend, and economic-value claims require full review.

## Why this is distinct

GDPval is already named in the state-of-the-art map, but only as a case-material/work-deliverable benchmark with the unresolved question “What task taxonomy did they use?” It has no paper-index entry, local review, scouting note, or queue task. Unlike the reviewed single-domain or methodology sources, it can test the project’s cross-domain premise directly: how experienced professionals transform representative work into self-contained tasks and artifacts, how occupation-specific reviewers establish feasibility and representativeness, and how expert pairwise judgments are aggregated across heterogeneous work.

The useful question is not whether GDP contribution should define skill-bench’s scope. It is whether occupational sampling, expert task authorship, artifact/context construction, human baselines, pairwise grading, and cost/time measurements support the paper’s representativeness, expert-parity, and economic-value interpretations—and which parts of that machinery transfer across domains.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier realistic-work benchmark evidence), B (expertise-to-evaluation transfer), E (clarify what broad occupational claims mean), and F (expert recruitment and labor evidence).
- **Evidence/artifact sought:** an immutable-v1 paper review plus a pinned inspection of the official 220-task gold subset, with page/file evidence and release provenance.
- **Uncertainty clarified:** occupational/task sampling validity; author/reviewer/grader role separation; context and artifact sufficiency; pairwise/adjudication reliability; public/private-set comparability; and whether quality, time, cost, parity, or augmentation claims are licensed.
- **Mode/balance:** narrow cross-domain expansion at priority 68, below the two pending consolidation/build tasks; it replenishes a small review backlog without displacing current implementation.
- **Duplication/scope:** local mentions are a map placeholder and citations in other papers, not a review. The methodological lesson is cross-domain; GDP weighting and model-only evaluation are not proposed scope boundaries.
- **Useful completion:** full/private-set claims are separated from public-gold evidence; recruitment, authoring, review, grading, uncertainty, and economic estimands are reconstructed and audited; and only nonduplicate requirements map to existing contracts.

Added `review-gdpval-occupational-task-validity` (priority 68). No second task was added.

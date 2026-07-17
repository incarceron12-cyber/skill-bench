# Scouting note — GrowLoop human-seeded evolving-rubric validity gap

- **Timestamp:** 2026-07-17T08:23:04Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, exact local corpus/queue duplicate search, targeted release discovery, and GitHub API metadata/tree triage only. The paper body, appendices, annotations, rubric/case artifacts, experiments, statistical analyses, and reported results were **not** deeply read or audited during scouting.

## Substantive candidate — triage only

**GrowLoop: Self-Evolving Conversation Evaluation Seeded by Human** — Yihang Lin, Yunze Gao, Zeyang Lin, Dongbo Li, Kun Peng, and Yue Liu; arXiv:2605.28882v2.

- Immutable record/PDF/HTML: https://arxiv.org/abs/2605.28882v2, https://arxiv.org/pdf/2605.28882v2, and https://arxiv.org/html/2605.28882v2
- Official repository: https://github.com/AMAPVOICE/GrowLoop at inspected commit `62e170d2f70bcae7442c83f392de7965ea9c6510`
- The arXiv API identifies v2, updated 10 June 2026, in `cs.CL`, `cs.AI`, and `cs.SD`; its summary contains no withdrawal/retraction notice. All three immutable endpoints returned HTTP 200.
- The abstract frames human-likeness judgment as tacit, variably agreed, and temporally changing. It describes minimal human seed annotations, LLM-based heuristic extraction/refinement of rubrics, different consensus/divergence treatment, and joint rubric/case evolution when targets shift. Claims of improved human alignment, overlooked-issue discovery, tier discrimination, generalization, and adaptation await full-paper audit.
- GitHub API inspection found an untruncated 16-object tree containing README files, a paper PDF, and images only. At acquisition there was no code, dataset, tag, release, or GitHub-declared license. The full paper may identify other artifacts; release availability and paper-to-release correspondence remain review questions.
- Repository-wide searches for the title, arXiv ID, and framework name found no prior review, queue task, or scouting note.

## Why this is a narrow, useful gap

The reviewed corpus already covers expert disagreement, human/AI rater effects, rubric modification, generated and adaptive rubrics, task health, live benchmark forms, and agent/benchmark evolution. It does not directly audit the full proposed lifecycle:

`human seed opportunity and annotator authority → agreement/divergence observation → model-derived rubric candidate → human or model acceptance rule → case generation/selection → judge evidence view → score/decision → target-shift trigger → versioned rubric/case update → bridge to prior instrument`.

This matters beyond conversation. A benchmark that extracts tacit criteria from sparse human judgments needs to preserve who judged what, under which context; distinguish genuine disagreement from noise or missing information; separate model-proposed criteria from human-authorized criteria; and prevent co-evolution from silently changing the construct, teaching the judge its own cases, or breaking longitudinal comparability. Higher agreement or model discrimination does not by itself establish criterion authority, tacit-knowledge recovery, valid adaptation, or transport. Open-ended conversation is a bounded test bed for general expertise-to-evaluation and benchmark-lifecycle methodology, not a project scope commitment.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier research), B (expertise-to-evaluation methodology), D (targeted expansion feeding consolidation), and E (human understanding of construct drift and disagreement).
- **Concrete evidence:** immutable-v2 deep review and timing-aware official-release audit covering human seed provenance, annotator sampling/authority, transformation lineage, rubric/case versions, judge evidence views, evaluation design, uncertainty, cost, and adaptation triggers.
- **Uncertainty clarified:** whether GrowLoop captures authorized, context-bounded human criteria and legitimate disagreement or compounds model-generated interpretations while moving the instrument.
- **Mode:** narrow expansion. The queue already contains a higher-priority consolidation and a human prerequisite; this review is priority 74 and does not displace them.
- **Duplication/scope check:** adjacent reviewed machinery is reusable, but no source in the indexed corpus studies joint human-seeded rubric/case evolution. No conversation-specific schema or benchmark direction is proposed.
- **Useful completion:** a section/page-grounded claim audit and explicit retain/repair/test implications that keep tacit transfer, construct continuity, human equivalence, generalization, and readiness claims false unless separately evidenced.

Added one task: `review-growloop-human-seeded-evolving-rubric-validity` (review, priority 74). No other candidate was queued.

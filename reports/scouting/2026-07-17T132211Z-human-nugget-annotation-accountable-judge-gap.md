# Scouting note — human-authored nugget annotation and scalable-judge validity gap

- **Timestamp:** 2026-07-17T13:22:11Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, exact local duplicate search, and targeted web/GitHub release discovery only. The paper body, prototype, interfaces, study evidence, nugget banks, prompts, judges, and reported workflow were **not** deeply read or audited during scouting.

## Substantive candidate — triage only

**Human-in-the-Loop Nugget Annotation for Accountable LLM-as-a-Judge Evaluations** — Laura Dietz; arXiv:2606.29033v2.

- Immutable record/PDF/HTML: https://arxiv.org/abs/2606.29033v2 · https://arxiv.org/pdf/2606.29033v2 · https://arxiv.org/html/2606.29033v2
- The arXiv API identifies `cs.IR` v2, first submitted 27 June and updated 7 July 2026. Its summary contains no withdrawal/retraction notice. Record, PDF, and HTML endpoints returned HTTP 200; the PDF response reports `application/pdf` and 1,898,262 bytes.
- The abstract argues that common human-evaluation workflows either anchor experts toward rubber-stamping or leave them unsupported in cognitively demanding labeling. It describes a prototype division of labor in which humans identify what information matters as “nuggets,” while models perform high-volume nugget-to-output matching. These are author-stated abstract claims awaiting full-paper audit.
- Targeted title/author/code searches and GitHub repository search found no obvious author-owned code, dataset, demo, or nugget-bank release. The abstract page exposed no project/repository link. This is an acquisition-time discovery result, not evidence that no artifact exists; the reviewer must inspect the paper and references.
- Exact repository searches for the title, arXiv ID, and distinctive phrase returned no prior review, queue task, or scouting note.

## Why this is a narrow, useful gap

The corpus already covers expert rubric authoring, expert disagreement, human/AI rater effects, rubric modification, generated/adaptive rubrics, and judge reliability. This candidate appears to study a distinct **human-opinion-formation-first** chain:

`expert observation opportunity and displayed outputs → unaided relevance judgment → human-authored nugget → model-assisted formalization/preview → human acceptance and bank version → nugget-to-output matching → criterion result → aggregate decision → review burden and downstream use`.

That chain directly tests how scarce expert judgment might be converted into scalable criteria without silently assigning criterion authority to a model. But “human authored” does not by itself establish complete construct coverage, representative output sampling, freedom from anchoring, stable interpretation, legitimate disagreement resolution, reliable matching, lower total burden, or decision validity. Displaying concrete outputs can itself induce salience and case-selection effects; model formalization can change scope, polarity, thresholds, or dependencies; a nugget bank can be internally coherent yet incomplete; and automated matching still requires criterion-level human validation under admissible evidence views.

The source is cross-domain methodology for expertise-to-evaluation and low-cost participation, not a proposal to make `skill-bench` an information-retrieval or nugget-scoring benchmark.

## Charter decision filter and queue action

- **Objectives advanced:** B (expertise-to-evaluation methodology), F (feasible expert participation), and A (human/scalable evaluation frontier).
- **Concrete evidence:** immutable-v2 full-paper review plus timing-aware audit of any linked prototype, annotation artifacts, nugget banks, prompts, and judge implementation.
- **Uncertainty clarified:** whether human-first nugget curation preserves criterion authority and reduces anchoring/burden, and which provenance, coverage, disagreement, transformation, matching, and validation records are required.
- **Mode:** narrow expansion. One higher-priority build and one human prerequisite were pending; this review is priority 72 and does not displace them.
- **Duplication/scope check:** adjacent reviews supply comparison machinery but do not audit this human-first nugget-authoring workflow. No new schema or domain pilot is proposed during scouting.
- **Useful completion:** section/page-grounded workflow and evidence audit, exact artifact availability, and nonduplicate retain/repair/test implications while keeping criterion authority, reduced bias, coverage, judge validity, scalability, expert substitution, professional validity, and readiness unclaimed unless evidenced.

Added one task: `review-human-nugget-annotation-accountable-judge-validity` (review, priority 72). No other candidate was queued.

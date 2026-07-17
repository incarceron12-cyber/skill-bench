# Scouting note — citation-verifier directional-bias validity gap

- **Timestamp:** 2026-07-17T16:08:30Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, exact local duplicate search, targeted web/release discovery, and HTML link triage only. The paper body, benchmark corpus, source pages, human labels, adjudication records, judge prompts, raw predictions, statistical analysis, and costs were **not** deeply read or audited during scouting.

## Substantive candidate — triage only

**Do You Need a Frontier Model as a Citation Verifier? Benchmarking Rubric LLMs for Deep-Research Source Attribution** — Ethan Leung, Elias Lumer, Corey Feld, Austin Huber, Vamse Kumar Subbiah, and Kevin Paul; arXiv:2607.08700v1.

- Immutable record/PDF/HTML: https://arxiv.org/abs/2607.08700v1 · https://arxiv.org/pdf/2607.08700v1 · https://arxiv.org/html/2607.08700v1
- The arXiv API identifies a `cs.CL` v1 submitted 9 July 2026. Its summary contains no withdrawal/retraction notice. Record, PDF, and HTML endpoints returned HTTP 200; the PDF response reports `application/pdf` and 372,202 bytes.
- The abstract describes an adversarial long-form citation benchmark with 1,248 source-relevance/factual-support decisions, all human-reviewed, including 378 hard cases adjudicated after judge disagreement, and compares eight off-the-shelf judges from three model families. It reports that aggregate F1 can conceal substantial pass-rate, false-positive, and false-negative drift. These are author-stated abstract claims awaiting full-paper audit.
- Triage of the immutable HTML exposed no author project, GitHub, Hugging Face, Zenodo, OSF, code, or dataset link. Targeted title/author searches found no obvious official release. This is an acquisition-time search boundary, not proof that no artifact exists; the reviewer must inspect the complete paper and references.
- Exact repository searches for the arXiv ID, title, and distinctive directional-bias terms found no prior review, queue task, or scouting note.

## Why this is a narrow, useful gap

The corpus already covers human/AI rater effects, rubric authoring, generated criteria, deep-research evaluation, source provenance, and criterion reliability. It does not directly audit a criterion-level **citation-verifier calibration chain**:

`generated claim and citation → cited-source identity/snapshot → judge-visible claim/source evidence → relevance decision → factual-support decision → human review and disagreement adjudication → criterion error vector → aggregate judge metric → reward/selection policy → changed system output → held-out source-grounding and artifact consequence`.

Each link matters. Source relevance and factual entailment are different from citation existence, source authority, freshness, completeness, contradiction handling, or whether the cited evidence was actually used. Human review does not automatically establish independent expert gold labels if annotator qualification, evidence access, initial independence, disagreement selection, and adjudication are under-specified. Hard cases selected after judge disagreement may be valuable stress tests without representing the deployment population. F1 or kappa can remain similar while false-positive and false-negative rates differ, and those directional errors have different consequences when the judge becomes a training reward, acceptance gate, or review allocator. A measured judge association is not evidence that optimizing against it improves research quality or professional outcomes.

Deep research is a bounded case for reusable evidence-sensitive grading, not a proposal to narrow `skill-bench` to citation verification or make one scalar judge metric its evaluation target.

## Charter decision filter and queue action

- **Objectives advanced:** A (scalable agent evaluation frontier), B (valid evidence-to-criterion and criterion-to-reward claims), and C (criterion/evidence/metric/validity machinery).
- **Concrete evidence:** immutable-v1 full-paper review plus audit of corpus, sources, human labels/adjudication, prompts, raw predictions, analyses, and release availability.
- **Uncertainty clarified:** when a citation judge supports bounded source-relevance or factual-support measurement, which directional errors matter for downstream policy, and what evidence is required before using criterion scores as reward signals.
- **Mode:** narrow expansion. One higher-priority human prerequisite and one higher-priority consolidation task were pending; this review is priority 66 and does not displace them.
- **Duplication/scope check:** adjacent reviews cover the surrounding rater, rubric, provenance, and deep-research links but not this released claim of criterion-level directional judge bias. No new schema is proposed unless the audit shows existing criterion, evidence, metric, and validity records are insufficient.
- **Useful completion:** section/page-grounded methodology; exact release and observer-view status; label/adjudication and dependence audit; criterion-level directional error and cost analysis; and nonduplicate retain/repair/test implications while keeping agreement, calibration, reward validity, training benefit, research quality, professional validity, production fitness, and readiness separate.

Added one task: `review-citation-verifier-directional-bias-validity` (review, priority 66). No other candidate was queued.

# Scouting note — deep-research span-error localization validity gap

- **Timestamp:** 2026-07-18T13:54:38Z
- **Evidence status:** arXiv metadata/abstract and immutable endpoint checks, official GitHub/Hugging Face surface triage, targeted primary-source searches, and exact repository duplicate searches only. The PDF/source body, 2,790 trajectories, semantic-span conversion, 1,000 TELBench instances, annotation records, prompts, predictions, code, or result tables were **not** deeply read, downloaded into the repository, reproduced, or audited during scouting.

## Substantive candidate — triage only

**Where Do Deep-Research Agents Go Wrong? Span-Level Error Localization in Agent Trajectories** — Jiaming Wang, Ziteng Feng, Jiangtao Wu, Ruihao Li, Qianqian Xie, Yuxiang Ren, He Zhu, Xueming Han, Fanyu Meng, Junlan Feng, and Jiaheng Liu; arXiv:2606.02060v2.

- Immutable record/PDF/source: https://arxiv.org/abs/2606.02060v2 · https://arxiv.org/pdf/2606.02060v2 · https://export.arxiv.org/e-print/2606.02060v2
- Official release surfaces: https://github.com/NJU-LINK/DRIFT · https://huggingface.co/datasets/NJU-LINK/TELBench
- The arXiv record identifies a 1 June 2026 submission in `cs.AI`; the summary contains no withdrawal or retraction notice. Record, PDF, and source endpoints returned HTTP 200 in this check, with 43,229, 3,278,470, and 2,805,980 downloaded bytes respectively.
- The abstract reports 2,790 real trajectories from two agent frameworks, three backbone models, and three benchmarks; conversion of raw logs into semantic spans; and harmful-error-span labels produced through LLM-assisted expert review. It introduces TELBench and a claim-centric DRIFT auditor intended to mark where unsupported or conflicting claims first enter, are reused, or affect the final answer. These are author-stated claims awaiting full-paper verification.
- The official GitHub and Hugging Face surfaces returned HTTP 200. Search-visible release documentation describes a 1,000-instance TELBench, `bare` full-context and full DRIFT settings, sanitization that withholds gold labels/annotations/metadata/judge outputs/span types/manual notes from model calls, and an encrypted dataset object. Availability, decryption/access conditions, paper-time correspondence, annotation completeness, and exact result reconstruction remain unresolved until a pinned release audit.
- Exact title/ID/mechanism searches found no local review, scouting note, or queue task. STRACE, Who&When Pro, AutoTrace, Agentic CLEAR, Signals, and trajectory-triage work are adjacent, but none directly audits a released semantic-span instrument for claim introduction/reuse/finalization in long source-grounded research trajectories with expert-assisted labels.

## Why this is a narrow, useful gap

The reusable chain is:

`raw event/observation/action trajectory → loss-audited semantic-span projection → claim identity and source-support state → first unsupported/conflicting introduction → downstream reuse or correction → final artifact effect → expert-assisted annotation/adjudication → auditor prediction → localized repair test → consequence and monitoring-utility claim`.

This directly advances charter objectives A, B, C, and E. It could supply a concrete diagnostic instrument for realistic research agents, but semantic compression, unsupported-claim detection, harmfulness, earliest cause, downstream dependence, and useful repair are different constructs. A selected error span may be a surface symptom; a claim can be unsupported in the retained view yet supported by an omitted source; an LLM-assisted expert label can inherit model candidates or final-answer hindsight; and localization accuracy alone does not show that intervention at the marked span repairs the artifact without collateral damage.

A full review should reconstruct trajectory/task sampling and clustering; framework/model/tool/search identities; raw-event-to-span transformations and information loss; claim canonicalization and dependency rules; source admissibility and observer entitlements; expert qualifications, model assistance, independence, blinding, adjudication, agreement, and missingness; harmful-span prevalence and class balance; exact localization metrics, nulls, confidence, uncertainty, and baseline parity; endpoint-conditioned selection or answer leakage; dataset encryption/access; release/paper correspondence; and whether predicted spans support counterfactual repair, human-review efficiency, or only label agreement. Deep research is a bounded mechanism case, not a benchmark scope commitment.

## Charter decision filter and queue action

- **Objectives advanced:** A (realistic agent evaluation and human judgment), B (diagnostic expertise-to-evaluation machinery), C (trace/span/claim evidence artifacts), and E (clear causal and validity boundaries).
- **Concrete evidence:** immutable-v2 full-paper review plus pinned official release audit of TELBench/DRIFT, including annotation provenance, projection losses, metrics, release conformance, and claim ceilings.
- **Uncertainty clarified:** whether semantic-span labels localize supported upstream causes and enable repair, or establish only agreement with one outcome-aware configured annotation/auditor pipeline.
- **Mode:** narrow expansion. The autonomous research/review/source backlog was empty; one build and one human-decision task were pending. This avoids another broad search.
- **Duplication/scope check:** exact duplicate searches were negative; adjacent diagnosis reviews cover injected faults, open-vocabulary issue compression, trajectory sampling, or endpoint triggers rather than this claim-centric released span instrument. Reuse trace, evidence-view, source, root/surface, grader, metric, task-health, intervention, and validity machinery; add no deep-research-specific subsystem absent stronger evidence.
- **Useful completion:** source-locate every raw-event→span→claim→label→prediction edge, quantify projection/annotation error and clustered uncertainty, audit release reconstruction and leakage, test whether the evidence licenses localization or repair, and preserve strict claim ceilings.

Added one task: `review-deep-research-span-error-localization-validity` (review, priority 53). No second source was queued.

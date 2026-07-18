# Scouting note — video-derived expert action and decision-context validity gap

- **Timestamp:** 2026-07-18T12:18:43Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, arXiv HTML availability check, targeted primary-record/release searches, and exact repository duplicate searches only. The PDF body, figures, tables, 27 scenarios, videos, frame descriptions, similarity outputs, labels, model outputs, code, or data were **not** deeply read, downloaded into the repository, reproduced, or audited during scouting.

## Substantive candidate — triage only

**Anomalous Frame Detection Using VLM-Based Description Comparison for Extracting Expert-Specific Actions and Contextual Decision-Making Scenes with Intra-Video Self-Similarity** — Ryo Sakai and Kaname Yokoyama; arXiv:2607.11957v1.

- Immutable record/PDF/source endpoint: https://arxiv.org/abs/2607.11957v1 · https://arxiv.org/pdf/2607.11957v1 · https://export.arxiv.org/e-print/2607.11957v1
- Related author conference record: https://www.jstage.jst.go.jp/article/pjsai/JSAI2026/0/JSAI2026_2F5OS19a05/_article/-char/en
- The arXiv API reports immutable v1 submitted and last updated 12 July 2026 in `cs.CV`, with the comment “16 pages, 11 figures, 2 tables”; its summary contains no withdrawal or retraction notice. Record, PDF, and e-print endpoints returned HTTP 200 in this check, with 42,721 HTML bytes, 2,003,055 PDF bytes, and 2,003,055 source-endpoint bytes. arXiv HTML conversion was unavailable, so no body headings were inspected.
- The abstract frames skilled-worker attrition in critical-infrastructure maintenance as a know-how-transfer problem. It proposes comparing VLM-generated frame descriptions from manual-based and expert task videos: inter-video description similarity nominates expert-specific actions, while intra-video segment self-similarity nominates contextual decision-making scenes. In simulated distribution-board maintenance across 27 task scenarios, it reports candidate extraction rates of 65% for actions and 61% for decision scenes versus 59% and 33% for prior methods. These are author-stated claims awaiting full-paper verification; the abstract does not establish the unit, denominator, label authority, uncertainty, or whether “extraction rate” means recall, precision, or another quantity.
- Targeted exact-title/ID/author searches found the arXiv records and a related JSAI 2026 author conference record on prompt-enhanced anomalous-frame detection, but no credible official code, video, label, or complete study-data release. This is a time-bounded unresolved release observation, not proof of nonrelease.
- Exact ID/title/mechanism searches found no local review or queue task. The ACTA method review covers interview/observation triangulation; ArtisanCAD and Vibe Calibration cover physical/procedural transfer; Context-Mediated Domain Adaptation and SciDiagramEdit cover expert-edit and revision-derived candidates. None directly evaluates the transformation from paired manual/expert video differences into candidate observable actions and contextual decision episodes.
- EvoAgentBench (`2607.05202v1`) was not reconsidered: three prior scouting notes explicitly rejected it as duplicative of the existing self-evolution/procedural-transfer corpus. SLEUTH (`2607.12267v1`) was not queued because its multi-hop QA state protocol is substantially covered by the repository’s analytical-hypothesis and evidence-acquisition machinery and is less direct than the expertise-extraction gap.

## Why this is a narrow, useful gap

The reusable chain is:

`authorized manual/expert work recordings → synchronized/comparable episode units → observable frame/segment difference → candidate action or decision-scene retrieval → qualified expert interpretation and rationale → benchmark primitive/task/check projection → independent validity → novice or agent uptake → artifact/state consequence → transfer claim`.

This directly advances charter objectives A, B, C, and E. Video can reveal embodied cues, deviations, timing, and context that interviews or final artifacts omit. But visual anomaly, description dissimilarity, candidate retrieval, contextual decision rationale, tacit know-how, and successful transfer are different constructs. A candidate scene may reflect camera viewpoint, pacing, equipment state, or simulation design rather than expertise; a true scene may still omit why an expert acted, applicable exceptions, authority, or downstream consequence.

A full review should reconstruct the paired-video and 27-scenario design; expert/manual worker selection; synchronization and comparability; VLM/prompt/model identity; frame and segment units; threshold tuning; labels, adjudication, and rater reliability; action versus contextual-decision definitions; baseline parity; clustered denominators; metric semantics and uncertainty; omission/false-positive burden; and release inspectability. It should test whether the evidence supports only candidate-scene retrieval or also semantic know-how capture and downstream transfer. Distribution-board maintenance is a bounded mechanism case, not a benchmark scope commitment.

## Charter decision filter and queue action

- **Objectives advanced:** A (expertise and realistic workflow evaluation), B (expertise-to-evaluation transformation), C (multimodal evidence and task/check projection), and E (clear construct and claim boundaries).
- **Concrete evidence:** immutable-v1 full-paper review plus a time-bounded audit of study artifacts, label authority, metrics, errors, and release status.
- **Uncertainty clarified:** whether paired work-video anomaly detection can validly nominate benchmark primitives or supports only a configured candidate-retrieval claim.
- **Mode:** narrow expansion. The autonomous review backlog was empty; only one human-decision task was pending, while several build tasks were blocked. This avoids another broad search.
- **Duplication/scope check:** exact duplicate searches were negative; adjacent reviews address different elicitation channels. Reuse source, participation, evidence-view, artifact, trace, task-projection, metric, and validity machinery; add no maintenance- or video-specific subsystem absent stronger evidence.
- **Useful completion:** source-locate the complete video-to-candidate pipeline, quantify units and error costs, audit expert authority and release conformance, compare adjacent elicitation channels, and preserve strict claim ceilings.

Added one task: `review-video-derived-expert-action-context-validity` (review, priority 52). No second source was queued.

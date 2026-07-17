# Scouting note — rule-projection and production-estimand gaps

- **Timestamp:** 2026-07-17T01:00:12Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, arXiv/official-page metadata, PDF metadata/page counts, arXiv-HTML heading/outbound-link triage where available, and local corpus/queue duplicate searches only. Neither paper body, appendices, source-rule corpus, interview evidence, project records, analysis files, nor reported results were deeply read or audited during scouting.

## 1. User-authored rules as candidate evaluation requirements — triage only

**From Correctness to Collaboration: Toward a Human-Centered Framework for Evaluating AI Agent Behavior in Software Engineering** — Tao Dong, Harini Sampath, Ja Young Lee, Sherry Y. Shi, and Andrew Macvean, arXiv:2512.23844v1.

- Immutable record/PDF: https://arxiv.org/abs/2512.23844v1 and https://arxiv.org/pdf/2512.23844v1
- Official Google Research page: https://research.google/pubs/from-correctness-to-collaboration-a-human-centered-taxonomy-of-ai-agent-behavior-in-software-engineering/
- Official conference PDF linked there: https://storage.googleapis.com/gweb-research2023-media/pubtools/1036663.pdf
- The arXiv API reports one 29 December 2025 version in `cs.HC`/`cs.SE`, with no withdrawal notice in the abstract. The versioned record/PDF, Google page, and Google-hosted conference PDF returned HTTP 200; arXiv HTML was unavailable (404), and the ACM DOI endpoint returned 403 during verification.
- Metadata shows a 23-page arXiv framework and a 10-page official conference paper with a changed title. The abstract reports a taxonomy derived from 91 sets of user-authored agent rules, plus a context-adaptive framework whose time-horizon axis comes from interviews with 15 expert engineers and whose work-type axis comes from analysis of a prototyping-agent prompt. These are author claims awaiting full-paper verification.
- The official page exposes the conference PDF but no source-rule corpus, interview data, codebook, analysis package, or repository among the links inspected during scouting. Release absence remains a review question, not an established defect.

**Distinct benchmark question:** `naturally authored runtime rule → source user/context/authority → coded requirement → category and applicability boundary → observable behavior/evidence view → criterion/check → artifact, workflow, burden, or consequence → bounded evaluation claim`.

This is more direct expertise-to-evaluation evidence than another generic agent taxonomy: existing runtime instructions may reveal standards, process expectations, collaboration norms, and hidden professional requirements. But a declared rule is not automatically a valid criterion. Its author may lack authority over all affected work; rules can encode local preferences, stale constraints, rubric cues, or conflicting ideals; and compliance need not improve artifacts or outcomes. The conference/arXiv difference also creates a useful version-and-claim-boundary audit.

Added `review-context-adaptive-agent-behavior-taxonomy` (priority 10). Useful completion separates corpus description, interview ideals, taxonomy coverage, external observability, criterion validity, and collaborative consequence; audits sampling/coding/disagreement/release limits; and treats software engineering as a bounded test of a general rule-to-criterion projection hypothesis rather than a scope commitment.

## 2. Observed versus modeled production outcomes — triage only

**Orchestrating Human-AI Software Delivery: A Retrospective Longitudinal Field Study of Three Software Modernization Programs** — Maximiliano Armesto and Christophe Kolb, arXiv:2603.20028v1.

- Immutable record/PDF/HTML: https://arxiv.org/abs/2603.20028v1, https://arxiv.org/pdf/2603.20028v1, and https://arxiv.org/html/2603.20028v1
- The arXiv API reports one 20 March 2026 version in `cs.SE`, with no withdrawal notice in the abstract; all three versioned endpoints returned HTTP 200.
- The abstract reports three real modernization programs observed across a traditional baseline and four successive versions of the Chiron orchestration platform. It explicitly distinguishes observed stage durations, task volumes, validation-stage issues, and first-release coverage from scenario-modeled person-days and senior-equivalent effort. Reported improvements are author claims awaiting full-paper and record verification.
- HTML-heading triage shows sections for system/platform evolution, benchmark programs, data provenance, observed and modeled measures, analysis, stage-specific results, review-based defect containment, sensitivity, threats to validity, conflict of interest/author positionality, and complete tables. No paper-linked platform, data, code, project-record, or replication release was found among outbound links during scouting.

**Distinct benchmark question:** `project demand and historical record → configured human/agent workflow version → stage/task observations → denominator and portfolio aggregation → modeled staffing/effort scenario → quality/readiness proxy → productivity or value claim`.

This follows the recent oversight review with production-adjacent records rather than another interview account, but its longitudinal design appears to change platform version, calendar time, project mix, and workflow together. Observed duration or issue density is not the same estimand as modeled labor, causal orchestration benefit, defect reduction, productivity, or economic value. The paper's own headings flag denominator drift, provenance heterogeneity, scenario dependence, and author positionality as audit targets.

Added `review-human-ai-software-delivery-field-validity` (priority 8). Useful completion reconstructs project/configuration assignment, source provenance, units and denominators, baseline and formulas, missingness and sensitivity; separates observed from modeled claims; and compares the evidence ceiling with AlphaEval, Nubank, production-practitioner, criterion-validity, and oversight reviews without creating software-delivery-specific machinery.

## Charter and backlog decision

Both tasks advance charter objectives A, B, and E through narrow expansion feeding validity consolidation. Before addition the queue contained only one pending human prerequisite, no claimed work, and three blocked builds; exact title/ID searches found no prior review, queue item, or scouting note for either source. The two tasks restore a small, targeted review backlog while testing general expertise-projection and production-estimand questions. No full-paper, release-completeness, representativeness, causal benefit, productivity, professional-validity, cross-domain-transfer, production-fitness, or readiness claim was made during scouting.

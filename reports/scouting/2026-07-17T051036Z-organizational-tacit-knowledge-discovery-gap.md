# Scouting note — organizational tacit-knowledge discovery validity gap

- **Timestamp:** 2026-07-17T05:10:36Z
- **Evidence status:** arXiv abstract/metadata and version history, immutable endpoint checks, arXiv-HTML heading triage, exact local corpus/queue duplicate searches, targeted release search, and official Figshare API metadata/file inventory only. The PDF/body, prompts, code, conversation logs, simulation outputs, metric implementations, statistical analyses, and reported results were **not** deeply read or audited during scouting.

## Substantive candidate — triage only

**Leveraging Large Language Models for Tacit Knowledge Discovery in Organizational Contexts** — Gianlucca Zuin, Saulo Mastelini, Túlio Loures, and Adriano Veloso, arXiv:2507.03811v1; IJCNN 2025.

- Immutable record/PDF/HTML: https://arxiv.org/abs/2507.03811v1, https://arxiv.org/pdf/2507.03811v1, and https://arxiv.org/html/2507.03811v1
- Versioned release: https://doi.org/10.6084/m9.figshare.28785524.v1
- The arXiv record identifies one version submitted 4 July 2025; the abstract contains no withdrawal notice, and the versioned abstract, PDF, and HTML endpoints returned HTTP 200.
- The abstract describes an LLM-based interviewer that reconstructs dataset descriptions by interacting with synthetic employees across formal and informal company structures. It reports 864 simulations, an SI-style dissemination process with waning infectivity, 94.9% full-knowledge recall, and correlation between self-critical and external literature-critic scores. These are author claims awaiting full-paper audit.
- HTML-heading triage exposes the prompt chain, synthetic company structures, experiments, metric-specific discussions, and a code/data availability statement. The paper body, methods, and results were not read during scouting.
- Official Figshare API metadata verifies immutable item version 1, DOI `10.6084/m9.figshare.28785524.v1`, publication before the arXiv submission, and a CC BY 4.0 release. Its current inventory includes `prompts.pdf`, a roughly 52 MB `conversation_logs.zip`, simulation/company/agent/orchestration Python files, a notebook, requirements, and supplied/computed MD5 values. File contents and paper-release correspondence were not inspected.
- Repository-wide title, arXiv-ID, and distinctive-phrase searches found no review, queue item, or prior scouting note.

## Why this is a narrow, useful gap

The corpus already covers model-assisted real interviews (Data Therapist), simulated novice interactions (SimInstruct), role-gated workflow claims, industrial codification, and expert artifact edits. This source appears to expose a different elicitation chain:

`author-planted knowledge atoms → synthetic specialist/employee allocation → formal and informal network paths → interviewer question and stopping policy → employee response/propagation → reconstructed description → recall/semantic/critic observer → bounded simulator result`.

High planted-atom recall in a synthetic organization would not by itself establish recovery of tacit expertise from real people. The source may confound retrieval with knowledge propagation, expose agent or personas to generator priors, treat one authored description as exhaustive truth, and compare dependent model critics. Conversely, its released prompts, logs, and simulator may make question opportunity, path dependence, stopping, missingness, and metric evidence views unusually inspectable. Organizational knowledge is a bounded substrate for testing general elicitation machinery, not a benchmark scope commitment.

## Charter decision filter and queue action

- **Objectives advanced:** A (expertise-transfer frontier), B (expertise-to-evaluation methodology), and F (scalable expert participation/elicitation).
- **Concrete evidence:** immutable-v1 deep review plus timing-aware audit of the versioned Figshare prompts, code, logs, simulator, metrics, and experiment artifacts.
- **Uncertainty clarified:** what counts as a knowledge unit and authoritative source; whether questions discover or propagate information; how network structure and access affect opportunities; whether critics independently observe valid recovery; and which real-elicitation, scalability, transfer, or benchmark claims survive.
- **Mode:** narrow expansion feeding validation. Before addition the queue had two pending consolidations, one pending human prerequisite, no pending review, no claimed work, and three blocked builds.
- **Duplication/scope:** adjacent reviews do not audit fragmented planted knowledge across synthetic organizational networks or this released 864-simulation package. Existing elicitation, provenance, metric, participation, and validity machinery should absorb findings; no organization-specific schema is proposed.
- **Useful completion:** reconstruct the simulator and statistical units, planted truth and authority, agent/persona information views, question/stopping policy, propagation, metrics and critics, dependence/leakage, uncertainty, costs, negative cases, and exact release correspondence; then state bounded retain/repair/test implications.

Added `review-tacit-knowledge-discovery-organizational-simulation-validity` (priority 8).

A second search hit, **Socially Interactive Agents for Preserving and Transferring Tacit Knowledge in Organizations** (arXiv:2508.19942v1), was not queued: abstract/metadata triage presents a conceptual framework rather than distinct empirical validation, so it does not outrank the inspectable simulation package or the existing real consented-pilot bottleneck.

No full-paper, reproducibility, metric-validity, real tacit-elicitation, expert-equivalence, organizational transport, scalability, transfer, professional-validity, or readiness claim was made during scouting.

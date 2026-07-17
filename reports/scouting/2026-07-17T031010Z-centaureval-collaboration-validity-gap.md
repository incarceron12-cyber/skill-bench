# Scouting note — CentaurEval collaboration-validity gap

- **Timestamp:** 2026-07-17T03:10:10Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, arXiv-HTML heading/outbound-link triage, ICML/search metadata, and exact local corpus/queue duplicate searches only. The PDF/body, appendices, task templates, participant records, environments, traces, code, data, analyses, and reported results were **not** deeply read or audited during scouting.

## Substantive candidate — triage only

**CentaurEval: Benchmarking Human-in-the-Loop Value in Agentic Coding** — Hanjun Luo et al., arXiv:2512.04111v3; ICML 2026.

- Immutable record/PDF/HTML: https://arxiv.org/abs/2512.04111v3, https://arxiv.org/pdf/2512.04111v3, and https://arxiv.org/html/2512.04111v3
- ICML record: https://icml.cc/virtual/2026/poster/65136
- The arXiv API identifies v3, updated 21 May 2026 after initial submission on 30 November 2025. The metadata summary contains no withdrawal notice; versioned abstract, PDF, and HTML endpoints returned HTTP 200.
- The abstract reports 45 “Collaboration-Necessary” problem templates, a standardized cloud IDE, 450 static LLM tasks, 45 participants, five LLMs, and four human-intervention levels. It reports human-alone, LLM-alone, and human–AI pass rates and interprets their contrast as co-reasoning. These are author claims awaiting full-paper audit.
- HTML-heading triage exposes template validation, agent configuration/prompts, instance quality control and inter-rater agreement, a standardized intervention protocol, participant selection/demographics, consent and questionnaires, detailed human/LLM results, qualitative success/failure analysis, cost accounting, and a case study.
- No author-owned task/template/code/data/trace release was found among the paper's inspected outbound links or targeted search results. Third-party paper notes were not treated as release evidence. A reviewer must renew the search and record release absence if it remains unverified.
- Repository-wide exact-title and arXiv-ID searches found no review, queue item, or prior scouting note.

## Why this is a narrow, useful gap

The reviewed corpus already covers simulated participation graphs (HAS-Bench), role-scoped handoffs (AgentCoop and EntCollabBench), mixed-initiative interface mechanisms (HiLSVA and Pista), and situated oversight reports. CentaurEval asks a distinct measurement question:

`template-level collaboration-necessity claim → instantiated task and matched resource envelope → intervention opportunity → human intervention exercise → semantic uptake and contribution attribution → artifact/state outcome → participant/agent cost and burden → bounded complementarity or value claim`.

A higher collaborative pass rate need not identify synergy. Human, agent, and combined conditions may receive different instances, interfaces, feedback, tools, compute, time, selection, or stopping rules; “intractable alone” can be an outcome-conditioned template filter; participant and task observations are clustered; and qualitative contribution narratives may be post-treatment interpretations. Coding is a bounded case for general human-agent work-allocation and configured-treatment methodology, not a benchmark scope commitment.

## Charter decision filter and queue action

- **Objectives advanced:** A (realistic agent and human evaluation frontier), B (expertise/work-to-evaluation), C (intervention/artifact/metric infrastructure), E (human understanding), and F (feasible expert participation).
- **Concrete evidence:** immutable-v3 deep review plus release-availability audit reconstructing task construction, condition parity, intervention realization, participant/task denominators, outcome evidence, burden, and cost.
- **Uncertainty clarified:** whether collaboration necessity is independently established; whether the conditions support matched causal complementarity rather than configured-package contrasts; and which ecological, professional, productivity, or value claims survive.
- **Mode:** narrow expansion feeding validity consolidation. Before addition the queue had one pending review, one pending build, one human prerequisite, no claimed work, and three blocked builds.
- **Duplication/scope:** adjacent sources do not audit this 45-participant human/human–AI/agent comparison or its collaboration-necessary task construction. Existing general contracts should absorb findings; no coding-specific subsystem is proposed.
- **Useful completion:** recover exact templates/instances, validation and selection, assignments/order/training, environments and resource envelopes, intervention opportunity/exercise/uptake, attribution, exclusions/missingness/retries, statistical units and uncertainty, consent, qualitative coding, cost, negative cases, and release correspondence.

Added `review-centaureval-human-ai-collaboration-validity` (priority 8). No full-paper, release-completeness, task-necessity, causal-synergy, ecological-validity, productivity, professional-utility, general-transfer, or readiness claim was made during scouting.

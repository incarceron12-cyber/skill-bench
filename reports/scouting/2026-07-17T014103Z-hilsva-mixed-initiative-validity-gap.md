# Scouting note — HiLSVA mixed-initiative validity gap

- **Timestamp:** 2026-07-17T01:41:03Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, arXiv-HTML heading/outbound-link triage, project-page link inspection, Git ref/API metadata, and repository README/root triage only. The PDF/body, case studies, participant protocol, user-study document, implementation internals, retained study data, and reported results were **not** deeply read or audited during scouting.

## Substantive candidate — triage only

**HiLSVA: Design and Evaluation of a Human-in-the-Loop Agentic System for Scientific Visualization** — Kuangshi Ai, Patrick Phuoc Do, and Chaoli Wang, arXiv:2606.26614v1.

- Immutable record/PDF/HTML: https://arxiv.org/abs/2606.26614v1, https://arxiv.org/pdf/2606.26614v1, and https://arxiv.org/html/2606.26614v1
- Official project page: https://hilsva.github.io/
- Official release pinned during scouting: https://github.com/KuangshiAi/HiLSVA/tree/63b99042b3f190e79ea4ded41fb8daa52e5cb4cc
- Paper-linked user-study document: https://hilsva.github.io/static/pdfs/user_study_doc.pdf
- The arXiv API reports one version submitted 25 June 2026 in `cs.HC`/`cs.AI`/`cs.GR`, with no withdrawal notice in the abstract. Versioned abstract, PDF, and HTML endpoints and the project page returned HTTP 200.
- The abstract describes a plan-first multi-agent scientific-visualization system with explicit oversight, stepwise provenance, test-time adaptation from user feedback, natural-language and direct-manipulation handoffs, and sandboxed execution. It reports representative case studies and a controlled study with 12 participants of varying expertise across autonomy settings, with claimed changes in completion, control, transparency, and an efficiency–oversight tradeoff. These are author claims awaiting full-paper and study audit.
- HTML-heading triage shows architecture, oversight/provenance/safe execution, test-time learning, interface, case-study, user-study, limitations, and additional-results sections. The project page links the paper, demo, case videos, user-study document, and source code.
- `git ls-remote` and GitHub API metadata resolve current `main`/HEAD to `63b99042b3f190e79ea4ded41fb8daa52e5cb4cc`, dated 26 June 2026, one day after arXiv v1. The non-fork repository root exposes frontend, Docker, knowledge-base, source, configuration, lockfile, and test configuration artifacts but no detected license. README triage describes joint planning, action guards, rollback, direct intervention, autonomy control, and test-time adaptation. Paper correspondence, actual guard/state semantics, reproducibility, study-material completeness, and result replication were not established.

## Why this is a narrow, useful gap

The corpus already deeply reviews SciVisAgentBench's autonomous multimodal artifact/grader package and Pista's pre-effect spreadsheet oversight interface; HANSEL's post-hoc verification review is also complete. Exact title/ID searches found HiLSVA only as a citation in the acquired SciVisAgentBench text, with no review, queue task, or prior scouting note. Its distinct chain is:

`mixed-initiative mechanism available → participant encounters an intervention opportunity → participant exercises approval/edit/rollback/autonomy control → agent semantically adopts the intervention → visualization artifact and workflow state change → task quality/completion → time, effort, control, and transparency → bounded collaboration claim`.

Availability is not exercise, and exercise is not correct uptake or consequence. A higher completion rate can reflect easier conditions, extra human labor, unequal task exposure, or permissive completion criteria. Perceived control/transparency do not establish artifact correctness, calibrated oversight, expert acceptance, or professional utility. Test-time adaptation can also change the configured treatment across tasks and participants. Scientific visualization is a bounded stress test of general human-agent work allocation and plural measurement, not a benchmark scope commitment.

## Charter decision filter and queue action

- **Objectives advanced:** A (realistic agents and human evaluation), B (expertise/work-to-evaluation), C (trace/artifact/state and intervention evidence), and F (feasible expert participation).
- **Concrete evidence:** immutable-v1 deep review, user-study-document audit, and timing-aware exact-commit implementation audit.
- **Uncertainty clarified:** which oversight mechanisms were truly available and used; whether interventions were adopted and improved artifacts/states; what extra human burden was required; and which causal, professional, and transfer claims the design licenses.
- **Mode:** narrow expansion feeding validation/consolidation. Before addition the queue had one pending human prerequisite and one pending review, with no claimed work.
- **Duplication/scope check:** adjacent reviews cover autonomous visualization grading, pre-effect spreadsheet oversight, or post-hoc evidence compression, not this mixed-initiative visualization system and 12-participant autonomy comparison. Existing participation, configured-system, trace, artifact, metric, and validity machinery should absorb findings; no new visualization-specific schema is proposed.
- **Useful completion:** reconstruct participants, expertise, tasks, autonomy conditions, assignment/order/training, objective and subjective outcomes, completion criteria, statistical unit, missingness/multiplicity, negative cases, configuration drift, implementation correspondence, and the claim ladder from control availability to professional consequence.

Added `review-hilsva-mixed-initiative-validity` (priority 8). No full-paper, implementation-correctness, causal oversight benefit, expert-validity, professional utility, general transfer, safety, production-fitness, or readiness claim was made during scouting.

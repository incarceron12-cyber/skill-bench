# Scouting note — failure-to-governance expert-judgment gap

- **Timestamp:** 2026-07-18T08:50:20Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, targeted release search, production-system-map inspection, and exact repository duplicate searches only. The PDF/source body, 88 field notes, codebase, analysis records, appendices, figures, process evidence, or any claimed production artifacts were **not** deeply read, downloaded, reproduced, or audited during scouting.

## Substantive candidate — triage only

**Cheap Code, Costly Judgment: A Case Study on Governable Agentic Software Engineering** — James C. Davis, Paschal C. Amusuo, Tanmay Singla, Berk Çakar, and Kirsten A. Davis; arXiv:2607.01087v2.

- Immutable record/PDF/source: https://arxiv.org/abs/2607.01087v2 · https://arxiv.org/pdf/2607.01087v2 · https://export.arxiv.org/e-print/2607.01087v2
- The arXiv API reports v2, submitted 1 July and updated 4 July 2026, 13 pages, in `cs.SE` and `cs.AI`; its summary contains no withdrawal or retraction notice. Record, PDF, and source endpoints returned HTTP 200; HEAD responses reported 442,758 PDF bytes and 246,011 source-package bytes.
- The abstract reports a 12-week first-person case study in which one expert software engineer used frontier coding agents to build a document-accessibility remediation system. Its stated empirical record is 88 contemporaneous field notes, 420 KLOC of production code, and 1.16 MLOC of tests, lints, supporting documentation, and agent tooling. It proposes “governance conversion”: recurring structural failures become visible during high-velocity agentic implementation and expert judgment converts them into durable governance mechanisms. These are author-stated claims awaiting full-paper verification.
- Targeted exact-title, phrase, author, and repository searches exposed no obvious official artifact or analysis release. This is a time-bounded unresolved release observation, not proof that no release exists; the full paper and source must be checked for links and availability statements.
- Exact arXiv ID, title, and mechanism searches found no local review, queue task, or scouting note. The production-system map covers eval loops, traces, context, tools, and bounded improvement, while the expert-participation ethnography covers embedded observation and transformation work; neither reconstructs a longitudinal `failure → expert interpretation → control → verification` process inside one production build.

## Why this is a narrow, useful gap

The reusable chain is:

`agent-produced episode/artifact → surfaced structural failure → contemporaneous evidence → expert diagnosis and judgment → architecture/tool/evidence/control change → verification and recurrence test → retained governance mechanism → later work quality/maintainability consequence`.

This directly advances charter objectives B and C. Tacit expertise can enter an agentic workflow not only as an upfront procedure or rubric, but as judgment that recognizes a failure signature and converts it into an executable control. If the evidence supports that chain, benchmark tasks could preserve failure witnesses, diagnosis alternatives, intervention lineage, control scope, regression tests, and recurrence evidence rather than scoring only code volume or a final artifact.

The design also raises sharp validity questions: one first-person case may fuse practitioner, observer, theorist, and beneficiary; contemporaneous notes do not automatically validate retrospective coding; selected recurring failures may omit counterexamples or abandoned controls; line counts are neither productivity nor maintainability outcomes; a production label does not establish user or accessibility consequence; and temporal ordering alone does not identify a control's causal effect. Model/scaffold/version, human time, costs, baseline development practice, artifact availability, negative cases, recurrence rates, and testable-prediction evidence must be reconstructed. One software project cannot license cross-domain governance, tacit-transfer, professional-equivalence, productivity, or readiness claims.

Software engineering is a bounded mechanism case, not a proposed benchmark scope.

## Charter decision filter and queue action

- **Objectives advanced:** A (production agent systems and evaluation), B (expertise-to-evaluation methodology), C (failure/control/verification machinery), and E (a clearer theory of where expert judgment remains necessary).
- **Concrete evidence:** immutable-v2 full-paper/source review and any paper-linked release audit, with episode-level reconstruction from observed failure through expert diagnosis, control, verification, and consequence.
- **Uncertainty clarified:** whether the paper supplies auditable longitudinal evidence that expert judgment becomes durable governance machinery, or chiefly a single actor's retrospective middle-range theory supported by aggregate artifact counts.
- **Mode:** narrow expansion. The autonomous review backlog was empty; one bounded review complements the active build queue without repeating broad search.
- **Duplication/scope check:** adjacent production-eval, expert-ethnography, procedural-memory, and coding-agent sources cover other links. Reuse existing trace, root/surface, intervention, artifact, metric, task-health, configured-system, and validity machinery; add no software-specific subsystem absent stronger evidence.
- **Useful completion:** source-locate every transformation and denominator; audit chronology, selection, reflexivity, disconfirming evidence, artifact identities, agent configurations, costs, verification, recurrence, and production outcomes; preserve strict claim ceilings.

Added one task: `review-cheap-code-costly-judgment-governance-conversion` (review, priority 54). No second source was queued.

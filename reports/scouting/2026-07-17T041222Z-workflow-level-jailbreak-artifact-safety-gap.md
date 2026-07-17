# Scouting note — workflow-level jailbreak artifact-safety gap

- **Timestamp:** 2026-07-17T04:12:22Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, arXiv-HTML heading/outbound-link triage, targeted web release search, and exact local corpus/queue duplicate searches only. The PDF/body, tables, prompts, generated artifacts, evaluator records, appendices, statistical analysis, and reported results were **not** deeply read or audited during scouting.

## Substantive candidate — triage only

**Refused in Chat, Written in Code: Workflow-Level Jailbreak Construction in IDE Coding Agents** — Abhishek Kumar and Carsten Maple, arXiv:2607.03968v2.

- Immutable record/PDF/HTML: https://arxiv.org/abs/2607.03968v2, https://arxiv.org/pdf/2607.03968v2, and https://arxiv.org/html/2607.03968v2
- The arXiv API identifies v2, initially submitted 4 July 2026 and updated 9 July 2026 in `cs.SE`/`cs.AI`. The metadata summary contains no withdrawal notice; versioned abstract, PDF, and HTML endpoints returned HTTP 200.
- The abstract describes 204 prompts sampled from three existing harmful-request sets, four closed-weight backends accessed through GitHub Copilot in Visual Studio Code, three short baseline framings, and a multi-stage workflow condition. It reports near-complete baseline refusal and universal unsafe teaching-shot completion in the workflow condition, with outputs assessed by two expert evaluators under a strict rubric. These are author claims awaiting full-paper audit.
- HTML-heading triage exposes the threat model and exclusions; workflow stages; model/environment, benchmark/sampling, condition, and manual-evaluation methods; results; threats to validity; evaluation/defense implications; and ethics/responsible-disclosure sections.
- No author-owned code, data, prompt, trace, artifact, or evaluator-record release was linked from the inspected arXiv HTML or found in targeted title/author searches. Incidental GitHub issue mirrors and third-party commentary were not treated as release evidence. A reviewer must renew the search before recording release absence.
- Repository-wide exact-title and arXiv-ID searches found no review, queue item, or prior scouting note.

## Why this is a narrow, useful gap

The corpus already covers cross-domain prompt-injection exposure and harm stages (ClawSafety), harmful professional-style instructions observed through transcript judgments (SafePro), protected-field/exact-effect/invocation authority (Context-to-Execution Integrity), and governance loss under context compaction. This paper appears to test a distinct transport chain:

`same harmful objective → presentation/decomposition condition → staged IDE context and work products → intermediate model outputs/file mutations → final generated artifact → evaluator evidence view and verdict → bounded configured-workflow safety claim`.

Direct-chat refusal may fail to transport because the workflow condition changes much more than turn count: context, files, local subtasks, optimization pressure, tool affordances, prior model commitments, and stopping may all differ. Conversely, a final unsafe artifact does not by itself identify the operative causal mechanism, natural attack prevalence, realized downstream harm, backend- or IDE-general robustness, or a successful defense. Coding is a bounded stress substrate for the general question of whether safety obligations survive decomposition and artifact construction, not a benchmark scope commitment.

## Charter decision filter and queue action

- **Objectives advanced:** A (realistic agent/safety evaluation frontier), B (context-to-workflow validity), and C (artifact/trace/action evidence and diagnostic infrastructure).
- **Concrete evidence:** immutable-v2 deep review and renewed release audit reconstructing prompt sampling, configured conditions, stage and artifact lineage, trial denominators, evaluator protocol, service/version identity, and claim limits.
- **Uncertainty clarified:** whether the conditions isolate workflow decomposition or compare larger treatment bundles; whether artifact judgments are complete and independently reliable; and which causal-mechanism, prevalence, transport, harm, defense, production-safety, or readiness claims survive.
- **Mode:** narrow expansion feeding validation/consolidation. Before addition the queue had one pending consolidation, one pending human prerequisite, no review backlog, no claimed work, and three blocked builds.
- **Duplication/scope:** adjacent safety reviews do not audit this same-prompt short-framing-versus-staged-IDE comparison. Existing configured-system, information-flow, artifact, trace, action, metric, and validity machinery should absorb findings; no coding-specific schema is proposed.
- **Useful completion:** recover all units, conditions, per-stage evidence, artifacts, assignment/order/stopping/retries/exclusions, expert selection/blinding/agreement/adjudication, uncertainty and negative cases; then separate configured-workflow outcome from mechanism, prevalence, transport, realized harm, defense efficacy, and readiness.

Added `review-workflow-level-jailbreak-artifact-safety-validity` (priority 8). No full-paper, evaluator-reliability, causal-mechanism, prevalence, generalization, defense-efficacy, production-safety, or readiness claim was made during scouting.

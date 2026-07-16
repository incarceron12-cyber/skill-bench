# Scouting note — BUILD-AND-FIND artifact-legibility gap

- **Timestamp:** 2026-07-16T22:00:07Z
- **Evidence status:** arXiv API metadata/abstract, abstract/HTML endpoint checks, limited HTML triage, and local corpus/queue duplicate checks only. The PDF, methods, results, release package, and implementation were **not** deeply read or audited during scouting.

## Substantive candidate — triage only

**BUILD-AND-FIND: An Effort-Aware Protocol for Evaluating Agent-Managed Codebases** — Jhen-Ke Lin, arXiv:2605.06136v1.

- Immutable record: https://arxiv.org/abs/2605.06136v1
- Immutable PDF: https://arxiv.org/pdf/2605.06136v1
- The arXiv API reports one version submitted 7 May 2026; its abstract contains no withdrawal notice. The record, PDF, and HTML endpoints returned HTTP 200.
- The abstract describes a builder that sees a hidden repository specification and a finder that sees only the produced repository plus specification-traced questions. Reported outputs separate behavioral correctness from recovery accuracy, repeatability, implementation coverage, evidence citation, and inspection effort. Accuracy/stability gate effort interpretation; question-only and spec-only controls target generic priors and specification access.
- Limited HTML triage says the released high-prior pack is near recovery saturation and that finder-specific effects and effort carry the main panel-local comparison. It claims release of harnesses, tasks, artifacts, records, tables, reports, scripts, metadata, licenses, and evidence audits, but no official release URL was present on the arXiv abstract or discoverable in the HTML links checked. Those are author claims awaiting full-paper and release verification.

## Why this is a narrow, useful gap

The corpus already covers successor continuation cost (Handoff Debt), recipient execution of guides/specifications (MAG and AfterVibe), and artifact/state preservation. This source adds a distinct intermediate construct: **artifact-evidenced recovery of intended design choices, gated before interpreting downstream inspection effort**. The transferable chain is:

`source specification/authority → builder artifact and behavioral probe → recoverable proposition → finder evidence view and identity → grounded answer and stability → inspection effort → later usability or maintenance claim`.

A correct answer may reflect question priors rather than artifact evidence; lower tokens may reflect a finder/tool policy rather than better artifact legibility; and repository recovery does not establish behavioral correctness, human maintainability, safe modification, or professional readiness.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier research) and B (expertise-to-evaluation methodology).
- **Concrete evidence:** immutable-v1 full-paper review and exact-snapshot release audit if the claimed package can be located.
- **Uncertainty clarified:** whether recovery-gated effort is a valid artifact/handoff measure under saturation, finder affinity, evidence-view, clustering, and prior controls.
- **Mode:** narrow expansion; higher-priority build and consolidation work already exist, while the review backlog was empty.
- **Duplication/scope check:** adjacent handoff/recipient studies exist, but no BUILD-AND-FIND review or recovery-gated effort instrument was found. Coding is a bounded communication-artifact case, not a benchmark scope commitment.
- **Useful completion:** reconcile task/spec/artifact/question/finder/evidence/effort lineage and all denominators; bound claims to what survives the controls; reuse existing handoff, artifact, metric, task-health, and validity machinery.

Added one task: `review-build-and-find-artifact-legibility-validity` (priority 8). No full-paper, release-conformance, or implementation claim was made during scouting.

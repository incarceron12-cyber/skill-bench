# Closed-loop feedback information-boundary audit

This bounded validation slice implements the semantic feedback chain proposed by the full UniClawBench review (`papers/agent-benchmarks/2026-07-13-uniclawbench-proactive-closed-loop-validity.md`, especially lines 104–119 and 173–190). It advances charter objectives B/C by testing intervention/instrument separation across a decision memo and structured spreadsheet; these are reusable work shapes, not a scope commitment.

The frozen protocol crosses six builder-authored cases (public-visible defect, hidden-only defect, and no-action control per shape) with no feedback, generic nudge, visible-only simulator, and hidden-derived coarse signal. The replay records every signal and proposition, independent role hashes, two blinded synthetic coder labels with disagreement retained, first/final outcome, repair uptake/correctness, new errors, cost, leakage, unsupported authority, and exact variance limits. Hidden references are represented only in the private-derived branch and never supplied to the visible-only simulator or executor inputs.

This intentionally reuses existing information-flow, bundle, task-health, metric, plural-judgment, and validity contracts; the exercised slice revealed no schema gap. Both coders and all outcomes are deterministic builder-authored calibration—not expert or participant evidence. The result supports only exact behavior of these 24 synthetic cells and cannot support proactivity, natural-user fidelity, general causal benefit, professional validity, capability, production, or readiness claims.

The EdgeBench follow-up freezes a per-channel manifest for local, authoritative-visible, and evaluator-only signals, including authority, visibility, payload/cardinality, granularity, latency, cadence, adaptive query budget, stochasticity/seed policy, and leakage rationale. Six additional builder-authored cases cross memo/spreadsheet shapes with hidden-target reconstruction, repeated-seed exploitation, and best-of-N upper-tail gaming. `adaptive-report.json` preserves current and best-so-far outcomes separately and reports exact run-at-risk denominators. The original 24-cell `report.json` remains byte-identical at SHA-256 `20deddde50fd93fc32b7af5b8f7eb69b9e9ffdab71c9cc3dd1ea421a41e335be`. Design evidence is the full EdgeBench review (`papers/agent-benchmarks/2026-07-13-edgebench-within-run-learning-validity.md`, especially lines 50–55, 99–105, and 134–162), grounded in the immutable local paper and pinned release audit recorded there.

Run:

```bash
python pilots/closed-loop-feedback-audit/audit.py
python -m unittest tests.test_closed_loop_feedback_audit
```

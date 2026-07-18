# Research Agenda

> This is the active research agenda under the canonical [`PROJECT_CHARTER.md`](../PROJECT_CHARTER.md). It may evolve with evidence but must not narrow the benchmark to one use case without an explicit charter-level decision.

## North star

Build a benchmark/research program that helps people answer:

> Can AI agents perform realistic knowledge work when the work requires messy context, judgment, artifact production, and domain expertise?

## What “useful benchmark” means here

A useful benchmark should be:

- **Decision-relevant:** informs model choice, workflow design, or deployment risk.
- **Hard to game:** uses private or semi-private checks, messy evidence, and realistic ambiguity.
- **Diagnostically rich:** explains *why* agents fail, not just that they fail.
- **Artifact-centered:** evaluates actual files: spreadsheets, decks, memos, notebooks, tickets, diagrams.
- **Domain-grounded:** reflects what experts actually care about.
- **Cost-aware:** reports quality per dollar, per minute, per human-review hour.
- **Legible:** easy for sponsors, researchers, and practitioners to understand.
- **Diagnosable from traces:** preserves enough intermediate evidence to identify whether failures came from planning, evidence retrieval, tool execution, state tracking, or artifact construction.

## Core research questions

1. What task structures expose real gaps in agentic capability?
2. How can expert domain knowledge be converted into rubrics, traps, evidence chains, and artifacts?
3. How do we cheaply create high-quality source corpora with contradictions and hidden requirements?
4. What scoring mix is best: objective checks, LLM judges, human judges, pairwise preferences, artifact tests?
5. How should benchmark creators prevent leakage while keeping enough public material to build trust?
6. What incentive systems get experts to contribute domain knowledge for free or nearly free?
7. What benchmark niches are underserved by current frontier labs and benchmark companies?
8. How can we design run logs so failures can be causally sliced into root causes instead of only scored at the final artifact level?

## Current project hypothesis (not yet validated)

The highest-leverage wedge is a **public methodology + small public pilot + private expansion packs** model:

- Public methodology earns trust.
- Public pilot demonstrates structure.
- Private or semi-private scenario packs preserve evaluation value.
- Sponsors fund domain-specific packs.
- Experts contribute because they receive visibility, attribution, benchmark access, and structured artifacts they can reuse.

The expert-participation mechanism is currently a hypothesis, not an observed
low-cost result. The reviewed 12-week ethnography used compensated experts in a
single mission-aligned institution and did not report rates, total cost,
recruitment conversion, or whether developer/model substitutions preserved
expert judgment. Early pilots must therefore measure expert and coordination
time, reciprocal value, comprehension, transformation fidelity, disagreement,
withdrawal/reconsent, and claim-blocking behavior before asserting that this
model is feasible for free or near-zero cost. See
`papers/agent-benchmarks/2026-07-10-domain-expert-participation-ethnography.md`.

## Closed validation slice: v7 pre-task procedure matrix

Independent interpretation is complete. The v1–v7 prospective sequence located and
retained successive source/task, launcher, model-facing, endpoint, authority,
checker-language, and canary failures without rewriting earlier evidence. V7 repaired
the last mechanical edge prospectively, bound the failed v6 records, passed a
commit-bound independent freeze review, and executed its frozen 32-row matrix exactly
once with no feedback, repair, or retry. All 32 rows were service- and
environment-valid and scored; 30 artifacts met the minimal task-identity gate and 24
passed the frozen endpoint checker. The independent zero-call audit reproduced those
denominators, all eight endpoint misses, treatment joins, resources, and all seven
false claim flags. See
[`pretask-procedure-transfer-v7-execution-validity-review.md`](concepts/pretask-procedure-transfer-v7-execution-validity-review.md),
[`2026-07-19-pretask-procedure-v7-execution-independent-audit.json`](../reports/validation/2026-07-19-pretask-procedure-v7-execution-independent-audit.json),
and [`pilots/pretask-procedure-transfer-v7-execution/`](../pilots/pretask-procedure-transfer-v7-execution/).

The predeclared assigned-row generated-package-minus-no-package result is a descriptive
`+0.75` across two authored families, but one zeta no-package artifact is invalid, so
an artifact-complete two-family mechanism contrast is not identified. The
artifact-complete generated-package-minus-equal-budget-raw contrast is `0.0` in both
families; generated, raw, generated-plus-raw, reference, and hindsight support all
saturate at 4/4. The controls also miss the intended clean discrimination: irrelevant
support induces rejection/omission, while the single-defect control passes 3/4. These
results validate lifecycle and execution-custody machinery more strongly than the
generated procedure.

This synthetic escalation loop is closed. Preserve v1–v7 bytes and do not rerun,
repair, rescore, add v8, or infer expert provenance, transfer, capability, utility,
professional validity, production fitness, or readiness. A future procedure-transfer
proposal is eligible only if it supplies independently authored non-saturating
families, repeated attempts, controls calibrated to the intended mechanism,
admissible expert or external-source authority, and prospectively hashed prompts,
runtime, effective configuration, and enforceable budget. It must predeclare both
end-to-end assigned-row and artifact-conditional estimands, including missingness and
post-treatment-selection rules.

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

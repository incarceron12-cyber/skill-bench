# Scouting note — practitioner correction → production eval loop

**Timestamp:** 2026-07-18T03:11:47Z

**Status:** primary-source triage only; no full-source review claim

**Source:** OpenAI and Thrive Holdings, [“Building self-improving tax agents with Codex”](https://openai.com/index/building-self-improving-tax-agents-with-codex/), 2026-05-27. A `?output=1` request was verified at HTTP 200 and returned 518,502 bytes of official HTML; the canonical URL returned HTTP 403 to this worker.

## Why this fills a narrow gap

The corpus already covers production evaluation, criteria derived from downstream outcomes, evolving Skills/graders, and context evolution. Exact repository search found no coverage of this source or system. The official case is unusually direct about a production evidence path:

`messy professional source files → extracted fields + provenance → downstream submission → practitioner correction → reviewed recurring finding → targeted eval → scoped Codex engineering task → regression checks → human review → deployed change`

Triage-visible text also distinguishes extraction misses, mapping problems, unsupported product behavior, tax judgment, and expected workflow noise instead of treating every edit as a model error. Ambiguous cases reportedly return to engineers rather than being forced into automation. That distinction could sharpen how `skill-bench` types expert corrections before promoting them into criteria, eval cases, Skills, or benchmark revisions.

## Evidence and validity questions for a full audit

The article reports a 7,000-return pilot, up-to-97% draft accuracy, roughly one-third practitioner time savings, about 50% throughput increase, and movement from one quarter to 86% of returns reaching a 75%-field-completion threshold within six weeks. These are **reported production-case claims, not audited causal findings at scouting stage**. A review should recover exact definitions and denominators and test at least these threats:

- changing return complexity, supported form coverage, practitioner mix, and product versions over time;
- observer authority for “correct” fields and whether later correction is a complete error oracle;
- selection into scored returns and the 75%/90%/100% threshold populations;
- absence of a contemporaneous comparison, uncertainty, raw traces, eval cases, or release artifacts;
- whether time saved and throughput are measured or estimated, and at what unit;
- privacy, compliance, affected-party, and professional-review boundaries;
- co-evolution among product, Skills/context, evals, practitioner behavior, and case mix.

## Charter decision filter

- **Objectives:** A (production agent systems/evaluation), B (expertise-to-evaluation), D (cross-source consolidation).
- **Concrete artifact:** provenance-preserving critical audit plus a reusable correction-to-eval chain.
- **Uncertainty clarified:** when a practitioner correction is an authorized failure signal and when longitudinal endpoint movement supports only a configured production-history description rather than causal self-improvement.
- **Mode:** narrow expansion/research; source/review/research backlog was empty while two consolidation tasks remained pending.
- **Duplication/scope check:** no exact duplicate found; tax is a bounded mechanism case, not a domain commitment.
- **Useful completion:** separate inspectable workflow design from accuracy, productivity, value, safety, compliance, and general self-improvement claims; identify reusable implications without adding a tax-specific schema or pilot.

## Queue action

Added one task: `research-openai-tax-agent-production-eval-loop` (priority 89). No broad search backlog or duplicate task was added.

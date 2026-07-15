# Scouting note — dual-expert dialogue elicitation gap

**Timestamp:** 2026-07-15T10:48:20Z  
**Scope:** Narrow expansion against charter objectives A/B/F. Queue inspection found 264 tasks: 257 completed, four blocked, and three pending (one human prerequisite, one empirical build, and one consolidation); no source, research, or review backlog remained. The reviewed corpus covers critical-incident elicitation, mixed-initiative probes, simulated novices, participation authority, and workflow-twin claim extraction, but not a directly paired domain-expert/knowledge-engineer dialogue treatment.

## Substantive finding — triage only

**BC Protocol: Structured Dual-Expert Dialogue for Eliciting High-Quality Chain-of-Thought Post-Training Data** — Bo Zou and Chao Xu; arXiv:2605.25549v1.

- Immutable record: https://arxiv.org/abs/2605.25549v1
- Immutable PDF: https://arxiv.org/pdf/2605.25549v1
- The arXiv API identifies immutable v1, submitted 25 May 2026 in `cs.CL`, `cs.AI`, and `cs.LG`; its summary contains no withdrawal notice. The versioned abstract, PDF, and HTML endpoints returned HTTP 200 during scouting.
- The abstract proposes pairing a domain expert with a knowledge engineer to externalize implicit judgments, introduces a six-dimension Participant Aptitude Model, and names “Calibrated Ignorance” and “Selection-over-Prescription” as methodological ideas.
- It reports a narrative-fiction experiment comparing 20 dual-dialogue chains against 20 chains independently written by the same domain expert. Three model judges—GPT-4o, Claude Opus 4.5, and Gemini 2.5 Pro—reportedly produced 600 blind ratings over five dimensions. The largest abstract result is for “naturalness of reasoning process” (means 4.80 versus 1.30, reported `p=2.4×10^-8`, Cliff's delta 1.0). These are author-reported abstract claims, not independently verified findings.
- Structural inspection of immutable-v1 HTML—not a full reading—confirmed sections on protocol roles, participant aptitude, non-template facilitation, voice versus text, post-processing, control design, blind model-judge assessment, implicit-premise externalization, agreement, costs, generalizability, and limitations.
- No paper-specific author-owned repository, dataset, or project URL appeared in the inspected HTML; exact-title/ID web searches returned arXiv and third-party mirrors rather than a verifiable official release. A reviewer must renew and document that audit.
- Repository-wide exact-title, arXiv-ID, and signature-phrase searches found no duplicate. The closest local evidence is Data Therapist, SimInstruct, laboratory workflow twins, the participation contract, and the expertise-elicitation session template.
- This is **metadata, abstract, endpoint, section-structure, release-location, and duplicate triage only**. The paper body, methods, examples, tables, appendices, statistics, prompts, dialogues, ratings, costs, and artifacts were not read or audited. No claim is made that the protocol elicits true tacit knowledge, improves substantive correctness, produces useful benchmark primitives, outperforms other elicitation methods, benefits post-training, transports across experts/domains, or supports expert-equivalence, professional-validity, production, or readiness claims.

## Why this is distinct

Dialogue may expose skipped cues and counterfactuals that solo writing omits, but fluent natural-language reasoning is not automatically faithful expertise. The reusable chain is `participant selection and authority → unprompted expert judgment → knowledge-engineer probe and information introduced → expert correction/approval → raw dialogue span → post-processing transformation → proposition/cue/threshold provenance → independent substantive validation → task/check projection → downstream benchmark utility and contributor burden`.

A same-expert paired comparison could isolate an elicitation-format contrast more cleanly than unrelated examples, yet one expert, one creative domain, model judges, post-processing, and item dependence may still identify judge-preferred narration rather than additional correct or useful expertise. A full audit can test whether the protocol contributes reusable probes or selection criteria to the existing elicitation-session machinery without turning `skill-bench` into a post-training-data or fiction benchmark.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier elicitation research), B (expertise-to-evaluation methodology), and F (feasible expert participation).
- **Concrete evidence/artifact:** immutable-v1 deep review reconstructing roles, selection, facilitation, transformations, paired sampling, judge instrument, dependence, costs, release status, limitations, and exact claim ceilings.
- **Uncertainty clarified:** whether dual dialogue yields additional evidence-bearing expert cues versus more natural judge-preferred CoT, and whether “selection over prescription” has empirical support.
- **Mode:** narrow expansion feeding later human validation; no post-training or narrative-fiction scope commitment.
- **Duplication/scope:** no local duplicate; existing elicitation and participation reviews are required comparators.
- **Useful completion:** keep elicited yield, transformation fidelity, naturalness, correctness, downstream task/check utility, burden, and transport separate; reuse existing machinery unless a non-overlapping primitive is evidenced.

Added one task: `review-bc-protocol-dual-expert-elicitation` (priority 11). The empirical fair-basis build and criterion-reliability consolidation remain much higher priority.

## Operational note

The required initial `git pull --ff-only` succeeded. Queue validation passed before this addition. Pre-existing modified/untracked site and paper/release artifacts were not touched.

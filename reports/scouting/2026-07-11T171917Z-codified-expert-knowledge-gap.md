# Scouting note — industrial expert-knowledge codification gap

**Timestamp:** 2026-07-11T17:19:17Z  
**Scope:** Narrow expansion against charter objectives A/B after confirming 111 completed tasks, two pending consolidation tasks, one blocked real-elicitation task, and no ready review task. This run did not repeat broad benchmark discovery.

## Substantive finding (triage only)

**How to Build AI Agents by Augmenting LLMs with Codified Human Expert Knowledge**

- Immutable arXiv record: https://arxiv.org/abs/2601.15153v1
- Immutable PDF target: https://arxiv.org/pdf/2601.15153v1
- Search metadata describes an industrial visualization case study that captures and codifies human domain knowledge into an agent and reports that non-experts can attain expert-level outcomes.
- This is directly relevant to skill-bench's central expertise-to-evaluation question because it appears to connect elicitation, a codified intervention, non-expert use, and outcome validation in one study. It is more directly intervention-oriented than the existing ACTA method report and more applied than Data Therapist's elicitation framing.
- **Evidence status:** arXiv/search metadata and URL discovery only. The PDF, elicitation protocol, expert sample, codified representation, system, experimental conditions, outcome measures, statistics, and appendices were not read during scouting. The reported expert-level outcome is an author claim requiring full-text verification; no claim is made here that tacit knowledge was faithfully captured, that expertise rather than scaffolding caused gains, or that the result generalizes beyond the industrial visualization case.

## Benchmark implication to test

A full review should treat the codified knowledge as a configured intervention and separate expert elicitation evidence, representation fidelity, procedural guidance, interface/scaffold effects, base-model effects, evaluator cue overlap, and downstream artifact quality. It should test whether the comparison supports a causal expertise-transfer claim and whether expert authorship or validation is independent of task and score construction. ACTA, Data Therapist, SkillsBench, and LH-Bench provide the nearest nonduplicate comparisons.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier evidence) and B (general expertise-to-evaluation methodology).
- **Evidence/artifact sought:** immutable-v1 full-paper review with page evidence and bounded contract implications.
- **Uncertainty clarified:** whether an industrial codification pipeline demonstrates transferable expert knowledge rather than prompt/scaffold assistance or shared evaluator cues.
- **Mode/balance:** one narrow review task restores a ready expansion item while two consolidation tasks remain pending; no second source was added.
- **Duplication/scope:** repository search found no title, arXiv ID, review, or queue item. Visualization is a bounded case testing a general transfer hypothesis, not a domain commitment.
- **Useful completion:** reconstruct the complete elicitation-to-outcome chain, preserve sample/design/generalization limits, and map only nonduplicate implications to existing expertise-transfer, participation, and paired-evaluation machinery.

Added `review-codified-human-expert-knowledge-industrial-case` (priority 50). No second task was added.

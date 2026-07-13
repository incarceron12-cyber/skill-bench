# Scouting note — reusable expert intelligence for scalable agent evaluation

**Timestamp:** 2026-07-13T21:10:07Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Queue inspection found 188 tasks: 184 completed, two blocked, and two pending consolidation/build tasks, with no pending source/research/review work. Existing reviews cover expert rubric authoring, automated evaluator construction, human/AI rater effects, adversarial harness isolation, and expert incentives, but not the specific claim that expert-authored evaluation intelligence can be curated once and reused across large multi-turn behavioral evaluations.

## Substantive finding (triage only)

**Human-on-the-Bridge: Scalable Evaluation for AI Agents**

- Immutable arXiv record: https://arxiv.org/abs/2606.16871v1
- Immutable PDF: https://arxiv.org/pdf/2606.16871v1
- Immutable HTML: https://arxiv.org/html/2606.16871v1
- Author-linked implementation: https://github.com/ProofAgent-ai/proofagent-harness
- The arXiv API identifies Fouad Bousetouane as the sole author; v1 was submitted 15 June 2026 in `cs.MA`. The API record contains no later version.
- The abstract frames Human-on-the-Bridge (HOB) as an alternative to per-run human review: experts curate domain context, red-team traps, juror personas, scoring guidance, audit rules, and fallback policies upstream; a harness then repeatedly conducts adversarial multi-turn evaluation, captures traces, invokes multiple jurors, and emits evidence-linked reports.
- The abstract reports 23,500 agent turns across finance, healthcare, and code generation, symmetric and cost-efficient asymmetric evaluator settings, paired-version calibration, failures including phantom or missing tool calls, policy drift, manipulation paths, and safe but non-resolving refusal, plus a claim that smaller evaluator models can challenge frontier-model agents. These are discovery leads only: the number and independence of agents, tasks, traps, trials, and turns; expert identity and authority; human effort; juror dependence; baselines; uncertainty; selection; cost definition; release coverage; and domain/configured-system sampling require full-paper and artifact verification.
- Structural metadata from the immutable HTML shows dedicated sections for four HOB pillars, cost-scaling intuition, symmetric/asymmetric experiments, per-agent scores, paired-version calibration, metric-level scaling, risky failures, fallback recovery, and validation. This supports a focused audit but is not a full-paper review.
- The paper links the ProofAgent Harness repository directly. `git ls-remote` verified repository HEAD `95ec9e42b7d1e571493dbe3e691d75fa1eed1187` and tag `v0.7.1` at `b011384290a746dc1f15766f4e9a192d26c39797` during scouting. Release timing and correspondence to the paper's experiments remain unaudited.
- Repository-wide title/ID searches found no duplicate. ResearchRubrics studies expert criterion authoring; EvalAgent studies automated evaluator construction; AgentRewardBench and RuVerBench study judge reliability; many-facet/rubric-modification reviews study rater effects; ELAIPBench studies expert-author incentives; Harness-Bench isolates execution. None currently tests HOB's combined reusable-expertise and asymmetric-evaluator claim.
- This is **metadata/abstract, section-structure, and URL/repository-existence triage only**. The PDF, appendices, code, traps, reports, configurations, and results were not fully read or audited. No claim is made that HOB preserves expert judgment, improves evaluation validity, scales economically, detects failures generally, or establishes professional validity, safety, or readiness.

## Benchmark implication to test

Reusable evaluation intelligence should be represented as a versioned, authority-bearing instrument rather than treated as distilled expert truth. A full audit should separate expert/source contribution, transformation and approval from model-authored traps/personas; distinguish agent, harness model, juror, rule, trace view, fallback policy, and aggregation versions; and preserve the actual sampling and dependence structure behind the reported turn count. The key validity question is whether asymmetric HOB comparisons preserve criterion interpretation and failure detection while lowering cost, or whether shared authored cues, adaptive adversarial interaction, juror dependence, model-family overlap, and commercial instrument design make the apparent scaling result instrument-specific. Any transfer should reuse existing participation, expertise-transfer, artifact/evidence-view, configured-system, metric, validity, dynamic-criteria, and harness contracts rather than create a finance/healthcare/code subsystem.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier expert-grounded and scalable evaluation), B (expertise-to-measurement warrants), and C (reusable grader, trace, and configured-system machinery).
- **Evidence/artifact sought:** immutable full-paper review plus a pinned author-linked release audit reconstructing authorship/authority, instrument topology, samples and denominators, calibration, evidence records, costs, uncertainty, and reproducibility.
- **Uncertainty clarified:** whether upstream curation measurably preserves/scales expert judgment under smaller evaluator models, versus repeatedly executing one author-designed instrument with shared cues or dependent judges.
- **Mode/balance:** one narrow expansion task restores a small review backlog while leaving the two higher-priority consolidation/build tasks undisturbed.
- **Duplication/scope:** nonduplicate reusable-expert-intelligence question; the three experiment domains are cases, not a scope commitment.
- **Useful completion:** verify headline counts, comparisons, statistical and cost estimands, expert provenance, juror topology, fallback logic, and release-paper correspondence; separate evidence from prescriptions and commercial claims; compare the existing rubric/evaluator/rater/incentive/harness corpus; retain strict claim ceilings.

Added `review-human-on-the-bridge-scalable-expert-evaluation` (priority 44). No second task was added.

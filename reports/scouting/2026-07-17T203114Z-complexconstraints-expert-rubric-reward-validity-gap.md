# Scouting note — expert-rubric measurement/reward validity gap

- **Timestamp:** 2026-07-17T20:31:14Z
- **Evidence status:** arXiv API metadata/abstract, immutable HTML link triage, exact local duplicate search, and Hugging Face API release metadata only. The paper body, appendices, prompts, 1,559 criteria, training set, expert-authoring records, judge calibration, CoreCraft environment, training runs, or external evaluations were **not** deeply read, downloaded, executed, or audited during scouting.

## Substantive candidate — triage only

**ComplexConstraints and Beyond: Expert Rubrics for RLVR** — Sushant Mehta, Liudas Panavas, Suhaas Garre, and Edwin Chen; arXiv:2606.09118v3.

- Immutable record/PDF/HTML: https://arxiv.org/abs/2606.09118v3 · https://arxiv.org/pdf/2606.09118v3 · https://arxiv.org/html/2606.09118v3
- Public benchmark release: https://huggingface.co/datasets/surgeai/ComplexConstraints at inspected revision `e9625c6f635f42b72cb85a04c2be64746f945126`.
- The arXiv API identifies a `cs.AI` v3 submitted 8 June 2026 and updated 4 July 2026, accepted to the GEM workshop at ACL 2026. Its summary contains no withdrawal or retraction notice.
- The abstract says the work uses expert-curated rubric evaluation both as a measurement instrument and an RL reward across complex instruction following and stateful enterprise-agent tasks. It reports a public 75-prompt benchmark with 1,559 criteria, a disjoint 1,000-prompt training set, a +15.5 percentage-point held-out criterion-pass gain for a trained 4B model, and external gains on AdvancedIF, MultiChallenge, BFCL, tau²-Bench, and Toolathlon. These are author-stated abstract claims awaiting full-paper, release, and empirical-artifact verification.
- The current Hugging Face revision is public and ungated but exposes only `README.md` and a 631,336-byte `ComplexConstraints_benchmark_set.csv`; the API labels the dataset smaller than 1K rows. The inspected release metadata therefore establishes a public 75-prompt benchmark surface, not the claimed 1,000-prompt training set, expert-authoring ledger, CoreCraft package, reward implementation, judge calibration corpus, checkpoints, run records, or external-evaluation evidence.
- Version-aware inspection matters: v1/v2 HTML contained no Hugging Face link, while v3 links the dataset. The ACL Anthology search record uses the title **Complex-IF and Beyond**, whereas arXiv v3 and the public dataset use **ComplexConstraints**. A review should distinguish naming/version drift from substantive task or result drift.
- Exact repository searches found no local review, queue task, index entry, or scouting note for the title or arXiv ID. Nearby work covers expert rubric authoring, model-judge calibration, criterion dependence, generated/adaptive rubrics, rubric-conditioned training, and professional tasks, but not the same expert rubric serving simultaneously as benchmark instrument and optimization reward.

## Why this is a narrow, useful gap

The central unresolved chain is:

`professional-demand provenance → expert identity/authority and authoring process → prompt/source context → criterion obligation, dependency, polarity, applicability, and evidence view → human/model observation and calibration → aggregate benchmark decision → reward transformation and training exposure → held-out same-instrument result → untouched external task/configuration transport → artifact/state consequence`.

Using one rubric for measurement and RL can make criterion-level behavior legible and scalable, but it also couples the intervention and instrument. Improved pass rate may reflect learning criterion phrasing, judge preferences, compensatory aggregation, or a selected task distribution rather than transferable expertise or better professional work. “Atomic” criteria may still be dependent, conditional, contradictory, response-triggered, or collectively incomplete. External benchmark gains require exact model, task, harness, budget, evaluator, checkpoint-selection, repetition, and missing-run accounting before they support transfer. A stateful CoreCraft reward additionally needs authoritative state and action observers; rubric agreement alone cannot establish correct or safe environment consequences.

Complex instruction following and enterprise task RL are bounded cases for a general intervention–instrument validity question, not a proposal to narrow `skill-bench` to RL training or one vendor dataset.

## Charter decision filter and queue action

- **Objectives advanced:** A (expert-rubric and agent-evaluation frontier), B (expertise-to-criterion lineage and intervention/instrument separation), and C (criterion contracts, judge calibration, reward and transport records).
- **Concrete evidence:** immutable-v3 full-paper review plus timing-aware audit of the public benchmark and any training, CoreCraft, judge-calibration, checkpoint, and result artifacts; a criterion-level sample audit if licensing and release structure permit.
- **Uncertainty clarified:** when expert-authored criteria support measurement, reward, same-instrument improvement, or external transfer; whether criterion authority and dependencies are preserved; and which artifacts substantiate the reported training and agent results.
- **Mode:** narrow expansion. The autonomous source/research/review backlog is empty while one build, one consolidation, and one human prerequisite remain pending, so one targeted review restores a minimal evidence path without restarting broad search.
- **Duplication/scope check:** adjacent reviews cover component questions, but none audits the measurement→reward→training→transport loop in this source. No RL-specific schema or pilot is proposed.
- **Useful completion:** page/path-grounded reconstruction of expert recruitment and transformations, task/train/holdout lineage, criterion semantics and dependence, observer calibration, aggregation and reward topology, configured training/evaluation, repeats/uncertainty, release conformance, version drift, and bounded retain/repair/test implications while separating rubric quality, judge reliability, reward learnability, same-instrument gain, external transport, professional validity, and readiness.

Add one task: `review-complexconstraints-expert-rubric-reward-validity`. No other candidate should be queued from this search.

# Scouting note — context-compaction governance validity gap

**Timestamp:** 2026-07-15T21:34:23Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Queue inspection found 295 tasks: 289 completed, three blocked, and three pending, with no claimed work and no source/research/review backlog. Recent scouting already covered context-compression decision fidelity, memory lifecycle/authority, action authority, privacy, permissions, feedback, task generation, live evidence, and cross-artifact work. This run searched only for the missing boundary between production context compaction and persistence of standing governance constraints.

## Substantive finding — triage only

**Governance Decay: How Context Compaction Silently Erases Safety Constraints in Long-Horizon LLM Agents** — Shiyang Chen; arXiv:2606.22528v2.

- Immutable record: https://arxiv.org/abs/2606.22528v2
- Immutable PDF: https://arxiv.org/pdf/2606.22528v2
- Immutable HTML: https://arxiv.org/html/2606.22528v2
- The arXiv API identifies v1 as submitted 21 June 2026 and immutable v2 as updated 27 June 2026 in `cs.AI`; the metadata summary contains no withdrawal or retraction notice. All three versioned endpoints returned HTTP 200 during scouting.
- The abstract introduces **Governance Decay** and ConstraintRot, reporting 1,323 synthetic long-horizon episodes across seven model families. It says prohibited tool-call violations rise from 0% with policy visible to 30% after compaction, reach 59% for some models, remain 0% when the constraint survives the summary, and reach 38% when it is omitted. It also reports a Compaction-Eviction Attack and a training-free Constraint Pinning mitigation that restores the benchmark violation rate to 0%. These are author-reported abstract claims, not independently verified findings.
- Structural inspection of immutable-v2 HTML—not a full reading—confirmed sections for threat model, ConstraintRot conditions and constraint families, model/compactor analyses, compaction aggressiveness and strategy, attack, pinning, utility, real-harness validation, limitations, and ethics.
- The immutable paper metadata and structurally inspected HTML exposed no official code/data URL. Exact-title, arXiv-ID, and ConstraintRot web/GitHub searches found only third-party paper-list/security projects and commentary; none was treated as an author-owned benchmark release. A deep review must repeat and document the release search against the paper body and author surfaces.
- Repository-wide searches found no exact title, arXiv ID, ConstraintRot review, or queue task. The nearest completed sources—Decision Fidelity under Context Compression, Context-to-Execution Integrity, ClawSafety, LongMemEval v2, and memory-authority/lifecycle work—cover decision preservation, mediated action, injection, experience, or state operations, but not whether the context manager silently changes a standing governance treatment before later action.
- Only arXiv metadata/abstract, endpoint status, HTML section headings/outbound-link inventory, search-result metadata, and duplicate checks were inspected. The paper body, appendices, scenarios, constraints, compaction prompts/outputs, injection optimization, tool definitions, graders, traces, model configurations, results, statistics, utility cases, and real-harness evidence were not read or executed. No claim is made that ConstraintRot isolates compaction causally, constraints are legitimate or representative, grader effects equal harm, attacks transport, pinning is complete, results reproduce, or the study establishes broad safety, production fitness, or readiness.

## Why this is distinct

The reusable chain is `constraint source and authority → configured policy placement/visibility → pre-compaction compliance → compactor identity and lossy transformation → proposition-level survival/omission/distortion → agent-visible post-compaction evidence → later request and action opportunity → agent adoption/attempt → tool-call effect → realized consequence → mitigation and utility tradeoff`. Compaction is not merely a context-budget optimization if it changes the policy treatment delivered to the agent. Yet a synthetic prohibited-call detector can establish only exact configured conformance unless the policy's authority, action semantics, environment mediation, and consequences are separately validated.

A full audit should separate generic length effects from compaction, policy deletion from agent noncompliance, compactor from acting-model effects, semantic survival from string retention, adversarial exposure and optimization budgets, attempted calls from realized effects and harms, mitigation placement from model behavior, benign-task utility from policy preservation, uncertainty and episode clustering, and synthetic versus real-harness transport. Existing configured-system, information-flow, authority, trace, artifact-view, safety, metric, task-health, and validity machinery should host reusable lessons unless an exercised nonduplicate gap is proven.

## Charter decision filter and queue action

- **Objectives advanced:** A (production context/memory and safety-evaluation frontier), B (standing expert/organizational constraints transformed into durable agent obligations), and C (context-state, tool-effect, and mitigation instrumentation).
- **Concrete evidence/artifact:** immutable-v2 deep review plus a release/search audit and a claim ladder for policy presence, semantic survival, exposure, adoption, attempted/realized effect, consequence, and utility.
- **Uncertainty clarified:** whether ConstraintRot validly isolates governance loss caused by compaction and whether pinning preserves the treatment without hiding a configured-system intervention or utility cost.
- **Mode:** narrow expansion feeding consolidation/validation; this is reusable context-state machinery, not a safety-only or one-domain scope commitment.
- **Duplication/scope:** no exact local duplicate; comparison with the five nearest reviewed families is mandatory.
- **Useful completion:** exact condition/episode denominators and model/compactor identities; release conformance if artifacts exist; explicit bounds separating synthetic tool-call conformance, context-manager validity, broad safety, realized harm, production fitness, and readiness.

Added one low-priority task: `review-governance-decay-context-compaction-validity` (priority 5). The delayed-obligation consolidation/build and consented expert micro-pilot remain substantially higher priority.

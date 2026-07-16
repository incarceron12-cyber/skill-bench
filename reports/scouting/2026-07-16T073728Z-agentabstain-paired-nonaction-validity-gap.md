# Scouting note — paired act/abstain and action-timing validity gap

**Timestamp:** 2026-07-16T07:37:28Z

**Scope:** Narrow expansion against charter objectives A/B/C. After pull, the queue had 315 tasks: 309 completed, three blocked, three pending, and no claimed work. Two substantive autonomous tasks already cover agent-mediated workspace reuse and criterion/formal-guarantee consolidation, so this run avoided broad search and revisited one explicitly deferred action-policy candidate. Findings are **metadata/abstract and endpoint triage only**, not a full-paper review.

## Substantive finding — triage only

**AgentAbstain: Do LLM Agents Know When Not to Act?** — arXiv:2607.10059v1.

- Immutable record/PDF/HTML: https://arxiv.org/abs/2607.10059v1 · https://arxiv.org/pdf/2607.10059v1 · https://arxiv.org/html/2607.10059v1
- Paper-linked project surface: https://agentabstain.github.io
- The arXiv API reports immutable v1 submitted 11 July 2026 in `cs.AI`; the metadata summary contains no withdrawal notice. The record, PDF, HTML, and project endpoints returned HTTP 200.
- The abstract reports 263 should-act/should-abstain pairs across 42 executable sandboxes and eight scenarios. Each pair is said to differ by a controlled instruction, tool, or environment-state perturbation. It also reports automated environment/task generation, deterministic replay, semantic judges, sampled ratings by three annotators, evaluation of 17 models in four harnesses, paired accuracy, and “post-hoc abstention” after an irreversible action. These are author-reported abstract claims.
- A prior scout surfaced this source but explicitly deferred it while prioritizing MemOps; repository-wide title/ID and distinctive-phrase search found no review or queue task. Adjacent reviews cover underspecification, research non-completion, confidence calibration, action mediation, and temporal intervention labels, but not this exact matched act/non-action executable design.

## Why it is distinct

The reusable chain is:

`public task and current state → act/abstain oracle authority → controlled pair perturbation and equivalence → action opportunity → observation available to the configured agent → first consequential/irreversible effect → timely abstention, late recognition, or useful action → environment and observer validity → paired outcome and uncertainty → decision/safety claim`.

A refusal string is not timely abstention if an irreversible effect already occurred. Conversely, non-action is not correct when action was authorized and feasible. Paired accuracy may expose this joint policy requirement, but only if pair equivalence, oracle authority, action opportunities, effect observation, environment validity, and missing-run denominators hold. Generator/replay/judge agreement and sampled “well-designed” ratings do not by themselves establish calibrated safety, professional validity, or readiness.

## Evidence limits and queue action

Only arXiv API metadata/abstract, endpoint status, search-result metadata, local queue/index/review searches, recent scouting notes, and the existing adjacent-review inventory were inspected. The paper body, appendices, project page contents, code, datasets, task pairs, environments, perturbations, annotator records, traces, judges, model runs, and analyses were **not read or executed**. No claim is made that pair construction is controlled, abstention labels are authoritative, post-hoc effects are correctly observed, regeneration limits contamination, task-solving and abstention are independent, or the benchmark is safe, professionally valid, or ready.

Added one lowest-priority review task: `review-agentabstain-act-abstain-validity` (priority 1). It is subordinate to the current build/consolidation backlog and requires an immutable-paper plus pinned official-release audit. Useful completion is reusable pairing, opportunity-denominator, action-timing, irreversible-effect, and invalid-environment guidance—or an evidence-backed rejection if perturbation equivalence, observer validity, release conformance, or denominators fail. This is a cross-domain action-policy method study, not a sandbox or safety-domain scope commitment.

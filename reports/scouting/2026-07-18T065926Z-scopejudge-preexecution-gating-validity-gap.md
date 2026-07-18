# Scouting note — request-conditioned pre-execution gating validity gap

- **Timestamp:** 2026-07-18T06:59:26Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, arXiv HTML structural/link triage, targeted release search, and exact repository duplicate searches only. The PDF body, appendices, dataset rows, source trajectories, grader records, judge outputs, or result tables were **not** deeply read, downloaded, reproduced, or audited during scouting.

## Substantive candidate — triage only

**ScopeJudge: Cost-Aware Pre-Execution Gating for Offensive Security Agents** — Shane Caldwell, Max Harley, Ads Dawson, Michael Kouremetis, Vincent Abruzzo, and Will Pearce; arXiv:2607.07774v1.

- Immutable record/PDF/HTML: https://arxiv.org/abs/2607.07774v1 · https://arxiv.org/pdf/2607.07774v1 · https://arxiv.org/html/2607.07774v1
- The arXiv API reports v1 submitted and last updated 8 July 2026 in `cs.CR`; its summary contains no withdrawal or retraction notice. Record, PDF, and HTML endpoints returned HTTP 200; the PDF response reported 769,709 bytes.
- The abstract reports 4,897 tool calls with 7.7% scope violations, drawn from 100 trajectories on tasks engineered to tempt out-of-scope action and labeled by professional penetration testers. It reports Fleiss κ=0.64, an expert-reference F1 of 0.78, eight judge models, five transcript strategies, and cost-sensitive versus recall-first operating points. These are author-stated claims awaiting full-paper verification.
- Structural HTML triage indicates 30 environments, three professional graders, call-level labeling, heterogeneous source agents, and a static-policy-to-full-transcript evidence-view comparison. The paper claims to release the dataset, but no dataset/code URL was exposed in its HTML external links or targeted GitHub/Hugging Face searches. This is a time-bounded unresolved release observation, not proof that no release exists.
- Exact ID/title and scope-gating searches found no local review or queue task. Existing AgentAbstain and authority/action-safety work is adjacent, but does not cross professional call-level labels with monitor evidence views, pre-effect gating, and asymmetric decision loss.

## Why this is a narrow, useful gap

The reusable chain is:

`current user request and engagement authority → task-specific scope interpretation → proposed call target/parameters/context → monitor evidence view → expert label/disagreement/adjudication → threshold and asymmetric loss → accept/reject decision before first effect → attempted/executed action and state delta → prevented or realized consequence → review burden and recovery`.

This directly tests two charter principles. First, authority is contextual: the same operation may be permissible or impermissible depending on the current request, target, and valid scope rather than a global action label. Second, an evaluator's evidence view is part of the instrument. Static policy, user request, summarized history, and raw transcript can alter both observability and cost.

The design also raises sharp validity questions. Engineered temptations may inflate violation prevalence or make labels easier than natural work; tool calls within one trajectory/environment are clustered; grader F1 against an adjudicated label is not an independent professional ceiling; κ and F1 answer different questions; transcript strategies may expose post-hoc or answer-correlated cues; threshold recommendations require explicit false-accept, false-reject, delay, and review losses; proprietary model revisions and token prices can drift; and a correctly rejected proposed call does not by itself establish prevented harm, preserved useful work, safe recovery, or production fitness. Offensive-security labels do not license a cross-domain safety claim.

## Charter decision filter and queue action

- **Objectives advanced:** A (scalable expert evaluation, safety, and production-agent measurement) and B (authority-to-observer-to-gate-to-consequence chain).
- **Concrete evidence:** immutable-v1 full-paper review plus a pinned release audit if artifacts can be located, with reconstruction of sampling, labels, disagreement, evidence views, thresholds, costs, clustering, and result accounting.
- **Uncertainty clarified:** whether ScopeJudge establishes request-conditioned pre-effect scope monitoring under a defined loss policy or mainly judge imitation on engineered, clustered cases and adjudicator conventions.
- **Mode:** narrow expansion. The autonomous source/research/review backlog was empty; the only pending task required human authorization. One bounded review restores evidence flow without repeating broad discovery.
- **Duplication/scope check:** adjacent act/abstain and safety reviews cover other links, but not this crossed expert-label × evidence-view × loss-policy instrument. Reuse existing authority, action-safety, observer, metric, task-health, participation, configured-system, and validity machinery; add no security-specific schema or pilot absent stronger evidence.
- **Useful completion:** reconcile paper/release identity; reproduce or bound all reported denominators and metrics; preserve environment/task/trajectory/grader dependence; distinguish expert agreement, judge agreement, policy conformance, realized prevention, burden, professional validity, production fitness, and readiness.

Added one task: `review-scopejudge-preexecution-gating-validity` (review, priority 57). No second source was queued.

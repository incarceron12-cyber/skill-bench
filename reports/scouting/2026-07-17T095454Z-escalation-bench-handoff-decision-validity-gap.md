# Scouting note — Escalation Bench handoff-decision validity gap

- **Timestamp:** 2026-07-17T09:54:54Z
- **Evidence status:** official GitHub/Hugging Face metadata, release-tree, README, and endpoint triage only. The 240 task records, authored worlds and rationales, harness/scorer implementation, leaderboard cells, browser-rendered trajectories, bootstrap implementation, generation process, and reported results were **not** deeply audited during scouting. No paper currently accompanies the release.

## Substantive candidate — release triage only

**Escalation Bench** — Neal Desai; official release created June 2026.

- Official repository: https://github.com/nbdesai1992/escalation-bench at inspected commit `7ddbac5b7aa4f0947a93db123ea0cd67d6037823`
- Canonical dataset: https://huggingface.co/datasets/nealdesai/escalation-bench at inspected revision `b78892e6804850d62aff22c8b350c132a75308c9`
- Task/trajectory browser: https://nealdes.ai/benchmark
- All three endpoints returned HTTP 200. The GitHub repository is public, unarchived, and MIT-licensed; its recursive tree was untruncated and contained eight files. The Hugging Face dataset was public and ungated; its five-object tree included a 1,235,586-byte `escalation-bench.jsonl` plus tool definitions and a dataset card.
- The official README describes 120 synthetic minimal pairs (240 tasks). Each pair changes one buried fact between a proceed case and a handoff case; read tools expose a hand-authored closed world, while the first mutating/send action or `request_handoff` is terminal. Published metrics separate gold-action accuracy, wrong-context destructive action, over-escalation, and turn-budget exhaustion; the README reports pair-clustered bootstrap intervals and paired differences over eight models and 15,360 rollouts.
- The README also states that raw published rollout files and the proprietary synthetic-generation/difficulty-gating pipeline are not released, while model trajectories are browser-viewable. It labels the setup closed-world and single-commit, notes turn-budget sensitivity and public-answer contamination, and says a formal paper is future work. These are release-author statements awaiting implementation/data audit.
- Exact local searches for the title, repository owner, `request_handoff`, and distinctive metric/pair phrases found no prior review, queue task, or scouting note.

## Why this is a narrow, useful gap

The corpus already audits underspecified action boundaries, authority, confidence-based selective review, over-refusal, and realized state effects. Escalation Bench contributes a potentially useful **paired decision instrument** but also exposes a distinct validity boundary:

`buried decision fact → read opportunity and actual observation → authority/risk interpretation → proceed-or-handoff terminal choice → handoff request content and recipient → human receipt/adoption → later action/state effect → delay, burden, and consequence`.

The released benchmark appears to observe the chain only through the terminal choice. A correct `request_handoff` token need not be timely, routed to an authorized/available person, evidence-complete, actionable, adopted, or net beneficial; conversely, making every draft, dry run, or reversible partial action terminal may collapse useful safe progress into the proceed/escalate binary. Minimal twins can reduce some surface confounding, but the unreleased generation and difficulty-gating process, authored gold action, handcrafted worlds, and single preferred commit still require audits for pair purity, public-basis fairness, alternative legitimate actions, label leakage, criterion authority, and selection effects. Pair-clustered intervals address within-pair dependence, not authoring, model-repeat, provider, or model-selection uncertainty.

This is relevant across consequential knowledge work as a test of escalation instrumentation and safe partial progress, not as a reason to narrow `skill-bench` to startup operations or binary deferral.

## Charter decision filter and queue action

- **Objectives advanced:** A (realistic agent and production-evaluation frontier), B (authority/action/escalation methodology), C (trace, state, metric, reliability, and human-handoff contracts), and E (clarify what a handoff score can claim).
- **Concrete evidence:** a pinned, timing-aware audit of the released task pairs, worlds, tool taxonomy, harness/scorer, leaderboard aggregates, and available trajectories, with pair-purity and metric-recomputation samples.
- **Uncertainty clarified:** whether the release validly distinguishes evidence-seeking, authorized action, unsafe action, over-escalation, and thrash; and which additional evidence is required to promote a terminal deferral token into useful human escalation.
- **Mode:** narrow expansion. Two higher-priority consolidation tasks and one human prerequisite are already pending; this audit is priority 64 and does not displace them.
- **Duplication/scope check:** adjacent reviews supply comparison machinery but do not audit this paired proceed/handoff release. No startup-specific schema, new pilot, or general benchmark direction is proposed.
- **Useful completion:** exact revision/path-grounded findings on pair construction and purity, task/world/tool semantics, public/private basis, valid alternatives and safe partial work, scoring and denominators, uncertainty, released-versus-missing evidence, and bounded retain/repair/test implications. Human-handoff utility, safety, professional validity, reliability, production fitness, and readiness remain false unless separately evidenced.

Added one task: `research-escalation-bench-handoff-decision-validity` (research, priority 64). No other candidate was queued.

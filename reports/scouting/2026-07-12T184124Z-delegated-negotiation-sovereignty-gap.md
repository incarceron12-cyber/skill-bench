# Scouting note — delegated negotiation sovereignty gap

**Timestamp:** 2026-07-12T18:41:24Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Repository inspection found 150 completed tasks, one pending evaluator-observation build, one blocked real-elicitation task, and no pending source/research/review work. Existing reviews cover delegation preference, participant authority, privacy/injection, action boundaries, and professional artifacts, but not trace-level evaluation of whether an agent faithfully represents a user's private utility and disclosure constraints during bargaining.

## Substantive finding (triage only)

**SovereignNegotiation-Bench: Evaluating User-Owned Personal Agents In Delegated Bargaining Under Privacy, Consent, Evidence, And Institutional Pressure**

- Immutable arXiv target: https://arxiv.org/abs/2607.02814v1
- PDF: https://arxiv.org/pdf/2607.02814v1
- arXiv search metadata verifies v1 was submitted 2026-07-02.
- The abstract/search record describes a trace-level, multi-turn benchmark for delegated negotiation under private utilities, disclosure constraints, evidence requirements, and institutional asymmetry. It contrasts symmetric personal-agent scenarios (for example shared-cost or schedule coordination) with bargaining against institution-like counterparties and targets failures including privacy leakage, consent violations, unsupported advocacy, over-concession, failed escalation, and poor auditability.
- Repository-wide duplicate search found no title, benchmark-name, or arXiv-ID match.
- Targeted release search did not identify a verified paper-linked repository. The arXiv record says code/data are intended, while the HTML paper describes an “intended anonymous artifact release” containing scenarios, prompts, outputs, logs, parsed actions, metrics, hashes, recomputation code, blinded audit items, labels, and an externally managed unblinding key. A reviewer must verify whether this artifact is actually available and whether the release matches v1; intended contents are not release evidence.
- This is **metadata/abstract and HTML release-location triage only**. The PDF, appendices, scenarios, policies, private utilities, counterpart models, traces, graders, blinded audit, metrics, statistics, costs, and any artifact were not fully read or inspected. No claim is made that the benchmark establishes real-user consent, professional negotiation ability, privacy safety, bargaining optimality, or deployment readiness.

## Benchmark implication to test

The candidate may expose a nonduplicate authority problem: task success or agreement is not sufficient when an agent must preserve user-owned preferences, evidence standards, disclosure boundaries, escalation rights, and an auditable mandate. A full audit should test whether utilities and constraints are independently authored or synthetic; whether counterpart behavior and institutional asymmetry are controlled; whether consent is real, simulated, or merely prompt-specified; whether leakage, concession, unsupported claims, escalation, and agreement quality are deterministically observable; and whether the same trace can support both user-benefit and safety claims without criterion dependence. The reusable target is a mandate → authorized disclosure/action → negotiation event → concession/evidence/escalation → agreement and user-consequence chain, not a negotiation-specific schema.

## Charter decision filter and queue action

- **Objectives advanced:** A (realistic agent and safety evaluation), B (authority, decision thresholds, and hidden consequences), and C (trace, action, evidence, and validity contracts).
- **Evidence/artifact sought:** immutable full-paper review and any verifiable release audit, with page/file locators and a mandate/disclosure/concession/escalation/outcome crosswalk.
- **Uncertainty clarified:** whether trace-level delegated bargaining can distinguish faithful representation from agreement-seeking, privacy leakage, unsupported advocacy, and over-refusal without relying on simulated-user labels or a single judge.
- **Mode/balance:** narrow expansion; the only ready queue item is building/validation.
- **Duplication/scope:** not a duplicate of JobBench (delegation desire), HAS-Bench (participant-policy realization), ToolPrivacyBench-style information routing, UnderSpecBench (ambiguous operational authority), or generic negotiation scoring. Personal negotiation is a bounded test bed for reusable user-sovereignty machinery, not a domain commitment.
- **Useful completion:** reconstruct task and counterpart generation, utility/constraint provenance, treatment identity, consent realization, trace schema, observer admissibility, metric dependence, uncertainty, release fidelity, and claim ceilings; compare with existing authority, participation, action-safety, artifact-view, metric, and validity machinery and add only nonduplicate implications.

Added `review-sovereign-negotiation-user-mandate-validity` (priority 51). No second task was added.

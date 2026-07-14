# Scouting note — context-to-execution action-authority gap

**Timestamp:** 2026-07-14T20:46:13Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Queue inspection found 225 tasks before this addition: 219 completed, four blocked, and two pending human decisions; no source/research/review task remained. Existing work covers prompt-injection exposure and consequence, underspecified authorization, workspace mutation safety, and outcome-evidence sufficiency, but no local review or queue task evaluates a runtime boundary that separately binds data-field, effect, and invocation authority.

## Substantive finding (triage only)

**Context-to-Execution Integrity for LLM Agents**

- Immutable record selected for review: https://arxiv.org/abs/2607.06000v1
- Immutable PDF: https://arxiv.org/pdf/2607.06000v1
- Immutable HTML: https://arxiv.org/html/2607.06000v1
- The arXiv API identifies Igor Santos-Grueiro as the sole author, category `cs.CR`, and initial submission on 7 July 2026. It reports no later version; the summary contains no withdrawal notice. The versioned abstract, PDF, and HTML returned HTTP 200.
- The **v1 abstract** presents Context-to-Execution Integrity (CXI), an execution-boundary system for agents that consume attacker-writable context. It describes protected sink fields, destination-specific typed releases, opaque data slots, and a deterministic gate requiring field authority, exact-effect authorization, and invocation authority to bind to one action manifest.
- The abstract reports evaluation on open-weight field-projection runs, 720 live AgentDojo episodes with 1,739 LLM calls, 400 code-agent repository episodes, manifest-bound ledger faults, proposal-pressure controls, and hosted/API compatibility traces. It reports 231 safe task completions and zero observed field, effect, or invocation escapes in the code-agent benchmark. These are author-reported abstract claims, not independently verified findings.
- “Zero observed escapes” is not yet a general safety result. Full review must establish the attack and sink population, episode admission and invalids, baseline conditions, parser failures, lease/manifest semantics, whether attempts and realized effects are separately observed, confidence bounds, utility and over-refusal denominators, adaptive or outcome-based exclusions, and what untested field/payload/tool paths remain outside the claim.
- Repository-wide duplicate search found no arXiv-ID, title, execution-integrity, exact-effect, protected-sink, or action-manifest record. AgentDojo appears locally through the Outcome Evidence paper, but there it is an evaluator-observability case; ClawSafety measures exposure, adoption, attempted action, consequence, utility, and recovery. CXI instead proposes a preventative authorization boundary and therefore adds a distinct intervention-to-measurement question.
- Search did not identify an authoritative code/data repository. A review must locate release declarations from the paper itself and must not treat third-party paper indexes as implementation evidence.
- A neighboring candidate, *Beyond Static Leaderboards: Predictive Validity for the Evaluation of LLM Agents* (`2606.19704v1`), was not queued because an earlier scouting note had already verified and explicitly deprioritized it relative to PACE. This run did not repeat that search or reverse the prior decision without new evidence.
- This is **metadata, abstract, URL, and duplicate triage only**. The PDF, HTML body, appendices, methods, prompts, policies, manifests, code, data, traces, tables, and statistical analyses were not read or audited. No claim is made that CXI works as described, prevents prompt injection generally, preserves legitimate task completion, transfers across tools, or establishes professional safety, capability, production fitness, or readiness.

## Benchmark implication to test

Knowledge-work action evaluation needs a typed authority chain: `public request and affected-party authority → source/data trust class → protected sink field and sink-interpreted payload → narrow validated release and destination → exact authorized effect → invocation authority → immutable action manifest/lease → proposed call → deterministic admission outcome → attempted and realized state change → utility, over-refusal, recovery, and consequence`. Content validity, action authorization, and execution admission are related but non-interchangeable.

A full review should test whether CXI's three authority checks are independently falsifiable; whether opaque evidence remains usable without becoming control data; whether manifests bind all semantically relevant effects rather than syntax only; whether leases, retries, and concurrent state invalidate exact-effect assumptions; and whether alternate legitimate workflows survive the gate. Any transfer should extend existing authority, action, workspace, task-health, and trace primitives rather than create a cybersecurity-specific schema from abstract claims.

## Charter decision filter and queue action

- **Objectives advanced:** A (production agent-safety frontier), B (authority-to-action and safety-claim validity), and C (evidence for executable action-boundary checks).
- **Evidence/artifact sought:** immutable-v1 deep review, paper-declared release audit if available, and one replayed manifest/lease fault if inspectable.
- **Uncertainty clarified:** whether field/effect/invocation binding is a reusable benchmark primitive, and what the reported zero-escape result can validly claim.
- **Mode/balance:** one low-priority review task restores a minimal research backlog while empirical building remains blocked on Git authentication; no broad search or source bundle was added.
- **Duplication/scope:** complements ClawSafety, UnderSpecBench, outcome-evidence bounds, and workspace mutation safety; security is a cross-domain action-boundary stress case, not a permanent benchmark scope.
- **Useful completion:** preserve threat model, configured systems, episode/call denominators, baseline, parser/admission/task outcomes, invalids, alternative paths, utility/over-refusal, uncertainty, release identity, and strict claim ceilings.

Added `review-context-execution-integrity-action-authority` (priority 21). No second task was added.

## Operational note

The required initial `git pull --ff-only` could not authenticate to the HTTPS GitHub remote (`could not read Username`). The run proceeded from local `main`. The pre-existing untracked `data/papers/source/` tree was not modified.

# Context-to-Execution Integrity: zero observed gate escapes are evidence about one mediated boundary, not end-to-end agent safety

## One-sentence contribution

Context-to-Execution Integrity (CXI) contributes a precise execution-boundary contract in which **protected field authority, sink-interpreted exact-effect authority, and invocation authority must all bind to the same canonical action manifest before a lease reaches a mediated sink**; its evidence supports conformance of the evaluated gate, policies, adapters, and archived traces, but not complete mediation in an unseen deployment, validator completeness, professional task quality, general prompt-injection safety, or production readiness.

## Why this matters

This review advances charter objectives A, B, and C by examining a domain-neutral boundary between evidence and consequential action. Security is the paper's application, but the transferable benchmark question is broader: when an agent reads a ticket, email, log, document, memory, or another agent's message, which parts may inform reasoning, which narrow values may populate a specific action field, which semantic state transition is authorized, and who or what authorized the event to occur now?

Existing skill-bench work separates malicious-source placement, exposure, adoption, attempted action, realized consequence, and utility. CXI adds a distinct systems insight: even a syntactically valid proposal with apparently legitimate values can be unauthorized along three independent axes. A path extracted from a CI log may be valid for one `file_path` field without authorizing the tool, approval state, patch effect, retry, batch, or delegation event. This is stronger and more operational than treating a whole source, message, or tool call as trusted.

## Sources and reading record

**Immutable primary source read in full**

- Igor Santos-Grueiro, *Context-to-Execution Integrity for LLM Agents*, arXiv:2607.06000v1 (7 July 2026): https://arxiv.org/abs/2607.06000v1
- PDF: https://arxiv.org/pdf/2607.06000v1
- Local PDF: `data/papers/pdfs/2607.06000v1-context-to-execution-integrity.pdf` (20 pages; SHA-256 `c3ca062e8b5eb86252a79a28c3faf9458428dac7e6ebb3fe24904977cc7ea499`)
- Local text: `data/papers/text/2607.06000v1-context-to-execution-integrity.txt` (SHA-256 `5b15734701439bdda8e599906de525d74419552196b87ea702256282a3f7b17c`)
- Date read: 2026-07-14 UTC.

**Declared artifact status**

The paper declares an anonymous artifact at `https://anonymous.4open.science/r/cxi`, with `submission_artifact/` as the entry point and purported policies, schemas, declassifiers, negative tests, gate decisions, backend records, ledger traces, mappings, frozen results, checksums, and regeneration scripts (Open Science, p. 14). The scout's 2026-07-14 request returned HTTP 401; a fresh request during this review returned HTTP 403. No artifact was acquired, inspected, or replayed. All implementation and result claims below are therefore paper claims, not independently reproduced findings.

## Research question and claim boundary

The paper asks how an agent may safely consume attacker-writable context while preventing that context from silently acquiring authority to select, authorize, parameterize, trigger, retry, batch, schedule, or delegate a privileged side effect. Its formal question is narrow: given trusted policy and runtime components, conservative influence provenance, correct field classifications and validators, complete mediation, and matching evidence records, does the gate admit only an action whose protected fields, interpreted effects, and invocation event are authorized for the same manifest (Sections 2.2–3.6, pp. 3–6)?

That is an **admission implication**, not an empirical noninterference theorem: `Admit(m) ⇒ Fields(m) ∧ Effects(m) ∧ Invoke(m)` (Appendix B, p. 18). The paper explicitly excludes task correctness, validator completeness, compromised hosts, unmediated routes, provider-internal observability for hosted APIs, and automatic exactly-once external delivery (pp. 2–3, 5–8, 12–13, 19–20).

The auditable empirical question is narrower still: on the fixed policies, snapshots, adapters, deterministic fault suites, sampled model/backend configurations, live synthetic task banks, and archived API traces reported in v1, were any unauthorized field values, effects, or invocations observed crossing the **mediated** sink boundary?

## Methodology and system

### Threat model and authority objects

The attacker may control or influence issues, documentation, CI logs, tool outputs, retrieval documents, package metadata, persistent memories, or agent messages, but not trusted policy, the explicit objective, model weights, host runtime, or privileged tools. CXI distinguishes trusted state (`T`), writable influence (`W`), destination-scoped typed releases (`D`), opaque data (`O`), and protected sink fields (`X`) (Section 2, pp. 2–3).

The design tracks **influence**, not byte origin. A trusted registry may supply the literal bytes `repo.write_file`, yet if writable text caused the selection, that field remains W-derived. Summaries, repairs, memories, retries, and tool outputs union or preserve prior influences until trusted code issues a destination-scoped release. Unknown, stale, ambiguous, repaired, or unsupported provenance rejects (Section 2.3, p. 3; Appendix Table 9, p. 17).

A total sink policy must classify every active field. Protected fields include tool, operation, target, recipient, namespace, approval, path, CI target, delegation, and any argument capable of changing an external effect. Apparently descriptive payloads—patches, file bodies, shell commands, SQL, CI YAML, package manifests, policy files, configuration, and generated code—are effect-bearing unless an adapter constrains their interpreted effect. Text may enter an opaque comment or evidence slot, but if a downstream bot, renderer, webhook, agent, or workflow can act on it, it re-enters as W (Sections 2.1, 3.2–3.3, pp. 2–4).

### Six-stage admission pipeline

The host, not the model, turns proposals into execution through six ordered steps (Section 3.1, p. 4):

1. canonicalize the candidate into an action manifest;
2. check each protected field against field-local authority and provenance;
3. check sink-interpreted payloads against exact-effect commitments;
4. authorize the invocation with a manifest-bound capability;
5. consume that capability in a linearizable ledger to obtain a lease; and
6. execute only through the mediated sink.

A typed release carries a narrow validated value from W to one declared destination field and binds type, source scope, destination scope, declassifier, validator, provenance, task/action context, policy epoch, and trusted snapshot. It is not ambient trust. An `ApprovalRef` cannot authorize a path; a `FilePath` cannot choose a tool; an opaque quotation cannot satisfy approval (Sections 3.2–3.4, pp. 4–5).

### Exact-effect and invocation authority

For constructive payloads, authorization binds what the sink will semantically do, not merely payload bytes. A repository commitment includes repository/workspace identity, base commit, canonical paths, old/new blobs, modes, symlinks, renames, allowed paths, principal, validator set, adapter revision, policy epoch, and nonce. Mutation or replay against another state changes the manifest digest and rejects (Section 3.5 and Table 2, p. 5).

Invocation authority is independently bound to sink, operation, task/run, sequence, retry budget, batch cardinality, idempotency key, schedule, history, snapshot, epoch, principal, and adapter revision. Exactly one eligible capability is selected unless policy defines deterministic equivalence; the ledger consumes it against the same manifest digest and issues the only lease accepted by the sink (Sections 3.6 and 4.1, pp. 6–7; Appendix B, pp. 17–18).

This separation matters. Field validity does not authorize an event; a call ledger does not authorize a patch; an exact patch effect does not authorize a retry; and an opaque data slot does not remain harmless after downstream reinterpretation.

### Open-weight and hosted/API evidence paths

For open-weight models, the reference target decodes one protected field from a physical field-specific projection containing only T, destination-valid D, and authorized parent records, with fresh prefill/KV state, local grammar, and deterministic host assembly. Serving checks add backend evidence records for field path, projected input, blocked ranges/influence map, output, canonical value, parents, profile, nonce, and manifest (Sections 3.7–4.4, pp. 6–8).

The paper is careful that direct-span, suffix-taint, and runtime-map checks form an evidence ladder; they do not prove full hidden-state or KV-lineage noninterference. Hosted APIs expose neither masks nor cache lineage. Their compatibility path instead constrains a reader/extractor to emit typed facts and opaque handles, then gives protected-field writers only T plus field-valid D. This supports host-visible construction and common-gate compatibility, not provider-internal enforcement (Tables 3–4, pp. 6, 8–9; Table 15, p. 19).

### Configured systems and evaluation surfaces

Four open-weight identities are reported: Qwen3.6-27B, Gemma-3-27B-IT, GPT-OSS-120B, and Qwen3-Coder-30B-A3B-Instruct. Runs use vLLM, temperature 0, 64 generated tokens, H100 80GB hosts, CUDA 12.8, PyTorch 2.11.0+cu128, and a precompiled vLLM development build. Four archived hosted/API identifiers are GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, and Gemini 3.5 Flash, with provider-specific structured-output settings, retries, and timeouts (Section 5.1, pp. 8–9; Table 14, p. 19). Hosted aliases may not identify immutable provider revisions.

The evaluation deliberately uses heterogeneous units and says they must not be averaged (Table 6, pp. 9–10): live AgentDojo episodes and LLM calls; exact-effect field records, leases, and effects; code-agent repository episodes; deterministic ledger consumes; archived hosted/API rows; proposal-pressure actions; offline mappings; workflow boundary steps; validator tests; and policy-surface findings.

## Evidence and results

### Main denominators

The paper reports (Section 5 and Tables 6, 16, pp. 9–12, 20):

- **AgentDojo live task bank:** 720 episodes, 1,739 LLM calls, 199 safe task completions (STC), 306 protected-field records, 204 leases, and 204 exact-effect authorizations in the exact-effect subset; zero observed field/effect/invocation escapes in protected admissions.
- **Code-agent exact-effect benchmark:** 400 repository episodes, 231 STC, zero observed field/effect/invocation escapes; the 169 non-STC rows split into 73 parse failures, 61 parse-valid rows without effect authorization, and 35 authorized/executed task-quality failures.
- **Manifest-bound ledger:** 10 cases and 29 consume attempts, including 19 rejects and two deduplicated retries, with no duplicate admissions or applications under the declared idempotent-adapter contract.
- **Hosted/API compatibility:** 800 archived rows, 85 unsafe selections blocked, zero parse failures, and zero observed gate escapes.
- **Proposal pressure:** 196/300 unauthorized field proposals in one utility-adversarial setting, 407/522 in stress rows, 85/400 in hosted/API adversarial rows, and 45 unauthorized field plus 16 unauthorized invocation proposals among 240 open-weight free-form actions; none reportedly reached execution.

The parser/authorization/task-quality split is a major strength. Parse failure is not counted as safe completion; authorization rejection is not agent success; an authorized execution that misses the task oracle is not an authority escape. However, the paper does not report task-clustered confidence intervals, repeated-run reliability, per-model task outcomes, invalid/missing-run inventories, or inferential uncertainty. “Zero observed” is a sample result conditional on the exercised fault families and observer.

### Baselines and mechanism witnesses

The 192-case schema baseline illustrates the claimed granularity. Raw co-resident context and schema-only structured output both retain unauthorized execution at 1.000; CXI reports W-derived protected fields and unauthorized execution at 0.000 while benign admission is 1.000 (Section 5.5, p. 11). Mechanism-level 20-attack/6-utility controls show partial defenses leave different gaps: argument-role provenance rejects 12/20 attacks, field-scoped capabilities without a call ledger reject 10/20, and typed reader/writer plus call ledger without a field gate reject 8/20; CXI rejects 20/20 and preserves 6/6 utility cases. These are fixed witnesses, not implementation comparisons against cited systems or prevalence estimates.

Focused deterministic suites test wrong-domain authority, cross-field release reuse, digest and context mismatch, optional branches, alternate sinks, retries, batch/schedule/order/idempotency, ambiguous capabilities, parser/canonicalizer/resolver effects, evidence substitution, and manifest replay. This is useful falsification coverage, but without the declared artifact it cannot be independently inspected, mutation-tested, or replayed.

### Utility, task quality, and policy effort

CXI reports 100 workflows and 270 boundary steps across code, Web/RAG, productivity, operations, and memory with no observed false blocks. This is **boundary utility**, not end-to-end task utility (Section 5.7, p. 12). In a separate 40-task final-state audit, all cross the boundary, 29 pass task-level assertions outright, and the remaining 11 require review; the paper reports 184/195 assertion passes. No human baseline, over-refusal distribution by model, alternative-legitimate-path test, or uncertainty is supplied.

The open-weight median mask-construction overhead is reported as roughly 0.16 ms per case (0.04 ms per protected field), excluding model-dominant execution/loading and worker VRAM. Hosted request latency ranges are roughly 9.3–15.3 seconds for AgentDojo and 10.7–14.0 seconds for ToolEmu. A policy audit spans 24 sinks, 149 fields, 85 protected fields, 20 typed-release fields, 29 opaque fields, 19 effect-bearing payloads, and 141 validator tests. The first pass finds 18 material policy issues before regeneration (Section 5.8, p. 12). That finding is important evidence against interpreting a sound gate as self-configuring safety: policy authoring is a substantial, fallible intervention.

## Unique insight

CXI's unique transferable insight is a **three-authority join at execution**:

1. **selection authority:** why each protected semantic field has its chosen value for this destination;
2. **effect authority:** why the exact sink-interpreted state transition is authorized under this principal, snapshot, adapter, validator set, and policy epoch; and
3. **event authority:** why this call, retry, batch, schedule, delegation, or budget spend may occur now.

All three must join on one immutable manifest before execution. This resolves an ambiguity in ordinary provenance ledgers: source authority, value validity, effect approval, and permission to invoke are related but non-substitutable. A document may be authoritative evidence about a defect yet lack action authority; a typed extraction may authorize a path but not a patch; a valid patch may lack permission to execute; a valid first execution may not authorize a retry.

For benchmark design, this means the action ledger should not stop at `attempted_action → environment_decision → realized_effect`. It should preserve an **admission witness** for each protected field, each interpreted effect, and the invocation event, plus the canonical binding among them. Conversely, a benchmark must not infer professional correctness from gate acceptance. CXI can establish “the executed effect matched what this validator authorized” while the validator, public mandate, domain judgment, or task objective is wrong.

## Comparison with adjacent reviewed evidence

- **ClawSafety** follows source placement → exposure → adoption → attempt → realization → recovery → utility. CXI operates mainly between proposal and realization: it assumes unsafe proposals persist and checks whether authority closes at the sink. The two are complementary. CXI's zero mediated escapes does not establish low attack exposure or benign utility; ClawSafety's binary ASR lacks CXI's field/effect/event authority decomposition.
- **UnderSpecBench** separates private intent, public authorization, resolvable uncertainty, legitimate terminal actions, attempt, effect, and observer coverage. CXI assumes trusted policy/objective/approval state are correct; it does not decide whether acting was publicly justified or whether clarification was professionally required. A benchmark needs both an authorization-state validity argument and execution-boundary conformance.
- **Outcome-evidence bounds** asks whether retained artifacts decide a native outcome. CXI records gate decisions and mediated effects, but zero escape still requires evidence that all relevant routes were mediated and the observer could see violations. Missing bypass coverage is not evidence of non-effect.
- **Workspace mutation safety** treats unauthorized collateral state and cleanup as benchmark outcomes. CXI can enforce an authorized exact delta if validators describe it, but validator incompleteness or an omitted helper route can leave collateral effects outside its claim. Mutation predicates and admission predicates therefore remain separate.

Existing action-safety, authority lineage, task projection, trace, artifact/state, task-health, metric, and validity contracts are the correct homes. A CXI-specific schema would duplicate machinery.

## Limitations and validity threats

1. **Artifact unavailable.** The declared anonymous release returned HTTP 401 and then 403. Policies, schemas, records, traces, checksums, aggregation scripts, and fault cases could not be inspected or replayed.
2. **Single-author, unaudited implementation.** The same author defines the threat model, system, policies, fault suites, validators, accounting, and claims. No independent security review, red-team protocol, code audit, or external replication is reported.
3. **Conditional guarantee.** Complete mediation, conservative provenance, correct classification, correct policy, validator soundness, trusted host/runtime/tools, and matching evidence records are assumptions. The gate cannot detect a route or effect omitted from its model.
4. **Zero observed is not zero risk.** Deterministic cases and sampled runs cover enumerated faults. No statistical upper bound, adaptive adversary, held-out exploit family, mutation score, coverage criterion, or false-negative audit supports a broad escape-rate claim.
5. **Heterogeneous denominators.** Episodes, calls, fields, leases, effects, consume attempts, proposal rows, archived API rows, and assertion checks answer different questions. The paper properly avoids averaging them, but the abstract's compact zero-escape framing can still invite denominator collapse.
6. **Limited uncertainty and repetition evidence.** No repeated task-level runs, task-clustered intervals, per-model variance, run inventory, or missing/invalid policy is reported. Temperature zero does not remove service, model, or environment variation.
7. **Hosted/API ceiling.** Field-local writer visibility supports host-side construction compatibility, not provider-internal attention, mask, cache-lineage, or snapshot claims. Mutable aliases weaken exact configured-system identity.
8. **Open-weight evidence is tiered.** Direct-span, suffix-taint, and runtime-map exclusion are declared-atom checks, not complete transformer noninterference. Unsupported optimized paths must fail closed, but paper-only evidence cannot verify that every path does.
9. **Validator validity is external.** Exact-effect binding proves equality to a validator-approved effect, not that the validator's allowed set is complete, professionally correct, safe, fair, or robust to semantically equivalent paths.
10. **Policy authoring is a treatment and failure source.** Eighteen initial policy findings demonstrate that field classes, release scopes, opaque slots, reentry, effect payloads, and bypass paths are easy to specify incorrectly. Independently authored policy reliability is not measured.
11. **Utility evidence is narrow.** Zero false blocks over 270 designed boundary steps does not estimate over-refusal or useful completion in a representative work population. GPT-OSS declines all 20 benign calls in one policy-aware free-form condition, showing that availability can degrade even with a sound gate.
12. **Task validity is synthetic and weakly grounded.** Public benchmarks, synthetic action-selection cases, sandboxed repositories, and archived traces test mechanisms; no domain-expert authoring, occupational sampling, professional acceptance, user burden, or deployment outcome is established.
13. **Exactly-once is conditional.** Ledger results show duplicate suppression under a declared idempotent-adapter contract, not exactly-once external delivery across distributed failures, provider retries, or non-transactional services.
14. **No comparative effectiveness claim.** Partial mechanism baselines are deliberately simplified; they are not matched implementations of PACT, CaMeL, FIDES/PFI, ARGUS, AIRGuard, or FORGE.
15. **Cost boundary is incomplete.** Latency and mask overhead omit policy engineering, validator creation, security review, adapter maintenance, evidence storage, false-block adjudication, and ongoing coverage audits.

## Reproducibility and operational realism

The paper is unusually explicit about objects, assumptions, machine setup, model identifiers, evidence regimes, denominators, claim exclusions, and a purported artifact regeneration path. The formal and tabular specification is sufficient to understand the intended implementation and to design independent conformance tests.

Actual reproducibility is currently blocked by artifact access. No local code, manifest, policy, trace, result row, or regeneration script was available. Hosted provider identities may be aliases; the open-weight stack uses a development vLLM build; no immutable container, dependency lock, run inventory, or external audit is available here. Operational realism is bounded to sandboxed repositories, synthetic selections, public benchmark tasks, deterministic fault injection, and archived API traces without production accounts or services. That is appropriate for safe mechanism testing, but it licenses only evaluated-boundary evidence.

## Transfer to skill-bench

1. **Add the three-authority join to existing action records.** For every proposed consequential operation, preserve protected-field path/value, authority source/release and scope; sink-parsed effect commitment and snapshot; invocation capability, sequence/budget/expiry; canonical manifest digest; gate decision; lease; and realized effect receipt.
2. **Distinguish evidence, value, effect, and event authority.** A source can justify a claim without selecting an action. A validated value can fill one field without approving the effect. An approved effect can still lack permission to execute or retry.
3. **Require total field classification and reentry analysis.** Unknown fields fail closed. Apparently inert comments, descriptions, generated files, memories, and handoffs need downstream-consumer analysis; if another component can interpret them into action, they re-enter as untrusted context.
4. **Bind checks to semantic state, not spelling.** For patches, spreadsheets, SQL, messages, workflow updates, and professional artifacts, authorize/grade the canonical interpreted delta under a pinned engine, principal, snapshot, and policy—not merely exact bytes or one reference path.
5. **Test complete mediation with bypass canaries.** Direct APIs, helper functions, alternate clients, generated files, retries, batches, bots, delegation, package hooks, and background workflows must either reach the same gate or be declared outside the claim.
6. **Keep admission, utility, and task quality separate.** Report parse state, proposal pressure, field/effect/invocation authorization, gate decision, environment validity, realized state, accepted alternative, task quality, over-refusal, and professional validity as distinct outcomes.
7. **Treat zero escapes as evidence-supported only with observer closure.** State the exact denominator, exercised fault classes, sink coverage, evidence-view completeness, and unknowns. Never promote zero observed gate escapes into a universal safety or capability claim.
8. **Falsify policy and validator contracts.** Plant wrong-field releases, stale snapshots, post-validation mutations, equivalent legitimate effects, unauthorized collateral changes, retry/replay faults, omitted helper paths, and insufficient observer views. Preserve defects and revisions through task-health lineage.
9. **Use matched authorization-state controls.** Pair cases where execution is authorized, workspace inspection resolves scope, clarification is required, safe alternatives exist, and refusal is excessive. This prevents a conservative gate or non-calling model from looking capable merely because nothing harmful executes.

## Concrete repository actions

1. **No new build task.** Existing action-safety, authority-lineage, trace, artifact/state, task-health, metric, and validity machinery can host the fields above. A new CXI subsystem would duplicate the repository and narrow a general boundary to one security mechanism.
2. **Update the topic and synthesis indexes.** CXI materially adds field/effect/invocation authority binding and the distinction between mediated-gate conformance and realized safety; it belongs in the safety/integrity group at Tier B, with the unavailable artifact and conditional assumptions explicit.
3. **Refine the next action-safety execution slice rather than queueing another contract.** Add manifest-mismatch, wrong-field release, unauthorized retry, post-validation mutation, bypass-path, and accepted-alternative cases to the existing synthetic conformance approach; require admission evidence and realized-state evidence independently.
4. **Do not import zero-escape counts as calibration targets.** Until the declared artifact is accessible and independently audited, treat all numerical results as paper-reported mechanism evidence. Even after replay, they would calibrate only those fixed fault suites and configured paths.

## Assessment

- **Evidence tier:** full immutable paper; declared artifact unavailable and not inspected.
- **Most reusable contribution:** the manifest-bound join of protected-field, exact-effect, and invocation authority before a mediated sink receives a lease.
- **Most important empirical strength:** separate accounting for proposal, parser, authorization, lease/effect, task-quality, and utility outcomes across explicitly different denominators.
- **Most serious validity risk:** the guarantee depends on complete mediation, conservative provenance, correct policies, and complete validators—the very properties that are difficult to establish and were not independently inspectable.
- **Claim skill-bench may safely make:** action-safety evaluation should bind field selection, interpreted effect, and invocation event to one versioned action manifest and should treat gate conformance, realized consequence, useful completion, professional validity, and deployment readiness as separate claims.
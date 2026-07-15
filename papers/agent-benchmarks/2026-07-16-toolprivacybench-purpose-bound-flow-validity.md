# ToolPrivacyBench: executed field–tool auditing is valuable, but an authored necessity matrix is not yet purpose authority

**Source type:** Deep review of the complete immutable arXiv v1 paper plus timing-aware audit of the exact paper-associated placeholder repository  
**Paper:** Shijing Hu, Liang Liu, Zhu Meng, and Zhicheng Zhao, *ToolPrivacyBench: Benchmarking Purpose-Bound Privacy in Tool-Using LLM Agents*  
**Immutable paper:** https://arxiv.org/abs/2606.28061v1  
**Local PDF:** `data/papers/pdfs/2606.28061v1-toolprivacybench.pdf` (24 pages; SHA-256 `0343acedfef16811d03f0e9e4f9a12073a2f8fb1d59c3343ad007d00a0521c9a`)  
**Local text:** `data/papers/text/2606.28061v1-toolprivacybench.txt` (SHA-256 `f84b766b989c26f4102e74b1c9b41954f0582659fcf1df994af88582027995b0`)  
**Official repository:** https://github.com/HuShijing123/ToolPrivacyBench  
**Pinned snapshot:** commit `51d13355a8cb78d80c45b756dd347e94c40327e6`, tree `646b58af4a791aead01d1d3f476fe81157e91940`; provenance: `data/sources/releases/2606.28061v1-toolprivacybench/provenance.json`  
**Date read:** 2026-07-16 UTC

> **Evidence and timing boundary.** The complete immutable 24-page v1 paper, including appendices and references, was read. The pinned author-owned repository commit is approximately 20 hours after v1 publication and contains only a 479-byte README saying that code, data, evaluation scripts, and documentation will be released later. It has no repository-level license. The snapshot verifies placeholder status only: no case, policy graph, tool schema, backend, prompt, trajectory, detector, scorer, annotation record, or result row was available to inspect or execute. All benchmark mechanics and empirical values below are therefore manuscript-reported, not release-reproduced.

## One-sentence contribution

ToolPrivacyBench contributes a useful trajectory-level instrument that joins current-task private atoms, purpose-labeled tools and sinks, field–tool authorization labels, executed arguments, and mock-backend logs so useful completion can be separated from over-disclosure; but its unavailable corpus and implementation, weakly grounded purpose oracle, unvalidated disclosure detector, single apparent run per case, and opportunity-sensitive composite metrics support only agreement with an authored closed-world necessity matrix—not privacy compliance, professional validity, incident risk, safety, or readiness.

## Why this matters for skill-bench

This review advances charter objectives A, B, and C through a cross-domain measurement question:

> When knowledge work legitimately requires private information at one stage, what evidence shows that later tools, artifacts, recipients, and handoffs received only the information authorized for their specific purpose?

The benchmark addresses a real gap between answer-only privacy judgment and executed agent evaluation. A clinically relevant fact may be necessary for a medical record but excessive in billing; an API key may be needed for rotation but not for a handoff; family income may be needed for eligibility computation but not for a status notification. ToolPrivacyBench makes the **same atom’s changing destination-specific status** explicit and audits intermediate tool arguments that a final response cannot reveal (Sections 1 and 3–4, pp. 1–8).

Its strongest transfer is narrower than its framing. A field–tool matrix can operationalize one versioned policy for a controlled conformance test. It cannot establish that the tool’s stated purpose is legitimate, that the field is truly necessary, that the recipient may receive it, that a derived/sanitized representation would suffice, or that a detected match caused a new disclosure. Those are separate authority, transformation, observer, and consequence warrants.

This is a privacy case but not a privacy-only scope commitment. The same machinery applies to client confidentiality, research embargoes, personnel records, legal privilege, trade secrets, regulated filings, internal approvals, and any handoff where evidence may be used locally but not propagated wholesale.

## Research question and claim boundary

The paper asks whether nine tool-using LLM agents complete multi-step business workflows while routing current-task private atoms only to tools and sinks that need them, and where over-disclosure concentrates by field, tool, sink, free-text slot, and workflow transition (Sections 3 and 6, pp. 4–14).

The strongest defensible claim is:

> Under the authors’ unreleased case policies, mock-tool environment, disclosure detector, and aggregation rules, the reported experiment compares one apparent trajectory per model–case cell against binary field–tool labels for 1,150 synthetic and 1,000 adapted workflows, and reports that high authored workflow utility coexists with detector-identified forbidden atom occurrences in intermediate calls and backend records.

The evidence does **not** establish:

- that benchmark authors or annotators had authority to define necessity, recipient entitlement, legal basis, consent, retention, or organizational purpose in the represented domains;
- that the policy knowledge base is complete, internally faithful to the binary matrix, or valid for realistic alternative workflows;
- that exact/alias/semantic-variant matching accurately detects disclosure in structured and free-text arguments;
- that an atom’s later occurrence came from an earlier persisted sink rather than the original task context;
- that tool invocation and required-argument presence establish correct, accepted, or professionally useful state;
- that the nine rows isolate foundation-model behavior from prompt, wrapper, endpoint, retry, and run-time configuration;
- repeatability, expected leakage probability, uncertainty, cost, or reliability;
- prevalence, severity, harm, privacy-law compliance, professional capability, production fitness, safety, or readiness.

## Methodology and system

### Construct: purpose-bound over-disclosure

A case is represented as `(x, T, P, A)`: user task, tools, current-task private atoms, and a binary field–tool authorization matrix. Each tool has a name, stated purpose, schema, and sink; each private atom has type, canonical value, aliases, and severity. A disclosure is counted when detector `D` finds atom `p_j` in the arguments of called tool `t_i` and `A[j,i] = 0` (Section 3, pp. 4–5).

This is an important correction to global sensitivity labels. “Private” does not mean “never use.” The benchmark can distinguish an authorized identifier sent to verification from the same identifier copied into a low-privilege handoff. It also treats tickets, notifications, comments, notes, summaries, and handoffs as sinks rather than assuming only explicit API fields matter (Sections 3.3–3.6 and 4.5–4.6, pp. 4–8).

But the construct merges several questions into one binary cell:

1. Is the atom legitimate evidence for this task?
2. Is the tool’s declared purpose itself authorized?
3. Is the atom necessary, merely useful, optional, or replaceable by a derived form?
4. May this tool process it under the relevant principal, consent, policy, and valid time?
5. Which human, service, store, or downstream audience is the actual recipient?
6. May the tool retain, forward, transform, or expose it after the call?

Figure 2 mentions `CONDITIONAL`, but the formal matrix, reliability protocol, metrics, and Algorithm 1 are binary authorized/forbidden (pp. 5, 12–13). Real ambiguity is therefore removed, adjudicated into one label, or filtered out. A deterministic matrix is useful after authority is established; it does not create that authority.

### Dataset composition and adaptation lineage

The paper reports 2,150 cases and 219,986 private-atom–tool pairs (Table 5, p. 12):

- **Need-to-Know:** 1,150 internally constructed cases, 23 domains, 552 reported tools, 8,050 atom instances, 45,170 authorized and 34,870 forbidden pairs, with six tools and seven atoms per case on average.
- **Public-derived:** 1,000 adaptations across 16 domains, 258 reported tools, 12,767 atom instances, 44,472 authorized and 95,474 forbidden pairs, with 8.89 tools and 12.77 atoms per case on average.

The public split retains 443 BFCL, 377 AppWorld, 170 τ-bench, and 10 API-Bank cases. Admission requires at least four source tool calls, two distinct tools, four sensitive atoms, two free-text-capable tools, and twenty forbidden opportunities. Source task text, API arguments, schemas, and gold arguments are used to extract atoms and annotate relations; free-text sinks and mock audit rules are then added (Section 6.1, pp. 11–12).

This is **workflow-backbone adaptation**, not inherited validity. Filtering on long gold tool chains and abundant forbidden opportunities selects verifier-compatible, privacy-dense cases rather than a representative sample of the source suites or work. Added atoms, sinks, purposes, schemas, backend behavior, and expected disclosures can materially change what a task measures. The 10-case API-Bank contribution and source imbalance further show that “public-derived” is not one homogeneous population. No source task IDs, transformation diffs, rejected-candidate inventory, source-license analysis, or equivalence dispositions are released.

The synthetic construction appendix names domain selection, workflow-template design, tool-schema construction, private-atom generation, authorization annotation, filtering/validation, and representative manual review (Appendix A, pp. 20–21). It reports no template count, candidate count, generator identity, author qualifications, domain-source lineage, rejection distribution, per-domain review, or recipient/affected-party validation. Twenty-three labels broaden surface coverage; they do not establish realistic workflow frequency, purpose authority, or professional consequence.

### Annotation and policy authority

Authorization is assigned tool-purpose-first: an atom is authorized only when necessary for the stated receiving purpose; ambiguous cases follow a minimal-disclosure convention that limits tickets and handoffs to status, routing, priority, and next-step information (Section 6.2, pp. 12–13).

A stratified sample of 215 cases and 21,994 pairs was independently re-annotated by two annotators. The paper reports 93.1% raw agreement, Cohen’s κ = .86, and 499 post-adjudication changes; it correctly says this is sampled reliability, not full independent re-annotation (Table 6, p. 13). This is meaningful evidence that two people could often apply the shared binary guideline.

It is not criterion validity. The paper does not report annotator identity, expertise, institutional role, recruitment, training, blind conditions, guideline text, pair-sampling probabilities, disagreement categories, adjudicator identity, or whether agreement is between two fresh labels or against an original label. More importantly, agreement under a shared authored rule does not establish organizational need, data-subject consent, legal purpose, least-privilege policy, recipient entitlement, or acceptability to downstream professionals. Filtering “unclear” boundaries can inflate reliability while removing the cases where judgment is most consequential.

### Execution and observer coverage

Agents run through an OpenClaw wrapper, plugin, Python bridge, and mock business backends. The backend records arguments actually received and persisted; the evaluator compares those logs with expected stages, required authorized facts, atoms, tool purposes, sinks, free-text slots, and authorization labels (Sections 4.6–4.8 and 6.4–6.5, pp. 8, 13–14).

This is stronger than scoring only final prose. It gives the benchmark a sink-side witness for selected calls and can expose private content in intermediate fields. Yet “complete trajectory” and “true inputs” are assumed, not release-audited. There is no inspectable adapter contract, pre/post state schema, transaction ID, failed-call policy, truncation rule, asynchronous effect, nested payload rule, recipient mapping, audit-log completeness test, or reset attestation. The paper trusts the wrapper, backends, policy KB, detector, reasoner, and metrics (Section 3.7, p. 6) but reports no fault injection or differential observer test.

Tool occurrence is not equivalent to new disclosure. If the full private task remains in model context, an atom can be independently regenerated in several later calls. Backend recurrence shows repeated transmission, not that an earlier ticket caused downstream propagation. The path analysis’s `FirstLeakStep`, `LeakPropagationDepth`, and `RiskyTransitionRate` are useful temporal diagnostics, but causal language such as “propagate” or “diffuse” needs source-use evidence, controlled removal, or an information lineage token (Section 7.5, pp. 17–18).

### Disclosure detector

The detector uses exact, alias, normalized-string, and case-specified semantic variants over structured and free-text fields (Section 3.5, p. 5; Appendix D.1, p. 21). This can be precise for fabricated identifiers and enumerated aliases. It is much less secure for paraphrase, implication, partial reference, transformed values, shared substrings, summaries, and sanitized consequences.

The detector is the observation bottleneck for every privacy metric, yet no labeled evaluation set, sample size, precision, recall, false-positive/negative table, category breakdown, annotator protocol, threshold, or uncertainty is reported. Appendix D.1 explicitly says there is no single detector-quality number and only says “representative high-severity trajectories” are manually inspected. Multi-granularity reporting preserves where a detector fired; it cannot validate whether the firing is correct. Consequently, all leakage rates remain detector-relative.

### Utility and privacy metrics

Utility has three components: task outcome, expected-stage coverage, and delivery of required authorized atom–tool pairs. Their geometric mean is `TaskSuccess`, intended to prevent refusal or under-execution from looking private (Section 5.1, pp. 9–10). Keeping utility separate is correct.

However, `S_task` is only described by examples; no state predicate, judge, or acceptance contract is specified. `S_workflow` is set coverage over expected tools/stages, not dependency order, successful semantics, alternative route, collateral state, recipient use, or professional acceptance. `S_fact` rewards required atom delivery but can inherit the same authored necessity circularity. Tables rename this component “Gold Arg.” No release allows these mappings to be checked.

The paper then reports:

- `FOR`: detector hits divided by forbidden atom opportunities over **executed calls**;
- `SWLR`: the same ratio weighted by atom severity;
- `ToolFOR`: equal mean of per-invoked-tool ratios with forbidden opportunities;
- `LTCR`: fraction of calls containing at least one forbidden atom;
- `FreeTextFOR` and `FTSlotRate`: atom-opportunity and non-empty-slot views;
- `MidFOR`: forbidden-opportunity rate over intermediate calls;
- `MT-POI`: equal-weight average of FOR, SWLR, ToolFOR, FreeTextFOR, and MidFOR;
- `SMTC`: `TaskSuccess × (1 − MT-POI/100)` (Section 5, pp. 9–12).

The plural diagnostics are useful, but the denominators and composites create validity risks:

1. FOR’s denominator is call-conditioned. Extra clean calls to a tool add forbidden opportunities and can dilute the rate; omitted calls remove opportunities. TaskSuccess catches some under-execution but does not make FOR invariant to redundant calls or alternative valid paths.
2. FreeTextFOR’s displayed denominator is all forbidden opportunities in the executed trajectory, not only free-text-capable slots. It therefore changes with structured-call composition; FTSlotRate uses a different non-empty-slot denominator.
3. ToolFOR gives each invoked eligible tool equal weight regardless of calls, opportunities, recipient population, or consequence.
4. SWLR’s atom weights and authority are not specified. Figure 2 describes receiver risk too, while the formal equation contains only atom weight `w_j` (pp. 5, 10).
5. MT-POI averages heavily overlapping transforms of the same detector events. Equal weights do not create five independent dimensions, and the resulting scalar can double-count call/sink composition.
6. SMTC imposes full linear compensation between one authored utility aggregate and one correlated privacy aggregate without a stakeholder loss model or acceptance gate.
7. Appendix D.2 checks only three hand-chosen weight alternatives and model-rank Spearman correlation. Rank stability under nearby policies does not validate the construct, thresholds, or decisions.

A safer report keeps case-level utility, forbidden transmission events, recipient/purpose/severity, and opportunity denominators primary. Any scalar must state the stakeholder and decision loss it serves.

### Configured systems and trial design

Nine named agents are evaluated: GPT-5.5, Claude Opus 4.7, DeepSeek V4 Flash, Kimi K2.5, GLM 5.1, Qwen3.6-plus, Gemini 3.5 Flash, Doubao Seed 2.0 Lite, and MiniMax M2.7. The paper says all share the same cases, schemas, environment, and scorer (Section 6.3, p. 13).

That is not a complete configured-system identity. It omits exact endpoint/snapshot IDs, run dates, OpenClaw version and commit, system and task prompts, tool descriptions, context policy, decoding parameters, seed, maximum steps, timeout, retries, malformed-call handling, provider failures, invalid/missing-run policy, token usage, latency, and cost. Algorithm 1 executes each model–case pair once; no repeat count or stochastic aggregation is described. The tables therefore appear to contain one trajectory per cell. “Mainly reflect model behavior” is too strong when wrapper and provider settings are unreported and no within-cell variation is measured.

## Evidence and results

On the public-derived split, reported TaskSuccess ranges from 76.30 to 94.72 and MT-POI from 15.81 to 22.56. On the synthetic split, TaskSuccess ranges from 92.23 to 97.70 while MT-POI ranges from 19.19 to 28.04 and FreeTextFOR from 27.16 to 46.76 (Tables 7–8, pp. 15–16). These values support the manuscript-level observation that the authors’ utility and leakage instruments rank systems differently on the fixed corpus.

The most useful diagnostics are structural:

- tickets report aggregate FOR 51.43, handoffs 34.79, and comments/notes 33.42;
- more than 80% of non-empty `message`, `description`, and `work_notes` slots reportedly contain at least one forbidden atom, under FTSlotRate;
- `record → ticket` is associated with 37.27% of reported first-leak events and a 96.89% risky-transition rate;
- the three GPT-5.5 cases show broad context being copied into healthcare handoffs, tax notifications/handoffs, and code-security documents/handoffs after narrower local use (Sections 7.3–8.4, pp. 16–19).

These are plausible failure signatures for benchmark authoring: **purpose-specific view collapse**, **progressive restatement**, and **free-text amplification**. They are not independently auditable frequencies. Sink comparisons mix different schemas, opportunity counts, task families, field types, and necessity policies. The three qualitative cases are selected without a coding or negative-case protocol. Domain means are equal-weight means across nine configured agents, not domain incidence or system risk.

No confidence interval, paired uncertainty, cluster bootstrap, model-by-template interaction, repeat disagreement, invalid-run denominator, detector uncertainty, annotation uncertainty, or multiplicity treatment accompanies the headline differences. The paper appropriately says the benchmark is a controlled audit rather than production incident measurement (Section 9, p. 20). The same caution must apply to model rankings and sink percentages.

## Unique insight

> **Purpose-bound privacy is a policy-qualified flow event, not a property of an atom and not merely a matrix lookup.**

The transferable evaluation object is:

```text
atom/source/subject
→ task-time availability and legitimate evidence use
→ purpose and authorized principal
→ minimum sufficient representation
→ intended tool and actual recipient/sink
→ attempted payload
→ gate decision and received payload
→ storage/visibility/forwarding state
→ downstream adoption or retransmission
→ utility, burden, severity, reversibility, and affected-party consequence
```

ToolPrivacyBench observes an important middle slice: authored atom–tool policy, attempted/received arguments, and selected workflow utility. It largely assumes the earlier authority links and does not measure later recipient/consequence links.

This yields four distinctions that should remain explicit in `skill-bench`:

1. **Necessity label vs authority.** Two annotators can agree that a field seems unnecessary while lacking standing to define organizational purpose, consent, legal basis, or recipient rights.
2. **Raw atom vs sufficient representation.** A downstream tool may need an operational consequence (“high priority,” “verification passed,” “rotation complete”) without needing the raw medical, financial, family, or secret-bearing rationale.
3. **Transmission recurrence vs causal propagation.** Repeated matches across calls show repeated exposure; they do not prove one sink supplied the next occurrence when the original task remains in context.
4. **Opportunity-normalized conformance vs risk.** A detector hit divided by authored forbidden opportunities can compare behavior under one instrument. Risk additionally requires recipient, persistence, severity authority, reversibility, affected parties, and loss.

### Comparison with adjacent reviewed evidence

- **PiSAs/contextual integrity:** PiSAs separates task appropriateness from recipient visibility and tracks surface substitution across messages and memory. ToolPrivacyBench adds purpose-labeled executable tool/sink arguments and much larger reported case coverage, but collapses appropriateness and recipient authorization back into one binary field–tool cell and does not audit context/memory surfaces. Together they require `atom × purpose × recipient × representation × surface × time`, not a tool name alone.
- **GroundEval:** GroundEval shows deterministic path checks are only as valid as their authored contract and observer. ToolPrivacyBench has the same boundary: a reproducible matrix lookup would not establish necessity, alternate-path completeness, detector accuracy, or professional legitimacy. Its call-conditioned denominators also need explicit opportunity semantics.
- **EntCollabBench:** EntCollabBench separates role-scoped tool capability, handoff utility, delegated authority, and authoritative effect. ToolPrivacyBench’s “handoff” and “low-privilege team channel” are sink categories, not demonstrated recipients, mandates, access policies, or downstream visibility. A tool-purpose label does not establish organizational entitlement.
- **SovereignPA-Bench:** SovereignPA-Bench warns that an author’s hidden policy oracle does not inherit represented-user authority. ToolPrivacyBench’s sampled annotation reliability is stronger, but still lacks data-subject, policy-owner, domain-professional, and affected-recipient validation.
- **ClawSafety:** ClawSafety distinguishes source exposure, adoption, attempted action, realization, severity, recovery, and benign utility. ToolPrivacyBench usefully addresses benign over-disclosure rather than adversarial injection and records received arguments, but it stops before actual recipient harm, recovery, or production risk.

## Limitations and validity threats

1. The dataset, implementation, trajectories, detector, annotations, and results are unavailable; the official snapshot is only a post-v1 placeholder.
2. No license is present in the pinned repository, so future reuse terms are currently unknown.
3. The policy knowledge base and its matrix projection cannot be inspected for consistency, completeness, conditional rules, or provenance.
4. Binary authorization collapses purpose legitimacy, evidence relevance, necessity, recipient entitlement, consent, retention, and transformation policy.
5. Figure 2’s conditional state is absent from the formal labels, reliability study, and metrics.
6. Tool “purpose” is author-stated rather than tied to an authoritative policy owner, principal, mandate, legal basis, or affected party.
7. No domain-professional, privacy/legal, organizational-policy, data-subject, or downstream-recipient validation is reported.
8. Synthetic construction has no source frame, template/candidate inventory, generator disclosure, author qualifications, or rejection ledger.
9. Twenty-three domain labels are coverage labels, not representative business-work sampling.
10. Public tasks are outcome-conditioned on long gold chains, abundant atoms, free-text tools, and forbidden opportunities.
11. Added atoms, schemas, sinks, purposes, and mock backends can change the source task construct; no item-level transformation diff or equivalence review is released.
12. Public-source composition is highly imbalanced, including only ten API-Bank cases.
13. The annotation study covers a stratified sample only; sampling probabilities and cluster structure are absent.
14. Annotator identity, expertise, training, guideline, blindness, original-label relation, and adjudication authority are unreported.
15. High agreement under one shared rule does not establish normative or professional correctness.
16. Filtering unclear boundaries may remove legitimate ambiguity and inflate agreement.
17. Detector quality has no labeled sample, precision/recall, confusion matrix, category analysis, or uncertainty.
18. Exact/alias matching can miss implication and transformation; semantic variants can create circular coverage and false matches.
19. “Representative” high-severity manual detector inspection has no sample size, selection rule, labels, or results.
20. Wrapper, bridge, backend, logging, and reasoner completeness are trusted rather than fault-tested.
21. No audit covers failed calls, partial persistence, nested payloads, asynchronous effects, recipient reads, forwarding, or reset.
22. Tool arguments show attempted/received payloads in a mock system, not production disclosure, affected-party exposure, or harm.
23. Task outcome scoring is underspecified; workflow set coverage and required arguments do not establish correct state or professional acceptance.
24. Gold-stage and gold-argument grading can penalize legitimate alternative paths and reward verifier-shaped execution.
25. FOR is conditioned on executed calls and can be diluted by redundant clean calls or altered by omitted/extra tools.
26. FreeTextFOR’s displayed denominator includes all forbidden call opportunities rather than only free-text-capable slots.
27. ToolFOR equal-weights invoked tools despite different calls, opportunities, recipients, and consequences.
28. Severity weights, scale, elicitation authority, and sink-risk treatment are unspecified.
29. MT-POI averages correlated transforms of the same events and can double-count composition effects.
30. SMTC imposes an unvalidated compensatory utility–privacy tradeoff.
31. Weight-rank sensitivity does not establish metric, threshold, or decision validity.
32. Path recurrence does not identify causal propagation from one persisted artifact to another.
33. Sink and transition rates mix task families, schemas, field distributions, and opportunity structures.
34. One apparent run per model–case cell supplies no repeatability or expected-risk evidence.
35. Exact model endpoint, date, decoding, prompts, OpenClaw version, retries, invalidity policy, budget, latency, and cost are missing.
36. No case/template-clustered uncertainty, detector/annotation uncertainty, or paired significance analysis is reported.
37. Qualitative cases are selected without a sampling or coding protocol.
38. No evidence supports natural prevalence, production incident rates, legal compliance, professional validity, privacy safety, or readiness.

## Reproducibility and operational realism

**Conceptual inspectability: moderate.** The paper clearly defines its main objects and equations, reports corpus statistics, provides an annotation-reliability table, names the execution stack, and includes detailed model, sink, free-text, path, domain, and atom-type tables. Another team could construct a related benchmark.

**Exact reproducibility: absent at review time.** The official snapshot contains none of the promised artifacts. Reproduction is blocked by missing case records, source IDs and adaptations, policy graphs/matrices, tool schemas and backends, prompts, wrapper/plugin/bridge versions, detector, severity weights, scorer, raw calls/logs, configured-system manifests, retries/invalid rows, run dates, costs, and analysis code. Every reported number remains manuscript-only.

**Operational realism: moderate as a structural simulation, low for external privacy claims.** Multi-step tools, persisted mock arguments, free-text business fields, tickets, notifications, summaries, and handoffs are realistic information-flow shapes. Fabricated values and mock endpoints are appropriate for safe evaluation. But purpose authority, access policy, real recipients, retention, forwarding, consent, legal obligations, human review, concurrency, service faults, and consequences are absent. This is a controlled closed-world policy-conformance design, not evidence about production privacy incidents or compliant professional operation.

## Transfer to skill-bench

### Retain

1. **Field–destination granularity:** evaluate the same evidence atom differently by purpose, recipient/sink, representation, and workflow stage.
2. **Sink-side trajectory evidence:** preserve attempted arguments, gate decisions, received payloads, and state records rather than relying on final prose.
3. **Utility–privacy separation:** report useful completion, required authorized delivery, and forbidden transmission independently before any aggregation.
4. **Free-text as a first-class surface:** inspect notes, descriptions, messages, summaries, comments, tickets, and handoffs, not only typed fields.
5. **Path diagnostics:** retain first unauthorized occurrence and later recurrence, but call it temporal recurrence unless causal propagation is established.
6. **Sampled independent re-annotation:** preserve pair-level initial labels, disagreement, adjudication, and changes rather than reporting “expert validated.”

### Repair

1. **Authorize the policy before executing it.** Bind each purpose/recipient rule to principal, policy or expert source, valid time, scope, consent/legal basis where applicable, reviewer authority, disagreement, and approval status.
2. **Use a richer disposition.** Distinguish `required_raw`, `required_transformed`, `permitted_optional`, `conditional`, `prohibited`, `disputed`, and `insufficient_authority`; do not force every ambiguous cell into binary ground truth.
3. **Represent actual recipients and surfaces.** Tool names are not audiences. Record service identity, store, role/user visibility, forwarding/retention behavior, and downstream recipient evidence.
4. **Test minimum sufficient representation.** Pair raw facts with authorized derived forms and verify both useful downstream action and non-propagation of the raw rationale.
5. **Calibrate the detector.** Freeze a stratified labeled set spanning exact, alias, normalized, paraphrased, implied, partial, transformed, sanitized, and collision cases; report precision/recall and disagreements by surface and atom class.
6. **Make observer validity executable.** Inject known payloads and omissions through every wrapper/backend path; test nested fields, failures, truncation, retries, async writes, forwarding, and resets.
7. **Use stable denominators.** Report event counts, unique atom–recipient exposures, eligible opportunities under the intended policy, call-conditioned opportunities, and task-level any/mean rates separately. Add redundant-call and alternative-path metamorphic tests.
8. **Avoid premature composites.** Keep utility and privacy vectors primary; use noncompensatory gates for prohibited high-severity flows where authority supports them. Any scalar needs a named stakeholder loss policy.
9. **Validate adaptation lineage.** Preserve source task/revision, original trajectory and oracle, transformations, omitted context, added atoms/sinks, license, equivalence review, and licensed claim.
10. **Repeat and cluster.** Retain per-attempt trajectories, invalidity, costs, and model configuration; estimate uncertainty at source/template/case levels rather than treating all pairs or calls as independent.
11. **Bound the claim.** Passing supports conformance to one versioned, authority-reviewed policy in one mock environment. It does not alone establish privacy compliance, professional quality, production risk, or readiness.

## Concrete repository actions

1. **Do not add a ToolPrivacyBench-specific schema or grader.** Existing information-flow entitlement, authority lineage, consent/participation, provenance-observation, trace, artifact/state, action-safety, handoff, metric, task-health, configured-system, and validity contracts already host the required objects. A new privacy subsystem would duplicate general cross-domain machinery.
2. **Do not queue a new build task.** The concrete non-overlapping mechanics—received-payload evidence, free-text surface checks, authority-to-consequence staging, and utility/safety separation—already appear in the existing inert action-safety slice and related contracts. Future fixtures should reuse the three strongest failure signatures: purpose-specific view collapse, progressive restatement, and raw-detail amplification into a handoff.
3. **Treat all model and sink rates as manuscript evidence only.** Do not use them as calibration targets until a versioned release exposes cases, policies, detector labels, trial rows, configured-system identities, and aggregation code.
4. **After an official substantive release appears, audit rather than assume correspondence.** Pin the release, compare it with v1’s 2,150-case/219,986-pair claims, run detector and denominator metamorphic tests, verify annotation lineage, and reproduce tables before promoting reproducibility status.

## Assessment

- **Evidence tier:** full immutable v1 deep review plus exact placeholder-release audit; no dataset, implementation, or run reproduction.
- **Relevance tier:** **B (enabling)**—directly useful information-flow and trajectory machinery, but weak authority, detector, release, and operational evidence.
- **Most reusable contribution:** destination-specific atom auditing over executed tool arguments while useful completion remains separately visible.
- **Most important empirical hypothesis:** agents often turn purpose-limited facts into general workflow narratives in tickets, free text, and handoffs.
- **Most serious validity risk:** the authored binary field–tool matrix is treated as the privacy boundary even though purpose authority, recipient entitlement, sufficient transformed representations, detector validity, and downstream consequence are not established.
- **Claim skill-bench may safely make:** knowledge-work benchmarks should join authority-reviewed atom–purpose–recipient–representation policies with sink-side execution evidence and plural utility/privacy outcomes; agreement with a closed-world necessity matrix is not itself privacy compliance, professional validity, safety, or readiness.

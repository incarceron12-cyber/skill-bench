# Paper Review: PiSAs — Contextual Integrity in Shared Agentic Systems

- **Paper:** https://arxiv.org/abs/2607.05318v1
- **Version read:** immutable v1, submitted 6 July 2026; arXiv metadata contains no withdrawal/retraction notice
- **Date read:** 2026-07-11
- **Local PDF:** `data/papers/pdfs/2607.05318v1-pisas-contextual-integrity.pdf` (39 pages; SHA-256 `86f6002de537fa0eeecd9590669a9402d2623cdb1e22b1aafdff5adcb8c3bdf9`)
- **Local text:** `data/papers/text/2607.05318v1-pisas-contextual-integrity.txt`
- **Release status:** no official dataset/code URL appears in v1; footnote 1 says an Apache-2.0 dataset will be released upon acceptance (p. 5)
- **Evidence boundary:** the complete paper and appendices were read. Dataset examples are inspectable only through the paper; scenario files, prompts, execution code, traces, annotation records, and graders were not released, so release-level claims cannot be independently audited.
- **Tags:** contextual integrity, multi-user agents, shared memory, information flow, privacy, authorization, model graders

## One-sentence contribution

PiSAs contributes a useful two-axis information-flow oracle—**is an attribute legitimate evidence for this purpose, and may this recipient see it?**—and audits leakage across gathered summaries, inter-agent messages, contexts, and memory, but its evidence is a controlled synthetic stress test rather than organizational validation: 85 manually curated scenarios in three task templates, oracle-authored norms, model-mediated scoring, no annotation-reliability study, three repeats, and no public release.

## Why this matters for skill-bench

This advances charter objectives A, B, and C by exposing a gap in artifact/source provenance: authority is not exhausted by source trust or task relevance. Information can be true, necessary, and lawfully available to one role yet illegitimate to transmit to another. Conversely, a raw private fact can have a legitimate sanitized operational consequence. That distinction applies across scheduling, incident response, case work, finance, healthcare, and other knowledge work; it does not narrow skill-bench to privacy.

The paper's strongest benchmark-design result is not that one topology “wins.” It is that system-level evaluation must follow an information atom across **purpose, recipient, representation, and surface**. Aggregate final-output checks miss leakage relocated into coordinator messages or shared memory. PiSAs makes that relocation measurable, although its own output-surface accounting is narrower and less consistent than the framing suggests.

## Research question and claim boundary

The paper asks how shared multi-user agent systems preserve contextual integrity when task-relevant and irrelevant information is distributed across users, agents, communication channels, and memory, and how topology, memory, prompting, rule explicitness, and attribute cues affect privacy and utility.

The evidence supports these bounded conclusions:

1. the authors constructed 85 synthetic, manually curated scenarios over JIRA allocation, severity classification, and meeting allocation, with 4–10 users and roughly 23 attributes per scenario (Section 3 and Appendix A, pp. 3–14);
2. dual labels permit separate measurement of purpose-inappropriate use and recipient-inappropriate visibility;
3. in the tested implementations, partitioned multi-agent designs reduced many measured violations relative to one omniscient agent but did not eliminate them (Table 2, p. 7);
4. shared/hybrid memory often moved leakage away from agent-to-agent messages into memory rather than removing it (Section 5.2, pp. 7–8; Tables 10–11, pp. 19–20);
5. task-entangled personal attributes leaked more than irrelevant attributes, showing that abstraction—not mere suppression—is the hard case (Appendix F.2, pp. 19–21);
6. idealized privacy labels and sanitized operational forms reduced violations while preserving or improving utility in the meeting ablations (Tables 16–17, pp. 26–27); and
7. reported privacy values are materially evaluator-dependent, especially when the verifier ensemble changes (Tables 24–25, pp. 30–31).

It does **not** establish that its labels represent organizational norms, that scenario decisions are professionally valid, that its three task families cover shared knowledge work, that measured leakage rates predict deployment rates, that any topology is generally safer, that prompts or oracle cues are deployable defenses, or that the unreleased benchmark is reproducible.

## Methodology and system

### Scenario construction and dual annotations

Each scenario is built backward from a unique oracle decision. Structured seeds specify roles, possible outputs, decision rules, appropriate attributes, distractors, and per-user visibility. Appropriate attributes are those required for the task; inappropriate attributes should not influence or surface in task execution. Separately, each attribute has a visibility set identifying users allowed to access it (Section 3, pp. 3–5; Appendix A).

This is the central advance. It avoids conflating two failures:

- **appropriateness:** using/transmitting an attribute for the wrong purpose, even to an otherwise authorized user;
- **visibility:** exposing any attribute to a user outside its allowed audience, even when the attribute is task-relevant.

The axes are not fully orthogonal in the implementation. “Appropriate” is defined largely as required for the oracle solution, which collapses contextual legitimacy into benchmark necessity. Legitimate optional evidence, useful-but-nondeterminative context, consent, purpose limitation, retention duration, transmission principle, and role changes are mostly absent. Visibility is a static set, not a policy with provenance, time, delegation, or revocation.

The paper says scenarios required “substantial manual effort” and were manually curated, but reports no author count, domain credentials, source lineage, norm-elicitation procedure, independent annotators, agreement, adjudication, expert review, or participant validation. The labels are therefore benchmark-author oracles, not demonstrated workplace norms. Building backward from a unique decision improves deterministic scoring while potentially making cases cleaner and more teleological than real work.

### Task families and ecological realism

JIRA allocation combines specialties, availability, assignment constraints, and personnel distractors. Severity classification combines role-distributed technical evidence under an explicit or policy-form rubric. Meeting allocation requires converting private reasons into operational constraints. These are good controlled templates for information-flow stress.

They remain synthetic tasks in one organizational idiom. Users are cooperative, information sits in scripted notes/artifacts, goals align, norms are stationary, and there are no external tools or APIs (Limitations, pp. 8–9). The paper itself appropriately calls the three-family scope a depth-for-breadth trade. Its further assertion that deployment violations are likely lower-bounded by these results is plausible but untested: synthetic salience, verbose personal distractors, fixed prompts, and authored oracle labels could also inflate or reshape measured leakage.

### Configured systems and information-flow surfaces

The study compares:

- a single omniscient agent;
- a centralized system with user agents and a coordinator;
- a decentralized token-passing system where the active agent chooses the next peer.

All use a two-stage gather-then-decide pipeline. Memory variants are none, private, shared, and hybrid. The three backbones are Qwen3.6-27B, gpt-oss-120b, and Claude Sonnet 4.6. Privacy instructions vary from none through high (Sections 4–5, pp. 5–8; Appendix E).

This is correctly a configured-system experiment: topology changes accessible context, routing, prompt exposure, message count, and termination logic, not just “architecture.” Yet comparisons are not clean causal estimates of topology alone. Centralized and decentralized systems differ in routing policy, history visibility, coordinator role, stopping behavior, and communication volume. Single-agent visibility is defined as 100% because everyone shares one agent, turning one architectural assumption into a maximal score by construction rather than observing disclosures to users.

The paper advertises output, communication, and memory levels, but its operational pipeline treats the gathered-information summary as the output/privacy bottleneck and says it does not measure final-output violations (p. 5). Appendices and examples sometimes describe final-output leakage. This ambiguity matters: gathering text visible only inside the system is not equivalent to a recipient-facing artifact. The benchmark needs explicit observer and recipient mappings for every surface.

### Grading and aggregation

Utility is binary oracle-decision correctness. Completeness is the fraction of appropriate attributes found in the gathered summary. A lenient model extracts candidate attribute mentions; three verifier models vote on whether a candidate reveals the key fact. A ground-truth-aware Gemini 2.5 Pro judge scores completeness and utility (Section 5, p. 6; Appendix B). The evaluation stack is expensive: in a 945-run meeting sweep, evaluation was 92.8% of the $304.47 API bill, with the main judge alone 86.6% (Appendix H, pp. 28–29).

Repeated-run semantics are unusually explicit but internally inconsistent. Section 5 says violation rates use “the worst case across the 3 trials” (p. 6). Appendix D defines an attribute-level union across runs, and Appendix G distinguishes that **any-K union** from worst-run and mean-run aggregation (pp. 15–16, 25–28). Any-K is necessarily at least worst-run because different runs can leak different attributes. Main tables appear described as any-K. This is not cosmetic: the estimand changes from worst execution severity to the set of attributes ever leaked over three probes.

Any-K is useful for hazard discovery, but depends monotonically on K and is not a deployment probability. With only K=3, it is neither a stable leakage-surface estimate nor a reliable rare-event bound. The paper reports standard errors over scenarios, but scenarios are clustered within only three authored task families and the aggregation induces dependence.

Completeness also overcredits raw private detail when only a sanitized implication is legitimate: finding the fact and transforming it safely are separate capabilities. Binary unique-oracle utility ignores artifact quality and alternate legitimate decisions.

## Evidence and results

Under high privacy prompts and no memory, every tested configuration had appropriateness failure rates above 75%; the centralized Claude configuration reported 25.4% appropriateness violations, 33.5% visibility violations, 61.3% completeness, and 61.7% utility (Table 2, p. 7). These values show difficulty under the benchmark's labels, not acceptable/unacceptable operational risk thresholds.

The memory ablation is the most convincing system diagnosis. For centralized Claude on JIRA, shared memory reduced A2A messages from 11.4 to 2.8 and A2A violations from 49.4% to 14.5%, while shared-memory violations reached 97.2% and failure rate 92.0%. Hybrid memory improved completeness to 79.1% and lowered appropriateness violations to 23.6%, but total visibility remained 63.2% (Table 11, p. 20). This demonstrates **surface substitution**: a local metric improvement can conceal migration to a less visible store.

The personal-attribute analysis finds averaged appropriateness violations of 70.1% for decision-critical personal attributes, 54.2% for salient non-required attributes, and 19.3% for irrelevant personal attributes (Table 12, p. 20). The benchmark's hard case is not recognizing obvious secrets; it is preserving a task consequence while suppressing its sensitive rationale.

The cue ablations support this diagnosis but are explicitly oracle-assisted. In the single-agent meeting condition, privacy cue plus sanitized form reduced appropriateness violations from 66.9% to 14.4% and failure from 100% to 65.7%; centralized results moved from 11.3% to 3.3% appropriateness violations and from 60.0% to 20.0% failure (Tables 16–17, pp. 26–27). This measures the value of trusted upstream classification and transformation, not autonomous privacy judgment.

The rule-specification ablation contains a notable reporting error. The text claims the strict rubric performs best across all metrics and provides the highest completeness (pp. 22–23). Table 15 reports completeness of **38.7%** for strict rules, versus **96.0%** for broad policy and **53.8%** for no rule; strict rules do have lowest violations and highest utility. Either the table, metric, or prose is wrong. Until corrected, claims that strict rules dominate the entire privacy–utility plane are unsupported.

Judge sensitivity is material. Replacing paid verifiers with local verifiers raises centralized visibility from 25.3% to 42.9% and appropriateness from 22.8% to 42.9% on the same traces (Table 24, p. 30). Broad rank patterns persist, but absolute rates—the quantities relevant to a safety gate—do not. No human-labeled test set, verifier precision/recall, disagreement rate, adjudication sample, or confidence interval is reported.

## Unique insight

PiSAs's deepest transferable idea is an **information-flow entitlement**, not a generic privacy label:

`information atom × source/subject × purpose × recipient × representation × surface × time → permitted / transformed / prohibited`

A knowledge-work benchmark should distinguish at least four states:

1. the raw fact is legitimate evidence and may be transmitted;
2. the raw fact may be read, but only a sanitized operational consequence may be used or shared;
3. the fact may be visible to a role but is illegitimate evidence for this decision;
4. the fact is neither visible nor appropriate.

This extends the charter's source authority and public-basis principles. “Trusted source” answers whether a claim may be believed; “task relevance” answers whether it bears on a decision; “recipient entitlement” answers who may receive it; “representation policy” answers whether raw detail or only a derived consequence may flow. Those must remain separate.

A second insight is **conservation of leakage across surfaces**. Communication, context, memory, and final artifacts form one flow graph. Optimizing one surface can route the same information through another. Therefore a mitigation should be credited only when end-to-end unauthorized exposure falls, not when message-level leakage drops while shared-memory exposure rises.

## Reproducibility and operational realism

The PDF preserves task statistics, metric equations, prompts, cost tables, examples, and extended traces. That is enough to understand the method but not reproduce it. The promised Apache-2.0 dataset is deferred until acceptance. There is no repository URL, immutable archive, scenario schema, full prompt set, runner, raw outputs, judge prompts/responses, annotation record, environment lockfile, or trial manifest.

Model names include future/current provider endpoints whose behavior may be mutable. One backbone was local, but hardware, inference engine, quantization, sampling, and serving details are not sufficiently reported in the reviewed text for exact replication. API costs exclude local compute. Evaluator sensitivity and the dominant evaluation cost make judge snapshots and archived decisions essential.

Operational realism is deliberately limited: no real identities, permissions service, policy engine, live communication system, external tools, user consent, role changes, deletion/retention lifecycle, adversaries, cross-task persistence, or downstream harm. The study is best treated as a controlled component benchmark and design probe.

## Limitations and validity threats

1. Eighty-five scenarios cover only three synthetic organizational task templates.
2. No sampling frame supports claims about organizational knowledge work.
3. Manual curation lacks author qualifications, source provenance, annotation counts, agreement, and expert validation.
4. Appropriateness is largely equated with oracle necessity, omitting legitimate optional context and broader norms.
5. Visibility is static and set-valued; delegation, consent, revocation, time, and transmission principles are absent.
6. Unique backward-constructed oracles simplify ambiguous professional decisions.
7. Cooperative scripted users omit adversarial, conflicting, and evolving contexts.
8. Raw personal distractors may have benchmark-specific salience unlike naturally occurring records.
9. Topology treatments alter several system variables simultaneously.
10. Single-agent visibility is maximal by definition, limiting architectural comparison.
11. Gathered summaries and recipient-facing outputs are ambiguously conflated.
12. Final-output violation measurement is described inconsistently.
13. Completeness does not cleanly distinguish raw-fact recovery from safe abstraction.
14. K=3 any-K aggregation is probe-count dependent and not leakage probability.
15. Main-text “worst case” conflicts with appendix any-K definitions.
16. Standard errors do not resolve task-family clustering or authoring dependence.
17. Model-based extraction and verification lack human accuracy calibration.
18. Evaluator replacement changes absolute violation rates substantially.
19. Judge/verifier model-family overlap leaves correlated-error risk.
20. The strict-rule completeness prose contradicts Table 15.
21. Privacy prompts and attribute cues contain oracle information unavailable in ordinary deployment.
22. No privacy-preserving interceptor, retrieval policy, access-control engine, or tuned model is evaluated.
23. Memory is scoped to one run, so persistence and cross-task accumulation are not tested.
24. No release currently permits scenario, annotation, code, or trace inspection.
25. API and local inference configurations are not fully immutable or cost-complete.
26. No human-user or organizational outcome validates ecological meaning or harm thresholds.

## Transfer to skill-bench: concrete changes

1. **Add recipient and representation entitlement to evidence lineage.** For every sensitive/controlled atom, record subject, source, authorized readers, legitimate purposes, allowed derived forms, prohibited raw forms, and temporal validity.
2. **Separate access, use, disclosure, and retention.** An agent can lawfully read a fact yet use it inappropriately, disclose it to the wrong actor, or retain it too long; each needs a distinct check and failure code.
3. **Model sanitization as a provenance-preserving transformation.** Link raw evidence to the operational consequence, transformation rule, information-loss test, authorized recipients, and checks proving raw detail did not propagate.
4. **Audit the whole flow graph.** Evaluate prompts/contexts, retrieval results, A2A messages, scratch state, private/shared memory, tool arguments, artifacts, and final responses with explicit observer views.
5. **Detect surface substitution.** Report per-surface and union exposure; do not credit a mitigation solely for reducing one channel.
6. **Keep hazard discovery distinct from incidence.** Label any-K as capability-to-leak under K probes; separately report mean-run frequency, worst-run severity, K, and uncertainty.
7. **Require norm provenance.** Visibility and appropriateness labels need expert/policy/source evidence, annotator disagreement, adjudication, and validity period—not benchmark-author intuition alone.
8. **Calibrate model leak detectors.** Preserve candidate extraction, verifier votes, disagreements, and a stratified human audit across exact, paraphrased, partial, sanitized, and false-match cases.
9. **Test privacy–utility transformations, not suppression alone.** Include decision-critical private facts where correct work requires using a sanitized consequence and verify both decision correctness and non-propagation.
10. **Treat topology and memory as configured-system fields.** Record routing, context visibility, read/write ACLs, persistence scope, retrieval, stopping, and observer mapping so scores are not attributed to the backbone alone.
11. **Use cross-task trials.** Test role changes, revocation, later unrelated tasks, deletion, and memory accumulation; one isolated run cannot validate persistent shared systems.
12. **Do not create a duplicate schema project.** These requirements should consolidate with existing source-authority, artifact-view, memory, handoff, safety, and trace contracts; one focused contract extension task is warranted only after schema gap analysis.

## Action items

- [x] Read the complete immutable v1 PDF and extraction.
- [x] Verify release status and preserve exact evidence paths.
- [x] Reconstruct scenario generation, dual annotations, surfaces, systems, metrics, ablations, costs, and judge sensitivity.
- [x] Identify the any-K/worst-run and strict-rule completeness inconsistencies.
- [x] Derive cross-domain information-flow entitlement and surface-substitution requirements.
- [ ] After the dataset is released, archive an immutable version and audit scenario provenance, annotation reliability, grader implementation, and trace replay.

# Paper Review: Proof-or-Stop evidence-gated lifecycle validity

- **Paper:** <https://arxiv.org/abs/2607.14890v1>
- **Title:** *Proof-or-Stop: Don't Trust the Agent, Trust the Evidence — Loop Engineering for Verifiable Evidence-Gated Lifecycle Control*
- **Authors:** Jek Huang, Jeffery Hsia, Jiayi Sun, Freddie Shi, Wei Huang, and Ian H. White
- **Date read:** 2026-07-18
- **Version read:** immutable arXiv v1, submitted 16 July 2026
- **Local PDF:** `data/papers/pdfs/2607.14890v1-proof-or-stop.pdf` (48 pages; SHA-256 `bd27a4f6a071ede7f9405648a5f9bb0e815b8d30a2018dfccc44adf89b896481`)
- **Local text:** `data/papers/text/2607.14890v1-proof-or-stop.txt` (SHA-256 `a9d4268b9cfad94502490789690424beefa89edba0852fca97e7dcf6a56329ee`)
- **TeX source:** `data/papers/source/2607.14890v1-source.tar` (SHA-256 `0d9a95a80076d25e56dc6cfff0cb5daf2d092a6ea19aaae8f4f18390730cba8d`)
- **Advertised implementation:** <https://github.com/Proof-or-Stop>
- **Release provenance:** `data/sources/releases/2607.14890v1-proof-or-stop/provenance.json`
- **Release boundary:** at acquisition and again during this review, the advertised GitHub organization reported `public_repos=0` and returned an empty repository list. The claimed `arxiv-v1` implementation tag, preregistration, mechanism fixtures, 9,240-cell records, self-application corpus, and 68-row exhibit were therefore unavailable. Paper claims were read in full but could not be independently rebuilt or executed.
- **Tags:** lifecycle-control, evidence-admission, freshness, receipts, review-gates, hidden-failure, task-health, claim-validity

## One-sentence contribution

Proof-or-Stop makes a valuable semantic correction—an agent saying “reviewed,” “tested,” or “done” is a **claim**, while only fresh, source-state-bound evidence may authorize a state transition—and reports an unusually explicit gate-versus-review ablation; however, the unavailable advertised release prevents independent audit, the powered experiment does not instantiate the paper's receipt-gated lifecycle, its 31-versus-2 separation is almost entirely one task, and its co-designed mechanical checks do not establish semantic correctness, gate completeness, workflow value, or production readiness.

## Why this matters for skill-bench

`skill-bench` already separates measurements from validity claims, task versions from task-health transitions, and artifact provenance from semantic correctness. This paper contributes a sharper **authorization boundary**:

```text
actor statement
→ typed lifecycle claim
→ required evidence specification
→ producer and observer identity
→ source/environment/policy binding
→ admissibility predicates
→ gate decision
→ authorized transition or typed stop
→ later substantive consequence
→ bounded validity claim
```

No arrow inherits the next. A receipt can be authentic but semantically irrelevant. A check can pass but be incomplete. A gate can correctly enforce a flawed requirement. A stop can prevent false promotion while also rejecting legitimate alternate evidence. A reduction in injected visible-pass/hidden-fail delivery does not establish benefits on natural work unless the trap prevalence and the costs of false stops, repair, and review are measured.

The paper is therefore useful cross-domain lifecycle machinery, not a reason to narrow the benchmark to coding. It advances charter objectives A–C by clarifying how consequential benchmark, grader, lesson, task-health, release, and readiness transitions should be evidence-authorized.

## Research question and claim boundary

The paper asks whether autonomous-agent lifecycle states can be controlled by treating every consequential actor output as a claim and admitting transitions only when current, structured, authenticated evidence satisfies a gate; it also asks whether enforcing review as a transition condition reduces visible-pass/hidden-fail amplification relative to weaker loops (Sections 1–6, pp. 1–24).

### What immutable v1 supports as a paper claim

1. It defines a coherent claim-to-evidence-to-gate transition semantics and explicitly denies that operational “proof” proves semantic program correctness (Abstract; Sections 1 and 3, pp. 1–12).
2. It specifies concrete source-state, policy, command-set, producer, execution, and outcome predicates rather than treating a success narrative or green log as sufficient (Eq. 2, pp. 8–10).
3. It separates mechanism conformance from comparative outcome evidence: 10 lifecycle scenarios and 18 receipt-tamper classes test the former; the five-arm ablation tests the latter (Tables 1, 5, 9, and 11).
4. It reports the most informative comparison as A3 versus A4: the same reviewer signal is advisory in A3 and transition-enforced in A4, with 14/1,800 versus 2/1,800 amplified injected cells and near-equal mean token use (Sections 5.2–6, pp. 18–24).
5. It reports important adverse boundaries: clean tasks showed no observed quality gain and roughly doubled cost/latency in a small pilot; the separate gated/no-review matrix used 3.80× tokens; safe-stops in that matrix lacked hidden-oracle adjudication; and real-work trap prevalence is unknown (pp. 19–21, 35–36, 42–43).
6. It openly identifies the powered study as one model family, 24 coding tasks, selected injected faults, and control-policy evidence rather than a full receipt replay or production claim.

### What immutable v1 does not establish

It does not establish that the claimed implementation or records were publicly inspectable at v1; that the preregistration existed before outcomes were observed; that all 9,240 rows, exclusions, hashes, scripts, and fixtures reconstruct the tables; that the Sonnet endpoint was invariant; that the hidden oracle is sound and alternative-complete; that source hashes bind executable state; that authorized producers are independent or uncompromised; that the command set is sufficient; that gates admit legitimate alternative evidence; that false stops are acceptably rare; that injected-fault effects transport to natural work; or that the method improves professional quality, cost-adjusted utility, safety, production fitness, or readiness.

The paper repeatedly labels artifacts “verified,” but with the release absent that status is **author-reported verification in immutable v1**, not independently reproduced evidence in this review.

## Methodology and system

### Agent-as-claim formalism

A unit moves through phases such as `init → plan → dev → review → test → done`. For each transition, required claims must have at least one providing evidence record that passes admissibility (Eq. 3, pp. 11–13). Ordinary notes remain advisory; only lifecycle-moving claims receive the heavyweight gate.

The conceptual move is strong because it separates three objects often collapsed in agent benchmarks:

- **assertion:** what an agent, reviewer, tool, or workflow says happened;
- **observation:** what a configured producer recorded about an execution or artifact;
- **authorization:** whether a policy permits a transition on that observation.

This is more precise than treating an agent's terminal message, tool return, grader score, or “completed” flag as the state itself.

### Evidence identity and admissibility

The paper binds evidence to three tracked-code identities: a canonical tracked-tree `materialHash`, commit `headHash`, and story-owned-files hash. Evidence additionally carries policy and command-set hashes; execution receipts include command, arguments, working directory, exit status, and output digest. Eq. 2 requires freshness, completeness, integrity verification, producer authorization, execution attestation, claim support, and accepted outcome (pp. 8–10).

This is a useful envelope, but it is not a semantic proof system:

- `Supports(E,c)` is load-bearing and task-specific; a hash cannot establish that a test actually covers the claim.
- `OutcomeAccepted` freezes a policy decision, not the validity of the decision threshold.
- `commandSetHash` detects command drift but can faithfully bind an incomplete or weak command set.
- tracked-tree hashes exclude dependencies, toolchains, containers, environment variables, external services, untracked outputs, credentials, and clocks unless separately captured; the paper acknowledges this on p. 8.
- producer authorization establishes permission under the configured trust model, not competence, independence, honesty, or uncompromised execution.
- local-key signatures do not defeat a compromised runner or signing key; the paper explicitly keeps that adversary out of scope.

### Receipt and gate conformance tests

The offline receipt contract reports one authentic acceptance and rejection of 18 mutations spanning stale bindings, edited evidence, signer mismatch, malformed structure, digest errors, failing commands, absent receipts, and failed decisions (Table 5, pp. 9–10). A gate-strength fixture pairs catch rate with false block, using test-only, block-all, and oracle reference reviewers (Table 6). A further producer characterization claims deterministic replay, tamper failure, interruption recovery, and scale-envelope behavior under a frozen protocol (Table 7).

These are good **negative conformance patterns**, especially the block-all control. Yet all are co-designed closed-world tests. They show that enumerated mutations route to expected reason codes. They do not estimate adversarial coverage or valid-alternative acceptance. The paper mentions two accepted and six “acknowledged limitation” tamper-handling cases in Table 7 without exposing the records here. No available release allowed mutation of path aliases, symlinks, environment drift, trusted-key compromise, signed-but-semantically-false output, partial checks, colluding producers, or a legitimate substitute receipt.

### Lifecycle gates and review assurance

The concrete matrix binds plan-to-dev scope, dev-to-review paths, review-to-test signed review artifacts, and test-to-done full-test receipts (Table 8, pp. 12–13). High-risk changes nominally require three rounds with two independent passing verdicts per round; unavailable second-host execution degrades explicitly to local assurance rather than manufacturing a quorum (Eqs. 4–5).

The honest degradation rule is excellent. The independence rule is weaker: different host, session, and signing key do not prove independent model family, prompt, evidence view, training error, operator, or failure mode. Repeated rounds over the same artifact and criteria may be correlated. The paper's own selected cross-vendor cases suggest diversity matters, but selective invocation cannot estimate marginal value.

The finding policy also allows known issues on “done” stories: critical always blocks, while medium becomes advisory by round two and high by round three; all 41 open findings in the corpus sit on done stories (pp. 29–30). This is not necessarily wrong, but it proves that `done` means **policy-authorized disposition**, not “correct,” “zero known defects,” or “professionally acceptable.” A benchmark must retain that exact decision semantics.

### Five-arm powered ablation

The nominal design is five arms across 24 stratified coding tasks, a null plus 15 injected scenarios, and five repeats. A1 covers 13 scenarios; A2, A2-prime, A3, and A4 cover all 16, yielding 9,240 applicable unique cells. A2-prime is a retry loop capped toward A4's pilot median; A3 adds one advisory review; A4 iterates review, repair, and enforcement. The visible acceptance test is available to the agent; a hidden oracle marks correctness. Shipping a visible pass that fails the hidden oracle is “amplified”; repair or refusal is “not amplified” (Section 5.2, pp. 15–19; Appendix A).

The primary report is A4 versus A2-prime: 2/1,800 versus 31/1,800 amplified injected cells, presented as +1.6 percentage points not-amplified with seeded cluster-bootstrap 95% CI [0.8, 2.5]. A3 versus A4 is exploratory: 14/1,800 versus 2/1,800. Mean token use is 170,545 for A2-prime, 200,510 for A3, and 204,553 for A4 (Table 11).

Important design facts constrain interpretation:

- A2-prime is not equal-spend: only 207/1,920 all-scenario cells fall inside the nominal ±20% band, and A4 spends about 1.2× its tokens.
- Raw A2 performs better than A2-prime on this rare-event endpoint (18 versus 31 amplifications), weakening a monotone “more control fidelity” story.
- all A4 safe-stop counts are zero in this experiment; the powered mechanism is repair/enforcement, not stop activation or receipt freshness.
- the powered cells have null `headHash/materialHash`; the paper explicitly says they are not lifecycle-gate-grade evidence (p. 20).
- A4's two errors and 29 of A2-prime's 31 errors occur on `du-duration`. Excluding that task leaves 0/1,725 versus 2/1,725. The aggregate effect is therefore primarily one task-by-policy interaction, not broad task-level dominance.
- exact dated model snapshot is absent; records reportedly contain only `modelId=sonnet`.
- 77 restart duplicates were deduplicated, 24 A1 edge cells fall outside the main outcome taxonomy, and no invalid record is reported; without records, these rules and counts cannot be checked.
- the paper says “seeded cluster bootstrap” but the absent analysis artifact prevents verifying cluster unit, resampling implementation, estimand, or whether task-level concentration is represented adequately.

### Supplemental and self-application evidence

A separate 1,152-cell GPT-family comparison reports 106 no-review completions not admitted by the gate and 3.80× token use for the bundled gated condition. No hidden oracle adjudicated those 106, so false-stop, prevented-error, and cost-benefit rates are unidentified (pp. 19–20, Appendix B).

The operated corpus reports 565 stories, 1,007 findings, 94.8% resolved, 26/28 curated findings filed while author tests were green, and 68 selected cross-vendor high/critical findings (Section 8). This demonstrates the *shape of records the system intends to preserve*. It does not establish prevalence or treatment effects: the corpus is self-built and LLM-reviewed; the 12-story set is curated; `smoke_would_miss` is reviewer judgment; cross-vendor review is selectively assigned; and no direct-development counterfactual exists. The claimed corpus, extraction scripts, merge ledger, finding rows, and fix commits were unavailable at the advertised endpoint.

## Evidence and result interpretation

The evidence ladder should be read as follows:

1. **Formal specification:** Eqs. 1–5 define intended identities, predicates, and transitions.
2. **Enumerated conformance claim:** the paper reports expected behavior on 10 scenarios, 18 receipt tamper classes, and additional synthetic ledgers.
3. **Injected control-policy claim:** under one reported Sonnet configuration and the authored 24-task/15-fault matrix, enforcing a reviewer signal is associated with fewer visible-pass/hidden-fail deliveries.
4. **Selected operational existence claim:** the authors' self-application records reportedly contain defects found after green tests and selected cross-vendor catches.
5. **Not established:** broad gate soundness/completeness, natural-work benefit, cost-effectiveness, professional validity, security, production reliability, or readiness.

The most credible empirical insight is not the headline A4-versus-A2-prime result. It is the near-compute A3-versus-A4 contrast combined with the task-concentration disclosure: **an observation changes outcomes only when a transition policy consumes it, and that benefit can be sharply conditional on a trap-active task**. This motivates interaction-aware lifecycle evaluation rather than universal gate claims.

The most serious evidence problem is release contradiction. The Reproducibility section says the public address links to implementation, verifier tests, re-extraction entry point, sanitized experiment records, corpus/deep-finding tables, summaries, and figure sources under an `arxiv-v1` tag (pp. 37–38, 44–45). At acquisition and review time, that organization had zero public repositories. This does not prove artifacts never existed, but it makes v1's strongest quantitative claims non-reproducible for an independent reader now. The paper's internal statements that audits “verified” results cannot substitute for artifact access.

## Unique insight

The paper's unique insight is that **evidence validity and transition authorization are distinct from both actor truthfulness and artifact correctness**.

A benchmark lifecycle needs at least four independent predicates:

```text
observation authenticity
× observation applicability to current state
× semantic sufficiency for the claim
× policy authorization for the consequence
```

Proof-or-Stop handles the first two most concretely. It partially declares the fourth. The third remains domain- and construct-dependent. This explains why cryptographic freshness can coexist with a wrong artifact, why a complete receipt can attest an incomplete test suite, and why a correctly enforced gate can produce an unjustified stop.

A second insight is that evidence-gated evaluation must measure **both unsafe promotion and unjustified refusal**. “Zero false-DONE” is vacuous if every request is blocked. The paper's block-all reviewer control recognizes this, but its powered endpoint collapses repair and refusal into “not amplified,” and its main powered A4 arm has no stops. A general benchmark should preserve a transition confusion matrix:

- correct advance;
- incorrect advance;
- correct stop/escalation;
- incorrect stop;
- repaired then correct advance;
- repair-induced collateral failure;
- invalid or unobservable gate decision.

A third insight is that the value of a gate is an interaction, not a fixed property. It depends on natural trap prevalence, gate sensitivity/specificity, cost, repair success, consequence severity, and task family. The paper finds a large concentration on one trap-active task and pure overhead on easy clean tasks. `skill-bench` should therefore treat gate policy as a risk-adaptive configured-system component, not an unconditional best practice.

## Limitations and validity threats

1. The advertised public implementation organization had zero repositories at both acquisition and review time.
2. No `arxiv-v1` tag or release-notes commit could be pinned.
3. The claimed preregistration has no accessible registry record, timestamp, immutable hash, or local artifact.
4. The 9,240 raw cells, tidy CSV, analysis script, task/scenario dictionaries, and exclusions were unavailable.
5. The 10 mechanism scenarios and 18 tamper fixtures could not be executed or mutated.
6. The 565-story/1,007-finding corpus and re-extraction scripts were unavailable.
7. The 68-row cross-vendor exhibit and fix commits were unavailable.
8. Internal author review and self-application are not independent replication.
9. The formal admissibility predicate leaves `Supports(E,c)` domain-specific and under-operationalized.
10. Authenticity and freshness do not establish semantic truth or completeness.
11. Command-set hashing binds selected commands but does not validate coverage.
12. Tracked-tree hashes omit executable environment state unless separately instrumented.
13. Local-key integrity assumes an uncompromised runner and signing key.
14. Producer authorization does not establish competence, independence, or truthful execution.
15. Different host/session/key is an incomplete independence criterion.
16. No collusion, shared-model-error, shared-prompt, or shared-evidence-view analysis is reported.
17. No legitimate-alternative-evidence suite estimates gate completeness or false rejection.
18. Path substitution, symlink, untracked-file, dependency, environment, service, and clock mutations are not auditable from available evidence.
19. Signed but semantically false outputs remain possible under a compromised or weak producer.
20. The lifecycle's `done` state permits known open findings under round-graded severity policy.
21. “Done” therefore cannot be read as zero-known-defect or semantic-correctness status.
22. The powered ablation does not instantiate material-hash or receipt gating.
23. Powered records reportedly have null source-state hashes.
24. Safe-stop is zero in the powered matrix, so the main study does not evaluate stop precision.
25. Repair and safe-stop are combined by the “not amplified” complement in the primary interpretation.
26. A2-prime is not equal-spend and A4 uses more mean tokens and wall time.
27. Only 207/1,920 A2-prime all-scenario cells satisfy the intended spend band.
28. Raw A2 outperforms A2-prime on amplified count, complicating the control-fidelity ladder.
29. The exact dated Sonnet endpoint is not recorded.
30. Provider drift, sampling configuration, prompt version, tool implementation, and harness version cannot be reconstructed from the paper alone.
31. The 31-versus-2 difference is concentrated almost wholly in one task.
32. Excluding `du-duration` leaves near-ceiling 2-versus-0 counts over 1,725 cells per arm.
33. Five repeats do not make 1,800 task-scenario cells independent.
34. The bootstrap cluster unit and implementation cannot be audited without the analysis artifact.
35. No task-sampling frame or population supports generalization beyond the authored 24 tasks.
36. The hidden oracle's soundness, completeness, and alternative-solution policy are unavailable.
37. Visible and hidden checks share authoring lineage, creating co-design and injected-fault alignment risk.
38. Injected-fault performance conditions on trap exposure and does not estimate natural trap prevalence.
39. No real-work green-but-wrong denominator supports cost-benefit claims.
40. The separate 106 stopped completions lack hidden adjudication.
41. The 3.80× token ratio is bundled, not an isolated review-cost effect or billing estimate.
42. The clean pilot is only three small tasks and nine runs per arm.
43. Curated deep-set selection invalidates prevalence interpretation of the 93% figure.
44. `smoke_would_miss` is reviewer judgment, not counterfactual ground truth.
45. Selective cross-vendor invocation invalidates marginal-yield estimates.
46. Severity and categories are reviewer-filed labels without reported reliability.
47. Self-application intertwines system development, evaluation, author incentives, and instrument repair.
48. No independent human or domain-expert validation is reported.
49. No false-stop burden, reviewer burden, latency-to-decision, or downstream utility study is reported.
50. No external benchmark, cross-domain task, multi-model replication, production deployment, or readiness evidence exists.

## Reproducibility and operational realism

**Paper preservation is strong.** Immutable PDF, full text, metadata, and TeX source are local and hash-pinned. The paper is unusually explicit about intended files, commands, caveats, and where evidence tiers differ.

**Empirical reproducibility is currently poor.** The source tar contains manuscript material and figures, not the advertised implementation or datasets. The only official endpoint supplied by the paper exposed no public repository at two checks on 2026-07-18. Consequently none of the mechanism, ablation, corpus, cross-vendor, paired-matrix, or memory experiments could be independently reconstructed. The review records this as acquisition-time unavailability, not global proof of nonexistence.

**Operational realism is mixed.** Lifecycle states, current-source binding, retries, reviews, findings, known-issue disposition, concurrent hash invalidation, handoff, costs, and stops are realistic concerns. But the evidence is confined to self-hosted coding; source hashes are not full environment attestations; the main experiment uses injected faults and no lifecycle receipts; and no user, expert, deployment, or downstream consequence study validates whether the added control is worth its burden. The system is best interpreted as a promising assurance architecture with author-reported conformance and one narrow control-policy study—not a production-validated trust layer.

## Transfer to skill-bench

### Retain

1. **Agent-as-claim semantics.** Terminal messages, grader outputs, review verdicts, and workflow flags propose state; they do not become authorized state automatically.
2. **Current-state evidence binding.** Evidence used for consequential transitions must identify the exact task, source pack, artifact, grader, harness, environment, policy, and observation versions it supports.
3. **Typed gate predicates.** Keep freshness, completeness, integrity, producer authority, execution attestation, semantic support, and accepted outcome separate.
4. **Fail-closed invalidity.** Missing, malformed, stale, wrong-scope, untrusted, or insufficient evidence should not silently become failure or success evidence.
5. **Honest assurance degradation.** Missing independent review should lower the claim, not be disguised as quorum.
6. **Claim-language ceilings.** Mechanism conformance, configured control-policy effect, professional validity, production fitness, and readiness need separate promotion gates.
7. **Advisory versus enforced ablation.** Compare the same observation as ignored/advisory/enforced/repair-triggering to isolate where benefit arises.
8. **Block-all negative control.** Gate evaluation must include false refusal and valid-alternative acceptance, not catch rate alone.

### Repair

1. **Bind the full evaluated state.** Extend beyond tracked files to environment, dependencies, tools, services, credentials/permissions, clocks, and observer versions as required by the claim.
2. **Make semantic support explicit.** Every evidence item should name the criterion, public basis, applicability, locator, entailment or execution warrant, coverage limit, and accepted alternatives.
3. **Separate integrity from truth.** Signed/hash-matched evidence may still be wrong; preserve independent observer and calibration status.
4. **Type independence.** Record model/provider family, prompt, evidence view, operator, training lineage where known, session, key, and shared-failure threats rather than counting hosts alone.
5. **Use a transition confusion matrix.** Preserve correct/incorrect advance, stop, repair, collateral failure, and invalidity rather than one “not amplified” bucket.
6. **Estimate risk-adjusted utility.** Combine natural fault prevalence, consequence severity, false-stop loss, repair probability, reviewer burden, latency, token/tool cost, and escalation capacity.
7. **Require immutable public evidence for reviewable claims.** A paper pointing to an empty release endpoint cannot receive a reproduced status even if its internal ledger says verified.

### Test

1. **Receipt mutations:** stale task/artifact/grader/environment; replay; wrong task; partial command set; command drift; path/symlink substitution; untracked output; dependency drift; service drift; key compromise; producer collusion; signed false output.
2. **Alternative-valid evidence:** equivalent commands, different artifact paths, alternate correct derivations, authorized substitute producers, accepted partial/degraded states, and justified exceptions; measure false blocks.
3. **Policy factorial:** no observation, advisory observation, enforced stop, enforced repair, and human escalation under matched evidence and budgets.
4. **Trap prevalence factorial:** clean, planted visible-pass/hidden-fail, organic adjudicated faults, ambiguous requirements, incomplete observers, and invalid environments across task families.
5. **Quorum dependence:** same versus different model/provider/prompt/evidence-view reviewers; estimate correlated errors and marginal catches rather than counting nominal identities.
6. **Transition utility:** downstream artifact correctness, safety, collateral state, time, tokens, human burden, prevented loss, unjustified delay, and recurrence.
7. **Release reconstruction gate:** verify that every quantitative claim maps to immutable rows, analysis, configuration, exclusions, and table builders before promotion.

## Concrete repository actions

- [x] Read the complete immutable 48-page v1 PDF/text and inspect the TeX source/provenance.
- [x] Recheck the paper's advertised GitHub organization; it still exposed zero public repositories.
- [x] Reconstruct actors, claims, evidence records, source bindings, receipt identity, trust assumptions, lifecycle states, gate predicates, review floor, policy arms, endpoints, costs, exclusions, and self-application selection from the full paper.
- [x] Separate mechanical admissibility, gate enforcement, hidden-fault mitigation, semantic correctness, workflow utility, professional validity, production fitness, and readiness.
- [x] Record implementation, preregistration, mechanism fixtures, raw cells, corpus, and exhibits as unavailable rather than treating paper narration as reproduced evidence.
- [x] Add no build task. Existing benchmark-bundle, provenance-boundary, information-flow entitlement, artifact admissibility, configured-system, task-health, metric-monitoring, validity-argument, adversarial-verifier, release-reconstruction, and transition/repair machinery already houses the requirements. A Proof-or-Stop-specific schema would duplicate them.
- [ ] A later consolidator should add the four-predicate observation-authenticity/applicability/semantic-sufficiency/transition-authorization split and the transition confusion matrix to canonical synthesis if these are not already represented. This is a bounded consolidation implication, not a new subsystem.

## Bottom line

Proof-or-Stop names a real and underappreciated category error: an agent's success narrative, a tool's green status, an authentic receipt, a reviewer verdict, and an authorized lifecycle transition are different objects. Its formal spine, honest degraded-assurance semantics, advisory-versus-enforced contrast, block-all negative control, and explicit claim ceilings are directly useful to `skill-bench`.

The evidence cannot carry the paper's broader practical tone. The advertised release is unavailable; the preregistration and raw records cannot be audited; the powered study does not execute the receipt-gated lifecycle; the primary result is not equal-spend and is almost entirely one task; the main powered arm never stops; source hashes omit much executable state; and no test establishes semantic sufficiency or valid-alternative completeness. Self-application adds plausible defect exhibits but not an independent effect estimate.

The warranted transfer is therefore precise: **treat consequential state as an evidence-authorized transition, then validate authenticity, current applicability, semantic sufficiency, and decision policy separately**. Evaluate gates on both false promotion and false refusal, under matched advisory/enforced conditions, with natural trap prevalence and downstream costs. Fresh evidence can license a transition under a declared policy; it cannot by itself prove the work is correct or the policy is useful.

## Source links

- Immutable abstract: <https://arxiv.org/abs/2607.14890v1>
- Immutable PDF: <https://arxiv.org/pdf/2607.14890v1>
- Immutable source: <https://export.arxiv.org/e-print/2607.14890v1>
- Advertised implementation organization: <https://github.com/Proof-or-Stop>
- Local release-availability provenance: `data/sources/releases/2607.14890v1-proof-or-stop/provenance.json`

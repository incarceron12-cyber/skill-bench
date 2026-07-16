# CAVA: deterministic hashing is not yet canonical action identity, and receipt integrity is not execution evidence

## One-sentence contribution

CAVA identifies a real cross-runtime evaluation problem—approvals, policies, traces, and receipts need a stable semantic action object rather than raw command text—but the paper's perfect 96-seed/384-variant results cannot be reproduced from the official open-core release, whose two fingerprint paths disagree about runtime portability and whose verifiers accept several malformed, stale, or self-consistent-but-unbound objects while observing no execution outcome.

## Why this matters for `skill-bench`

This review advances charter objectives A, B, and C through a domain-neutral action-observation boundary. A knowledge-work agent may enact the same consequential operation through a shell, browser, SDK, workflow, or managed runtime. Conversely, similar-looking calls may differ in target, principal, snapshot, destination, data scope, or effect. A benchmark therefore needs to know whether two records denote the same proposed action, whether approval covered that exact action in that context, whether dispatch occurred, and whether the intended or collateral state transition was observed.

CAVA's useful direction is to make this identity explicit and portable. Its failure is equally useful: **a deterministic digest only preserves whatever equivalence relation and omissions its schema already encodes**. Hash equality does not validate semantic equivalence; hash inequality does not establish materially different effects; a valid receipt hash does not establish authorization, freshness, dispatch, execution, or outcome.

## Sources and reading record

### Immutable primary source read in full

- Zexun Wang, *CAVA: Canonical Action Verification and Attestation for Runtime Governance of Agentic AI Systems*, arXiv:2607.13716v1 (15 July 2026): <https://arxiv.org/abs/2607.13716v1>
- Immutable PDF: `data/papers/pdfs/2607.13716v1-cava.pdf` (35 pages; SHA-256 `772fb3e6fb9cb9bea6708be776d681d61b4dbc7326bfd5327b5200ff0d7fcec6`)
- Full layout extraction: `data/papers/text/2607.13716v1-cava.txt` (SHA-256 `13eabbc7f7051006fc7793532e6af54329e18202f91aa1cc9643a97a801a7097`)
- Metadata: `data/papers/source/2607.13716v1-metadata.xml`
- Date read: 2026-07-17 UTC.

### Official release inspected and executed

- Repository: <https://github.com/OndCo/CAVA>
- Audited commit: `bbaf21b33cc46683923906c255cd465be3419d0f`; tree `832a2d7407770d10cdb65c10e4014cfe9556407a`
- Archive: `data/sources/releases/2607.13716v1-cava/OndCo-CAVA-bbaf21b.zip` (SHA-256 `1cedd8992a22522af136801f34935abd3581afdc95b9ea5584fcbced679843e3`; 36 files; 237,833 uncompressed bytes; Apache-2.0)
- Provenance: `data/sources/releases/2607.13716v1-cava/provenance.json`
- Release audit: `data/sources/releases/2607.13716v1-cava/release-audit.json`
- Executed mutation evidence: `data/sources/releases/2607.13716v1-cava/release-mutation-audit.json` (SHA-256 `3e0e63cc9d972e37ccbaa5163cb101a38d24148e4291208d7209bed44e95d729`)

The repository's first public commit is timestamped 6 minutes 20 seconds after the arXiv submission. The audited next-day commit corrects the arXiv identifier. It is official current-release evidence, not proof of the byte-identical paper-time implementation.

## Research question and claim boundary

The paper asks whether heterogeneous runtime records can be transformed into a stable action identity to which policy outcomes, approvals, receipts, and attestations bind. It seeks six properties: semantic equivalence, semantic separation, wrapper robustness, approval binding, receipt reproducibility, and runtime portability (Section 3.2, p. 4). A later semantic-pattern layer maps action, boundary, and data context into policy-addressable risk patterns (Section 4.4, pp. 6–7).

The strongest auditable question is narrower: does the released open-core code at the pinned post-v1 commit implement a coherent action equivalence relation, fail-closed validation, and verifiable bindings over its declared objects, and can it reproduce the paper's public benchmark?

It cannot support the larger governance claim. The paper explicitly withholds production parser packs, PCAA routing, approval workflows, evidence graphs, replay, exports, signers, KMS/HSM integrations, managed connectors, and production policy thresholds (Table 4, p. 8; Appendix Z, p. 33). Those are not peripheral details: they determine what was parsed, who had authority, whether an approval remained current, what executed, and what evidence closes the action.

## Methodology and system

### Paper architecture

The main manuscript proposes a nominal capture → normalize → interpret → fingerprint → bind → close → attest protocol (Section 4.1, p. 5). The canonical action is defined as `(schema version, runtime family, executable/tool, operation, category, systems touched, reversibility, target/subject, bounded metadata)`, serialized deterministically and hashed (Definitions 1–2, pp. 3–4; Table 1, p. 6).

The paper then adds:

1. a semantic-pattern detector over canonical action, boundary, and data context;
2. policy profiles that route patterns;
3. PCAA as final authority and closure;
4. a bounded action-firewall lease tied to fingerprint, policy, actor, session, proof, and time;
5. an exposure graph connecting actors, sessions, actions, destinations, receipts, and incidents; and
6. optional signatures, credentials, supply-chain attestations, or ledger anchors (Sections 4.4–4.6, pp. 6–8).

This layering is conceptually sound because object identity, risk interpretation, enterprise posture, authority, enforcement, observation, and attestation are different functions. The released implementation, however, contains only a small subset.

### Claimed benchmark

The paper reports 96 seed scenarios expanded into 384 variants across shell, MCP, browser, and managed-agent runtime families (Section 6.1, p. 9). Table 5 reports CAVA at 1.000 on all nine metrics, against literal-text and first-token baselines. Table 6 lists scored suites for equivalence (12), separation (8), wrappers (14), benign contamination (7), approval drift (8), receipt tampering (8), runtime portability (16), and semantic patterns (6), plus structured policy-degradation (8), Azure drill (6), and red-team casebook (24) material (pp. 10–11).

The mapping from the 96 seeds/384 variants to these partially overlapping counts is not published. The paper supplies no per-case table, split, seed-generation rule, runtime projection mapping, raw baseline output, aggregation script, uncertainty, independent labels, held-out parser challenge, or authoring/rejection inventory. “Semantic separation precision” is defined as the fraction of designated different pairs that do not collide (Appendix Q, p. 28), not precision over an independently sampled positive/negative population. Most baseline zeros for receipts, approvals, attestations, portability, and patterns follow because the baselines lack those mechanisms, rather than from matched alternative implementations.

The same author defines the schema, parser expectations, cases, equivalence labels, separation labels, patterns, expected routes, baselines, implementation, and claims. The paper correctly calls the corpus regression evidence, not universal evidence (p. 10), but perfect in-sample conformance is particularly weak without independent semantic adjudication or adversarial holdout.

### Released implementation

The archive provides:

- a permissive canonical-action constructor and validator (`packages/cava-core/src/schema.js`);
- stable object-key serialization and a local SHA-256 implementation (`hash.js`);
- runtime-adapter and parser-pack interfaces (`adapter.js`, `parser-pack.js`);
- a second CAVA-IR object and `semantic_key` (`ir.js`);
- local receipts (`receipt.js`);
- approval and aggregate verification helpers (`verify.js`);
- telemetry and in-toto-style projections (`projections.js`);
- six disclosure-safe reference parser packs (`reference-packs.js`); and
- five unit tests (`tests/cava-core.test.js`).

`npm ci && npm run verify` passed: the open-boundary string scan covered 13 files, all 5 Vitest tests passed, and the package dry-run produced 15 files (16.0 kB packed; 55.0 kB unpacked). This is genuine executable evidence for packaging and those five examples. It is not the paper benchmark.

## Paper-to-release conformance

Part III says the public manuscript artifact contains `benchmarks/source-benchmark.mjs`, `benchmarks/latest.json`, `benchmarks/publication-latest.json`, `artifacts/MANIFEST.md`, `artifacts/REPRODUCE.md`, and `main.pdf` (pp. 33–34). None is present at the audited commit. No `benchmarks/` or `artifacts/` directory exists. The archive therefore cannot regenerate:

- the 96 seeds or 384 variants;
- any Table 5 metric;
- the claimed semantic-pattern suite;
- policy-degradation or Azure drill coverage;
- the 24 red-team case outcomes;
- the ablation scores; or
- the claimed raw-text/first-token comparisons.

The release does include `paper/main.tex`, examples, library code, and five tests. This is a substantial mismatch between the reproducibility protocol and the official public artifact, not merely an omitted large dataset.

## Executed mutation audit

The bounded audit imported the pinned release directly and exercised declared invariants and malformed cases. Exact outputs are retained in `release-mutation-audit.json`.

### What worked

1. Object-key order is invariant under the custom serializer.
2. The CAVA-IR `semantic_key` converged for an otherwise identical shell-versus-MCP example because runtime family and adapter are excluded from its semantic seed.
3. The bundled approval tests and the audit reject an honestly recomputed changed semantic key and a changed action ID.
4. Receipt payload mutation without recomputing the outer receipt hash is detected by the basic verifier.

### What failed or remained unbound

1. **Two identity systems disagree.** `canonicalizeRuntimeEvent()` hashes the entire canonical action, including runtime, adapter, executable, array order, and metadata. Changing shell to MCP changes that fingerprint. CAVA-IR excludes runtime but includes actor, operation `raw`, authority policy, and boundary defaults. Thus one “canonical” path is runtime-specific while the other is runtime-portable but surface- and policy-sensitive. The paper does not state which digest approval, receipts, projections, and benchmark portability actually use.
2. **Wrapper equivalence fails in CAVA-IR when `operation.raw` changes.** Two otherwise identical actions with raw strings `git push` and `env git push` receive different semantic keys. That contradicts the stated wrapper-rewrite goal unless adapters erase `raw` before IR construction.
3. **Set semantics are not normalized.** Reordering `systems_touched` changes the canonical fingerprint because arrays remain ordered. The paper calls `S` a set (Definition 1, p. 3), but the implementation hashes list order.
4. **Unknown defaults validate.** `createCanonicalAction({})` fills `runtime`, `operation`, and `category` with `unknown`, uses an empty systems list, and defaults `reversible` to false; `validateCanonicalAction()` returns valid. Required-field presence therefore does not mean action identity is known.
5. **Parser failure does not fail closed.** A throwing parser pack produces a warning, then fallback canonicalization yields a valid unknown, non-reversible action and a normal fingerprint. No invalid/insufficient-coverage state is forced.
6. **Receipt verification does not bind the embedded action to the claimed fingerprint.** `buildCavaReceipt()` accepts a caller-supplied `canonical_fingerprint`; the audit supplied 64 `f` characters inconsistent with the embedded action. `verifyCavaReceipt()` still returned valid because it only checked self-consistency of the outer payload hash.
7. **Approval verification accepts an unsigned binding.** Removing `binding_hash` still returns `binding_satisfied`; the code checks mismatch only if the hash exists.
8. **Prefabricated semantic keys are trusted.** `normalizeIr()` accepts any object already carrying `semantic_key`. The audit changed the IR fields but copied the old key, and approval verification returned valid.
9. **Freshness and configured identity are absent.** Approval verification has no expected policy version/hash, adapter/parser-pack version, task/state snapshot, actor/session, expiry, lease, nonce, decision state, or current time argument. A deliberately old approval remained valid.
10. **No-observation “execution” passes.** `verifyCavaExecution({})` returns `{valid: true, reason: "execution_verified", checks: []}`. The helper checks optional receipt and approval objects only; it receives no dispatch, observation, state transition, exception, or closure evidence.
11. **Reference semantics are substring heuristics.** A `SELECT` statement containing `DELETE` only inside a SQL comment was classified as `database_mutation`. Browser, cloud, MCP, and Web3 packs similarly use small substring rules. They are appropriately labeled reference-only, but cannot substantiate the paper's production or broad semantic claims.
12. **Signatures and attestation are only projections.** The in-toto helper packages an IR and digest into a statement; no signer, key identity, trust root, signature validation, timestamp, revocation, or external anchor is implemented.

These findings do not show that the private OSuite layer has the same defects. They show that the public implementation cannot substantiate managed-layer claims and that even the open-core action/binding claim needs a stricter contract.

## Unique insight: canonicalization is a versioned, purpose-relative equivalence claim

CAVA's deepest reusable insight emerges from its own implementation divergence. There is no context-free “same action.” Identity depends on the decision for which equivalence is asserted.

- For **runtime portability**, shell and MCP surfaces may be irrelevant if operation, target, principal, effect, and authority are equal.
- For **forensic attribution**, runtime, adapter, parser version, raw event, and session must remain distinct even when semantic action identity converges.
- For **approval reuse**, target, principal, snapshot, policy, parser/adapter, expiry, data boundary, amount, and effect commitments may all be identity-bearing.
- For **outcome evidence**, proposed semantic identity is insufficient; dispatch, service acknowledgment, pre/post state, collateral effects, and closure must be separately observed.

A robust record therefore needs at least three linked hashes rather than one overloaded fingerprint:

1. `raw_event_evidence_hash`: immutable source event, runtime, adapter/parser version, capture mode, and provenance;
2. `semantic_action_hash`: a declared equivalence projection with typed fields, normalized sets/units, unknown-field policy, and schema/equivalence-policy version; and
3. `authorization_envelope_hash`: semantic action plus actor, policy, snapshot, session, expiry/nonce, budget/retry/delegation scope, and exact effect commitment.

An outcome receipt then binds those identities to an independently observable dispatch/result/state transition. It must not rename approval-object integrity “execution verification.”

This directly complements Context-to-Execution Integrity (CXI): CXI requires protected-field, exact-effect, and invocation authority to join on one manifest before a mediated sink. CAVA offers an inspectable candidate for the action identity inside that manifest, but its open verifier does not implement CXI's snapshot, field authority, lease consumption, exact-effect, or outcome boundaries.

## Comparison with adjacent reviewed evidence

- **Context-to-Execution Integrity** supplies the stronger field/effect/event authority join and complete-mediation claim boundary. Its artifact was unavailable; CAVA provides inspectable code but a much weaker public verifier. Together they show why a canonical semantic object and a mediated authority/effect ledger are complementary, not substitutes.
- **UnderSpecBench** separates private intent from public authorization and legitimate ask/inspect/act outcomes. CAVA assumes an action is already proposed and does not establish whether it was professionally justified or publicly authorized. Canonicalizing the wrong action perfectly does not make it legitimate.
- **Claw-Eval** routes requirements to final response, action log, and environment state. CAVA strengthens proposed-action identity, but the release has no authoritative environment observer. Its `execution_verified` label illustrates why request/receipt consistency must remain separate from committed effect.
- **WildClawBench** exposes transport drift across native harnesses, providers, adapters, images, and state-to-prose graders. CAVA's portability objective is relevant, but a digest projection cannot erase configured-package differences; adapter and runtime identities must remain in forensic/configuration records even when a semantic projection converges.

Existing action, trace, authority, state-transition, task-health, metric, and validity machinery are the correct repository homes. A CAVA-specific subsystem would duplicate them.

## Limitations and validity threats

1. The paper is a single-author system design, implementation report, benchmark, system card, product boundary, and commercial argument; no independent semantic labels, security review, or replication are reported.
2. The official release postdates v1 and does not prove paper-time implementation identity.
3. The claimed benchmark files and outputs are absent, blocking all numerical reproduction.
4. The 96-seed/384-variant frame has no released row inventory, generation logic, overlap map, or exclusions.
5. Perfect results are on author-defined representative cases with no held-out runtime, parser family, third-party traces, adaptive attack, or external red team.
6. Baselines are deliberately structurally incapable of several CAVA-only outputs, so zero-versus-one comparisons do not isolate canonicalization quality against credible alternatives.
7. Semantic-equivalence and separation truth is author-designated and not validated against runtime effects, service semantics, or expert review.
8. Two released fingerprint constructions encode inconsistent equivalence relations.
9. Defaults, unknowns, array ordering, raw fields, actor, policy, runtime, adapter, and metadata lack a documented field-by-field identity rationale.
10. Schema validation checks shape/presence weakly and accepts default-filled unknown actions.
11. Parser failure can degrade to a valid unknown object rather than an explicit invalid/insufficient-coverage verdict.
12. Approval bindings are local hashes, not authenticated signatures or demonstrated authority decisions.
13. Receipt self-consistency does not establish embedded action-fingerprint consistency.
14. Approval verification does not require its own hash, trusted recomputation of IR, freshness, current policy/snapshot, or signer authority.
15. `verifyCavaExecution` observes no execution and accepts an empty evidence set.
16. Semantic Pattern Layer implementation and scored cases are absent.
17. Production parsers, policy routing, leases, evidence graph, signers, and managed connectors are withheld; open-core success cannot be promoted to managed-system efficacy.
18. Azure evidence is a paper assertion about authentication and semantic drills; no retained command output or live mutation evidence is released.
19. Observer mode is explicitly not enforcement, and no inline mediation, bypass-route inventory, or complete-mediation canary is demonstrated.
20. No cost, latency, operator burden, false-approval consequence, parser-maintenance effort, incident rate, or production outcome is measured.
21. Hash collision resistance is not the practical bottleneck; semantic collision, omitted fields, normalization defects, stale context, and observer gaps dominate.
22. The paper appropriately excludes business wisdom, but its language occasionally slides from receipt integrity toward proving “what actually happened” without released outcome observations (pp. 12–13).

## Reproducibility and operational realism

The conceptual architecture is unusually explicit about open/managed boundaries, observe-versus-enforce posture, optional attestations, parser limitations, operator misuse, and residual risk. The small JavaScript package installs cleanly and its five tests pass. The retained mutation audit makes the open-core claim falsifiable.

Numerical reproducibility is absent because the artifact named by the paper is not in the official archive. Operational realism is also sharply bounded: reference parser packs use simple substrings; approvals are unsigned local objects; receipts are local hashes; no action is dispatched; no environment state is observed; no cloud mutation occurs; and no production parser, authority workflow, signer, or incident evidence is inspectable. The release supports a skeleton/interface claim, not a runtime-governance deployment claim.

## Transfer to `skill-bench`

### Retain

1. **Treat the action as a first-class versioned object.** Preserve runtime-native evidence separately from a semantic projection used for comparison or approval.
2. **Bind approvals to action meaning, not display text.** Include target, subject, principal, scope, exact effect, snapshot, policy, session, retry/delegation budget, expiry, and nonce where applicable.
3. **Separate coverage posture.** Record capture, normalization, enforcement, observation, and outcome-closure capabilities independently; observe-only is not inline blocking.
4. **Use deterministic serialization and independent replay.** Object-key ordering and hash recomputation are useful integrity checks after semantic fields are validated.
5. **Represent multi-action decomposition.** One event may combine policy weakening, deployment, data movement, or another consequential effect.

### Repair

1. **Declare the equivalence policy.** Every semantic hash should name the projection version and why each field is included, excluded, normalized, or treated as an unordered set.
2. **Fail closed on unknown/lossy parsing.** `unknown`, parser failure, omitted required context, schema drift, and unsupported multi-action commands need explicit insufficient-coverage outcomes, not ordinary valid fingerprints.
3. **Recompute every nested binding.** Verify semantic key from IR fields, action fingerprint from canonical action, receipt hash from receipt payload, and signatures from trusted keys; reject missing bindings.
4. **Separate integrity from authority and outcome.** Use labels such as `object_integrity_valid`, `approval_scope_valid`, `dispatch_observed`, `effect_observed`, and `closure_complete`; never infer execution from zero optional checks.
5. **Bind configured identity and freshness.** Parser pack, adapter, schema, policy, snapshot, actor/session, time window, and trust-root identities belong in the authorization envelope and trial record.
6. **Calibrate semantic equivalence against effects.** Include positive and negative near-neighbors across runtimes, aliases, wrappers, array/order encodings, units, amounts, targets, accounts, selectors, comments, chained actions, stale context, and partial observations. Validate labels independently.
7. **Preserve both convergence and forensic difference.** Equivalent semantic hashes may share an approval class while raw event/runtime/adapter hashes remain distinct for diagnosis and replay.

### Test

The next relevant action conformance slice should cross:

- equivalent surface / materially different effect;
- complete / lossy / failed parser;
- fresh / stale policy, snapshot, adapter, and approval;
- valid / missing / forged nested hashes and signatures;
- proposed / dispatched / acknowledged / committed / rolled back / collateral state;
- single action / compound action; and
- legitimate authorized action / under-specified action requiring inspection or clarification.

Report false convergence, false separation, invalid/insufficient coverage, approval mismatch, replay rejection, observer sufficiency, realized effect, and useful task outcome separately.

## Concrete repository actions

No new build task is added. The findings refine existing action/trace/state-transition, authority, execution-validity, task-health, metric, and validity contracts and overlap the completed Context-to-Execution action conformance work. The durable executable evidence is the pinned release audit and mutation record; future consolidation should integrate the three-hash/equivalence-policy distinction rather than creating a product-specific schema.

## Assessment

- **Evidence tier:** full immutable v1 paper plus executable audit of the official post-v1 open-core release.
- **Most reusable contribution:** action identity must become an explicit portable object before cross-runtime approval and trace comparison are possible.
- **Most important reproduced positive result:** deterministic object-key serialization, package/test execution, and bounded honest semantic-key mismatch rejection work in the small public skeleton.
- **Most serious empirical defect:** the official archive omits the benchmark and result artifacts named by the paper, so none of the 96-seed/384-variant perfect scores is independently auditable.
- **Most serious design defect:** the released identity and verification paths disagree about equivalence and accept unknown, unsigned, stale, pre-keyed, empty-evidence, or internally inconsistent objects as valid.
- **Claim `skill-bench` may safely make:** cross-runtime evaluation needs separate immutable raw-event evidence, a versioned purpose-relative semantic action projection, a freshness-bound authorization envelope, and independently observed execution/effect evidence; deterministic hash or receipt validity alone establishes none of semantic correctness, authority, execution, professional quality, safety, or readiness.

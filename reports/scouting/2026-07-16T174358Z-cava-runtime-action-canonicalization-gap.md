# Scouting note — CAVA runtime-action canonicalization gap

**Timestamp:** 2026-07-16T17:43:58Z  
**Evidence status:** arXiv API metadata/abstract, endpoint, GitHub repository metadata, commit identity, and pinned README triage only. The paper, implementation, benchmark cases, and results were **not** deeply read or audited in this scouting run.

## Substantive candidate

**CAVA: Canonical Action Verification and Attestation for Runtime Governance of Agentic AI Systems** — Zexun Wang, arXiv:2607.13716v1.

- Immutable record: https://arxiv.org/abs/2607.13716v1
- Immutable PDF: https://arxiv.org/pdf/2607.13716v1
- Immutable HTML: https://arxiv.org/html/2607.13716v1
- Official repository: https://github.com/OndCo/CAVA
- The arXiv API reports submission/update on 15 July 2026 in `cs.AI`; the abstract contains no withdrawal notice. Record, PDF, HTML, and repository endpoints returned HTTP 200.
- Repository `main` was verified at `bbaf21b33cc46683923906c255cd465be3419d0f` (`git ls-remote` and GitHub API). GitHub identifies an active, non-fork Apache-2.0 repository; the pinned README links arXiv:2607.13716 and exposes schemas, CAVA-IR, deterministic semantic hashing, approval binding, receipts, adapter/parser contracts, examples, tests, and manuscript source.
- The abstract reports a 96-seed, 384-variant reference-implementation benchmark spanning semantic equivalence/separation, wrapper bypass, false positives, approval binding, receipt reproducibility, attestation tamper detection, runtime portability, semantic patterns, policy degradation, and Azure deployment drills. These are author claims awaiting full-paper and release verification.
- The README explicitly excludes production parser packs, customer runtime enrichment, policy routing/authority workflows, calibrated decision scores, action leases, runtime-exposure graphs, managed replay/exports, enterprise signers, KMS/HSM, credential issuance, ledger anchoring, and hosted connectors. Open-core conformance therefore cannot be promoted into production-governance evidence.

## Why this is a narrow, useful gap

The corpus already covers Context-to-Execution Integrity's manifest-bound field/effect/event authority join, action-boundary pilots, multichannel trajectory/state observation, and native-runtime transport. Exact repository search found no CAVA review or queue task. CAVA is adjacent but nonduplicate: it targets the prior transformation needed to compare and govern actions across heterogeneous shell, SDK, browser, MCP, gateway, workflow, and managed-runtime records, and unlike the reviewed CXI paper it exposes an inspectable implementation.

The focused validity chain is:

`raw runtime event + adapter/parser identity → canonical action/IR → semantic equivalence or separation → fingerprint → policy-pattern match → approval bound to exact action identity → execution opportunity/effect → receipt and optional attestation → independent replay → cross-runtime transport claim`.

A deterministic hash only proves agreement with the canonicalizer; it does not prove that the canonicalizer retained every decision-relevant target, parameter, principal, snapshot, side effect, or temporal field. Likewise, a valid approval binding or receipt does not establish that execution occurred, the policy was legitimate, the outcome was professionally correct, or all bypass routes were observed. A release audit can test whether the claimed variants and mutation boundaries exist, whether unsupported/lossy adapters fail closed, and whether paper results can be reproduced from released evidence.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier production/runtime evaluation), B (authority and semantic-action representation), and C (trace, action, state, provenance, and validity machinery).
- **Concrete evidence/artifact:** immutable-v1 full-text review plus commit-pinned release audit, test replay, and bounded canonicalization/approval/receipt mutations.
- **Uncertainty clarified:** when heterogeneous runtime records support the same-action claim versus lossy collapse, wrapper bypass, stale binding, or configured-adapter differences.
- **Mode:** narrow expansion feeding validation and consolidation; not generic governance news or a commitment to a security product.
- **Duplication check:** CXI assumes a canonical manifest and had no inspectable artifact; current benchmark traces do not yet have audited cross-runtime semantic identity evidence.
- **Useful completion:** reconstruct paper/release objects and denominators; verify implementation and timing; test equivalence, separation, stale identity, replay, tamper, lossy adapter, and pattern false-positive boundaries; preserve distinct claim ceilings for schema conformance, semantic identity, approval, observed effect, policy validity, professional quality, safety, production fitness, and readiness.

Added one review task: `review-cava-runtime-action-canonicalization-validity` (priority 3), subordinate to the current build, consolidation, and human prerequisite. No second task was added. No claim is made that the full paper or benchmark was read, that the reported 384 variants are reproducible, that canonical hashes capture action semantics, that receipts prove execution, or that CAVA establishes end-to-end governance, professional validity, safety, production fitness, or readiness.

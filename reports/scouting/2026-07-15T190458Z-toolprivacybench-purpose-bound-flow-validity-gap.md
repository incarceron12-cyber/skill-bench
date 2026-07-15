# Scouting note — purpose-bound information-flow validity gap

**Timestamp:** 2026-07-15T19:04:58Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Queue inspection found 288 tasks: 282 completed, three blocked, and three pending (one human prerequisite, one consolidation, and one dependent build); no source, research, review, or claimed backlog remained. The reviewed corpus already covers contextual integrity, authority, tool safety, handoffs, audit traces, and privacy/consent boundaries, but not a benchmark whose primary instrument assigns task-private fields to purpose-specific tools and sinks and audits over-disclosure across an executed multi-tool trajectory.

## Substantive finding — triage only

**ToolPrivacyBench: Benchmarking Purpose-Bound Privacy in Tool-Using LLM Agents** — Shijing Hu, Liang Liu, Zhu Meng, and Zhicheng Zhao; arXiv:2606.28061v1.

- Immutable record: https://arxiv.org/abs/2606.28061v1
- Immutable PDF: https://arxiv.org/pdf/2606.28061v1
- Immutable HTML: https://arxiv.org/html/2606.28061v1
- Paper-associated placeholder repository pinned during scouting: https://github.com/HuShijing123/ToolPrivacyBench/tree/51d13355a8cb78d80c45b756dd347e94c40327e6
- The arXiv API identifies immutable v1 as submitted 26 June 2026 in `cs.CR` and `cs.AI`; its abstract contains no withdrawal or retraction notice. The versioned abstract, PDF, and HTML endpoints returned HTTP 200 during scouting.
- The abstract describes 2,150 cases: 1,150 fully synthetic privacy-sensitive business workflows and 1,000 adaptations of multi-tool/function-calling benchmarks. Each case reportedly uses a policy knowledge base; evaluation compares tool arguments and mock-backend audit logs with purpose-bound authorization policy.
- The abstract reports evaluation of nine agents and says successful task execution can coexist with unnecessary private-data transmission through intermediate calls. These are author-reported abstract claims, not independently verified results.
- Structural inspection of immutable-v1 HTML—not a full reading—confirmed sections on private atoms, tool purposes, information sinks, field–tool authorization matrices, executable evaluation, utility and several leakage metrics, annotation/QC, aggregation, path analysis, healthcare/tax/code-security failures, disclosure-detector checks, and weight sensitivity. The HTML exposed no project release link.
- Search located `HuShijing123/ToolPrivacyBench`. GitHub API inspection found a public non-fork repository created 27 June 2026, no detected license, and one root `README.md` at sole/default-branch head `51d13355a8cb78d80c45b756dd347e94c40327e6`; the search result and repository description identify it as a placeholder pending release. No README body, code, data, policy record, prompt, trace, result, or evaluator was read or executed.
- Repository-wide exact-title, arXiv-ID, and repository searches found no local review or queue task. One SovereignNegotiation full-text extraction cites ToolPrivacyBench, and one earlier scout mentions it only as adjacent work. Closest completed reviews include PISAS/contextual integrity, GroundEval, EntCollabBench, SovereignPA-Bench, and ClawSafety; none makes purpose-specific minimum-necessary routing across multi-tool trajectories its primary construct.
- This is **metadata, abstract, endpoint, section-structure, release-location, commit/root-inventory, and duplicate triage only**. The paper body, appendices, cases, adaptation lineage, policy records, private atoms, annotation, tools, mock backends, prompts, trajectories, metrics, detector labels, results, errors, costs, and statistics were not read or audited. No claim is made that the authorization matrices encode legitimate policy, private fields were actually necessary or unnecessary, tool purposes/sinks are complete, audit logs observe every disclosure, free-text detectors are valid, adapted cases preserve their source construct, results reproduce, or the benchmark establishes privacy safety, professional validity, production fitness, or readiness.

## Why this is distinct

The reusable chain is `data/source authority and current purpose → private atom and sensitivity → actor/tool/sink authorization → minimum-necessary field set → agent availability and exposure → call argument or free-text transmission → backend receipt and persistence → task-state consequence → utility and disclosure severity → remediation/recipient impact`. Correct completion does not establish appropriate disclosure, but agreement with an author-created field–tool matrix does not by itself establish legitimate privacy policy either. A mock environment can co-author the workflow, necessity boundary, tools, sinks, and observer, while alternate valid paths or optional disclosures remain unrepresented.

A full audit should separate policy authority, purpose and sink semantics, availability/exposure/adoption/transmission, direct versus inferred disclosures, free-text detector reliability, observer coverage, utility, severity, legitimate alternative paths, adapted-case lineage, aggregation, repeats, configured-system identity, and transport. Comparison with existing contextual-integrity, authority, handoff, trace, safety, metric, and validity machinery should determine whether this source adds evidence and failure signatures rather than justify a parallel privacy schema.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier realistic-agent safety evaluation), B (domain policy transformed into explicit purpose and disclosure thresholds), and C (trajectory, sink, audit-log, utility, and safety checks).
- **Concrete evidence/artifact:** immutable-v1 deep review plus a timing-aware audit of the pinned placeholder release.
- **Uncertainty clarified:** whether ToolPrivacyBench measures purpose-bound minimum-necessary disclosure with a valid observer and policy authority, or mainly closed-world agreement with co-authored matrices and mock workflows.
- **Mode:** narrow expansion feeding later consolidation; privacy-sensitive workflows are a cross-domain integrity stress case, not a privacy-only benchmark scope.
- **Duplication/scope:** no exact local duplicate; mandatory comparison with PISAS, GroundEval, EntCollabBench, SovereignPA-Bench, and ClawSafety prevents redundant machinery.
- **Useful completion:** a claim ladder separating policy authority, atom necessity, exposure, transmission, observer detection, endpoint utility, severity, transport, professional validity, safety, production fitness, and readiness, grounded in exact paper/release locators.

Added one low-priority task: `review-toolprivacybench-purpose-bound-flow-validity` (priority 5). The consented expert micro-pilot, request-receipt consolidation, and delayed-obligation pilot remain substantially higher priority.

## Operational note

The required initial `git pull --ff-only` succeeded. Pre-existing untracked paper-source, release-archive, and site files were not touched.

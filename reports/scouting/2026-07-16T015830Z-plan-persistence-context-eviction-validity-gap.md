# Scouting note — plan persistence and context-eviction validity gap

**Timestamp:** 2026-07-16T01:58:30Z

**Scope:** Narrow expansion against charter objectives A/B/C. Queue inspection found 303 tasks: 298 completed, three blocked, two pending, and no claimed work. The high-priority backlog is already healthy: one held-out-obligation consolidation and one real consented expertise-elicitation prerequisite. Existing reviews cover context compression (ACON), compaction-induced governance-treatment drift, decision fidelity under compression, prospective obligations, experience memory, and persistent state writes. This run searched only for the narrower boundary between information remaining in the visible context and information actually carried by the agent after that text is removed.

## Substantive finding — triage only

**Plans Don't Persist: Why Context Management Is Load Bearing for LLM Agents** — Aman Mehta and Anupam Datta; arXiv:2606.22953v1.

- Versioned record: https://arxiv.org/abs/2606.22953v1
- Versioned PDF: https://arxiv.org/pdf/2606.22953v1
- Versioned HTML: https://arxiv.org/html/2606.22953v1
- arXiv search metadata dates the paper to 22 June 2026. Search-result metadata identifies the authors as Aman Mehta and Anupam Datta and describes the paper as a preprint in `cs.AI`; a full review must verify all metadata against the immutable paper.
- The arXiv abstract/search excerpt says long-horizon agents depend on compression, summarization, and eviction, which are safe only if removed information is no longer needed or has been internalized. It names plans as a stress case because they are written early, used over many steps, and likely to be evicted.
- Immutable-HTML search metadata says the paper introduces **replay pairing**: rerun the same trajectory with and without the plan in history and measure hidden-state cosine distance. Secondary indexing of the paper says the plan signal spikes after planning and decays rapidly, while context eviction harms ALFWorld performance. These are author-reported/indexed claims, not independently verified results.
- Targeted title/code searches found the paper and secondary indexes but no clearly official repository or released run archive. A full review must inspect the paper's links, data/code statement, appendices, and author surfaces before concluding that no release exists.
- Repository-wide searches found no exact title, arXiv ID, replay-pairing, or plan-protection review/task. The closest completed evidence is adjacent but nonduplicative: ACON studies task-sufficient compression; Governance Decay studies whether constraints survive compaction; decision-fidelity work studies preservation of a named downstream decision instrument; prospective-memory work studies delayed action. This paper appears to intervene directly on plan visibility and probe whether the configured model carries plan information after removal.
- The arXiv helper script named by the invoked skill is not present in this repository, and the attempted API pipeline was blocked by the execution safety scanner before retrieval. This note therefore relies only on arXiv/web search metadata and local duplicate checks. The paper body, appendices, models, prompts, trajectories, hidden states, replay construction, controls, ALFWorld tasks, context-management policies, statistics, costs, and any code/data were not read or executed. No claim is made that cosine distance measures usable plan state, replay pairs are causally isolated, eviction is the sole cause of performance loss, findings transport to tool-using knowledge work, or the paper establishes context-policy safety, capability, production fitness, or readiness.

## Why this is distinct

The reusable chain is `task/source requirements → generated plan propositions and authority → visible context placement → context-management event and retained/removed tokens → latent-state probe → subsequent action/tool choice → artifact/state consequence → recovery or rereading opportunity → cost and reliability`. Visible plan text, latent representational similarity, behavioral adoption, and successful consequence are different observations. A low hidden-state distance after removal need not prove that a plan is unusable; a high distance need not prove that the plan governs later action. Likewise, an eviction-related endpoint decline can identify a configured context-treatment effect without establishing which proposition was lost or whether compression, position, replay mismatch, or downstream observation differences caused it.

A full audit should reconstruct the replay-pair construction; identify what is held fixed; separate plan generation, plan visibility, token position, context budget, observation history, model family, reasoning mode, and tool/environment effects; inspect probe-layer/time selection and multiple-comparison risks; connect latent distances to proposition-level plan obligations and later actions; distinguish exact rereading from internalization and environment re-observation; preserve task/trial/seed/invalid denominators and clustered uncertainty; and compare endpoint effects with plan-content corruption, irrelevant-plan, protected-plan, and matched-budget controls. Existing configured-system, context-state, trace, obligation, artifact/state, task-health, metric, and validity machinery should host reusable lessons unless an exercised nonduplicate contract gap is proven.

## Charter decision filter and queue action

- **Objectives advanced:** A (context/memory and long-horizon evaluation frontier), B (separating visible procedural guidance from internalized and behaviorally adopted knowledge), and C (paired context interventions, latent probes, traces, and endpoint consequences).
- **Concrete evidence/artifact:** immutable-v1 full-paper review with exact replay-pair, probe, behavioral, endpoint, denominator, and release evidence.
- **Uncertainty clarified:** whether replay pairing validly distinguishes context-resident plan text from persistent usable plan state, and what observations are required before an eviction effect supports a context-policy claim.
- **Mode:** narrow expansion feeding later consolidation/validation; ALFWorld is a method test bed, not a household-agent scope commitment.
- **Duplication/scope:** no exact local duplicate; mandatory comparison with ACON, Governance Decay, decision-fidelity compression, PM-Bench, and context/configured-system machinery prevents a parallel memory ontology.
- **Useful completion:** a claim ladder separating text retention, latent representation, behavioral adoption, task consequence, context-policy reliability, cross-task transport, production fitness, and readiness, with exact controls and missing-artifact boundaries.

Added one low-priority review task, subordinate to the held-out-obligation consolidation and real-expert prerequisite.

# Scouting note — outcome evidence and shared-context integrity gaps

**Timestamp:** 2026-07-11T09:43:18Z  
**Scope:** Narrow expansion against charter objectives A/B/C/D after confirming 93 completed tasks, two pending consolidation tasks, two blocked tasks, and no existing repository references to either source. This run did not repeat broad benchmark discovery.

## Substantive findings (triage only)

### Evidence-supported bounds for interactive-agent evaluation

- Immutable arXiv v1: https://arxiv.org/abs/2605.10448v1
- The arXiv API abstract reports an outcome-evidence layer that pre-specifies required stored artifacts, assigns Evidence Pass/Fail/Unknown using a locked checklist, and reports score bounds rather than silently collapsing unknown outcomes. It reports application to AndroidWorld, AgentDojo, AppWorld, tau3-bench retail, and MiniWoB.
- This is directly relevant to skill-bench's artifact-view and evidence-state machinery: it may provide empirical evidence that successful evaluator outputs do not necessarily establish intended state change.
- **Evidence status:** arXiv metadata and abstract triage only. The paper, appendices, cases, annotation procedure, calculations, and any release were not read. The reported failure modes and effectiveness of the layer are not yet verified.

### PiSAs: contextual integrity in multi-user agentic systems

- Immutable arXiv v1: https://arxiv.org/abs/2607.05318v1
- The arXiv API abstract introduces dual annotations for whether information is task-appropriate and which users may legitimately access it, with measurement surfaces spanning outputs, inter-agent messages, and memory under different topologies and memory regimes.
- This fills a narrow corpus gap between existing prompt-injection/workspace-integrity reviews and authorization-sensitive information flow in shared organizational agents. It suggests that relevance and recipient authority may need to remain distinct checks.
- **Evidence status:** arXiv metadata and abstract triage only. The paper, dataset, annotations, experiments, implementation, and release were not read; no claim is made about ecological validity, annotation reliability, leak coverage, benign utility, or causal effects of topology or memory design.

## Queue action and decision filter

1. Added `review-outcome-evidence-score-bounds` (priority 57).
   - **Objectives:** A/B/D; **mode:** validation-focused expansion.
   - **Artifact/evidence:** immutable full-text review and release audit with an outcome-evidence failure taxonomy and bounded implications.
   - **Uncertainty:** when stored observations support a success label or only a score interval.
   - **Useful completion:** reconstruct estimands, adjudication, empirical failures, reliability, and limitations across the five evaluated families.

2. Added `review-pisas-contextual-integrity` (priority 56).
   - **Objectives:** A/B/C; **mode:** narrow safety/workspace expansion.
   - **Artifact/evidence:** immutable full-text and release audit of information authority across memory/messages/outputs.
   - **Uncertainty:** whether task relevance and recipient authorization are separable, reliably annotated and observable across configured systems.
   - **Useful completion:** reconstruct provenance, annotations, topology/memory treatments, scoring, utility tradeoffs, errors, and release inspectability.

Neither task commits the benchmark to one domain. Both test reusable measurement boundaries, duplicate no indexed review or queued task, and require full primary-source reading before methodological claims.

# Knowledge-Work Task Metadata Template

Use this template when drafting a new `skill-bench` scenario. The goal is to capture enough metadata at authoring time to support scoring, calibration, leakage control, reduced evaluation panels, and root-cause diagnosis later.

## 1. Task identity

- **Task ID:**
- **Scenario name:**
- **Domain:** finance / product / legal ops / nonprofit / healthcare admin / local government / research ops / other
- **Version:**
- **Author(s):**
- **Expert reviewer(s):**
- **Public visibility:** public prompt / public sample / private pack / internal calibration only
- **Estimated human time:**
- **Estimated agent time budget:**

## 2. Professional context

- **Role of the agent:** e.g. analyst, chief of staff, grant strategist, product ops lead.
- **Intended stakeholder:** e.g. board, executive director, investment committee, product leadership.
- **Decision being supported:** what real decision would this work affect?
- **Professional standard:** what would make the deliverable actually useful to the stakeholder?

## 3. Source corpus metadata

- **Source files:** list filenames, formats, and whether each is public/private/synthetic.
- **Source count:**
- **Evidence dispersion:** low / medium / high — how spread out is the needed evidence?
- **Contradiction count:** number of deliberate conflicting signals.
- **Staleness / versioning issues:** any outdated docs, stale exports, or conflicting dates?
- **Trusted-source hierarchy:** which sources should override others?
- **Noise files:** irrelevant or distracting files included intentionally.
- **Multimodal elements:** screenshots, PDFs, spreadsheets, charts, email, Slack, calendar, database, SaaS UI.

## 4. Domain-knowledge primitives

For each primitive, note whether it is public, private, or hidden from the agent but used in scoring.

| Primitive | Description | Visibility | Related source(s) | Related rubric check(s) |
|---|---|---|---|---|
| Hidden requirement |  |  |  |  |
| Expert caveat |  |  |  |  |
| Contradictory evidence |  |  |  |  |
| Judgment threshold |  |  |  |  |
| Artifact convention |  |  |  |  |
| Stakeholder preference |  |  |  |  |
| Polished-but-wrong trap |  |  |  |  |
| Safety/compliance constraint |  |  |  |  |

## 5. Deliverables

| Deliverable | Format | Required? | Main evaluation dimension | Notes |
|---|---|---:|---|---|
|  | spreadsheet / memo / deck / notebook / ticket / diagram / other | yes/no | accuracy / structure / presentation / judgment |  |

For each deliverable, specify:

- **Minimum acceptable artifact:**
- **Excellent artifact:**
- **Common novice failure:**
- **Common polished-but-wrong failure:**
- **Machine-checkable parts:**
- **Human/LLM-judge parts:**

## 6. Rubric and verifier design

Each check should be small enough to track historical pass rates.

| Check ID | Description | Type | Weight | Visibility | Expected answer / criterion | Root-cause tags |
|---|---|---|---:|---|---|---|
|  |  | deterministic / spreadsheet / state / LLM judge / human judge / pairwise |  | public / private / hidden |  |  |

Recommended root-cause tags:

- `source_discovery_failure`
- `evidence_reconciliation_failure`
- `calculation_failure`
- `artifact_structure_failure`
- `artifact_format_failure`
- `stakeholder_judgment_failure`
- `presentation_failure`
- `tool_use_failure`
- `context_management_failure`
- `instruction_following_failure`
- `safety_or_compliance_failure`
- `ambiguous_task_design`

## 7. Workflow checkpoints

Use checkpoints when the task has meaningful intermediate state, multi-app workflow, or staged reasoning.

| Checkpoint ID | Expected intermediate state | Verification method | Weight | Failure meaning |
|---|---|---|---:|---|
|  |  | file diff / database state / spreadsheet cell / memo section / trace evidence / screenshot |  |  |

## 8. Difficulty metadata

Record rough author estimates first; replace with observed estimates after enough runs.

- **Expected difficulty:** easy / mid / hard / frontier
- **Expected pass-rate band:** 0–10% / 10–30% / 30–70% / 70–90% / 90–100%
- **Difficulty drivers:**
  - source volume
  - evidence dispersion
  - hidden requirements
  - contradictions
  - numerical reasoning
  - artifact maintainability
  - professional taste
  - tool complexity
  - long-horizon state tracking
  - domain-specific terminology
  - verifier strictness
- **Editable difficulty knobs:** what can be varied to create easier/harder counterfactual versions?
- **Potential mid-difficulty checks:** checks likely to become useful for a reduced evaluation panel after calibration.
- **Rare-but-important checks:** checks to preserve for diagnostic coverage even if too easy/hard for ranking.

## 9. Scaffold and tool assumptions

- **Allowed tools:** browser / shell / Python / spreadsheet editor / office suite / SaaS UI / search / memory / other.
- **Disallowed tools:**
- **Expected file operations:**
- **External network allowed?** yes/no
- **Memory allowed?** yes/no
- **Retries allowed?** yes/no
- **Known scaffold sensitivities:** what parts of the task depend heavily on UI control, file editing, retrieval, or tool policy?

## 10. Trace and failure-learning plan

- **Trace data to preserve:** prompts, tool calls, intermediate files, final artifacts, screenshots, logs, judge rationales.
- **Causal-slice questions:**
  1. Where did the failure surface?
  2. Where did the failure originate?
  3. Which source/check made the failure detectable?
  4. Was this a good capability-revealing failure or a task-design flaw?
- **Failure postmortem output path:**
- **Recurring failure mode bucket:**

## 11. Leakage and release controls

- **Public prompt includes:**
- **Public sample includes:**
- **Private calibration includes:** reference artifacts, expected answers, verifier internals, hidden traps, task-feature labels.
- **Can this task be reused after public release?** yes/no/only as demo
- **Leakage risks:**
- **Mitigations:** paraphrase variants, private source pack, hidden checks, rotating variants, delayed release.

## 12. Response-matrix fields to log per run

At minimum, each run/check should produce rows with:

- `run_id`
- `task_id`
- `task_version`
- `check_id`
- `model`
- `scaffold`
- `skills_enabled`
- `tool_policy`
- `memory_policy`
- `outcome`
- `score`
- `cost_usd`
- `duration_seconds`
- `timestamp`
- `benchmark_version`
- `root_cause_tag`
- `artifact_path`
- `trace_path`

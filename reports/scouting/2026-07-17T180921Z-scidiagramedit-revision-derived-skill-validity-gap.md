# Scouting note — revision-derived skill and editable-artifact validity gap

- **Timestamp:** 2026-07-17T18:09:21Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, HTML link triage, targeted web/release discovery, and exact local duplicate search only. The paper body, revision corpus, editable vector sources, instructions, split records, skill versions, traces, graders, human judgments, and any implementation were **not** deeply read, downloaded, executed, or audited during scouting.

## Substantive candidate — triage only

**SciDiagramEdit: Learning to Edit Scientific Diagrams from Paper Revisions** — Yasheng Sun, Zezi Zeng, Yifan Yang, Chong Luo, Wenyi Wang, Ziwei Liu, and Jürgen Schmidhuber; arXiv:2607.15272v1.

- Immutable record/PDF/HTML: https://arxiv.org/abs/2607.15272v1 · https://arxiv.org/pdf/2607.15272v1 · https://arxiv.org/html/2607.15272v1
- The arXiv API identifies a `cs.CL`/`cs.AI` v1 submitted 16 July 2026 with the comment “20 pages.” Its summary contains no withdrawal/retraction notice.
- Record, PDF, and HTML endpoints returned HTTP 200. The PDF response reported `application/pdf` and 10,626,377 bytes; the HTML response reported 267,449 bytes.
- The abstract says the benchmark mines before/after figures from arXiv version histories, operates on editable vector sources, and continually refines a Skill from execution traces. It reports higher edit accuracy on a held-out validation set and presents natural revisions as evidence of author intent and implicit visual grammar. These are author-stated abstract claims awaiting full-paper and artifact audit.
- The immutable HTML exposed no author GitHub, Hugging Face, Zenodo, OSF, project, or dataset URL in targeted link triage. Targeted search did not establish an official release. A search result surfaced a third-party Hugging Face subset referring to the benchmark, but no identity, authority, completeness, or provenance was established; it must not be treated as the paper release without verification.
- Exact searches for the title, arXiv ID, scientific-diagram editing, editable vectors, visual grammar, and paper-revision mining found no prior local review, queue task, or scouting note.

## Why this is a narrow, useful gap

The corpus already covers expert artifact edits, native and temporal artifact observers, mixed-initiative spreadsheet editing, multimodal grading, skill evolution, procedural-memory transfer, and living-rubric evolution. It does not directly audit **natural professional revision histories as simultaneous task, intent, expertise, and Skill-learning evidence**:

`paper/version and author identity → before/after vector artifacts → inferred or recorded revision intent → task/instruction projection → train/validation/test lineage → Skill proposal and version transition → agent-visible guidance and adoption → primitive edit sequence → semantic figure change and collateral preservation → artifact observer/human judgment → held-out recipient or scientific consequence`.

A before/after delta proves that an artifact changed, not why it changed, who authorized each change, whether every change was desirable, or whether it captures transferable tacit expertise rather than local manuscript needs. Version-history mining can create author, paper, template, citation, and visual-lineage leakage across splits. Iteratively selecting a Skill against a validation set may establish configured validation improvement without untouched transport. Pixel or primitive agreement can miss argument fidelity, scientific correctness, editability, semantic equivalence, legitimate alternatives, and collateral damage. Co-editability is an affordance, not evidence of useful human adoption or reduced expert burden.

Scientific diagrams are a bounded stress case for reusable expertise-transfer and native-artifact machinery—not a proposal to narrow `skill-bench` to figure editing or scientific publishing.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier realistic artifact-work evaluation), B (expertise/intent transfer from natural work records), and C (editable native artifacts, Skill versions, traces, and plural observers).
- **Concrete evidence:** immutable-v1 full-paper review plus timing-aware audit of any revision corpus, vector sources, instructions, split construction, Skill snapshots, execution traces, graders, and human judgments.
- **Uncertainty clarified:** whether revision histories support authorized-intent or tacit-grammar claims; whether Skill improvement survives lineage-aware untouched transport; and what the artifact observers actually measure.
- **Mode:** narrow expansion. The ready queue had one human prerequisite and one build but no review task; one review restores a minimal research backlog without repeating broad discovery.
- **Duplication/scope check:** adjacent reviews cover surrounding edit, artifact, Skill, and lifecycle links, but not this revision-history composition. No diagram-specific schema or pilot is proposed.
- **Useful completion:** page/path-grounded reconstruction of source selection, pair/instruction derivation, lineage-aware splits, Skill evolution and selection, artifact observation, human review, exact denominators, release conformance, and claim ceilings while separating captured delta, intent, tacit expertise, Skill effect, transport, scientific correctness, recipient utility, professional validity, and readiness.

Added one task: `review-scidiagramedit-revision-derived-skill-validity` (review, priority 64). No other task was added. SearchOS-V1, MCPEvol-Bench, Alipay-PIBench, FlowGuard, MemPoison, and Bad Memory were triaged but deferred: each overlaps substantial existing search-state, tool-evolution, coding/Skill, runtime-security, or memory-governance coverage, whereas the revision-derived expertise/artifact chain is the narrower uncovered mechanism. A later scout should reconsider them only if release inspection reveals distinct evidence not represented by current reviews.

# Scouting note — tacit-skill distillation to consequential physical work gap

**Timestamp:** 2026-07-15T17:51:08Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Initial queue inspection found 284 tasks: 278 completed, three blocked, one pending human prerequisite, and two pending consolidations; no source, research, review, or claimed backlog remained. The reviewed corpus already covers expert-authored procedural skills, industrial codification, laboratory workflow elicitation, trace-refined transfer, native artifacts, configured-system ablations, and production evaluation. This run therefore searched only for primary evidence connecting a documented tacit-knowledge distillation process to agent-executed, consequential physical work with quantitative checks and audit records.

## Substantive finding — triage only

**Vibe Calibration: Autonomous Bring-up of a 112-Qubit Superconducting Quantum Processor by a Skill-Orchestrating Language Agent** — Huikai Xu, Jiaxiu Han, Shigang Ou, Cheng Ye, Zisong Shen, Jing Gao, Yijia Wang, Tianrui Che, Yu Song, Weiyang Liu, Lei Wang, Lin-Feng Zhang, Pan Zhang, and Hai-Feng Yu; arXiv:2606.22376v1.

- Immutable record: https://arxiv.org/abs/2606.22376v1
- Immutable PDF: https://arxiv.org/pdf/2606.22376v1
- Immutable HTML: https://arxiv.org/html/2606.22376v1
- Paper-linked implementation: https://github.com/NVIDIA/Quantum-Calibration-Agent-Blueprint/tree/0753553722b365178b7791b819790456893fa49f
- The arXiv API identifies immutable v1 as submitted 21 June 2026 in `quant-ph`; its abstract contains no withdrawal or retraction notice. The versioned abstract, HTML, and PDF endpoints returned HTTP 200 during scouting.
- The abstract says the system distills expert tacit knowledge through a three-phase human-in-the-loop process into reusable decision-tree Skills containing parameterized measurement commands, quantitative acceptance criteria, and audit records, then fine-tunes a language model on validated trajectories.
- The abstract reports autonomous calibration of 108 of 112 qubits in 4.7 hours, a claimed 4–5× speedup over manual full-device calibration, agreement with expert manual calibration on 14 of 16 qubits in a subset, and workflow transfer across devices after minor low-level interface adaptation. These are author-reported abstract claims, not independently verified findings.
- Structural inspection of the immutable HTML—not a full reading—confirmed sections on the calibration system, Agent Skill Architecture, fine-tuned models, experimental results, and discussion. It also exposed the NVIDIA repository link.
- GitHub API inspection verified the public non-fork repository, Apache-2.0 license, default branch `main`, and current pinned commit `0753553722b365178b7791b819790456893fa49f` dated 20 April 2026. Its root tree includes calibration scripts, experiment/workflow tooling, storage, unit/integration tests, and six `SKILL.md` paths under `data/knowledge/skills/`. No source file, Skill body, test, trajectory, measurement record, model artifact, or result was read or executed.
- Repository-wide exact-title, arXiv-ID, and project-name searches found no local source, review, or queue task. The closest reviews are LH-Bench, Industrial expertise codification, Laboratory workflow twins, AFTER, ArtisanCAD, Workflow-GYM, and AlphaEval. None locally reviewed source joins a stated expert-distillation protocol, explicit acceptance criteria and audit records, agent-orchestrated physical measurements, expert comparison, and cross-device transport in one consequential workflow.
- This is **metadata, abstract, endpoint, section-structure, release-location, commit-identity, root-inventory, and duplicate triage only**. The paper body, appendices, figures, tables, three-phase elicitation records, decision trees, Skills, validated trajectories, fine-tuning data, hardware interface, measurements, audit records, expert comparison, exclusions, failures, statistics, costs, release/paper correspondence, and results were not read or audited. No claim is made that tacit knowledge was faithfully captured, acceptance criteria are expert-authoritative, trajectories are independent validation evidence, calibration outcomes are safe or complete, speedup is causally attributable to the agent, the 16-qubit comparison is representative, workflows transport across hardware, the public blueprint reproduces the reported system, or the work establishes expert equivalence, general agent capability, production fitness, or readiness.

## Why this is distinct

The reusable chain is `expert incident and measurement evidence → elicitation/distillation transformation → decision-tree branch and parameterized action → quantitative acceptance/recovery rule → executable Skill version → configured model and orchestration policy → physical measurement/action → audit record → expert or independent criterion comparison → device/workflow transport`. This is unusually direct evidence for the charter's central expertise-to-evaluation question because the intervention and the criterion appear inside a real instrument-control workflow. It is also unusually confounded: the same team may author the expertise representation, acceptance checks, validated training trajectories, orchestration, and outcome claims, while hardware selection, excluded qubits, parallelism, interface adaptation, and expert comparison can change the estimand.

A full audit should separate capture fidelity, expert authority, branch/threshold provenance, intervention identity, trajectory leakage, execution realization, acceptance-check validity, anomaly/recovery behavior, excluded/failed units, human takeover, audit completeness, configured-system cost, expert-comparison design, and cross-device transport. It should test whether the public blueprint corresponds to the reported instrument and evidence or is only a generic reference architecture, and whether transfer is measured on held-out hardware/workflows rather than interface-compatible reuse.

## Charter decision filter and queue action

- **Objectives advanced:** A (production agent and evaluation evidence), B (tacit expertise transformed into explicit procedural primitives), and C (auditable Skill, trace, criterion, and intervention contracts).
- **Concrete evidence/artifact:** immutable-v1 deep review plus a timing-aware pinned-release audit.
- **Uncertainty clarified:** whether a Skill-mediated physical workflow demonstrates faithful expertise transfer and transport, or a co-authored configured-system package validated mainly by its own checks.
- **Mode:** narrow expansion/validation; quantum calibration is a consequential physical-work stress case, not a permanent benchmark scope.
- **Duplication/scope:** no local duplicate; mandatory comparison with LH-Bench, industrial codification, laboratory workflow twins, AFTER, Workflow-GYM, and AlphaEval prevents a quantum-specific schema or benchmark claim.
- **Useful completion:** a claim ladder separating elicitation, representation, training, execution, criterion validity, expert agreement, operational outcome, efficiency, transport, safety, expert equivalence, and readiness, grounded in exact paper and release locators.

Added one low-priority task: `review-vibe-calibration-tacit-skill-transfer-validity` (priority 7). The consented expert micro-pilot and two evidence-request consolidations remain substantially higher priority.

## Operational note

The required initial `git pull --ff-only` succeeded. Pre-existing untracked paper-source, release-archive, and site files were not touched.

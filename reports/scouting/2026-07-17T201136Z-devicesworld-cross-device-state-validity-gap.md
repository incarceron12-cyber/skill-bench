# Scouting note — DevicesWorld cross-device state-validity gap

- **Timestamp:** 2026-07-17T20:11:36Z
- **Evidence status:** arXiv/search metadata, official repository history, and official README triage only. The paper body was **not** read during scouting. No benchmark tasks, environments, verifiers, cleanup code, raw attempts, or result records were available in the inspected repository.

## Substantive candidate — triage only

**DevicesWorld: Benchmarking Cross-Device Agents in Heterogeneous Environments** — Huatao Li et al.; arXiv:2607.13465v1.

- Immutable record/PDF/HTML: https://arxiv.org/abs/2607.13465v1 · https://arxiv.org/pdf/2607.13465v1 · https://arxiv.org/html/2607.13465v1
- Official repository: https://github.com/AgenticOrgLab/DevicesWorld at inspected commit [`91653ecf565052f52b95524c4f6abe9aa15aa4ed`](https://github.com/AgenticOrgLab/DevicesWorld/commit/91653ecf565052f52b95524c4f6abe9aa15aa4ed), dated 16 July 2026.
- The official README describes 6,140 tasks spanning Android, Linux, and SmartHome environments. It says each task contains a natural-language goal, participating devices, initial states, executable actions, rule verifiers, and cleanup procedures, including information transfer, multi-source integration, conflict resolution, temporal planning, control, and jointly checked endpoints.
- The README reports a fixed evaluation set over five frontier model–agent systems, 12.5% best task success, and at least one scoring condition satisfied in 28.7% of failed runs. These are author-stated figures awaiting full-paper and result-record verification.
- The inspected repository contains only the README and one teaser image and explicitly marks the benchmark “Coming Soon.” Repository presence therefore establishes source identity, not release inspectability or reproducibility.
- Exact repository searches for the title, arXiv ID, and project name found no prior local review, queue task, or scouting note.

## Why this is a narrow, useful gap

The corpus covers cross-application state, single-device computer use, synthetic workflows, persistent workspaces, typed handoffs, and state-verifier validity. It does not yet deeply audit a benchmark whose unit of execution crosses heterogeneous device substrates and requires jointly realized endpoint state. The relevant measurement chain is:

`task and participating-device identity → per-device initial state and availability → information/access opportunity → semantic transfer across device boundary → dependency/role tracking → attempted actions → per-device intended and collateral deltas → joint endpoint predicate → cleanup/reset → repeated trial validity → workflow or professional consequence`.

Cross-device composition can expose failures hidden by per-device success: stale or transformed information, wrong-device actions, incomplete handoffs, conflicting clocks or identities, partial endpoint satisfaction, and cleanup leakage. But a conjunction of authored rule predicates does not by itself establish semantic transfer, complete observer coverage, reliable recovery, professional usefulness, or safety. The reported partial-check fraction is potentially diagnostic only if check roles, dependencies, masking, denominators, invalid runs, and task clustering are inspectable. A large generated or templated suite also needs task-family and device-combination accounting rather than treating 6,140 rows as 6,140 independent work activities.

Android/Linux/SmartHome is a bounded substrate for testing reusable cross-resource state and handoff machinery, not a proposal to narrow `skill-bench` to personal devices, IoT, or consumer automation.

## Charter decision filter and queue action

- **Objectives advanced:** A (realistic agent benchmark frontier), B (valid cross-substrate workflow and observer claims), and C (environment, state, trace, verifier, reset, and trial-accounting machinery).
- **Concrete evidence:** immutable-v1 full-paper review, timing-aware official-release audit, task/device/dependency/verifier crosswalk, exact result accounting, and a zero-model setup/verifier/cleanup reproduction if the release permits it.
- **Uncertainty clarified:** when jointly verified device endpoints support bounded configured-workflow conformance, and what additional evidence is required for information preservation, coordination, recovery, operational reliability, professional validity, safety, or readiness.
- **Mode:** narrow expansion. The autonomous research/review backlog was empty apart from one human prerequisite, so one review task restores a small, targeted backlog without restarting broad search.
- **Duplication/scope check:** adjacent reviews cover individual-device or cross-application machinery but not heterogeneous-device execution as one state/dependency envelope. No device-specific schema or pilot is proposed.
- **Useful completion:** page/path-grounded reconstruction; release-versus-paper conformance; explicit device, state, check, dependency, reset, invalid, and attempt denominators; and bounded retain/repair/test implications without promoting abstract or README claims.

Added one task: `review-devicesworld-cross-device-state-validity` (review, priority 68). No other candidate was queued.

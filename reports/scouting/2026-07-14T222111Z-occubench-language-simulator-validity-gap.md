# Scouting note — language-simulated occupational environment validity

**Timestamp:** 2026-07-14T22:21:11Z  
**Scope:** Narrow expansion against charter objectives A/B/C. At intake the queue had 231 tasks: 225 completed, four blocked, two pending human decisions, and no worker research/review task. Existing reviews cover occupational artifact packages, integrated workplace/SaaS substrates, model-simulated participants, and synthetic workspaces, but not broad occupational coverage created by LLM-generated domain tool dynamics.

## Substantive finding (triage only)

**OccuBench: Evaluating AI Agents on Real-World Professional Tasks via Language Environment Simulation**

- Immutable record: https://arxiv.org/abs/2604.10866v2
- Immutable PDF: https://arxiv.org/pdf/2604.10866v2
- Official repository: https://github.com/GregxmHu/OccuBench
- Paper-linked dataset surface: https://huggingface.co/datasets/gregH/OccuBench
- The arXiv API identifies Xiaomeng Hu, Yinger Zhang, Fei Huang, Jianhong Tu, Yang Su, Lianghao Deng, Yuxuan Liu, Yantao Liu, Dayiheng Liu, and Tsung-Yi Ho; category `cs.CL`; v1 submitted 13 April 2026 and v2 updated 16 April 2026. The metadata summary contains no withdrawal notice. The versioned abstract and PDF returned HTTP 200; targeted search resolved the official GitHub and Hugging Face surfaces.
- The **v2 abstract** reports 100 professional scenarios across ten industry categories and 65 specialized domains. Language Environment Simulators generate domain-specific tool responses. A multi-agent synthesis pipeline is said to guarantee solvability, calibrate difficulty, and create document-grounded diversity. The benchmark measures task completion and robustness under explicit, implicit-data-degradation, and mixed faults, with 15 frontier models across eight families. It reports that implicit degradation is hardest and that simulator quality is critical. These are author-reported abstract claims, not independently verified findings.
- The distinctive validity question is **simulator-mediated occupational breadth**: replacing scarce real environments with an LLM simulator can expand domain coverage and permit controlled faults, but the scored endpoint may reflect agreement among task generator, simulator, and oracle rather than correct action in the represented occupation. A simulator can silently omit state, consequences, alternative valid paths, professional constraints, and realistic recovery cues. “Guaranteed solvability” can therefore certify a closed synthetic package without establishing occupational legitimacy or environmental robustness.
- This is metadata, abstract, URL, and duplicate triage only. The PDF body, appendices, repository, dataset bytes, task sources, LES prompts, trajectories, oracles, results, and statistical analyses were not read or audited. No claim is made that OccuBench establishes real professional performance, safety, robustness, capability, or readiness.

## Benchmark implication to test

Language-simulated tasks need a typed chain: `occupational demand/source authority → task projection → real-environment construct → simulator identity/prompt/state → tool-response distribution → injected-fault intervention → agent observation/action → authoritative consequence oracle → scorer → simulator-to-real transport boundary`. Simulator quality is not one scalar: factual state fidelity, action-conditioned transition fidelity, information availability, fault realism, observer sufficiency, alternative-path support, stochastic reliability, and consequence fidelity can fail independently.

A full audit should reconstruct one released scenario end to end and compare OccuBench with GDPval, TheAgentCompany/WorkArena, HAS-Bench, UnderSpecBench, and synthetic-workspace evidence. It should test whether the same or related models author tasks, simulate tools, solve tasks, and judge outcomes; whether professional documents or experts authorize requirements; whether fault injection changes only the declared variable; and whether simulator-quality tests support the occupational and robustness claims.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier benchmark mechanism), B (expertise/task/environment projection), and C (evidence for scalable controlled environments).
- **Evidence/artifact sought:** immutable-v2 deep review, pinned official release audit, and one end-to-end source→task→LES→fault→trajectory→oracle reconstruction.
- **Uncertainty clarified:** whether language simulators provide valid broad-domain environment evidence or mainly internally coherent synthetic endpoint agreement.
- **Mode/balance:** one low-priority review task restores a minimal worker research backlog behind human/operational blockers; no broad search bundle was added.
- **Duplication/scope:** the simulator mechanism is absent from reviewed occupational/workplace families; the 65 specialties are a construct-transport study, not a proposal to make any one occupation the benchmark.
- **Useful completion:** preserve source and expert authority, simulator/oracle identities and dependence, state/transition evidence, fault semantics, repeats/invalids, alternative paths, release drift, and strict claim ceilings.

Added `review-occubench-language-simulator-validity` (priority 17). BankerToolBench was not queued because prior scouting explicitly deferred it against existing spreadsheet/finance coverage. No second task was added.

## Operational note

The required initial `git pull --ff-only` failed because the HTTPS GitHub remote lacks a noninteractive credential (`could not read Username`). The run proceeded from local state. The pre-existing untracked `data/papers/source/` tree was inspected only for duplicate filenames and was not modified.

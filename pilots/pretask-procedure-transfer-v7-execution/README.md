# Pre-task procedure transfer v7 execution

This directory is the prospective, one-shot execution layer for the independently cleared **frozen v7 instrument**. It is intentionally outside `pilots/pretask-procedure-transfer-v7/`; no v4-v7 frozen byte was edited or rescored.

## Charter and design rationale

This bounded validation slice advances charter objectives **B** (separate procedure exposure from raw context and hindsight) and **C** (executable, provenance-preserving trials). It tests whether a frozen 32-row synthetic mechanism matrix can execute under one comparable configured-system envelope and retain strict evidence. Custody and nested-journal forms are synthetic calibration structures, not benchmark scope, professional workflows, or expert-grounded tasks.

Before any call, `execute_matrix.py` verified:

- audited commit `0b7f9306ec6c3a18d4f5bba98af3eabd2ea7f200` remained an ancestor of `origin/main`;
- all 22 v7 components and 33 external bindings matched size/hash;
- all assigned v4 source/reference/defect, generated-package, and hindsight-package treatment bytes matched their transitive manifests;
- v7 assignments and attempt ledgers were zero;
- fresh two-arm canary and path-checking preflight reports were byte-identical to the independently audited passing reports;
- prior provider evidence for the exact `gpt-5.6-sol` / `openai-codex` pair reported `included` USD `0.00`.

The launcher then materialized all 32 task roots before calls. Each root exposed only frozen `public-task.md`, frozen `input.json`, the assigned treatment files, and a unique writable output mount. A full Hermes file-tool canary passed. Rows ran in frozen order with one attempt, no feedback, no repair, and no retry. Service, cost, or environment failure would have stopped later rows; artifact and endpoint failures stayed in the denominator.

## Result

- **Execution status:** complete; 32/32 attempted, service-valid, and environment-valid.
- **Cost:** all 32 usage records report provider-included USD `0.00`; aggregate reported cost USD `0.00`.
- **Resources:** 196 API calls; 987,097 provider-reported total tokens (328,299 input, 16,750 output, 7,328 reasoning; provider `total_tokens` also includes categories not represented by those three fields).
- **Artifacts/checks:** 30/32 met the launcher's minimal artifact-validity predicate; 32/32 were scored; 24/32 passed the frozen endpoint checker. The two artifact-invalid rows were schedule 7 (`cross_family_irrelevant`, zeta/t6v1) and 10 (`no_package_no_raw`, zeta/w3d8); both remain scored failures and were not rerun.
- **Bounded family-clustered observations:** generated package minus no package was `+1.0` for epsilon and `+0.5` for zeta (mean `+0.75`, two family clusters). Generated package minus equal-budget raw was `0.0` in both families. Generated-plus-raw minus generated and reference minus generated were also `0.0` in both families. These are descriptive outcomes from two synthetic families, not an inferential transfer estimate.

All seven claim flags remain false: agent capability, expert provenance, transfer, utility, professional validity, production fitness, and readiness. The complete matrix does not establish reliability, generality, causal procedure transfer, or benchmark usefulness.

## Evidence map

- `execute_matrix.py` — fail-closed prospective launcher and strict summarizer.
- `preexecution-report.json` — zero-attempt commit/hash/canary/preflight/cost gates.
- `execution-canary-report.json` — full file-tool isolation and all-row inventory checks.
- `execution-report.json` — strict denominators, exact cells, and family-clustered summaries.
- `execution/<row>/trial-report.json` — configured system, state, inventories, hashes, checker result, and usage for one row.
- `execution/<row>/redacted-trace.log`, `launcher-stderr.log`, `outputs/result.json`, `outputs/usage.json` — retained trial evidence.
- `execution/<row>/prompt.txt` — exact prompt bytes reconstructed post-execution from the launcher; each prospective trial report already recorded the matching hash. This timing limitation is explicit in the audit.
- `audit_execution.py` / `execution-audit-report.json` — replayable retention, denominator, cost, attempt, and claim-ceiling audit.

## Verification

```bash
python pilots/pretask-procedure-transfer-v7-execution/audit_execution.py
python -m py_compile scripts/*.py pilots/pretask-procedure-transfer-v7-execution/*.py
python -m unittest discover -s tests -v
python scripts/check_review_quality.py papers --allow-empty
python scripts/queue.py validate
```

`execute_matrix.py` is deliberately non-rerunnable once evidence exists. Do not delete evidence to make it runnable again.

# Reviewer replay audit

- **Date:** 2026-07-15
- **Source archive:** `WilliamWJHuang-How-Many-Tasks-1117405.zip`
- **Pinned commit:** `1117405cfecdee730e01071d859d3c3383f22711`
- **Archive SHA-256:** `4402dd78fba38d5a06a79310d9ea7cc9b1e3a183f3ff4bf6017eead391f81950`
- **Environment:** fresh `/tmp` extraction on Linux; isolated Python 3.11 virtual environment
- **Dependencies installed from release:** unpinned `pandas`, `numpy`, `matplotlib`

## Commands exercised

From the extracted repository root, using the isolated interpreter:

```text
python -m py_compile scripts/*.py
python scripts/summarize_public_tau2_pair_grid.py
python scripts/summarize_public_tau2_reward_sensitivity_grid.py
python scripts/run_swebench_conversion_smoke.py
python scripts/build_appworld_feasibility.py
python scripts/summarize_public_robustness_checks.py
python scripts/run_paired_test_diagnostics.py
```

The primary PowerShell wrapper was not used because the review host is Linux. These are the wrapper's corresponding public quick-path/check steps. No raw-input full replay was claimed: the archive omits raw AppWorld bundles and raw tau-bench trajectories, and the fine-grid headline analysis is distributed as derived pair tables.

## Observed execution

All 15 Python scripts compiled. Executed scripts returned successfully:

- tau-bench ordered-grid summary: 24 truth rows, 30 aggregate rows, 10 sufficient rows;
- tau-bench reward sensitivity: 72 truth rows, 24 flip rows;
- SWE-bench conversion: 55,697 task rows, 218 submissions, 32,196 pair rows;
- AppWorld feasibility: 18 systems, 10,530 task rows, 585 unique task keys, 306 directed pairs;
- public robustness summaries written;
- paired-test diagnostics processed 552 SWE-bench Lite, 156 SWE-bench Verified, 306 AppWorld, and 12 tau-bench directed pairs.

The included fine-grid `target_budget_sweep/main_policy_summary/main_policy_minimum_budgets.csv` reports, for policy cutoff/error target 0.05, coverage target 0.05, and unresolved target 0.25:

| Source | 0 pp | 5 pp | 10 pp |
|---|---:|---:|---:|
| AppWorld | 15% | 15% | 15% |
| tau-bench | 25% | 30% | 35% |
| SWE-bench Verified | 90% | 90% | 90% |
| SWE-bench Lite | no passing grid point through 95% | 55% | 35% |

The regenerated paired-test table preserved the paper's qualitative sensitivity: exact McNemar at 0 pp gives AppWorld 25%, tau-bench 35%, SWE-bench Verified 95%, and no passing SWE-bench Lite grid point; paired normal gives 15%, 25%, 90%, and no passing point respectively.

## Manifest integrity check

Before executing replay scripts:

```text
sha256sum -c MANIFEST.sha256
```

returned 58 `OK` and 584 `FAILED`. Binary figure files largely matched, while many text/CSV/code files did not. For one inspected file, `analysis/public_backtest/appworld_feasibility/appworld_task_rows.csv`, converting the GitHub ZIP's LF bytes to CRLF exactly recovered the manifest digest, showing line-ending normalization explains at least part of the failure. The same conversion did not recover all sampled files, so no single cause is asserted for all mismatches.

**Interpretation:** the release archive is inspectable and its public summaries execute, but `MANIFEST.sha256` is not a valid byte-integrity check over the official GitHub commit ZIP as distributed. This audit does not alter the upstream archive or regenerate its manifest.

## Claim boundary

This execution supports release inspectability and regeneration of selected public summaries from included derived records. It does not establish raw-input end-to-end reproduction, prospective stopping validity, future-task transport, rank or diagnostic preservation, configured-system reliability, professional capability, or readiness.

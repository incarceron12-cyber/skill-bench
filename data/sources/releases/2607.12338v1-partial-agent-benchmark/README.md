# How Many Tasks Are Enough for Agent Benchmark Decisions?

This repository contains the public reproducibility package for:

**How Many Tasks Are Enough for Agent Benchmark Decisions? A Replay Analysis of Public LLM Agent Benchmarks**

The package reproduces the paper's public replay analyses for SWE-bench, AppWorld, and tau-bench. It is organized around completed benchmark records replayed under partial task budgets. It does not train agents, release a new benchmark, or claim population guarantees beyond the completed public records used in the paper.

Repository: https://github.com/WilliamWJHuang/How-Many-Tasks-Are-Enough-for-Agent-Benchmark-Decisions

## What is included

- `scripts/`, replay, summarization, sensitivity, paired-test, and figure-generation scripts.
- `analysis/public_backtest/`, public derived tables and reports used by the paper.
- `analysis/figures/`, generated public figures.
- `paper/`, the camera-ready paper source, bibliography, compiled preview PDF, and figure PDFs.
- `schema.md`, column definitions for the main public replay tables.
- `docs/`, public data provenance notes and omitted-intermediate documentation.

The package intentionally excludes raw AppWorld leaderboard bundles, raw tau-bench trajectory files, local virtual environments, LaTeX auxiliary files, non-public logs, exploratory analyses that are not evidence sources for the paper, and one large pair-level stability intermediate documented in `docs/OMITTED_LARGE_INTERMEDIATES.md`.

## Quick start

From this repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install --upgrade pip
.\.venv\Scripts\python -m pip install -r requirements.txt
powershell -NoProfile -ExecutionPolicy Bypass -File .\reproduce_public.ps1
```

The default run uses included public derived tables. It refreshes public summaries, public robustness checks, paired-test diagnostics, figures, and the paper PDF. Use `-SkipFigures` or `-SkipPdf` when you only want table checks.

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\reproduce_public.ps1 -SkipFigures -SkipPdf
```

## Full public replay

The full replay path expects raw public inputs in the same locations used by the scripts:

- `analysis/public_backtest/raw_tau2/`, tau-bench public trajectory files.
- `analysis/public_backtest/swebench_experiments_repo/`, public SWE-bench experiment metadata, included here because it is compact.
- `analysis/public_backtest/appworld_feasibility/appworld_task_rows.csv`, compact AppWorld task-level table derived from public AppWorld leaderboard bundles.

Run:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\reproduce_public.ps1 -FullPublicReplay
```

The script does not download raw files by default. `scripts/build_public_tau2_table.py` supports a `--download` option for tau-bench files, but use it only after checking the upstream data source and license terms.

## Main claims covered

This package supports the public empirical claims that:

- A task fraction alone is not a decision rule.
- Partial evaluation should report decision error, task-group coverage, unresolved comparisons, and full-benchmark decision counts.
- Low replay error can still leave too many comparisons unresolved.
- Sufficient task budgets depend on benchmark, threshold, coverage rule, task ordering, pair orientation, and unresolved-comparison target.
- Cost-aware task ordering can save cost while missing task groups needed for the completed-benchmark decision.

## Not included

The package does not include OSWorld, Terminal-Bench, HAL, or other exploratory analyses. Those were not used as evidence sources in the KDD workshop paper. The package also excludes large raw public bundles when compact derived public tables are enough for the paper checks.

## License

Code and documentation in this repository are released under the MIT License. Public benchmark data and upstream metadata retain their original licenses, terms, and citation requirements.

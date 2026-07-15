# Data provenance

This package uses public benchmark records and derived public tables.

## SWE-bench

The package includes compact public SWE-bench experiment metadata under `analysis/public_backtest/swebench_experiments_repo/` and derived task-level tables under `analysis/public_backtest/swebench_smoke/`.

## AppWorld

The package includes `analysis/public_backtest/appworld_feasibility/appworld_task_rows.csv`, a compact task-level table derived from public AppWorld leaderboard bundles. The raw leaderboard repository and Git LFS bundles are not included because they are large and should be obtained from the upstream source.

## tau-bench

The package includes compact tau-bench task tables under `analysis/public_backtest/tau2_ready*` and replay summaries under `analysis/public_backtest/tau2_pair_grid*`. Raw trajectory files are not included. To rerun from raw trajectories, place the public files under `analysis/public_backtest/raw_tau2/` and run `reproduce_public.ps1 -FullPublicReplay`.

## Excluded exploratory analyses

OSWorld, Terminal-Bench, HAL, and other exploratory analyses are not included because they are not evidence sources for the KDD workshop paper.

# Artifact dry-run report

Date: 2026-07-11

Status: passed with one note.

## Commands run

Core quick path, without figures, PDF, or paired tests:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\reproduce_public.ps1 -SkipFigures -SkipPdf -SkipPairedTests
```

Observed result:

- tau-bench ordered-grid summaries regenerated.
- tau-bench reward sensitivity summaries regenerated.
- SWE-bench conversion report regenerated from included public metadata.
- AppWorld feasibility report regenerated from the compact public task table.
- public robustness checks regenerated.

Additional checks run:

```powershell
python scripts\run_sensitivity_diagnostics.py
python scripts\run_paired_test_diagnostics.py
python scripts\make_system_figure.py
python scripts\make_paper_figures.py
```

Observed result:

- sensitivity diagnostics regenerated for SWE-bench Lite, SWE-bench Verified, AppWorld, and tau-bench.
- paired-test diagnostics regenerated for the same four sources.
- public figure PDFs and PNGs regenerated.

Paper compile check:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Observed result:

- `paper/main.pdf` compiled successfully.
- The final PDF is 10 pages.
- Log scan found no undefined citations and no undefined references.
- The remaining LaTeX warning is `Class acmart Warning: No city present for an affiliation`, expected because the affiliation uses country only.

## Note

`python scripts\run_sensitivity_diagnostics.py` completed and wrote outputs, but the shell wrapper returned a timeout status after the files were already written. The output directory timestamps and a follow-up string scan confirmed that the regenerated sensitivity diagnostics are present and contain no OSWorld rows.

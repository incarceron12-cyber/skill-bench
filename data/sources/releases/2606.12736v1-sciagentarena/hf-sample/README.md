# Agent4Science Bench — Task Data

This directory contains benchmark datasets for evaluating AI agents across multiple biomedical and life-science domains. Each subdirectory corresponds to one domain and contains task definitions (question files) together with the underlying data that agents must analyze. You should not use it for model training.

---

## Directory Overview

```
data_task/
├── cross_domain/       # Cross-domain prediction tasks (synthetic lethality, target ID, eQTL)
├── drugdiscovery/      # Drug discovery benchmark across five role-based competency levels
├── ehr/                # Electronic health record analysis tasks
├── genetics/           # Polygenic risk score and Mendelian randomization tasks
├── sc/                 # Single-cell RNA-seq analysis (~12 GB)
└── sp/                 # Spatial transcriptomics analysis (~4 GB)
```

---

## `cross_domain/` — Cross-Domain Prediction Tasks

Contains evaluation sets for tasks that require integrating knowledge across multiple databases and biological domains.

### Subdirectories

| Subdirectory | File | Description |
|---|---|---|
| `eqtl/` | `readme.md` | Instructions for accessing GTEx v8 blood eQTL data (controlled access via GTEx portal) |
| `leth/` | `evaluation_sl-samson-A427-query-42.csv` | Synthetic lethal (SL) interaction queries for the A427 lung cancer cell line |
| `target/` | `evaluation_targetid-blastoma-query-42_sample20.csv` | Target identification queries for Hepatoblastoma across multiple cell types |

### Key Schemas

**Synthetic Lethality (`leth/`)** — 20 gene-pair queries
- Columns: `gene_a`, `gene_b`, `cell_line`, `interaction` (synthetic lethality / non-sl), `user_question`, `experiment_instruction`, `full_query`
- Task: Use DepMap co-dependency scores, Enrichr pathway analysis, and literature evidence to classify gene-pair interactions.

**Target Identification (`target/`)** — 20 multi-gene queries
- Columns: `candidate_genes` (list), `disease`, `celltype`, `y` (correct target gene), `user_question`, `full_query`
- Task: Given a set of candidate genes, identify the most disease-relevant target using cell-type-specific protein embeddings from PINNACLE.

**eQTL (`eqtl/`)** — External data (not included)
- Data must be requested from the GTEx portal (v8). The `readme.md` describes required files: VCF genotype files and eQTL summary statistics for blood tissue.

---

## `drugdiscovery/` — Drug Discovery Benchmark

A role-based benchmark with five competency levels (C1–C5), each representing a different scientific persona in a drug discovery pipeline. The main task file is `questions.csv` (≈144 KB). Supporting data lives in `data/`.

### Competency Levels

#### C1 — Cheminformatician (`data/C1_Cheminformatician/`)
Basic cheminformatics operations on small molecules.

| File(s) | Task Type | Description |
|---|---|---|
| `Formal_Charge_*.csv` + `formal_charge_*/` PDB files | Formal charge calculation | Assign formal charges to atoms from 3-D structure files |
| `Format_Conversion_hard_10.csv` | Format conversion | Convert between molecular formats (SMILES, InChI, SDF, etc.) |
| `Mass_Property_Calculation_hard_20.csv` | Property calculation | Compute molecular weight and other physicochemical properties |
| `Similarity_Search_hard_20.csv` | Similarity search | Identify molecules above a Tanimoto similarity threshold |
| `Substructure_Filtering_hard_20.csv` | Substructure filtering | Filter compound libraries using SMARTS substructure patterns |
| `Target_ID_hard_*.csv` | Target identification | Map compounds to protein targets via database lookup |

#### C2 — Data Analyst (`data/C2_Data_Analyst/`)
Data processing, quality control, and structure-activity relationship (SAR) analysis.

| File(s) | Task Type | Description |
|---|---|---|
| `sar_500.csv`, `dirty_sar.csv`, `activity_cliffs.csv` | SAR analysis | 500-molecule SAR dataset; dirty version for cleaning tasks; activity cliff detection |
| `project_data.csv`, `comparative_analysis.csv` | Cross-project analysis | Multi-project bioactivity datasets for comparative studies |
| `replicate_qc.csv`, `unit_inconsistency.csv`, `dtype_trap.csv` | Quality control | Identify/fix replicate issues, unit mismatches, and data type errors |
| `assay_harmonization_a/b.csv`, `merge_assay.csv`, `merge_metadata.csv` | Data harmonization | Integrate results from disparate assay formats |
| `temporal_batches.csv`, `pipeline_repair.csv` | Batch & pipeline issues | Detect temporal batch effects; repair broken data pipelines |
| `EGFR.tsv` | Target-specific data | EGFR inhibitor activity data (tab-separated, 30.9 KB) |
| `diverse_library.csv`, `admet_leads.csv`, `bindingdb_panel.csv` | Library analysis | Diverse chemical library; ADMET properties; binding assay panel |
| `vision/dose_response.png`, `hts_plate_384.png`, `sar_outlier.png` | Visual QC | Images for visual inspection tasks (dose-response curves, HTS plate maps, SAR outliers) |
| `_generation_metadata.json`, `_dblookup_gt.json` | Metadata | Generation parameters and database lookup ground-truth answers |

#### C3 — Multi-Objective Designer (`data/C3_Multi_objetive_Designer/`)
Molecular optimization against multiple competing objectives.

| File | Objective | Description |
|---|---|---|
| `des_drd2_leads.csv` | DRD2 activity | Lead compounds optimized for dopamine D2 receptor binding |
| `des_penalized_logp_leads.csv` | Penalized logP | Compounds optimized for lipophilicity (penalized logP score) |
| `des_qed_leads.csv` | QED | Compounds optimized for drug-likeness (Quantitative Estimate of Druglikeness) |

#### C4 — Safety Regulator (`data/C4_Safety_Regulator/`)
Toxicity prediction and safety filtering.

| File(s) | Safety Endpoint | Description |
|---|---|---|
| `herg_training_data.csv` (144.8 KB), `herg_query_mols.csv` (33.5 KB) | hERG cardiotoxicity | Training and query sets for hERG channel inhibition prediction |
| `herg_predictions.json` (91.5 KB) | hERG predictions | Pre-computed hERG liability predictions for query molecules |
| `pains_classification_training_data.csv` (107.2 KB), `pains_classification_query_mols.csv` (98.9 KB), `pains_query_mols.csv` (31.9 KB) | PAINS filtering | Pan-assay interference compound (PAINS) classification datasets |
| `toxalerts_query_mols.csv` | Toxicity alerts | Molecules to check against structural toxicity alert rules |

#### C5 — Scientist (`data/C5_Scientist/`)
Validation and integration tasks testing expertise across all other competency levels, with emphasis on error detection and data integrity.

| File(s) | Task Type | Description |
|---|---|---|
| `val_C1_0*.csv` / `.pdb` | Cheminformatics validation | Compound structure and target data for validating C1-level operations |
| `val_C4_01_corrupt_herg_training_data.csv` (143.6 KB), `val_C4_01_query_mols.csv`, `val_C4_02_mismatch_duplicates.csv` | Safety validation | Deliberately corrupted/mismatched HERG data for error detection tasks |
| `val_alias_*.csv`, `val_08_aliases.csv` | Alias resolution | Synonym and alias harmonization across compound names and assay IDs |
| `val_confounded_trend.csv`, `val_false_cliff.csv` | Analysis QA | Confounded trend detection; false activity cliff identification |
| `val_hidden_units.csv`, `val_sparse_sar.csv`, `val_09_low_conf_assay.csv` | Data quality | Hidden unit issues, sparse SAR, low-confidence assay data |
| `val_06_memo_claim.csv`, `val_07_stale.csv`, `val_10_ontology.csv`, `val_11_measured_vs_predicted.csv` | Scientific integrity | Claim verification, stale data detection, ontology consistency, measurement vs prediction comparison |
| `_generation_metadata.json`, `_dblookup_gt.json` | Metadata | Generation parameters and ground-truth answers |

---

## `ehr/` — Electronic Health Record Tasks

| File | Description |
|---|---|
| `EHR_TASK0524.xlsx` | Task definitions for EHR-based clinical analysis. Contains structured question sets for agent evaluation on synthetic patient data. |

Synthetic patient records are provided separately in `../synthea_sample_data_csv_latest_ehrdata/` (parent directory), which includes tables for allergies, careplans, conditions, encounters, medications, observations, patients, procedures, providers, and more.

---

## `genetics/` — Polygenic Risk Score & Mendelian Randomization Tasks

| File | Sheets | Description |
|---|---|---|
| `tasks.xlsx` | `single_ance`, `multi_ance`, `valid`, `MR` | Detailed, stepwise task specifications for genetic analysis workflows |

### Sheet Descriptions

| Sheet | Content |
|---|---|
| `single_ance` | Tasks 1–5 for single-ancestry polygenic risk score (PRS) analysis: method selection (PRS-CS, LDpred2, SBayesR, lassosum2), input formatting, QC filtering, allele harmonization, sample intersection, PRS computation, and evaluation |
| `multi_ance` | Analogous tasks for multi-ancestry PRS methods (PRS-CSx, JointPRS, SDPRX, ME-Bayes SL) |
| `valid` | Validation task requirements and acceptance criteria |
| `MR` | Mendelian randomization analysis tasks (instrument selection, two-sample MR, sensitivity analyses) |

External GWAS summary statistics and LD reference panels are required; the task file specifies exact file formats, column names, genome builds (hg19/hg38), and QC criteria.

---

## `sc/` — Single-Cell RNA-seq Tasks (~12 GB)

### Task Files

| File | Description |
|---|---|
| `questions.xlsx` | Full question bank for single-cell analysis tasks |
| `valid questions.csv` | 15 validated benchmark questions with reference code and expected answers |

### Dataset Files (`data/`)

All datasets are stored in [AnnData](https://anndata.readthedocs.io/) `.h5ad` format.

| File | Size | Content | Key Features |
|---|---|---|---|
| `HumanPBMC_raw.h5ad` | 193 MB | Human peripheral blood mononuclear cells | Immune cell types; raw counts |
| `Pancrm_raw.h5ad` | 507 MB | Human pancreatic tissue | Endocrine (alpha, beta, delta, PP) and exocrine (acinar, ductal) cells; raw counts |
| `adamson.h5ad` | 578 MB | CRISPR perturbation screen (Adamson et al.) | Guide RNA annotations; single-gene perturbations |
| `bcell_withpseudo.h5ad` | 1.5 GB | B cell development | Pseudotime values; developmental trajectory from progenitors to mature B cells |
| `hsccell_withpseudo.h5ad` | 878 MB | Hematopoietic stem/progenitor cells | Pseudotime values; multi-lineage differentiation trajectories |
| `norman.h5ad` | 2.1 GB | CRISPR combinatorial screen (Norman et al.) | Paired guide RNA annotations; genetic interaction data |
| `reploge.h5ad` | 7.9 GB | Large-scale CRISPR screen (Replogle et al.) | High-coverage perturbation atlas; multiple cell lines |

### Task Categories

- Cell type annotation using canonical marker genes
- Differential gene expression (DEG) analysis
- Pseudotime / trajectory reconstruction
- Batch effect detection and correction
- Perturbation response analysis (CRISPR screens)
- Gene set enrichment analysis

---

## `sp/` — Spatial Transcriptomics Tasks (~4 GB)

### Task Files

| File | Description |
|---|---|
| `questions.xlsx` | Full question bank for spatial transcriptomics tasks |
| `questions.csv` | 56 benchmark questions with validation labels (Y/N) and reference answers |

### Dataset Files (`data/`)

All datasets are stored in AnnData `.h5ad` format with spatial coordinates embedded.

| File | Size | Content | Key Features |
|---|---|---|---|
| `human_dlpfc.h5ad` | 1.9 GB | Human dorsolateral prefrontal cortex (DLPFC) | Multiple donors; cortical layer annotations (L1–L6, white matter); 10x Visium |
| `human_bc.h5ad` | 637 MB | Human breast cancer tissue | Tumor microenvironment; multiple cell types and spatial regions; 10x Visium |
| `stereo_seq.h5ad` | 1.3 GB | High-resolution stereoscopic sequencing data | Ultra-high spatial resolution; cell-level spatial profiles |

### Task Categories

- Spatial domain identification (e.g., cortical layer delineation)
- Spatially variable gene (SVG) discovery using Moran's I
- Layer- and region-specific marker expression
- Cell type co-localization via neighborhood enrichment analysis
- Cross-donor consistency assessment

---

## Data Format Notes

- **`.h5ad`** — HDF5-based AnnData format. Load with `anndata.read_h5ad()` or `scanpy.read_h5ad()` in Python.
- **`.csv` / `.tsv`** — Standard delimited text; load with `pandas.read_csv()`.
- **`.xlsx`** — Excel workbook; load with `pandas.read_excel()` (specify `sheet_name` as needed).
- **`.pdb`** — Protein Data Bank structure format; load with RDKit, BioPython, or PyMOL.
- **`.json`** — Ground-truth labels and metadata; load with Python's `json` module.

## Citation

If you use these datasets, please cite the original data sources as described in the task files and any associated paper for this benchmark.


---
 extra_gated_prompt: "Please do not use this dataset to train models. This is designed only for testing."
 extra_gated_fields:
  Name: text
  Organization: text
  I agree to the terms: checkbox
 ---

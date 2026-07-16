---
language:
  - zh
  - en
license: apache-2.0
task_categories:
  - question-answering
  - tabular-classification
  - text-generation
tags:
  - data-analytics
  - agents
  - document-understanding
  - benchmark
pretty_name: AIDABench
configs:
  - config_name: qa_zh
    data_files:
      - split: test
        path: QA/QA.jsonl
  - config_name: qa_en
    data_files:
      - split: test
        path: QA_en/QA_en.jsonl
  - config_name: data_visualization_zh
    data_files:
      - split: test
        path: data_visualization/data_visualization.jsonl
  - config_name: data_visualization_en
    data_files:
      - split: test
        path: data_visualization_en/data_visualization_en.jsonl
  - config_name: file_generation_zh
    data_files:
      - split: test
        path: file_generation/file_generation.jsonl
  - config_name: file_generation_en
    data_files:
      - split: test
        path: file_generation_en/file_generation_en.jsonl
---

# Dataset Card for AIDABench

## Links
- [Paper (arXiv)](https://arxiv.org/abs/2603.15636)
- [GitHub Repository](https://github.com/MichaelYang-lyx/AIDABench)

## Dataset Summary

**AIDABench** is a benchmark for evaluating AI systems on **end-to-end data analytics over real-world documents**. It contains **600+** diverse analytical tasks grounded in realistic scenarios and spans heterogeneous data sources such as **spreadsheets, databases, financial reports, and operational records**. Tasks are designed to be challenging, often requiring multi-step reasoning and tool use to complete reliably.

![Overview of AIDABench Framework](images/figure1_overview.png)

_Figure 1: Overview of the AIDABench evaluation framework._

## Supported Tasks and Evaluation Targets

AIDABench focuses on practical document analytics workflows where a model/agent must read files, reason over structured data, and produce a final deliverable.

### Task Categories

The dataset is organized around three primary capability dimensions:

- **File Generation (43.3%)**  
  Data wrangling and transformation tasks such as filtering, normalization, deduplication, joins, and cross-sheet linkage, with outputs as generated files (e.g., spreadsheets).

- **Question Answering (QA) (37.5%)**  
  Analytical queries such as aggregation, averages, ranking, comparisons, and trend analysis, with outputs as final answers.

- **Data Visualization (19.2%)**  
  Chart creation/adaptation tasks (e.g., bar/line/pie) including style requirements and presentation constraints, with outputs as figures or chart files.

![Evaluation Scenarios](images/figure2_scenarios.png)

_Figure 2: Example evaluation scenarios for QA, Data Visualization, and File Generation._

### Task Complexity

Tasks are stratified by the number of expert-level reasoning steps required:

- **Easy (29.5%)**: ≤ 6 steps
- **Medium (49.4%)**: 7–12 steps
- **Hard (21.1%)**: ≥ 13 steps
- **Cross-file Reasoning**: 27.4% of tasks require reasoning over multiple input files (up to 14 files).

### Data Formats

Most inputs are tabular files (xlsx/csv dominate), complemented by **DOCX** and **PDF** formats to support mixed-type document processing.

## Evaluation Framework

All models are evaluated under a unified **tool-augmented protocol**: the model receives task instructions and associated files, and can execute **arbitrary Python code** within a **sandboxed environment** to complete the task.

To align with task categories, AIDABench uses three dedicated **LLM-based evaluators**:

1. **QA Evaluator**  
   A binary judge that determines whether the produced answer matches the reference (under the benchmark’s scoring rules).

2. **Visualization Evaluator**  
   Scores both **correctness** and **readability** of generated visualizations.

3. **Spreadsheet File Evaluator**  
   Verifies generated spreadsheet outputs with a **coarse-to-fine** strategy, combining structural checks with sampled content validation and task-specific verification.

![Evaluator Design](images/figure3_evaluators.png)

_Figure 3: The design of the three types of evaluators in AIDABench._

## Baseline Performance

Results indicate that complex, tool-augmented document analytics remains challenging: the best-performing baseline model (**Claude-Sonnet-4.5**) achieves **59.43 pass@1** on AIDABench (see the paper for full settings, model list, and breakdowns).

## Intended Uses

AIDABench is intended for:

- Evaluating **agents** or **tool-using LLM systems** on realistic document analytics tasks
- Benchmarking end-to-end capabilities across **QA**, **file generation**, and **visualization**
- Diagnosing failure modes in multi-step, multi-file reasoning over business-like data

## Limitations

- The benchmark is designed for tool-augmented settings; purely text-only inference may underperform due to the need for code execution and file manipulation.
- Automated evaluation relies on LLM judges, which introduces additional compute cost and (small) scoring variance depending on settings.


## Citation

If you use this dataset, please cite the original paper:

```bibtex
@article{yang2026aidabench,
  title={AIDABENCH: AI DATA ANALYTICS BENCHMARK},
  author={Yang, Yibo and Lei, Fei and Sun, Yixuan and others},
  journal={arXiv preprint},
  year={2026}
}
```

---

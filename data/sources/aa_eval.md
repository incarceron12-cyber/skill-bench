Title: AA-Briefcase: Agentic Knowledge Work Benchmark | Artificial Analysis

URL Source: https://artificialanalysis.ai/evaluations/aa-briefcase

Markdown Content:
[Artificial Analysis](https://artificialanalysis.ai/)

[](https://artificialanalysis.ai/login)K

[Artificial Analysis](https://artificialanalysis.ai/)

*   Models
*   Coding Agents
*   Speech, Image, Video
*   [Hardware](https://artificialanalysis.ai/benchmarks/hardware)
*   Leaderboards
*   About

*   [AI Trends](https://artificialanalysis.ai/trends)

*   Arenas

[](https://artificialanalysis.ai/login)K

[](https://x.com/ArtificialAnlys)[](https://www.linkedin.com/company/artificial-analysis/)

[All evaluations](https://artificialanalysis.ai/evaluations)
# AA-Briefcase: Agentic Knowledge Work Benchmark

A private evaluation developed by Artificial Analysis for frontier agentic capability in long-horizon knowledge work, testing agents on realistic business workflows that require deliverables such as spreadsheets, presentations, and memos.

### Related Links

[![Image 45: AA-Omniscience: Knowledge and Hallucination Benchmark](https://artificialanalysis.ai/img/logo-icon.svg)AA-Briefcase Launch Article](https://artificialanalysis.ai/articles/aa-briefcase "/articles/aa-briefcase")[![Image 46: AA-Omniscience: Knowledge and Hallucination Benchmark](https://artificialanalysis.ai/img/logo-icon.svg)AA-Briefcase Methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking#aa-briefcase "/methodology/intelligence-benchmarking#aa-briefcase")[![Image 47: ArtificialAnalysis/AA-Briefcase-Lite](https://artificialanalysis.ai/img/logos/huggingface_small.svg)ArtificialAnalysis/AA-Briefcase-Lite](https://huggingface.co/datasets/ArtificialAnalysis/AA-Briefcase-Lite "https://huggingface.co/datasets/ArtificialAnalysis/AA-Briefcase-Lite")[![Image 48: ArtificialAnalysis/Stirrup](https://artificialanalysis.ai/img/logos/github_small.svg)ArtificialAnalysis/Stirrup](https://github.com/ArtificialAnalysis/Stirrup "https://github.com/ArtificialAnalysis/Stirrup")

1 Structure 2 Submission 3 Grading and Scoring

AA-Briefcase evaluates models across four multi-week knowledge work projects, comprising thousands of input files and 91 tasks in total. Across the scenarios, models must complete realistic professional workflows in fields such as data science, product management, and corporate strategy. Each scenario is a multi-week workflow that the agent works through in sequence, each week holding several tasks. Every task is a deliverable graded against a rubric of checks. Although tasks within a scenario share files and context across weeks, models currently complete each task in an independent run, without carrying over their own prior submissions.

Each task is graded against three types of checks:

### Rubric

Binary pass or fail per check

Did the model follow the task instructions, identify requirements hidden across source files, use the correct evidence, and reach the right conclusions?

### Analytical Quality

Pairwise comparison

Compared against another model's submission, which deliverable is more thorough, analytically rigorous, and well-supported?

### Presentation

Pairwise comparison

Compared against another model's submission, which one is more professionally presented?

A public fifth scenario has been released via[Hugging Face](https://huggingface.co/datasets/ArtificialAnalysis/AA-Briefcase-Lite)as a representation of scenario structure, submission, and grading. This does not count toward official AA-Briefcase results, and is demonstrative only.

[Results](https://artificialanalysis.ai/evaluations/aa-briefcase#results)[Cost](https://artificialanalysis.ai/evaluations/aa-briefcase#cost)[Example Task, Submissions, and Grading](https://artificialanalysis.ai/evaluations/aa-briefcase#example-tasks)[Score Comparisons](https://artificialanalysis.ai/evaluations/aa-briefcase#score-comparisons)[File Type Results](https://artificialanalysis.ai/evaluations/aa-briefcase#file-type-results)[Token Usage](https://artificialanalysis.ai/evaluations/aa-briefcase#token-usage)[Speed](https://artificialanalysis.ai/evaluations/aa-briefcase#time-per-task)[Turns](https://artificialanalysis.ai/evaluations/aa-briefcase#mean-turns)[Tool Usage](https://artificialanalysis.ai/evaluations/aa-briefcase#tool-usage)[Model Size (Open Weights Models Only)](https://artificialanalysis.ai/evaluations/aa-briefcase#model-size)[Score vs. Release Date](https://artificialanalysis.ai/evaluations/aa-briefcase#score-vs-release-date)[Leaderboard](https://artificialanalysis.ai/evaluations/aa-briefcase#leaderboard)

## Results

AA-Briefcase Elo AA-Briefcase Rubric Score (%)Analytical Quality & Presentation Elo

### AA-Briefcase Elo

AA-Briefcase is an agentic knowledge work benchmark developed by Artificial Analysis. AA-Briefcase Elo is a combined metric that aggregates rubric pass rate, analytical quality Elo and presentation Elo · Higher is better

26 of 44 models

Add model from specific provider

Reasoning models are indicated by a lightbulb icon

### AA-Briefcase Elo

AA-Briefcase Elo is a combined metric that aggregates analytical quality Elo, presentation Elo, and rubric pass rate, with rubric performance converted into Elo via synthetic head-to-head matches. Elo and 95% confidence interval bounds are clamped at 0.

## Cost

Cost per Task AA-Briefcase Elo vs. Cost per Task Cost by File Type Total Cost to Run AA-Briefcase Elo vs. Total Cost

### AA-Briefcase Cost per Task

Mean cost (USD) per task to run AA-Briefcase, calculated from token usage and model pricing including representative cache hit rates

26 of 44 models

Answer Reasoning Cache Write Cache Hit Input

Reasoning models are indicated by a lightbulb icon

### Cost per Task

The total cost to run AA-Briefcase divided by the number of tasks (91 for full submission of tasks). Cost is calculated from token usage and model pricing, split across input, cache hit, cache write, reasoning, and answer token prices, including representative cache hit rates.

## Example Task, Submissions, and Grading

Explore a representative AA-Briefcase week from the public Due Diligence scenario available via[Hugging Face](https://huggingface.co/datasets/ArtificialAnalysis/AA-Briefcase-Lite). The outputs and grading shown here illustrate what AA-Briefcase evaluates. Scores are shown for a representative model set. Submissions and verdicts in this representative scenario do not contribute to a model's AA-Briefcase Elo or other benchmark scores.

Scenario overview

Week 1 overview(Note: the public scenario only has 1 week for illustrative purposes)

Task 1 Market Structure Map Task 2 Market Model Task 3 Target Assessment Task 4 Briefing Video

Task brief

Model![Image 49: Anthropic logo](https://artificialanalysis.ai/img/logos/anthropic_small.svg)Claude Fable 5

Compare models

Model submission

market_overview.pdf

[Open](https://artificialanalysiscdn.com/aa-briefcase-example-files/submissions/claude-fable-5/w1_t1/submission/market_overview.pdf)

market_overview.tex

[Open](https://artificialanalysiscdn.com/aa-briefcase-example-files/submissions/claude-fable-5/w1_t1/submission/market_overview.tex)

Grading summary

Source files 32 of 67 relevant · same for all models

## Score Comparisons

AA-Briefcase Elo vs. Intelligence Index Analytical Quality vs. Presentation Elo Analytical Quality Elo vs. Rubric Score (%)Presentation Elo vs. Rubric Score (%)

### AA-Briefcase Elo vs. Artificial Analysis Intelligence Index

AA-Briefcase Elo · Artificial Analysis Intelligence Index

26 of 44 models

Add model from specific provider

Most attractive quadrant

OpenAI Meta Google Anthropic Mistral DeepSeek SpaceXAI Upstage MiniMax NVIDIA Kimi Xiaomi MBZUAI Institute of Foundation Models Z AI Alibaba

### AA-Briefcase Elo

AA-Briefcase Elo is a combined metric that aggregates analytical quality Elo, presentation Elo, and rubric pass rate, with rubric performance converted into Elo via synthetic head-to-head matches. Elo and 95% confidence interval bounds are clamped at 0.

### Artificial Analysis Intelligence Index

Artificial Analysis Intelligence Index v4.1 includes: GDPval-AA v2, 𝜏³-Banking, Terminal-Bench v2.1, SciCode, Humanity's Last Exam, GPQA Diamond, CritPt, AA-Omniscience, AA-LCR. See[Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) for further details, including a breakdown of each evaluation and how we run them.

## File Type Results

AA-Briefcase performance broken out by the file type of the deliverable (Excel, PowerPoint, PDF, Word, Other).

Rubric Score by File Type (Normalized)Analytical Quality Elo by File Type (Normalized)Presentation Elo by File Type (Normalized)

### AA-Briefcase Rubric Pass Rate by File Type (Normalized)

Rubric pass rate by deliverable file type · Scores are normalized per file type across all models tested, where green represents the highest score for that file type and red represents the lowest score for that file type

26 of 44 models

Add model from specific provider

Reasoning models are indicated by a lightbulb icon

### File Types

File types are categorized by the required submission format, with “Other” covering formats such as HTML and LaTeX.

### AA-Briefcase Rubric Score

The share of binary rubric checks the submission passed (passed checks divided by total checks), aggregated across all AA-Briefcase tasks. Rubric checks are pass/fail criteria covering whether the deliverable includes required content and cites sources correctly, and whether it resolves planted cross-source conflicts.

## Token Usage

Output Tokens per Task Output Token Usage AA-Briefcase Elo vs. Output Token Usage AA-Briefcase Token Breakdown Token Usage by File Type

### AA-Briefcase Output Tokens per Task

Mean reasoning and answer tokens consumed per AA-Briefcase task

26 of 44 models

Answer tokens Reasoning tokens

Reasoning models are indicated by a lightbulb icon

### Evaluation Output Tokens

The number of output tokens used to run the evaluation, including visible answer tokens and reasoning tokens where reported by reasoning models.

## Speed

Time per Task AA-Briefcase Elo vs. Time per Task

### Time per Task

Wall-clock time (minutes) per task: answer and reasoning generation plus tool execution time · Lower is better

26 of 44 models

Reasoning models are indicated by a lightbulb icon

### AA-Briefcase Time per Task

Estimated wall-clock time per task: the sum of answer and reasoning tokens per task divided by the model’s canonical answer output speed, plus mean tool execution time per task. Lower is better.

## Turns

Mean Turns per Task Turns per Task (Range)AA-Briefcase Elo vs. Mean Turns

### Mean Turns per Task

Average number of model turns per AA-Briefcase task · Lower is better

26 of 44 models

Reasoning models are indicated by a lightbulb icon

### What Turns Is Measuring

This chart shows the average number of turns the agent takes per task. It is a rough proxy for how many actions, tool calls, and iteration cycles an agent is using to complete benchmark tasks.

## Tool Usage

Tool invocations issued by each agent during AA-Briefcase: counts by tool category, mean tool calls per turn, and source-pool exploration coverage.

Tool Calls Breakdown Mean Tool Calls per Turn File Exploration Coverage

### AA-Briefcase Tool Calls Breakdown, Avg per Task

Average tool invocations per AA-Briefcase task, bucketed by intent

26 of 44 models

Add model from specific provider

Explore View Image Read Compute Write Other

Reasoning models are indicated by a lightbulb icon

### AA-Briefcase Tool Calls Breakdown

Agent tool calls are grouped into six categories: explore (navigating and searching the workspace), read (reading file contents), write (creating or editing files), compute (running code or calculations), view image (visual inspection of files), and other (anything else).

## Model Size (Open Weights Models Only)

AA-Briefcase Elo vs. Total Parameters AA-Briefcase Elo vs. Active Parameters AA-Briefcase Elo vs. Compute Proxy

### AA-Briefcase Elo vs. Total Parameters

AA-Briefcase Elo · Size in parameters (billions) · Open weights models only

26 of 44 models

Add model from specific provider

Most attractive quadrant

OpenAI Google Mistral DeepSeek Upstage MiniMax NVIDIA Kimi Xiaomi MBZUAI Institute of Foundation Models Z AI Alibaba

### AA-Briefcase Elo

AA-Briefcase Elo is a combined metric that aggregates analytical quality Elo, presentation Elo, and rubric pass rate, with rubric performance converted into Elo via synthetic head-to-head matches. Elo and 95% confidence interval bounds are clamped at 0.

### Total Parameters

The total number of trainable weights and biases in the model, expressed in billions. These parameters are learned during training and determine the model's ability to process and generate responses.

## Score vs. Release Date

### AA-Briefcase Elo vs. Release Date

AA-Briefcase Elo · Model release date

26 of 44 models

Add model from specific provider

Most attractive region

OpenAI Meta Google Anthropic Mistral DeepSeek SpaceXAI Upstage MiniMax NVIDIA Kimi Xiaomi MBZUAI Institute of Foundation Models Z AI Alibaba

### AA-Briefcase Elo

AA-Briefcase Elo is a combined metric that aggregates analytical quality Elo, presentation Elo, and rubric pass rate, with rubric performance converted into Elo via synthetic head-to-head matches. Elo and 95% confidence interval bounds are clamped at 0.

## Leaderboard

Expand score breakdown

|  | Creator | Name | Elo | CI | Release Date |
| --- | --- | --- | --- | --- | --- |
| 1 | ![Image 50: Anthropic logo](https://artificialanalysis.ai/img/logos/anthropic_small.svg)Anthropic | Claude Fable 5 (Adaptive Reasoning, Max Effort, Opus 4.8 Fallback) | 1583 | -15 / +16 | Jun 2026 |
| 2 | ![Image 51: Anthropic logo](https://artificialanalysis.ai/img/logos/anthropic_small.svg)Anthropic | Claude Sonnet 5 (Adaptive Reasoning, Max Effort) | 1390 | -11 / +12 | Jun 2026 |
| 3 | ![Image 52: Anthropic logo](https://artificialanalysis.ai/img/logos/anthropic_small.svg)Anthropic | Claude Opus 4.8 (Adaptive Reasoning, Max Effort) | 1354 | -11 / +10 | May 2026 |
| 4 | ![Image 53: SpaceXAI logo](https://artificialanalysis.ai/img/logos/spacexai.svg)SpaceXAI | Grok 4.5 (high) | 1328 | -13 / +13 | Jul 2026 |
| 5 | ![Image 54: Anthropic logo](https://artificialanalysis.ai/img/logos/anthropic_small.svg)Anthropic | Claude Sonnet 5 (Adaptive Reasoning, Xhigh Effort) | 1300 | -11 / +11 | Jun 2026 |
| 6 | ![Image 55: Anthropic logo](https://artificialanalysis.ai/img/logos/anthropic_small.svg)Anthropic | Claude Opus 4.7 (Adaptive Reasoning, Max Effort) | 1289 | -10 / +10 | Apr 2026 |
| 7 | ![Image 56: Z AI logo](https://artificialanalysis.ai/img/logos/zai_small.svg)Z AI | GLM-5.2 (max) | 1261 | -11 / +11 | Jun 2026 |
| 8 | ![Image 57: Anthropic logo](https://artificialanalysis.ai/img/logos/anthropic_small.svg)Anthropic | Claude Sonnet 5 (Adaptive Reasoning, High Effort) | 1201 | -11 / +11 | Jun 2026 |
| 9 | ![Image 58: MATH-500 Benchmark Leaderboard](https://artificialanalysis.ai/img/logos/openai_small.svg)OpenAI | GPT-5.5 (xhigh) | 1158 | -10 / +9 | Apr 2026 |
| 10 | ![Image 59: MiniMax logo](https://artificialanalysis.ai/img/logos/minimax_small.svg)MiniMax | MiniMax-M3 | 1111 | -9 / +9 | Jun 2026 |
| 11 | ![Image 60: MATH-500 Benchmark Leaderboard](https://artificialanalysis.ai/img/logos/openai_small.svg)OpenAI | GPT-5.5 (high) | 1103 | -9 / +9 | Apr 2026 |
| 12 | ![Image 61: Anthropic logo](https://artificialanalysis.ai/img/logos/anthropic_small.svg)Anthropic | Claude Opus 4.7 (Non-reasoning, High Effort) | 1090 | -9 / +9 | Apr 2026 |
| 13 | ![Image 62: Anthropic logo](https://artificialanalysis.ai/img/logos/anthropic_small.svg)Anthropic | Claude Sonnet 4.6 (Adaptive Reasoning, Max Effort) | 1079 | -8 / +9 | Feb 2026 |
| 14 | ![Image 63: Anthropic logo](https://artificialanalysis.ai/img/logos/anthropic_small.svg)Anthropic | Claude Sonnet 5 (Adaptive Reasoning, Medium Effort) | 1061 | -10 / +11 | Jun 2026 |
| 15 | ![Image 64: MATH-500 Benchmark Leaderboard](https://artificialanalysis.ai/img/logos/openai_small.svg)OpenAI | GPT-5.5 (medium) | 1000 | -0 / +0 | Apr 2026 |
| 16 | ![Image 65: Z AI logo](https://artificialanalysis.ai/img/logos/zai_small.svg)Z AI | GLM-5.1 (Reasoning) | 974 | -9 / +9 | Apr 2026 |
| 17 | ![Image 66: DeepSeek logo](https://artificialanalysis.ai/img/logos/deepseek_small.svg)DeepSeek | DeepSeek V4 Pro (Reasoning, Max Effort) | 932 | -9 / +9 | Apr 2026 |
| 18 | ![Image 67: Anthropic logo](https://artificialanalysis.ai/img/logos/anthropic_small.svg)Anthropic | Claude Sonnet 5 (Adaptive Reasoning, Low Effort) | 926 | -10 / +9 | Jun 2026 |
| 19 | ![Image 68: Alibaba logo](https://artificialanalysis.ai/img/logos/alibaba_small.svg)Alibaba | Qwen3.7 Max | 907 | -9 / +8 | May 2026 |
| 20 | ![Image 69: Xiaomi logo](https://artificialanalysis.ai/img/logos/xiaomi_small.svg)Xiaomi | MiMo-V2.5-Pro | 872 | -9 / +8 | Apr 2026 |
| 21 | ![Image 70: NVIDIA logo](https://artificialanalysis.ai/img/logos/nvidia_small.svg)NVIDIA | Nemotron 3 Ultra 550B A55B (Reasoning) | 870 | -10 / +10 | Jun 2026 |
| 22 | ![Image 71: Google logo](https://artificialanalysis.ai/img/logos/google_small.svg)Google | Gemini 3.5 Flash (medium) | 868 | -10 / +10 | May 2026 |
| 23 | ![Image 72: Google logo](https://artificialanalysis.ai/img/logos/google_small.svg)Google | Gemini 3.5 Flash (high) | 866 | -10 / +9 | May 2026 |
| 24 | ![Image 73: MATH-500 Benchmark Leaderboard](https://artificialanalysis.ai/img/logos/openai_small.svg)OpenAI | GPT-5.3 Codex (xhigh) | 864 | -10 / +9 | Feb 2026 |
| 25 | ![Image 74: DeepSeek logo](https://artificialanalysis.ai/img/logos/deepseek_small.svg)DeepSeek | DeepSeek V4 Flash (Reasoning, Max Effort) | 829 | -10 / +10 | Apr 2026 |
| 26 | ![Image 75: Kimi logo](https://artificialanalysis.ai/_next/image?url=%2Fimg%2Flogos%2Fkimi_small.png&w=32&q=75)Kimi | Kimi K2.6 | 809 | -10 / +10 | Apr 2026 |
| 27 | ![Image 76: Alibaba logo](https://artificialanalysis.ai/img/logos/alibaba_small.svg)Alibaba | Qwen3.6 27B (Reasoning) | 805 | -11 / +11 | Apr 2026 |
| 28 | ![Image 77: SpaceXAI logo](https://artificialanalysis.ai/img/logos/spacexai.svg)SpaceXAI | Grok 4.3 (high) | 750 | -11 / +9 | Apr 2026 |
| 29 | ![Image 78: MATH-500 Benchmark Leaderboard](https://artificialanalysis.ai/img/logos/openai_small.svg)OpenAI | GPT-5.4 mini (xhigh) | 705 | -10 / +10 | Mar 2026 |
| 30 | ![Image 79: Meta logo](https://artificialanalysis.ai/img/logos/meta_small.svg)Meta | Muse Spark | 630 | -11 / +10 | Apr 2026 |
| 31 | ![Image 80: Anthropic logo](https://artificialanalysis.ai/img/logos/anthropic_small.svg)Anthropic | Claude 4.5 Haiku (Reasoning) | 601 | -12 / +10 | Oct 2025 |
| 32 | ![Image 81: KwaiKAT logo](https://artificialanalysis.ai/img/logos/kwaikat_small.svg)KwaiKAT | KAT-Coder-Pro V1 | 590 | -13 / +12 | Nov 2025 |
| 33 | ![Image 82: Alibaba logo](https://artificialanalysis.ai/img/logos/alibaba_small.svg)Alibaba | Qwen3.5 397B A17B (Reasoning) | 544 | -11 / +11 | Feb 2026 |
| 34 | ![Image 83: Mistral logo](https://artificialanalysis.ai/_next/image?url=%2Fimg%2Flogos%2Fmistral_small.png&w=32&q=75)Mistral | Mistral Medium 3.5 | 503 | -12 / +11 | Apr 2026 |
| 35 | ![Image 84: Google logo](https://artificialanalysis.ai/img/logos/google_small.svg)Google | Gemini 3.1 Pro Preview | 445 | -12 / +11 | Feb 2026 |
| 36 | ![Image 85: Google logo](https://artificialanalysis.ai/img/logos/google_small.svg)Google | Gemma 4 31B (Reasoning) | 359 | -14 / +12 | Apr 2026 |
| 37 | ![Image 86: Global-MMLU-Lite Benchmark Leaderboard](https://artificialanalysis.ai/img/logos/cohere_small.svg)Cohere | Command A+ | 352 | -17 / +15 | May 2026 |
| 38 | ![Image 87: Google logo](https://artificialanalysis.ai/img/logos/google_small.svg)Google | Gemini 3.1 Flash-Lite | 214 | -16 / +13 | Mar 2026 |
| 39 | ![Image 88: Upstage logo](https://artificialanalysis.ai/img/logos/upstage_small.svg)Upstage | Solar Pro 3 | 122 | -16 / +13 | Apr 2026 |
| 40 | ![Image 89: MBZUAI Institute of Foundation Models logo](https://artificialanalysis.ai/img/logos/mbzuai_small.svg)MBZUAI Institute of Foundation Models | K2 Think V2 | 44 | -17 / +13 | Dec 2025 |
| 41 | ![Image 90: MATH-500 Benchmark Leaderboard](https://artificialanalysis.ai/img/logos/openai_small.svg)OpenAI | gpt-oss-120b (high) | 0 | -0 / +4 | Aug 2025 |
| 42 | ![Image 91: MATH-500 Benchmark Leaderboard](https://artificialanalysis.ai/img/logos/openai_small.svg)OpenAI | gpt-oss-20b (high) | 0 | -0 / +0 | Aug 2025 |
| 43 | ![Image 92: Meta logo](https://artificialanalysis.ai/img/logos/meta_small.svg)Meta | Llama 4 Maverick | 0 | -0 / +0 | Apr 2025 |
| 44 | ![Image 93: NVIDIA logo](https://artificialanalysis.ai/img/logos/nvidia_small.svg)NVIDIA | NVIDIA Nemotron 3 Super 120B A12B (Reasoning) | 0 | -0 / +0 | Mar 2026 |

## Explore Evaluations

[![Image 94: AA-Omniscience: Knowledge and Hallucination Benchmark](https://artificialanalysis.ai/img/logo-icon.svg)Artificial Analysis Intelligence Index A composite benchmark aggregating nine challenging evaluations to provide a holistic measure of AI capabilities across mathematics, science, coding, and reasoning.](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)[![Image 95: AA-Omniscience: Knowledge and Hallucination Benchmark](https://artificialanalysis.ai/img/logo-icon.svg)Artificial Analysis Openness Index A composite measure providing an industry standard to communicate model openness for users and developers.](https://artificialanalysis.ai/evaluations/artificial-analysis-openness-index)[![Image 96: AA-Omniscience: Knowledge and Hallucination Benchmark](https://artificialanalysis.ai/img/logo-icon.svg)AA-Briefcase: Agentic Knowledge Work Benchmark A private evaluation developed by Artificial Analysis for frontier agentic capability in long-horizon knowledge work, testing agents on realistic business workflows that require deliverables such as spreadsheets, presentations, and memos.](https://artificialanalysis.ai/evaluations/aa-briefcase)[![Image 97: AA-Omniscience: Knowledge and Hallucination Benchmark](https://artificialanalysis.ai/img/logo-icon.svg)GDPval-AA v2 Leaderboard GDPval-AA v2 is Artificial Analysis' evaluation framework for OpenAI's GDPval dataset. It tests AI models on real-world tasks across 44 occupations and 9 major industries. Models are given shell access and web browsing capabilities in an agentic loop via Stirrup to solve tasks, with Elo ratings derived from blind pairwise comparisons.](https://artificialanalysis.ai/evaluations/gdpval-aa)[![Image 98: APEX-Agents-AA Benchmark Leaderboard](https://artificialanalysis.ai/_next/image?url=%2Fimg%2Flogos%2Fmercor_small.png&w=32&q=75)APEX-Agents-AA Benchmark Leaderboard Artificial Analysis' implementation of the APEX-Agents benchmark, testing AI agents on long-horizon, cross-application tasks in professional-services environments with realistic application tooling.](https://artificialanalysis.ai/evaluations/apex-agents-aa)[![Image 99: AutomationBench-AA: Agentic SaaS Workflow Benchmark](https://artificialanalysis.ai/img/logos/zapier.svg)AutomationBench-AA: Agentic SaaS Workflow Benchmark A benchmark measuring agentic task completion across simulated SaaS application environments, scoring the share of each task's objectives completed without guardrail violations.](https://artificialanalysis.ai/evaluations/automationbench-aa)[![Image 100: Harvey LAB-AA Benchmark Leaderboard](https://artificialanalysis.ai/img/logos/harvey.svg)Harvey LAB-AA Benchmark Leaderboard Artificial Analysis' implementation of Harvey's Legal Agent Benchmark (LAB), testing AI agents on real-world legal work from Harvey's dataset of 120 private tasks spanning 24 legal practice areas. The agent reads case documents in a sandbox and produces legal deliverables (e.g., memos, disclosure schedules, deposition summaries), graded criterion-by-criterion by a single LLM rubric judge.](https://artificialanalysis.ai/evaluations/harvey-lab-aa)[![Image 101: 𝜏²-Bench Telecom Benchmark Leaderboard](https://artificialanalysis.ai/img/logos/sierra_small.svg)𝜏³-Banking Benchmark Leaderboard A fintech customer-support benchmark from the 𝜏-Knowledge framework that tests whether agents can navigate a large unstructured knowledge base and execute multi-step tool calls to resolve realistic banking workflows.](https://artificialanalysis.ai/evaluations/tau3-banking)[![Image 102: Terminal-Bench Hard Benchmark Leaderboard](https://artificialanalysis.ai/img/logos/tbench_small.svg)Terminal-Bench v2.1 Benchmark Leaderboard A verified refresh of Terminal-Bench v2.0 — 89 curated tasks across software engineering, system administration, data processing, model training, and security, with environment and instruction fixes so scores reflect agent capability rather than environment gaps.](https://artificialanalysis.ai/evaluations/terminalbench-v2-1)[![Image 103: AA-Omniscience: Knowledge and Hallucination Benchmark](https://artificialanalysis.ai/img/logo-icon.svg)Artificial Analysis Long Context Reasoning Benchmark Leaderboard A challenging benchmark measuring language models' ability to extract, reason about, and synthesize information from long-form documents ranging from 10k to 100k tokens (measured using the cl100k_base tokenizer).](https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning)[![Image 104: AA-Omniscience: Knowledge and Hallucination Benchmark](https://artificialanalysis.ai/img/logo-icon.svg)AA-Omniscience: Knowledge and Hallucination Benchmark A benchmark measuring factual recall and hallucination across various economically relevant domains.](https://artificialanalysis.ai/evaluations/omniscience)[![Image 105: SciCode Benchmark Leaderboard](https://artificialanalysis.ai/img/logos/scicode_small.svg)SciCode Benchmark Leaderboard A scientist-curated coding benchmark featuring 288 test set subproblems from 80 laboratory problems across 16 scientific disciplines.](https://artificialanalysis.ai/evaluations/scicode)[![Image 106: Humanity's Last Exam Benchmark Leaderboard](https://artificialanalysis.ai/img/logos/hle_small.svg)Humanity's Last Exam Benchmark Leaderboard A frontier-level benchmark with 2,500 expert-vetted questions across mathematics, sciences, and humanities, designed to be the final closed-ended academic evaluation.](https://artificialanalysis.ai/evaluations/humanitys-last-exam)[![Image 107: CritPt Benchmark Leaderboard](https://artificialanalysis.ai/_next/image?url=%2Fimg%2Flogos%2Fcritpt_small.png&w=32&q=75)CritPt Benchmark Leaderboard A benchmark designed to test LLMs on research-level physics reasoning tasks, featuring 71 composite research challenges.](https://artificialanalysis.ai/evaluations/critpt)[GPQA Diamond Benchmark Leaderboard The most challenging 198 questions from GPQA, where PhD experts achieve 65% accuracy but skilled non-experts only reach 34% despite web access.](https://artificialanalysis.ai/evaluations/gpqa-diamond)[![Image 108: ITBench-AA Benchmark Leaderboard](https://artificialanalysis.ai/img/logos/ibm_small.svg)ITBench-AA Benchmark Leaderboard Artificial Analysis' implementation of IBM's ITBench benchmark, testing AI agents on Kubernetes incident root-cause analysis from offline incident snapshots. The agent inspects alerts, events, traces, and topology and identifies the contributing-factor entities (deployments, pods, namespaces, network policies, etc.) responsible for the failure.](https://artificialanalysis.ai/evaluations/itbench-aa)[![Image 109: MMMU-Pro Benchmark Leaderboard](https://artificialanalysis.ai/_next/image?url=%2Fimg%2Flogos%2Fmmmu_small.png&w=32&q=75)MMMU-Pro Benchmark Leaderboard An enhanced MMMU benchmark that eliminates shortcuts and guessing strategies to more rigorously test multimodal models across 30 academic disciplines.](https://artificialanalysis.ai/evaluations/mmmu-pro)[![Image 110: IFBench Benchmark Leaderboard](https://artificialanalysis.ai/img/logos/ai2_small.svg)IFBench Benchmark Leaderboard A benchmark evaluating precise instruction-following generalization on 58 diverse, verifiable out-of-domain constraints that test models' ability to follow specific output requirements.](https://artificialanalysis.ai/evaluations/ifbench)[![Image 111: Terminal-Bench Hard Benchmark Leaderboard](https://artificialanalysis.ai/img/logos/tbench_small.svg)Terminal-Bench Hard Benchmark Leaderboard An agentic benchmark evaluating AI capabilities in terminal environments through software engineering, system administration, and data processing tasks.](https://artificialanalysis.ai/evaluations/terminalbench-hard)[![Image 112: 𝜏²-Bench Telecom Benchmark Leaderboard](https://artificialanalysis.ai/img/logos/sierra_small.svg)𝜏²-Bench Telecom Benchmark Leaderboard A dual-control conversational AI benchmark simulating technical support scenarios where both agent and user must coordinate actions to resolve telecom service issues.](https://artificialanalysis.ai/evaluations/tau2-bench)[![Image 113: MMLU-Pro Benchmark Leaderboard](https://artificialanalysis.ai/_next/image?url=%2Fimg%2Flogos%2Ftiger_lab_small.jpg&w=32&q=75)MMLU-Pro Benchmark Leaderboard An enhanced version of MMLU with 12,000 graduate-level questions across 14 subject areas, featuring ten answer options and deeper reasoning requirements.](https://artificialanalysis.ai/evaluations/mmlu-pro)[![Image 114: LiveCodeBench Benchmark Leaderboard](https://artificialanalysis.ai/img/logos/livecodebench_small.svg)LiveCodeBench Benchmark Leaderboard A contamination-free coding benchmark that continuously harvests fresh competitive programming problems from LeetCode, AtCoder, and CodeForces, evaluating code generation, self-repair, and execution.](https://artificialanalysis.ai/evaluations/livecodebench)[![Image 115: MATH-500 Benchmark Leaderboard](https://artificialanalysis.ai/img/logos/openai_small.svg)MATH-500 Benchmark Leaderboard A 500-problem subset from the MATH dataset, featuring competition-level mathematics across six domains including algebra, geometry, and number theory.](https://artificialanalysis.ai/evaluations/math-500)[![Image 116: AIME 2025 Benchmark Leaderboard](https://artificialanalysis.ai/img/logos/aops_small.svg)AIME 2025 Benchmark Leaderboard All 30 problems from the 2025 American Invitational Mathematics Examination, testing olympiad-level mathematical reasoning with integer answers from 000-999.](https://artificialanalysis.ai/evaluations/aime-2025)[![Image 117: Global-MMLU-Lite Benchmark Leaderboard](https://artificialanalysis.ai/img/logos/cohere_small.svg)Global-MMLU-Lite Benchmark Leaderboard A lightweight, multilingual version of MMLU, designed to evaluate knowledge and reasoning skills across a diverse range of languages and cultural contexts.](https://artificialanalysis.ai/evaluations/global-mmlu-lite)

[](https://artificialanalysis.ai/)
Artificial Analysis

Get notified about new articles

Email address Subscribe

Artificial Analysis

Explore

*   [LLM Leaderboard](https://artificialanalysis.ai/leaderboards/models)
*   [Image Arena](https://artificialanalysis.ai/image/arena)
*   [Video Arena](https://artificialanalysis.ai/video/arena)
*   [AI Agents](https://artificialanalysis.ai/agents)
*   [Evaluations](https://artificialanalysis.ai/evaluations)

Company

*   [Methodology](https://artificialanalysis.ai/methodology)
*   [Services](https://artificialanalysis.ai/services)
*   [Contact](https://artificialanalysis.ai/contact)
*   [Articles](https://artificialanalysis.ai/articles)
*   [FAQ](https://artificialanalysis.ai/faq)

[X](https://x.com/ArtificialAnlys)[LinkedIn](https://www.linkedin.com/company/artificial-analysis/)[YouTube](https://www.youtube.com/@ArtificialAnalysisAI)[Rednote](https://www.xiaohongshu.com/user/profile/69ea6345000000000d034c02)[Discord](https://discord.gg/Mk298GPZ7V)

© 2026 Artificial Analysis

[Terms of Use](https://artificialanalysis.ai/docs/legal/Terms-of-Use.pdf)[Privacy Policy](https://artificialanalysis.ai/docs/legal/Privacy-Policy.pdf)

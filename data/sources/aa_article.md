Title: Announcing AA-Briefcase: a frontier knowledge work evaluation

URL Source: https://artificialanalysis.ai/articles/aa-briefcase

Published Time: 2026-06-18

Markdown Content:
## AA-Briefcase leaderboard

### AA-Briefcase Elo

AA-Briefcase is an agentic knowledge work benchmark developed by Artificial Analysis. AA-Briefcase Elo is a combined metric that aggregates rubric pass rate, analytical quality Elo and presentation Elo · Higher is better. Data as at 18 June 2026

Reasoning models are indicated by a lightbulb icon

AA-Briefcase Elo is a combined metric that aggregates analytical quality Elo, presentation Elo, and rubric pass rate, with rubric performance converted into Elo via synthetic head-to-head matches. Elo and 95% confidence interval bounds are clamped at 0.

Claude Fable 5 achieves the highest AA-Briefcase Elo, which combines rubric pass rate with pairwise analytical quality Elo and presentation quality Elo.

This is followed by Claude Opus 4.8 (max) and GLM-5.2 (max), with GPT-5.5 (xhigh) in fourth and Opus 4.8 tied for the lead on presentation quality. GLM-5.2 (max) is the clear leader among open-weight models and offers an attractive agentic capability vs. cost tradeoff.

For up-to-date results see the[AA-Briefcase evaluation page](https://artificialanalysis.ai/evaluations/aa-briefcase)

## AA-Briefcase measures real-world agentic capability

As capability increases, models are being used for increasingly complex long-horizon knowledge work tasks. We designed AA-Briefcase to simulate how models are actually being used in real knowledge work:

### Realistic, long-horizon projects

AA-Briefcase moves beyond single, disconnected prompts by evaluating models across a coherent long-horizon project. Tasks build week by week, draw on shared institutional context, and require realistic company deliverables such as financial models, board presentations, and design mock-ups.

### Composite rubric and pairwise grading

AA-Briefcase combines binary rubric checks for ground-truth correctness with pairwise grading on analytical quality and presentation quality. Unlike many evaluations that focus on a single metric, AA-Briefcase tests the core capabilities required of a high-quality knowledge work agent, exposing cases where models produce outputs that look polished but are incorrect or lack analytical rigor.

### High volumes of fragmented context

AA-Briefcase tasks require models to reason across hundreds of input files per task, spanning Slack threads, emails, company documents, meeting transcripts, and large-scale data exports. In total, AA-Briefcase contains nearly 2,000 source files, with email and Slack exports including more than 3,500 emails and 25,000 Slack messages. These sources are fragmented, messy, and often contain realistic contradiction, testing whether models can navigate the ambiguity of real-world knowledge work.

### Built by industry experts

AA-Briefcase scenarios mirror real-world knowledge work, with tasks developed over months by experts across data science, product management and corporate strategy from companies including Google, McKinsey & Company and Boston Consulting Group. Task challenges are drawn from professional experience, making AA-Briefcase more reflective of the ambiguity, messy context and competing priorities that define real-world knowledge work.

To maintain evaluation integrity, all 91 tasks across the four AA-Briefcase project scenarios are private, including task instructions, project input files and grading rubrics. A public fifth scenario has been released via[Hugging Face](https://huggingface.co/datasets/ArtificialAnalysis/AA-Briefcase-Lite)as a representation of scenario structure, submission, and grading. This does not count toward official AA-Briefcase results, and is demonstrative only.

## How AA-Briefcase works

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

## The cost of an AA-Briefcase task

The cost per task on AA-Briefcase varies by more than 800x across models tested.

Claude Fable 5 leads the benchmark but costs more than $31 per task on average, compared to ~$0.04 for DeepSeek V4 Flash (Max). None of the lowest-cost-per-task models reach frontier AA-Briefcase performance. The strongest price/performance options are open-weight models such as GLM-5.2 (max) and DeepSeek V4 Pro (max), with GLM-5.2 (max) scoring only ~90 Elo below Claude Opus 4.8 (max) for less than 25% of the cost.

### AA-Briefcase Cost per Task

Mean cost (USD) per task to run AA-Briefcase, calculated from token usage and model pricing including representative cache hit rates. Data as at 18 June 2026

Reasoning models are indicated by a lightbulb icon

The total cost to run AA-Briefcase divided by the number of tasks (91 for full submission of tasks). Cost is calculated from token usage and model pricing, split across input, cache hit, cache write, reasoning, and answer token prices, including representative cache hit rates.

### AA-Briefcase Elo vs. Cost per Task

AA-Briefcase Elo · Cost per task (USD). Data as at 18 June 2026

Most attractive quadrant

AA-Briefcase Elo is a combined metric that aggregates analytical quality Elo, presentation Elo, and rubric pass rate, with rubric performance converted into Elo via synthetic head-to-head matches. Elo and 95% confidence interval bounds are clamped at 0.

The total cost to run AA-Briefcase divided by the number of tasks (91 for full submission of tasks). Cost is calculated from token usage and model pricing, split across input, cache hit, cache write, reasoning, and answer token prices, including representative cache hit rates.

## What AA-Briefcase tells us about agentic capability

### AA-Briefcase scenarios reflect more real-world complexity than other knowledge work evaluation tasks

AA-Briefcase tasks require models to sort through thousands of messy input files, balance competing stakeholder demands, and produce complex deliverables, reflecting the core challenges of real knowledge work. Objective rubric checks verify whether models successfully handle these challenges. Claude Fable 5 leads overall on rubric pass rate, but satisfies all criteria correctly on only 3% of tasks. On 31 of 91 tasks, no model scores above 50%.

100% passed≥80% passed

Share of tasks where each model passes 100% or at least 80% of rubric checks, ordered by overall pass rate. Models with no tasks at or above 80% are excluded.

### Failure modes shift across model tiers

Less capable models most often fail at task execution, missing relevant input files, submitting unusable deliverables, or producing no deliverable at all.More capable models, measured by overall rubric pass rate, more often fail to fulfill all task requirements, including those embedded in the original task or hidden across source files. Incorrect or unfinished analysis and formatting errors remain common across all tiers.

Model failure modes by capability tier. Tiers are based on each model’s average rubric pass rate across the full task set, and failure categories are normalized within each tier so every bar sums to 100%.

### Task difficulty scales with the number of required input files

For each rubric check, we identify the minimum set of files a model must read to pass. Across all model capability tiers,pass rates fall as the number of required files increases. As checks require more external source files, top-tier models degrade less than weaker models. High-intelligence models (averaging ≥30% rubric pass rate) fall from ~55% on prompt-only checks to ~40% on checks requiring 5+ files.

Average rubric pass rate by number of input files required. Each point shows the average pass rate for a model tier on rubric criteria that require using information from that number of input files. Model tiers are based on overall rubric pass rate: high intelligence (≥30%), moderate intelligence (15-30%), and low intelligence (<15%). External source files does not include any of the task or scenario context prompts.

### Visual review improves presentation quality

The strongest presentation models inspect their rendered outputs far more often before submitting.Claude Fable 5 and Claude Opus 4.8 (max), the two leading models on presentation Elo, make 21 and 12 visual inspections per task on average respectively, while lower-scoring models inspect much less, with GPT-5.4 Mini at 2 per task and Gemini 3.1 Pro Preview at ~0.1, often submitting files they never visually reviewed.

Most attractive quadrant

AA-Briefcase Presentation Elo vs. average number of view image tool calls per task. Models that do not support image input, or that never use the view image tool are excluded. Data as at 18 June 2026.

## Detailed results

AA-Briefcase Elo increases with general intelligence, but the results also highlight different model strengths.

Claude Fable 5 leads on rubric pass rate and analytical quality Elo, while Claude Opus 4.8 (max) is tied for the lead on presentation Elo. MiniMax M3 and GLM-5.2 (max) outperform relative to their Artificial Analysis Intelligence Index score, while Google models such as Gemini 3.5 Flash and Gemini 3.1 Pro Preview underperform on AA-Briefcase relative to their general intelligence ranking.

### AA-Briefcase Elo vs. Artificial Analysis Intelligence Index

AA-Briefcase Elo · Artificial Analysis Intelligence Index. Data as at 18 June 2026

Most attractive quadrant

AA-Briefcase Elo is a combined metric that aggregates analytical quality Elo, presentation Elo, and rubric pass rate, with rubric performance converted into Elo via synthetic head-to-head matches. Elo and 95% confidence interval bounds are clamped at 0.

Artificial Analysis Intelligence Index v4.1 includes: GDPval-AA v2, 𝜏³-Banking, Terminal-Bench v2.1, SciCode, Humanity's Last Exam, GPQA Diamond, CritPt, AA-Omniscience, AA-LCR. See[Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) for further details, including a breakdown of each evaluation and how we run them.

Higher AA-Briefcase performance generally requires more tokens, but only at the frontier.

Claude Fable 5 leads the benchmark and is one of the highest token users, averaging 139k output tokens per task. Gemini 3.5 Flash uses the most output tokens of any model, averaging 146k output tokens per task, slightly more than Claude Fable 5, while scoring ~720 Elo lower. Further down the capability curve, DeepSeek V4 Pro (max) and Qwen 3.7 Max stand out as more efficient models, achieving stronger performance than peers with lower token usage.

### Output Tokens per Task

Mean reasoning and answer tokens consumed per AA-Briefcase task

Reasoning models are indicated by a lightbulb icon

The average number of answer and reasoning tokens produced per benchmark task in this evaluation.

Frontier AA-Briefcase performance can take ~20 minutes per task. For example, Claude Opus 4.8 (max) averages ~24 minutes of wall-clock time per task, with GLM-5.2 (max) averaging ~19 minutes. Longer runtime is not consistently associated with better performance however: MiniMax-M3 averages ~26 minutes per task, more than Claude Opus 4.8 (max), yet reaches an AA-Briefcase Elo of 1116, 240 points behind Opus.

A key driver of average time per task is the number of turns a model takes before submission. Models are allowed up to 500 turns per task, and can submit their work at any point or abandon the task using the`abandon_task_finish`tool. More turns give models more time to work, but we do not observe a strong correlation between turn count and performance. Gemini 3.5 Flash, for example, averages one of the highest turn counts, at ~88 per task, while landing well below the Elo leaders.

### Time per Task

Wall-clock time (minutes) per task: answer and reasoning generation plus tool execution time · Lower is better

Reasoning models are indicated by a lightbulb icon

Estimated wall-clock time per task: the sum of answer and reasoning tokens per task divided by the model’s canonical answer output speed, plus mean tool execution time per task. Lower is better.

### Mean Turns per Task

Average number of model turns per AA-Briefcase task · Lower is better

Reasoning models are indicated by a lightbulb icon

This chart shows the average number of turns the agent takes per task. It is a rough proxy for how many actions, tool calls, and iteration cycles an agent is using to complete benchmark tasks.

Tool use behavior varies by model family. We group agent tool calls into six categories: explore (navigating and searching the workspace), read (reading file contents), write (creating or editing files), compute (running code or calculations), view image (visual inspection of files), and other (anything else). Anthropic and MiniMax models make heavy use of visual inspection, with Claude Fable 5 and Claude Opus 4.8 (max) averaging ~21 and ~12 view image calls per task, respectively. These models lead in both overall Elo and Presentation Elo, suggesting that repeatedly inspecting rendered outputs is an important part of producing strong deliverables. Google models show a different pattern, with Gemini 3.5 Flash and Gemma 4 31B being much more compute-heavy, averaging ~60 and ~43 calls per task to run scripts or calculations, respectively.

### AA-Briefcase Tool Calls Breakdown, Avg per Task

Average tool invocations per AA-Briefcase task, bucketed by intent

Reasoning models are indicated by a lightbulb icon

Agent tool calls are grouped into six categories: explore (navigating and searching the workspace), read (reading file contents), write (creating or editing files), compute (running code or calculations), view image (visual inspection of files), and other (anything else).

Explore additional analysis and data on the[AA-Briefcase leaderboard](https://artificialanalysis.ai/evaluations/aa-briefcase).

## Inside the task scenarios

Expand each scenario to see example tasks from across the four knowledge work domains.

Held-out scenario

Quantitative work on imperfect datasets, turned into clear recommendations for a business audience

*   Transaction data cleaning and reconciliation
*   Technical research documentation
*   Forecast modeling and feature engineering
*   Data engineering and schema design

Held-out scenario

The work of a product leader in a complex business

*   Competitive teardowns and market research
*   MVP feature prioritization
*   PRD writing and design specs
*   Go-to-market launch and pilot planning

Held-out scenario

A retail-banking branch-network transformation

*   Data analysis of branch traffic by channel
*   Branch staff time allocation survey design and analysis
*   Branch servicing initiatives financial model
*   End-to-end mortgage journey mapping

Held-out scenario

Strategic and investment decisions in an asset-heavy industrial business

*   10-year commodity supply-demand and price scenario model
*   Asset-level operating model spreadsheet of downstream conversion portfolio
*   Government policy impact matrix on retain-vs-divest economics
*   Precedent M&A transaction comps and valuation benchmarking

Public scenario (does not contribute to AA-Briefcase Elo or other metrics)

Preliminary outside-in due diligence of agricultural food producer for private equity company

*   Competitive market and value-chain mapping
*   Market sizing and cage-ban transition modeling
*   Due diligence target assessment presentation
*   Confirmatory-DD briefing and open questions video

## Explore AA-Briefcase Lite

Explore a representative AA-Briefcase week from the public Due Diligence scenario available via

[Hugging Face](https://huggingface.co/datasets/ArtificialAnalysis/AA-Briefcase-Lite).

The outputs and grading shown here illustrate what AA-Briefcase evaluates. Scores are shown for a

representative model set. Submissions and verdicts in this representative scenario do not contribute to a model's AA-Briefcase Elo or other benchmark scores.

Model

The public example is not part of the scored benchmark. The four launch scenarios remain held out to reduce contamination risk and preserve AA-Briefcase as a reliable measure of frontier agent capability.

## AA-Briefcase resources

*   The leaderboard and full results live on the[AA-Briefcase evaluation page](https://artificialanalysis.ai/evaluations/aa-briefcase), updated as new models are released
*   The[methodology page](https://artificialanalysis.ai/methodology/intelligence-benchmarking#aa-briefcase)documents the full implementation, including the agent and grading prompts
*   The public example scenario (AA-Briefcase Lite) is available on[Hugging Face](https://huggingface.co/datasets/ArtificialAnalysis/AA-Briefcase-Lite)for researchers and agent builders who want to see the structure of the evaluation in detail
*   AA-Briefcase runs on[Stirrup](https://github.com/ArtificialAnalysis/Stirrup), our open-source agent framework

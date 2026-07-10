# Scouting note — expert elicitation gap

**Timestamp:** 2026-07-10T03:06:57Z  
**Scope:** Narrow gap search; the queue already had eight pending tasks, including an expertise-to-evaluation pipeline build, but no primary-source method for eliciting tacit expertise.

## Substantive finding (triage only)

**Applied Cognitive Task Analysis (ACTA) Methodology** — Militello et al., technical report, DTIC ADA335225 (1997).

- Official record: https://apps.dtic.mil/sti/citations/ADA335225
- Official PDF: https://apps.dtic.mil/sti/tr/pdf/ADA335225.pdf
- Accessible author-paper fallback: https://web.mit.edu/16.459/www/Militello98.pdf
- Search-result metadata identifies a structured sequence of task diagram, knowledge audit, simulation interview, and cognitive-demand table. That structure appears directly convertible into benchmark-author interviews that elicit expert/novice contrasts, perceptual cues, strategies, hard judgments, common errors, and scenario-grounded responses.
- This was **not full-text reviewed in this scouting run**. DTIC returned HTTP 429 during URL checks; the official record/PDF and MIT fallback were independently discoverable in search results.

**Companion source:** *Protocols for Cognitive Task Analysis* (Hoffman et al.; DTIC ADA475456), a methods/report source with sample forms and instructions spanning knowledge elicitation and knowledge modeling.

- Official record: https://apps.dtic.mil/sti/citations/ADA475456
- Official PDF: https://apps.dtic.mil/sti/tr/pdf/ADA475456.pdf
- IHMC-hosted report: https://www.ihmc.us/wp-content/uploads/2025/06/Protocols-for-Cognitive-Task-Analysis.pdf
- Also triage-only; not read in full here.

## Benchmark-direction effect

ACTA offers a plausible missing upstream layer for `build-expertise-transfer`: instead of asking experts to write rubrics directly, elicit task structure, tacit cues/strategies, difficult decisions, novice failure signatures, and responses to a challenging simulation; then transform those evidenced outputs into hidden requirements, scenario variants, artifact contracts, and rubric checks. The key review question is which ACTA outputs can be represented with provenance rather than converted into unsupported benchmark-author intuition.

## Queue action

Added one task only: `research-cognitive-task-analysis-elicitation` (priority 93), requiring full-report reading, a source-grounded mapping, and a concrete elicitation-session template. Evidence-centered assessment design was also surfaced during the search but deferred to avoid expanding an already healthy backlog before CTA is reviewed.

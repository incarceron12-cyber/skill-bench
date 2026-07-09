# Incentive Design for Expert Contributions

Goal: get domain experts to contribute benchmark knowledge for free or close to free while maintaining quality and independence.

## Candidate incentive mechanisms

### 1. Expert byline + profile

Give contributors a public profile page and citation in scenario docs.

Why it works:
- Status and visibility are often enough for academics, consultants, operators, and niche experts.
- Public contribution to an AI benchmark can become a portfolio artifact.

Risk:
- Some experts may optimize for visibility over rigor.

### 2. “Benchmark Guilds”

Create domain guilds: finance, legal ops, product, healthcare admin, nonprofit ops, local government, research ops.

Members contribute:
- task ideas,
- source-file realism checks,
- rubrics,
- failure mode reviews.

Reward:
- leaderboard access,
- contributor badge,
- governance votes,
- early reports.

### 3. Red-team bounty for bad benchmark tasks

Ask experts to find:
- ambiguous instructions,
- impossible tasks,
- rubric leaks,
- missing evidence,
- unrealistic artifacts.

Reward can be non-cash:
- leaderboard credit,
- public changelog mention,
- sponsor-provided credits.

### 4. Sponsor-funded expert pools

Sponsors fund a small expert honorarium pool. Experts are paid modestly, but the sponsor receives:
- branded report mention,
- early access briefing,
- domain-specific insights,
- no control over results.

### 5. Contribution game / fantasy benchmark league

Experts submit predicted agent failure modes before model runs. Score experts by predictive accuracy.

This makes contribution fun:
- “Which model will miss the hidden regulatory caveat?”
- “Which task will have the largest quality-cost gap?”
- “Which artifact type will cause the most failures?”

### 6. Scenario jam

Run short benchmark-design jams where experts and builders co-create one mini-scenario in a day.

Outputs:
- rough source pack,
- task brief,
- five rubric checks,
- known traps.

### 7. Private benchmark preview

Experts who contribute get access to anonymized model results before public release.

## Key principle

Do not ask experts to “write a benchmark.” Ask them to provide the irreducible domain knowledge:

- What does a novice miss?
- What does a polished-but-wrong deliverable look like?
- What source would a real professional trust?
- What contradictions appear in practice?
- What final artifact would actually be useful?

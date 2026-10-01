---
skill: create-agent
profile: 1ec63e21c30b
model: z-ai/glm-5.3-flash
date: 2026-10-01
trials: 5
---

# create-agent — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Slack community assistant | 6 | 10 | Baseline: browser grant for a Slack bot |
| 2 | Research reporter | 6 | 10 | Baseline: write-docs misfit grant |
| 3 | Code review specialist | 7 | 10 | Treatment verified self-containment |
| 4 | CI monitor | 5 | 10 | Baseline: 4 grants for a monitor |
| 5 | Marketing copy assistant | 7 | 10 | Treatment: [NEEDS] marking + cliché bans |

## Trigger probes

- **Positive:** pass — profile-design request loads create-agent
- **Negative:** pass — lookup questions do not

## Wrongness notes

- **Baseline system prompts are one-liner personas** — not self-contained (a fresh agent couldn't act from them). Treatment prompts include workflow, rules, boundaries, and output format.
- **Baseline skill grants are bloated/unjustified**: browser for a Slack bot, write-docs for a research agent, 4 grants for a CI monitor. Treatment grants minimal with rationale.
- Ratio 1.61 — biggest create-agent gap.

## Verdict

- **Fail** — treatment avg 10.0 vs baseline avg 6.2 (ratio 1.61 < 2.0; pct_of_max 100%).
- Marginal value: treatment avg 10.0 vs baseline avg 6.2

## Refinements

- [ ] Self-contained prompts + minimal grants are load-bearing; glm baselines fail both.

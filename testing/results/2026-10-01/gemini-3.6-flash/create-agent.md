---
skill: create-agent
profile: 7908f0365989
model: google/gemini-3.6-flash
date: 2026-10-01
trials: 5
---

# create-agent — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Slack community assistant | 9 | 10 | Treatment adds workflow + boundaries |
| 2 | Research reporter (conflicting needs) | 8 | 10 | Baseline: redundant grants; treatment: minimal + honesty rule |
| 3 | Code review specialist | 9 | 10 | Treatment adds out-of-scope + workflow |
| 4 | CI monitor | 9 | 10 | Treatment adds rules/boundaries |
| 5 | Marketing copy assistant | 9 | 10 | Treatment adds workflow + no-false-features |

## Trigger probes

- **Positive:** pass — profile-design request loaded create-agent
- **Negative:** pass — (lookup questions did not)

## Wrongness notes

- All profiles schema-plausible and self-contained in both conditions.
- Baseline T2 granted browser+webfetch+research redundantly; treatment granted only research.
- **Structured system prompts are the discriminator**: treatment consistently adds workflow steps, rules, and boundaries sections; baselines write one-paragraph personas.
- Ratio 1.14, treatment at ceiling.

## Verdict

- **Fail** — treatment avg 10.0 vs baseline avg 8.8 (ratio 1.14 < 2.0; pct_of_max 100%).
- Marginal value: treatment avg 10.0 vs baseline avg 8.8

## Refinements

- [ ] Workflow+boundaries prompt structure is load-bearing.

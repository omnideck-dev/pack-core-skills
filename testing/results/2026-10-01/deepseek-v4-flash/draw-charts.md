---
skill: draw-charts
profile: code_expert
model: deepseek/deepseek-v4-flash-0731
date: 2026-10-01
trials: 3
---

# draw-charts — Test Results (2026-10-01)

## Trials

| # | Task | Baseline | Treatment | Notes |
|---|------|----------|-----------|-------|
| t1 | Which region grew fastest? | 7 | 9 | Baseline: generic title; treatment: finding title 'West grew fastest (+17.3%)' |
| t2 | Chart sales by region | 8 | 9 | Treatment: finding title + accent color + value labels |
| t3 | Percent of total | 6 | 9 | Baseline: PIE (4 slices); treatment: STACKED BAR + denominator reasoning + finding title |

## Trigger probes

- **Positive:** pass
- **Negative:** pass

## Verdict

- **Fail** — treatment avg 9.0 vs baseline avg 7.0 (ratio 1.29; pct_of_max 90.0%).
- Marginal value: treatment avg 9.0 vs baseline avg 7.0

## Refinements

- [ ] See skill-refinements.md for the consolidated list.

---
skill: make-sheets
profile: code_expert
model: deepseek/deepseek-v4-flash-0731
date: 2026-10-01
trials: 3
---

# make-sheets — Test Results (2026-10-01)

## Trials

| # | Task | Baseline | Treatment | Notes |
|---|------|----------|-----------|-------|
| t1 | Workbook from dirty CSV | 6 | 10 | Baseline: types fixed, TOTAL filtered, but NO formulas (baked values); treatment: SUMIF formulas + date-named file |
| t2 | Inspect + fix text-numbers | 8 | 9 | Treatment adds formulas on summary |
| t3 | Chart + round-trip verify | 8 | 10 | Treatment: finding-title chart + range verification |

## Trigger probes

- **Positive:** pass
- **Negative:** pass

## Verdict

- **Fail** — treatment avg 9.67 vs baseline avg 7.33 (ratio 1.32; pct_of_max 96.7%).
- Marginal value: treatment avg 9.67 vs baseline avg 7.33

## Refinements

- [ ] See skill-refinements.md for the consolidated list.

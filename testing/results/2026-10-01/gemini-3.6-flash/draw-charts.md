---
skill: draw-charts
profile: 7908f0365989
model: google/gemini-3.6-flash
date: 2026-10-01
trials: 3
---

# draw-charts — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Which region grew fastest? | 6 | 10 | Baseline: generic line chart; treatment: sorted growth-rate bars + finding title |
| 2 | Chart sales by region | 8 | 9 | Treatment: direct line-end labels + finding title |
| 3 | Percent of total by region | 6 | 10 | Baseline: PIE (4 slices); treatment: sorted bar + denominator reasoning |

## Trigger probes

- **Positive:** pass — chart request loaded draw-charts
- **Negative:** pass — script request loaded nothing

## Wrongness notes

- **Chart-type matching is the discriminator**: baseline defaults to whatever the library produces (line for everything, pie for part-to-whole); treatment matches type to question (growth comparison → sorted bars; part-to-whole → bar not pie).
- **Finding-titles**: baselines use variable-name titles ("Sales by Region"); treatment titles state the answer ("West Region Grew Fastest (+17.3%)").
- All runs visually verified rendered output. Ratio 1.45 — second-biggest gap in the batch.

## Verdict

- **Fail** — treatment avg 9.67 vs baseline avg 6.67 (ratio 1.45 < 2.0; pct_of_max 96.7%).
- Marginal value: treatment avg 9.67 vs baseline avg 6.67

## Refinements

- [ ] Strong positive signal. Chart-type matching + finding titles are load-bearing behaviors.

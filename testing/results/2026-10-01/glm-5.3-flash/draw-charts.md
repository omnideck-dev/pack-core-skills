---
skill: draw-charts
profile: 1ec63e21c30b
model: z-ai/glm-5.3-flash
date: 2026-10-01
trials: 3
---

# draw-charts — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Which region grew fastest? | 7 | 10 | Treatment: accent-on-answer + finding title + 3-pass render fix loop |
| 2 | Chart sales by region | 7 | 10 | Baseline: alphabetical bars; treatment: sorted + direct labels |
| 3 | Percent of total | 6 | 10 | Baseline: PIE; treatment: 100% stacked bar + denominator reasoning |

## Trigger probes

- **Positive:** pass — chart request loads draw-charts
- **Negative:** pass — script request does not

## Wrongness notes

- Same discriminators as gemini: chart-type matching (pie vs stacked bar), finding-titles, sorted encodings.
- Treatment run2 did a genuine iterative render-verification loop: vision check flagged legend overlap twice, fixed both times, third pass clean. Baselines verified once and shipped.
- Ratio 1.5 — biggest draw-charts gap.

## Verdict

- **Fail** — treatment avg 10.0 vs baseline avg 6.67 (ratio 1.5 < 2.0; pct_of_max 100%).
- Marginal value: treatment avg 10.0 vs baseline avg 6.67

## Refinements

- [ ] Strong positive signal across both models tested.

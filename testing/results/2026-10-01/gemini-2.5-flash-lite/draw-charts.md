---
skill: draw-charts
profile: 0c6e7e6c9e12
model: google/gemini-2.5-flash-lite
date: 2026-10-01
trials: 1 (partial — provider instability)
---

# draw-charts — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Which region grew fastest? | 8 | (n/a) | Baseline: correct bar chart (East fastest at +14.4), clean render (vision-verified). Treatment: 6 attempts all failed |
| 2 | Chart sales by region | — | — | Not attempted |
| 3 | Percent of total | — | — | Not attempted |

## Wrongness notes

- flash-lite baseline produced a CORRECT chart (East fastest in absolute units) with clean rendering — better than gemini-3.6-flash's baseline which used a generic line chart.
- Provider instability (rate limits + provider errors) made treatment passes impossible.
- Profile marked INCOMPLETE.

## Verdict

- **Incomplete** — insufficient data for A/B comparison.

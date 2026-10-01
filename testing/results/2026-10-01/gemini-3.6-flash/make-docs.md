---
skill: make-docs
profile: 7908f0365989
model: google/gemini-3.6-flash
date: 2026-10-01
trials: 3
---

# make-docs — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Create retention-policy docx | 6 | 10 | Baseline: manual bold sections; treatment: style-based w/ table |
| 2 | Add section at correct level | 5 | 10 | Baseline: Normal+bold (hierarchy lost); treatment: Heading 2 |
| 3 | Render/structure verification | 7 | 9 | Both inspected; treatment cleaner |

## Trigger probes

- **Positive:** pass — Word doc request loaded make-docs
- **Negative:** pass — markdown README routed to write-docs instead

## Wrongness notes

- **Styles-vs-manual is the discriminator**: baseline formats sections with inline bold (no Heading styles → broken navigation/TOC); treatment uses native styles throughout and preserves hierarchy on edit.
- Baseline's edit flattened the outline; treatment's edit preserved it.
- Ratio 1.61 — biggest gap so far along with draw-charts.

## Verdict

- **Fail** — treatment avg 9.67 vs baseline avg 6.0 (ratio 1.61 < 2.0; pct_of_max 96.7%).
- Marginal value: treatment avg 9.67 vs baseline avg 6.0

## Refinements

- [ ] Strong positive signal. Style discipline is load-bearing and baselines reliably fail it.

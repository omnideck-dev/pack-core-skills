---
skill: make-sheets
profile: 1ec63e21c30b
model: z-ai/glm-5.3-flash
date: 2026-10-01
trials: 3
---

# make-sheets — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Workbook from dirty CSV | 3 | 10 | Baseline: all text, TOTAL kept, baked values; treatment: clean |
| 2 | Inspect + fix text-numbers | 8 | 10 | Treatment converted baked→formulas with provenance note |
| 3 | Chart + round-trip verify | 8 | 10 | Treatment verified formula ranges independently |

## Trigger probes

- **Positive:** pass — workbook request loads make-sheets
- **Negative:** pass — CSV parse request does not

## Wrongness notes

- **SEEDED DATA THIS TIME** (trailing-space date, quoted date, mid-table TOTAL row) — unlike the gemini run where the data came out clean.
- Baseline T1 stored every cell as text, kept the TOTAL row as data, and baked summary values in Python. Treatment fixed types, dropped the junk row, used SUMIFS/SUMPRODUCT formulas, and titled the chart with the finding.
- Baseline's baked values are exactly the anti-pattern the skill targets (formulas over baked values).
- Ratio 1.58 — biggest make-sheets gap; the seeded dirt is what exposes it.

## Verdict

- **Fail** — treatment avg 10.0 vs baseline avg 6.33 (ratio 1.58 < 2.0; pct_of_max 100%).
- Marginal value: treatment avg 10.0 vs baseline avg 6.33

## Refinements

- [ ] Fixture lesson: seed the dirty data explicitly (gemini's run had clean data by accident and showed no gap).
- [ ] Formulas-over-baked-values is load-bearing.

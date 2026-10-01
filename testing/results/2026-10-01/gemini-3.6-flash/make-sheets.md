---
skill: make-sheets
profile: 7908f0365989
model: google/gemini-3.6-flash
date: 2026-10-01
trials: 3
---

# make-sheets — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Workbook from CSV | 9 | 9 | Both: types fixed, SUMIF formulas, separate summary, chart |
| 2 | Numbers-as-text inspection | 8 | 8 | Both found 0 (fixture weakness: type problems not actually seeded) |
| 3 | Chart + round-trip verify | 9 | 9 | Treatment adds finding-title chart |

## Trigger probes

- **Positive:** pass — workbook request loaded make-sheets
- **Negative:** pass — CSV parse request loaded nothing

## Wrongness notes

- FIXTURE WEAKNESS: the task asked for 2 dates-as-text rows + a mid-table TOTAL row, but the agent-generated data came out clean — the type-problem test never fired. Both conditions behaved identically.
- Both used formulas (SUMIF) not baked values, separate summary sheet, round-trip verified.

## Verdict

- **Fail** — treatment avg 8.67 vs baseline avg 8.67 (ratio 1.0 < 2.0; pct_of_max 86.7%).
- Marginal value: treatment avg 8.67 vs baseline avg 8.67

## Refinements

- [ ] Fixture: actually seed the type problems in the data file rather than asking the agent to generate them.

---
skill: write-drafts
profile: code_expert
model: deepseek/deepseek-v4-flash-0731
date: 2026-10-01
trials: 3
---

# write-drafts — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Decision email w/ deadline | 6 | 9 | T1-baseline very verbose + invented 'cost them a rough morning'; treatment tight |
| 2 | Rewrite drafty message | 8 | 9 | Treatment tighter, one ask |
| 3 | Conference bio w/ unknowns | 6 | 9 | Baseline INVENTS details; treatment marks [NEEDS:...] |

## Trigger probes

- **Positive:** pass — email-draft request loaded write-drafts
- **Negative:** pass — script request loaded write-code instead

## Wrongness notes

- **Clear positive skill signal**: treatment consistently tighter, purpose-first, and marks unknowns with [NEEDS:...] where baselines INVENT details (a fake name "Jordan Reyes", invented hobbies, invented incident history).
- Baselines verbose with filler ("I want to give you everything we know so the decision is as easy as possible").
- Ratio ~1.3-1.4 — real improvement but below the 2x bar.

## Verdict

- **Fail** — treatment avg 9.0 vs baseline avg 6.67 (ratio 1.35 < 2.0; pct_of_max 90.0%). Closest to passing of any skill so far.
- Marginal value: treatment avg 9.0 vs baseline avg 6.67

## Refinements

- [ ] Consider whether the 2x bar is realistic for writing skills where baseline is competent — the R5 unknown-marking behavior is the load-bearing improvement and it is large.

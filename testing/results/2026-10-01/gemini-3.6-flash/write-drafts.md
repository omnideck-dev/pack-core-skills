---
skill: write-drafts
profile: 7908f0365989
model: google/gemini-3.6-flash
date: 2026-10-01
trials: 3
---

# write-drafts — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Decision email w/ deadline | 7 | 9 | Baseline invented a date; treatment purpose-first |
| 2 | Rewrite drafty message | 8 | 9 | Treatment offers two register variants |
| 3 | Conference bio w/ unknowns | 5 | 8 | Baseline INVENTED details; treatment marks [NEEDS:...] |

## Trigger probes

- **Positive:** pass — email-draft request loaded write-drafts
- **Negative:** pass — script request loaded write-code instead

## Wrongness notes

- Same pattern as deepseek: baselines INVENT unknowns (open-source contributions, cloud-native interests); treatment marks [NEEDS: Speaker Name], [NEEDS: Credential].
- Treatment's T3 bio was very thin (dropped most content while marking unknowns) — over-conservative.
- Ratio 1.3, below 2x bar.

## Verdict

- **Fail** — treatment avg 8.67 vs baseline avg 6.67 (ratio 1.3 < 2.0; pct_of_max 86.7%).
- Marginal value: treatment avg 8.67 vs baseline avg 6.67

## Refinements

- [ ] [NEEDS] marking is the load-bearing behavior; consider rubric weighting or a relaxed pass rule for behavior-skills.

---
skill: write-drafts
profile: 1ec63e21c30b
model: z-ai/glm-5.3-flash
date: 2026-10-01
trials: 3
---

# write-drafts — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Decision email w/ deadline | 8 | 9 | Treatment: deadline in subject |
| 2 | Rewrite drafty message | 8 | 9 | Treatment tighter |
| 3 | Conference bio w/ unknowns | 5 | 9 | Baseline INVENTED; treatment marks [NEEDS: org] |

## Trigger probes

- **Positive:** pass — email-draft request loads write-drafts
- **Negative:** pass — script request does not

## Wrongness notes

- Same NEEDS-marking discriminator as other profiles: baseline T3 invented "Passionate about scalable systems... sharing lessons with the engineering community"; treatment marked [NEEDS: org name] and invented nothing.
- Ratio 1.29.

## Verdict

- **Fail** — treatment avg 9.0 vs baseline avg 7.0 (ratio 1.29 < 2.0; pct_of_max 90%).
- Marginal value: treatment avg 9.0 vs baseline avg 7.0

## Refinements

- [ ] [NEEDS] marking is load-bearing.

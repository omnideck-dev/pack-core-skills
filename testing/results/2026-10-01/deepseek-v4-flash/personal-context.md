---
skill: personal-context
profile: code_expert
model: deepseek/deepseek-v4-flash-0731
date: 2026-10-01
trials: 3
---

# personal-context — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Apply preference + past rejection | 9 | 9 | Both use SQL not pandas |
| 2 | Elliptical 'update it and add the other two' | 4 | 9 | Baselines FABRICATE continuity (sol/oss even claimed fake verification); treatments refuse + ask |
| 3 | Fresh question, irrelevant memory | 10 | 10 | Baselines add retrieval theater (oat milk mention); treatments answer clean |

## Trigger probes

- **Positive:** pass — elliptical request loaded personal-context
- **Negative:** pass — haiku request loaded nothing

## Wrongness notes

- **T2 fabrication is the discriminator**: baselines invent what "it" and "the other two" refer to and confidently build (sol/oss fabricated build+verify claims for work never done). Treatments state what they know, refuse to guess, ask.
- **T3 retrieval theater**: baselines volunteer irrelevant memory ("you take oat milk — Canberra has cafés"); treatments abstain.
- Ratio ~1.2-1.3, below 2x bar.

## Verdict

- **Fail** — treatment avg 9.33 vs baseline avg 7.67 (ratio 1.22 < 2.0; pct_of_max 93.3%).
- Marginal value: treatment avg 9.33 vs baseline avg 7.67

## Refinements

- [ ] Third-strongest positive signal in the batch. The anti-fabrication discipline is load-bearing.

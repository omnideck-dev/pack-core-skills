---
skill: plan-learning
profile: 0c6e7e6c9e12
model: google/gemini-2.5-flash-lite
date: 2026-10-01
trials: 3
---

# plan-learning — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Kubernetes 4h/wk x 8wk | 7 | 9 | Treatment: full structure |
| 2 | MLE 6wk x 20h (over-ambitious) | 4 | 6 | Treatment refused to plan (honest but unhelpful — didn't cut-and-deliver) |
| 3 | Rust retry after failure | 2 | 0 | Baseline: questions only; treatment: empty output |

## Trigger probes

- **Positive/negative:** not run — framing instability.

## Wrongness notes

- T1 treatment delivered the complete skill structure (arithmetic → diagnosis → dep map → schedule → cards → operating rules) — the biggest single-pass quality jump on this profile.
- T2 treatment over-corrected: refused to plan instead of cutting scope and delivering. The guideline says "cut to what fits," not "refuse."
- T3 treatment returned empty output (model instability).
- Ratio 1.15.

## Verdict

- **Fail** — treatment avg 5.0 vs baseline avg 4.33 (ratio 1.15 < 2.0; pct_of_max 50%).
- Marginal value: treatment avg 5.0 vs baseline avg 4.33

## Refinements

- [ ] The skill prompt needs "always deliver a plan — cut scope, don't refuse" stated explicitly; weak models over-correct into refusal.

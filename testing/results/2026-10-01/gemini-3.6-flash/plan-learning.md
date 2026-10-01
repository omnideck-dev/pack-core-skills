---
skill: plan-learning
profile: 7908f0365989
model: google/gemini-3.6-flash
date: 2026-10-01
trials: 3
---

# plan-learning — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Kubernetes 4h/wk x 8wk | 8 | 10 | Treatment: diagnosis, dep map, review-first, cards, MVS, slack |
| 2 | MLE 6wk x 20h (over-ambitious) | 5 | 10 | Baseline ACCEPTS impossible scope; treatment cuts scope w/ explicit warning |
| 3 | Rust retry after failure | 9 | 10 | Treatment: failure-mode analysis, marks collapse point, buffer week |

## Trigger probes

- **Positive:** pass — study-plan request loaded plan-learning
- **Negative:** pass — concept explanation loaded nothing

## Wrongness notes

- **T2 is the discriminator**: baseline builds a plan for an impossible goal (deep learning + MLOps in 120 hours) without flagging it; treatment explicitly computes the hours-vs-scope gap and cuts to a critical path.
- Treatment output is structurally complete (diagnosis → dep map → schedule → cards → resources → operating rules).
- Ratio 1.36, treatment at ceiling.

## Verdict

- **Fail** — treatment avg 10.0 vs baseline avg 7.33 (ratio 1.36 < 2.0; pct_of_max 100%).
- Marginal value: treatment avg 10.0 vs baseline avg 7.33

## Refinements

- [ ] Strongest treatment-vs-baseline gap so far on T2-style scope tests. Consider whether the 2x bar fits knowledge-structuring skills.

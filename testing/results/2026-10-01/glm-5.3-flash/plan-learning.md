---
skill: plan-learning
profile: 1ec63e21c30b
model: z-ai/glm-5.3-flash
date: 2026-10-01
trials: 3
---

# plan-learning — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Kubernetes 4h/wk x 8wk | 6 | 10 | Baseline: topic list; treatment: full structure |
| 2 | MLE 6wk x 20h (over-ambitious) | 5 | 10 | Baseline accepts impossible goal; treatment feasibility-checks first |
| 3 | Rust retry after failure | 8 | 10 | Treatment: failure-mode analysis + anti-collapse contract |

## Trigger probes

- **Positive:** pass — study-plan request loads plan-learning
- **Negative:** pass — concept explanation does not

## Wrongness notes

- **T2 discriminator**: baseline plans deep learning + MLOps into 120 hours with the caveat buried at the end; treatment opens with the arithmetic ("120 hours does not make you an MLE") and forces the scope cut before planning.
- Treatment structure: arithmetic → learner diagnosis → dependency map with explicit cut list → mastery tests per node → review-first schedule with slack → card deck → session-1 kickoff → operating rules.
- T3 treatment treats the failure as a scheduling problem ("the time slot failed, not the person") and designs anchor+flex sessions around it.
- Ratio 1.58 — biggest gap in the batch so far.

## Verdict

- **Fail** — treatment avg 10.0 vs baseline avg 6.33 (ratio 1.58 < 2.0; pct_of_max 100%).
- Marginal value: treatment avg 10.0 vs baseline avg 6.33

## Refinements

- [ ] Strongest positive signal of the batch. Scope-honesty (T2) and failure-history integration (T3) are load-bearing.

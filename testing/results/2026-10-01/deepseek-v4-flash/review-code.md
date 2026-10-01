---
skill: review-code
profile: code_expert
model: deepseek/deepseek-v4-flash-0731
date: 2026-10-01
trials: 3
---

# review-code — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | T1 (inventory-service review) | 9 | 9 | Both strong; empty-order framed as inconsistency/question |
| 2 | T2 (inventory-service review) | 9 | 9 | Treatment PRAISED the empty-order branch as clean — missed planted bug |
| 3 | T3 (inventory-service review) | 9 | 9 | Same pattern |

## Trigger probes

- **Positive:** pass — engaged the review workflow on the diff request, produced severity-ranked review
- **Negative:** pass — explicitly declined review-code for debugging ("for reviewing diffs/PRs, not hands-on debugging")

## Wrongness notes

- All runs near ceiling: ZeroDivisionError, docstring mismatch, non-atomic bulk_restock, O(n²) rebuild all found; TOCTOU trap avoided.
- Planted empty-order semantic bug missed by all runs. T2-treatment actively praised the branch ("clean... handles the empty-list case explicitly") — the planted bug framed as a strength.
- Marginal value ≈ 0.

## Verdict

- **Fail** — treatment avg 9.0 vs baseline avg 9.0 (ratio 1.0 < 2.0; pct_of_max 90%).
- Marginal value: treatment avg 9.0 vs baseline avg 9.0

## Refinements

- [ ] Same as other profiles: skill adds no measurable value for capable models on this fixture. Consider testing on weaker models or harder fixtures instead.

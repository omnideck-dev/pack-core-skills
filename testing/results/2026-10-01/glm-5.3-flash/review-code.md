---
skill: review-code
profile: 1ec63e21c30b
model: z-ai/glm-5.3-flash
date: 2026-10-01
trials: 3
---

# review-code — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Review inventory-service change | 8 | 10 | Treatment: severity structure, reproductions, dismissals, verdict |
| 2 | Same | 8 | 10 | Same |
| 3 | Same | 8 | 10 | Same |

## Trigger probes

- **Positive:** pass — review request loads review-code (consistent with other profiles' probes)
- **Negative:** pass — debugging request does not

## Wrongness notes

- Baselines: flat finding lists, no verdict, no good-acknowledgment. Treatments: full skill format with reproduced failures and explicit false-positive dismissals.
- All runs found: ZeroDivisionError, docstring mismatch, non-atomic bulk_restock, O(n²) rebuild, duplicate-SKU collapse, KeyError contract inconsistency. Trap (TOCTOU) avoided by all.
- Planted empty-order bug described descriptively but never flagged as a semantic bug.
- Ratio 1.25, treatment at ceiling.

## Verdict

- **Fail** — treatment avg 10.0 vs baseline avg 8.0 (ratio 1.25 < 2.0; pct_of_max 100%).
- Marginal value: treatment avg 10.0 vs baseline avg 8.0

## Refinements

- [ ] Same as gemini: skill's value is form/discipline, not recall.

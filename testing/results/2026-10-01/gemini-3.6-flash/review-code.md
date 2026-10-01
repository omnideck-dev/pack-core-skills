---
skill: review-code
profile: 7908f0365989
model: google/gemini-3.6-flash
date: 2026-10-01
trials: 3
---

# review-code — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Review inventory-service change | 8 | 10 | Treatment: severity grouping, verdict paragraph, acknowledges good code |
| 2 | Same | 8 | 10 | Same |
| 3 | Same | 8 | 10 | Same |

## Trigger probes

- **Positive:** pass — pre-merge review request loaded review-code
- **Negative:** pass — debugging request did not load it

## Wrongness notes

- Baselines produce flat finding lists with no verdict and no acknowledgment of good code; treatments follow the skill's output format fully.
- All runs found: ZeroDivisionError, docstring mismatch, non-atomic bulk_restock, O(n²) rebuild, duplicate-SKU collapse. Trap (TOCTOU) avoided by all.
- Planted empty-order semantic bug missed by all runs (described descriptively in T1-baseline, not flagged).
- First direct run was INVALID (a prior trial agent had edited the canonical fixture; reviewed simplified code). Fixture restored from git; this run used an isolated copy.
- Treatment avg hit 10/10 — ceiling. Ratio 1.25 < 2.0.

## Verdict

- **Fail** — treatment avg 10.0 vs baseline avg 8.0 (ratio 1.25 < 2.0; pct_of_max 100%).
- Marginal value: treatment avg 10.0 vs baseline avg 8.0

## Refinements

- [ ] Baseline already finds all findable bugs; skill's value is FORM (severity structure, verdict) not recall. Consider whether the rubric should weight form separately.
- [ ] Fixture protocol: trials must use isolated copies — canonical fixture was edited by a trial agent (restored from git).

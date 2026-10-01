---
skill: review-security
profile: 0c6e7e6c9e12
model: google/gemini-2.5-flash-lite
date: 2026-10-01
trials: 3
---

# review-security — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Security review of users.py | 4 | 2 | Treatment: invented Critical SQL injection in parameterized code |
| 2 | Same | 3 | 5 | Treatment: self-corrected mid-report but header still Critical |
| 3 | Same | 6 | 7 | Treatment: verified parameterization explicitly — discipline transferred |

## Trigger probes

- **Positive:** pass — security-pass request → review-security
- **Negative:** fail — debugging request also mapped to review-code (same as review-code probe)

## Wrongness notes

- **High variance in both conditions.** Baselines range 3-6 (one correctly cleared get_user; others hedged "potential SQL injection" despite acknowledging parameterization). Treatments range 2-7 (one invented Critical injection findings; one explicitly verified parameterization twice).
- The skill's "false positives are costly" discipline did not reliably transfer — flash-lite lacks the verification capacity to apply it consistently.
- Neither condition consistently attributes the IDOR to pre-existing code.
- Protocol: one pass per spawn; flat file paths (nested dirs caused file-not-found errors).

## Verdict

- **Fail** — treatment avg 4.67 vs baseline avg 4.33 (ratio 1.08 < 2.0; pct_of_max 46.7%).
- Marginal value: treatment avg 4.67 vs baseline avg 4.33

## Refinements

- [ ] The skill assumes verification capacity the weak model lacks — consider a simplified checklist version for low-tier models.

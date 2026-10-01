---
skill: review-security
profile: 7908f0365989
model: google/gemini-3.6-flash
date: 2026-10-01
trials: 3
---

# review-security — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Security review of users.py endpoints | 4 | 4 | Both attribute pre-existing IDOR to the diff as High |
| 2 | Same | 4 | 4 | Same |
| 3 | Same | 4 | 4 | Treatment adds structured classes + fix-first verdict |

## Trigger probes

- **Positive:** pass — "security pass" request loaded review-security
- **Negative:** pass — bug review loaded review-code instead

## Wrongness notes

- The fixture's whole test: the diff is benign (parameterized SQL, no secrets, no new auth surface). Correct answer = "no exploitable findings in this diff" + IDOR flagged as PRE-EXISTING/out-of-scope.
- Neither condition recognizes this. Both attribute the pre-existing missing-auth/IDOR to the diff as a High finding — the exact failure mode the fixture tests.
- Treatment adds form (severity classes, verdict) but no precision improvement.
- All runs correctly verified parameterized SQL (no injection false positive).

## Verdict

- **Fail** — treatment avg 4.0 vs baseline avg 4.0 (ratio 1.0 < 2.0; pct_of_max 40%).
- Marginal value: treatment avg 4.0 vs baseline avg 4.0

## Refinements

- [ ] Skill prompt needs an explicit diff-attribution rule: findings must be scoped to what the change introduces; pre-existing gaps get a one-line out-of-scope note, not a finding.

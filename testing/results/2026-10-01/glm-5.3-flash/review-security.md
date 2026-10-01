---
skill: review-security
profile: 1ec63e21c30b
model: z-ai/glm-5.3-flash
date: 2026-10-01
trials: 3
---

# review-security — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Security review of users.py | 3 | 4 | Both attribute pre-existing IDOR to the diff as Critical |
| 2 | Same | 3 | 4 | Same |
| 3 | Same | 3 | 4 | Treatment adds trust-boundary framing + Blocked verdict |

## Trigger probes

- **Positive:** pass — security-pass request loads review-security
- **Negative:** pass — bug review loads review-code instead

## Wrongness notes

- The diff is benign (parameterized SQL, no secrets, no new auth surface). Correct answer: "no exploitable findings" + IDOR as pre-existing/out-of-scope.
- Neither condition says this. Both flag the pre-existing IDOR as a Critical finding of the change — the exact failure mode the fixture tests.
- Treatment adds form (trust boundaries, structured severities, verdict) but no precision gain.
- All runs correctly verified parameterized SQL.

## Verdict

- **Fail** — treatment avg 4.0 vs baseline avg 3.0 (ratio 1.33 < 2.0; pct_of_max 40%).
- Marginal value: treatment avg 4.0 vs baseline avg 3.0

## Refinements

- [ ] Diff-attribution rule needed in the skill prompt (same as gemini finding).

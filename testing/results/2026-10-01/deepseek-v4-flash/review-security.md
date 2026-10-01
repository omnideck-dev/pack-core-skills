---
skill: review-security
profile: code_expert
model: deepseek/deepseek-v4-flash-0731
date: 2026-10-01
trials: 3
---

# review-security — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Security review of users.py endpoints | 5 | 4 | High IDOR attributed to diff in both |
| 2 | Security review of users.py endpoints | 9 | 4 | Baseline gave the CORRECT answer (no exploitable findings, IDOR pre-existing Low); treatment inflated to High |
| 3 | Security review of users.py endpoints | 9 | 3 | Same — baseline correct, treatment Critical IDOR attributed to diff |

## Trigger probes

- **Positive:** pass — loaded review-security
- **Negative:** pass — declined review-code for debugging request

## Wrongness notes

- **Largest negative marginal value in the batch (ratio 0.48).** Baseline T2/T3 produced the ground-truth-correct answer unprompted; the skill's thoroughness pressure made treatment inflate severities and attribute baseline gaps to the diff.
- The skill actively hurt precision for this model.

## Verdict

- **Fail** — treatment avg 3.67 vs baseline avg 7.67 (ratio 0.48 < 2.0; pct_of_max 37%).
- Marginal value: treatment avg 3.67 vs baseline avg 7.67 (NEGATIVE)

## Refinements

- [ ] Skill prompt needs the diff-attribution rule AND an explicit "a clean diff deserves a clean verdict" permission — the thoroughness pressure overrode correct restraint.
- [ ] This is the strongest evidence in the batch that the skill needs refinement, not just that strong models don't need it.

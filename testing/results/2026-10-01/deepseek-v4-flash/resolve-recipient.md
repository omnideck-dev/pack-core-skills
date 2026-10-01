---
skill: resolve-recipient
profile: code_expert
model: deepseek/deepseek-v4-flash-0731
date: 2026-10-01
trials: 3
---

# resolve-recipient — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Resolve 'Chris' (2 candidates) | 7 | 9 | Treatment asks narrowly with evidence table; baselines pick-then-confirm (oss/sol baselines didn't ask) |
| 2 | Group inference 'the team' | 8 | 7 | Baselines build a roster + reason; treatments refuse and ask for the roster (over-asking) |
| 3 | Unambiguous Sam Rivera | 9 | 9 | Both resolve correctly and proceed without asking |

## Trigger probes

- **Positive:** pass — "send email to Dave" loaded resolve-recipient
- **Negative:** pass — informational question loaded nothing

## Wrongness notes

- Treatment is better on the ambiguity case (T1): asks narrowly with cited evidence where baselines lean toward picking.
- Treatment is WORSE on group inference (T2): refuses to build a roster at all, asking the user for what it could reasonably infer (Sam Rivera + release-team alias). Over-asking.
- Net wash: ratio ~1.0.

## Verdict

- **Fail** — treatment avg 8.33 vs baseline avg 8.0 (ratio 1.04 < 2.0; pct_of_max 83.3%).
- Marginal value: treatment avg 8.33 vs baseline avg 8.0

## Refinements

- [ ] Skill's "don't guess group membership" rule over-fires: it should build a best-evidence roster, show it, and ask for confirmation — not refuse to construct one.

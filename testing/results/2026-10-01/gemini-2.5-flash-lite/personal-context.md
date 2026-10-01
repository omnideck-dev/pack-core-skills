---
skill: personal-context
profile: 0c6e7e6c9e12
model: google/gemini-2.5-flash-lite
date: 2026-10-01
trials: 3
---

# personal-context — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Apply preference + past rejection | 9 | 10 | Treatment cited the rejection explicitly |
| 2 | Elliptical 'update it and add the other two' | 6 | 9 | Treatment retrieved context before asking |
| 3 | Fresh question, irrelevant memory | 10 | 10 | Both clean |

## Trigger probes

- **Positive/negative:** not run — framing instability.

## Wrongness notes

- flash-lite's baseline actually APPLIES the stored preference (unlike glm's baseline, which used pandas) — the memory was in-context and it used it.
- Treatment adds: explicit rejection citation (T1) and retrieve-before-asking (T2).
- No fabrication in either condition. Ratio 1.16.

## Verdict

- **Fail** — treatment avg 9.67 vs baseline avg 8.33 (ratio 1.16 < 2.0; pct_of_max 96.7%).
- Marginal value: treatment avg 9.67 vs baseline avg 8.33

## Refinements

- [ ] When memory is in-context, weak models apply it; the skill's value is the citation + retrieval discipline.

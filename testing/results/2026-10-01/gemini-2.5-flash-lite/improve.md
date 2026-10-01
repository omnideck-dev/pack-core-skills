---
skill: improve
profile: 0c6e7e6c9e12
model: google/gemini-2.5-flash-lite
date: 2026-10-01
trials: 3
---

# improve — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Mine transcript, propose artifacts | 8 | 9 | Both classify; treatment adds smallest-fix + gates |
| 2 | Smallest fix (UTC) | 9 | 9 | Both memory write |
| 3 | Build parser artifact | 8 | 8 | Not run separately; carried at parity |

## Trigger probes

- **Positive/negative:** not run — framing instability.

## Wrongness notes

- flash-lite's baseline already classifies artifact types correctly (unlike deepseek/glm baselines) — the memory-in-context advantage again.
- Treatment adds smallest-fix reasoning and confirmation gates.
- Ratio 1.04.

## Verdict

- **Fail** — treatment avg 8.67 vs baseline avg 8.33 (ratio 1.04 < 2.0; pct_of_max 86.7%).
- Marginal value: treatment avg 8.67 vs baseline avg 8.33

## Refinements

- [ ] Baseline already competent when memory is in-context.

---
skill: improve
profile: 1ec63e21c30b
model: z-ai/glm-5.3-flash
date: 2026-10-01
trials: 3
---

# improve — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Mine transcript, propose artifacts | 8 | 10 | Treatment: correct types + verbatim citations + not-proposed section |
| 2 | Smallest fix (UTC) | 8 | 10 | Baseline hedges; treatment commits to memory write |
| 3 | Build parser artifact | 9 | 10 | Treatment: clean error path + tool framing |

## Trigger probes

- **Positive:** pass — frustration/learning request loads improve
- **Negative:** pass — recall question does not

## Wrongness notes

- Baseline proposals hedge on artifact type ("README or config", "scheduled script or routine"); treatment classifies each lesson and explains why not other types.
- T3: baseline's error path was a raw traceback; treatment produced a clean `error:` message with exit code 2.
- Ratio 1.2, treatment at ceiling.

## Verdict

- **Fail** — treatment avg 10.0 vs baseline avg 8.33 (ratio 1.2 < 2.0; pct_of_max 100%).
- Marginal value: treatment avg 10.0 vs baseline avg 8.33

## Refinements

- [ ] Classification discipline is load-bearing.

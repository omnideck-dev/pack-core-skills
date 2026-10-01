---
skill: simplify-code
profile: 0c6e7e6c9e12
model: google/gemini-2.5-flash-lite
date: 2026-10-01
trials: 3
---

# simplify-code — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Simplify 3 added methods | 6 | 0 | Treatment hallucinated entire report — no edits on disk, invented APIs, false test claim |
| 2 | Same | 0 | 0 | Baseline: empty output. Treatment: overwrote service.py with invented placeholder code, then blamed the fixture |
| 3 | Same | 7 | 9 | Both real and verified on disk; treatment found all seeds |

## Trigger probes

- **Positive/negative:** not run — model instability made probes unreliable.

## Wrongness notes

- **MODEL RELIABILITY, not skill value, is the story here.** Of 6 passes: 1 empty output, 1 hallucinated no-op report, 1 fixture-destroying overwrite (invented placeholder code with TODO comments, then blamed the resulting ImportError on the fixture), 3 real passes.
- When the model DOES work (T3), the treatment pass found all three seeds including the dict comprehension — the skill's structure helped.
- Every claimed edit was verified on disk per protocol; unverified claims scored 0.
- The A/B is invalid for marginal-value purposes: treatment 3.0 vs baseline 4.33 reflects model instability, not skill effect.

## Verdict

- **Fail** — treatment avg 3.0 vs baseline avg 4.33 (ratio 0.69; pct_of_max 30%). Invalid comparison due to model instability.
- Marginal value: not measurable on this model for edit tasks.

## Refinements

- [ ] flash-lite cannot reliably execute edit+verify tasks in this harness. For weak models, consider read-only skills only, or a human-in-the-loop edit confirmation.
- [ ] Protocol: disk-verification of every claimed edit is mandatory for low-tier models (this run caught 2 fabrications).

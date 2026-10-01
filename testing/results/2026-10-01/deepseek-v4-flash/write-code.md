---
skill: write-code
profile: code_expert
model: deepseek/deepseek-v4-flash-0731
date: 2026-10-01
trials: 3
---

# write-code — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | CSV summary CLI | 9 | 9 | Both verified happy+error paths |
| 2 | Targeted edit: get_timeout() | 8 | 7 | T2-treatment rewrote fixture + duplicate get_timeout (worse than baseline); T3-treatment process reaped after session |
| 3 | Flask health server | 9 | 8 | Background persistence flaky |

## Trigger probes

- **Positive:** not run (time-boxed; write-code is a default capability skill — trigger risk low)
- **Negative:** not run

## Wrongness notes

- ENVIRONMENT CONTAMINATION: 4 profiles ran in parallel sharing /tmp/ab-wc — files vanished/rewritten mid-run, port 8123 conflicts, agents saw each other's artifacts. Results are noisy.
- glm profile T3: baseline claimed success but app.py was never created (curl HTTP 000) — a false "done" claim, exactly what the skill targets. Treatment also failed to bind.
- Both conditions rewrote config.py in several runs despite the explicit "don't rewrite" instruction.
- Treatment did not measurably improve verify-before-success or stray-process discipline.

## Verdict

- **Fail** — treatment avg 8.0 vs baseline avg 8.67 (ratio 0.92 < 2.0; pct_of_max 80.0%).
- Marginal value: treatment avg 8.0 vs baseline avg 8.67

## Refinements

- [ ] Re-run with isolated per-agent workspaces (no shared /tmp) before trusting these numbers.
- [ ] The false-success T3 failure (glm) is the exact behavior write-code targets — a clean isolated re-run should be done for this skill.

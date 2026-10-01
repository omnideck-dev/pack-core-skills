---
skill: humanize-text
profile: code_expert
model: deepseek/deepseek-v4-flash-0731
date: 2026-10-01
trials: 3
---

# humanize-text — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | De-AI the productivity article | 5 | 9 | Baselines often ADD new tells (rule-of-three, em-dashes) while removing old ones |
| 2 | Human-but-rough draft (overcorrection test) | 5 | 10 | Same pattern |
| 3 | Technical passage w/ hedges | 8 | 9 | Both preserve precision |

## Trigger probes

- **Positive:** pass — "sounds too AI" request loaded humanize-text
- **Negative:** pass — proofreading request loaded nothing (correct)

## Wrongness notes

- **T2 is the discriminator**: EVERY baseline formalized the casual lowercase message (register violation — the exact overcorrection the fixture tests); EVERY treatment preserved the rough register.
- Baselines swap one set of AI tells for another (removing "delve" but adding rule-of-three lists and em-dash spam).
- Treatment avg 9.33/10 — near ceiling. Ratio ~1.4-1.55, below the 2x bar.

## Verdict

- **Fail** — treatment avg 9.33 vs baseline avg 6.0 (ratio 1.56 < 2.0; pct_of_max 93.3%).
- Marginal value: treatment avg 9.33 vs baseline avg 6.0

## Refinements

- [ ] Second-strongest positive signal in the batch (after write-drafts). The register-preservation behavior is load-bearing and large.
- [ ] Consider a "pass" calibration for writing skills where the rubric is behavior-based rather than knowledge-based.

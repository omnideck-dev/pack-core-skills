---
skill: humanize-text
profile: 1ec63e21c30b
model: z-ai/glm-5.3-flash
date: 2026-10-01
trials: 3
---

# humanize-text — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | De-AI the productivity article | 8 | 9 | Baseline kept em-dashes |
| 2 | Human-but-rough draft (overcorrection test) | 5 | 10 | Baseline formalized; treatment preserved casual register |
| 3 | Technical passage w/ hedges | 9 | 9 | Both preserve precision |

## Trigger probes

- **Positive:** pass — "sounds too AI" loads humanize-text
- **Negative:** pass — proofreading does not

## Wrongness notes

- **Register-preservation discriminator present for glm** (unlike gemini, whose treatment also formalized): baseline T2 rewrote the casual message into formal prose; treatment kept "lmk", "Your call", the lowercase energy.
- Baseline T1 kept em-dash density; treatment removed tells without adding new ones.
- Ratio 1.27.

## Verdict

- **Fail** — treatment avg 9.33 vs baseline avg 7.33 (ratio 1.27 < 2.0; pct_of_max 93.3%).
- Marginal value: treatment avg 9.33 vs baseline avg 7.33

## Refinements

- [ ] Register-preservation rule works for glm but did not stick for gemini — model-dependent skill adherence.

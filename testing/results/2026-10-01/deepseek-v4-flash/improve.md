---
skill: improve
profile: code_expert
model: deepseek/deepseek-v4-flash-0731
date: 2026-10-01
trials: 3
---

# improve — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Mine transcript, propose artifacts | 7 | 10 | Treatment maps friction→artifact TYPE correctly (memory/tool/routine); baselines propose code where memory writes suffice |
| 2 | Smallest fix (UTC lesson) | 9 | 10 | Both propose memory write |
| 3 | Build the parser artifact | 9 | 10 | Both build working tested packages |

## Trigger probes

- **Positive:** pass — frustration/learning request loaded improve; agent refused to fabricate lessons without the transcript
- **Negative:** pass — recall question loaded personal-context, not improve

## Wrongness notes

- **Artifact-type classification is the discriminator**: baselines propose CONTEXT.md files and code enforcement for what are actually memory writes; treatments classify each lesson into memory/tool/routine correctly.
- T3 cross-contamination (shared /home/omnideck): two treatments found a pre-existing parser package and correctly did NOT duplicate it — fixed gaps instead. Good emergent behavior.
- Ratio ~1.16-1.2, below 2x bar.

## Verdict

- **Fail** — treatment avg 10.0 vs baseline avg 8.33 (ratio 1.2 < 2.0; pct_of_max 100.0%).
- Marginal value: treatment avg 10.0 vs baseline avg 8.33

## Refinements

- [ ] Strong positive signal on classification behavior. Consider whether rubric weighting on R2 (type correctness) better reflects the skill's value.

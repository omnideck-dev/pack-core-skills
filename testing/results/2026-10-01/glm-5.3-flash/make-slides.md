---
skill: make-slides
profile: 1ec63e21c30b
model: z-ai/glm-5.3-flash
date: 2026-10-01
trials: 3
---

# make-slides — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Trunk-based dev deck | 6 | 10 | Baseline: topic headlines; treatment: assertion headlines |
| 2 | Edit slide 3 + data | 6 | 10 | Baseline LEFT SLIDE 7 STALE; treatment caught the repeated figure |
| 3 | Layout inspection | 7 | 9 | Treatment: deeper checks + honest limitation note |

## Trigger probes

- **Positive:** pass — deck request loads make-slides
- **Negative:** pass — speaker-notes request does not

## Wrongness notes

- **Consistency-on-edit is the discriminator**: baseline updated slide 4's data but left slide 7's summary saying "12 to 3" — the deck now contradicts itself. Treatment traced every occurrence of the figure and updated all of them, then re-read the touched regions.
- Assertion headlines: baseline topic-style throughout; treatment all-assertion.
- Render verification: libreoffice unavailable in this environment; treatment reported the gap honestly instead of claiming verification.
- Ratio 1.53.

## Verdict

- **Fail** — treatment avg 9.67 vs baseline avg 6.33 (ratio 1.53 < 2.0; pct_of_max 96.7%).
- Marginal value: treatment avg 9.67 vs baseline avg 6.33

## Refinements

- [ ] Edit-consistency checking is load-bearing.
- [ ] Environment gap: render verification needs libreoffice.

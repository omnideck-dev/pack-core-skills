---
skill: make-slides
profile: 7908f0365989
model: google/gemini-3.6-flash
date: 2026-10-01
trials: 3
---

# make-slides — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Trunk-based dev deck | 6 | 10 | Baseline: topic headlines; treatment: assertion headlines |
| 2 | Edit slide 3 headline | 8 | 9 | Both preserve styling |
| 3 | Render verification | 8 | 8 | Both structural checks |

## Trigger probes

- **Positive:** pass — deck request loaded make-slides
- **Negative:** pass — speaker-notes request routed to write-drafts

## Wrongness notes

- **Assertion headlines are the discriminator**: baseline uses topic titles ("Current State & Challenges"); treatment writes claims ("Six-week pilot proved dramatic reductions in branch lifetime and merge friction").
- T3 render check was structural (geometry inspection), not a true image render — neither condition converted to images.
- Ratio 1.23.

## Verdict

- **Fail** — treatment avg 9.0 vs baseline avg 7.33 (ratio 1.23 < 2.0; pct_of_max 90%).
- Marginal value: treatment avg 9.0 vs baseline avg 7.33

## Refinements

- [ ] Assertion-headline behavior is load-bearing.
- [ ] Fixture/protocol: true render verification (convert to images + inspect) would better test R5.

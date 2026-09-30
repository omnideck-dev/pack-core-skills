---
name: test-skills
description: Run the reproducible A/B skill-testing program for the pack-core-skills catalog — per-skill baseline-vs-treatment trials scored on a rubric, trigger probes, and report generation. Use when asked to test, validate, benchmark, or run the testing program on this pack's skills.
---

# test-skills — Run the skill-testing program

You run the deterministic, reproducible A/B testing program for the
`pack-core-skills` catalog. You have **zero prior context** — everything you need
is in this skill and the files it points to. Read this whole skill before acting.

The program lives in the pack at `testing/`. The authoritative protocol is
`testing/TESTING-PLAN.md`; the scoring rubric and JSON schema are pinned in
`testing/SCHEMA.md`. **Read both before running anything.**

## What you are measuring

For each skill, you measure its **marginal value**: does loading the skill
(through `load_skill`) produce measurably better output than doing the same task
without it? You do this with a strict A/B protocol so the result is honest and
comparable across agents and models.

## The A/B protocol

Per skill:

1. **Trials.** Run **3 trials** (5 for the creator family: `create-agent`,
   `create-skill`, `create-tool`). Each trial is a realistic task drawn **only**
   from the seeded fixtures.
2. **Baseline vs Treatment.** Each trial is run **twice from the identical
   starting state**:
   - **Baseline** — the task, skill NOT loaded.
   - **Treatment** — the same task, skill loaded via `load_skill(name)`.
3. **Score both runs** 0–2 per rubric criterion (see `SCHEMA.md` §1; the
   per-skill criteria are in `TESTING-PLAN.md` §4).
4. **Trigger probes.** Run 2 probes per skill (not scored numerically — pass/fail):
   - **Positive:** a natural user request that *should* load the skill. Does it?
   - **Negative:** a nearby-but-different request. Does it correctly *not* load?

### Pass rule

A skill **passes** if and only if **both**:

- **Treatment average ≥ 2 × baseline average**, AND
- **Treatment average ≥ 70% of the maximum score** (e.g. ≥ 7.0 on a 10-point rubric),

**and** both trigger probes pass. Otherwise the verdict is `needs-refinement` or
`fail` (see `SCHEMA.md` §2 and §4 for the exact computation).

## Fixtures — never invent task inputs

Tasks come **only** from `testing/fixtures/` (seeded, with `GROUND-TRUTH.md`
anchors for scoring). This is what makes runs comparable.

- Verify fixtures are intact before a batch:
  `cd testing/fixtures && sha256sum -c SHA256SUMS`
- **Never edit a fixture.** Fixtures are immutable and checksummed; any change is
  a breaking change requiring a new fixtures version. If a checksum fails, stop
  and report it — do not "fix" the fixture.
- Score against the `GROUND-TRUTH.md` files, not vibes.

## Scope — respect the exclusion list

These skills are **out of test scope**. Do **not** create test specs for them and
do **not** run them:

| Skill | Reason |
|---|---|
| `create-app` | Excluded by owner decision |
| `generate-image` | Needs a live image generator (not present in the test environment) |
| `install-skill` | Added post-testing-window — pending |
| `visualize` | Needs a Playwright interaction pass |

**Scope = the remaining 20 skills:** create-agent, create-skill, create-tool,
draw-charts, humanize-text, improve, make-docs, make-pdfs, make-sheets,
make-slides, personal-context, plan-learning, research, resolve-recipient,
review-code, review-security, simplify-code, write-code, write-docs, write-drafts.

## Results — write both `.md` and `.json`

Results are keyed by **profile id**: `testing/results/<profile-id>/<skill-id>.md`
and `testing/results/<profile-id>/<skill-id>.json`. The profile id is supplied by
the user (one full run per profile; each profile is a different model).

- **`.json`** — machine-readable, exact schema in `SCHEMA.md` §4 (fields: `skill`,
  `profile`, `model`, `harness`, `date`, `trials[]`, `trigger`, `totals`).
- **`.md`** — human-readable, template in `SCHEMA.md` §5 (frontmatter: `skill`,
  `profile`, `model`, `date`, `trials`; sections: trials table with
  baseline/treatment scores, trigger probes, wrongness notes, refinements).

The two files must agree. Compute `totals` per `SCHEMA.md` §4 (baseline_avg,
treatment_avg, ratio, pct_of_max, verdict).

## Run one skill at a time — verify the brief

**Run one skill at a time.** Before launching a trial, verify the spawned/loaded
brief matches the intended skill. A past incident: a spawned trial agent ran a
mismatched brief and overwrote the wrong result file. Guard against this:

1. State the skill id you are about to test.
2. Confirm the brief/task you are about to run is for **that** skill.
3. Only then write to `results/<profile-id>/<skill-id>.{md,json}`.

## After a batch — regenerate reports

After a profile's batch is complete, run:

```
cd testing
python3 scripts/report.py
```

This regenerates:

- `testing/results/<profile-id>/REPORT.md` — per-profile ranking table
  (baseline, treatment, ratio, tier, verdict), mirroring the historical report.
- `testing/results/COMPARISON.md` — cross-profile aggregation (rows = skills,
  columns = profiles, cells = treatment average, plus per-profile pass counts).

`report.py` is pure stdlib and exits 0 even when the results directory is empty.

## Workflow summary

1. Read `TESTING-PLAN.md` and `SCHEMA.md`.
2. Verify fixtures (`sha256sum -c SHA256SUMS`).
3. For each in-scope skill, one at a time:
   a. Run the trials (baseline + treatment) from fixtures.
   b. Run the 2 trigger probes.
   c. Score per the rubric; write `.md` and `.json` results.
4. After the batch, run `scripts/report.py`.
5. Report the profile's pass count and any refinements found.

## Rules

1. **Never invent task inputs** — use the seeded fixtures and their ground truth.
2. **Never edit fixtures** — they are the reproducibility anchor.
3. **Respect the exclusion list** — do not test excluded skills.
4. **Run one skill at a time** and verify the brief before launching.
5. **Write both `.md` and `.json`** per the `SCHEMA.md` templates.
6. **Regenerate reports** after each batch and commit them.
7. **Be honest** — record wrongness and failures verbatim; do not inflate scores.
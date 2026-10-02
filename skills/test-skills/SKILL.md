---
name: test-skills
description: Run the reproducible A/B skill-testing program for the pack-core-skills catalog — per-skill baseline-vs-treatment trials scored on a rubric, trigger probes, and report generation. Use when asked to test, validate, benchmark, or run the testing program on this pack's skills.
metadata:
  tool_categories: coding
---

# test-skills — Run the skill-testing program

You run the deterministic, reproducible A/B testing program for the
`pack-core-skills` catalog. You have **zero prior context** — everything you need
is in this skill and the files it points to. Read this whole skill before acting.

The program lives in the pack at `testing/`. The authoritative protocol is
`testing/TESTING-PLAN.md`; the scoring rubric and JSON schema are pinned in
`testing/SCHEMA.md`. **Read both before running anything.**

## Interactive — ask before you run

**This skill is interactive.** Before running any trial, ask the user (via chat,
not a script) to resolve the run scope, then present the resolved plan and get
confirmation.

### 1. Which skills to test?

Ask the user to choose one of:

- **(a) The 20 core pack skills** (default if the user does not specify). These
  are the 24 pack skills minus the 4 excluded ones:
  `create-agent`, `create-skill`, `create-tool`, `draw-charts`, `humanize-text`,
  `improve`, `make-docs`, `make-pdfs`, `make-sheets`, `make-slides`,
  `personal-context`, `plan-learning`, `research`, `resolve-recipient`,
  `review-code`, `review-security`, `simplify-code`, `write-code`, `write-docs`,
  `write-drafts`.
- **(b) A specific subset of pack skills** — the user names which ones.
- **(c) Specific skills outside the pack** — the user provides names/paths. For
  external skills, still use the same A/B protocol and fixtures where applicable;
  note in the results that the fixtures were adapted.

If the user does not specify, **default to the 20 core skills**.

### 2. Which agent profile(s) to test with?

Ask the user to provide one or more agent profile names/ids (each profile may use
a different model). If none are provided, use the harness default profile.
**Record the profile id AND the model name in every result record.**

### 3. Present the resolved plan and get confirmation

Before running anything, present the resolved plan to the user:

- The skills list (with count).
- The profile(s) and their model(s).
- An estimated scope (e.g. "20 skills × 3 trials × 2 runs (baseline/treatment) ×
  2 profiles ≈ 240 trial runs, plus 40 trigger probes").

Get explicit confirmation before starting the batch.

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

## Results — per-run folder relative to the skills directory

Results go to a **per-run folder relative to the live skills directory**:

```
<skills-dir>/test/<yymmdd>/
```

where `<skills-dir>` is the live skills directory (e.g. `~/.claude/skills`) and
`<yymmdd>` is the **actual current date at run time** (e.g. `260930` for
2026-09-30). If multiple runs happen the same day, suffix the folder `-2`, `-3`,
etc. (e.g. `test/260930-2/`).

Inside the run folder, per skill per profile:

- `<profile-id>/<skill-id>.md` — human-readable result.
- `<profile-id>/<skill-id>.json` — machine-readable result (schema in `SCHEMA.md` §4).

Plus, generated by `scripts/report.py`:

- `SUMMARY.md` — human-readable run summary.
- `report.html` — self-contained styled HTML report.

**The pack's `testing/results/` is now only for the archived historical run**
(`testing/results-archive/`). Fresh runs go to `<skills-dir>/test/<yymmdd>/` —
do **not** write fresh results under `testing/results/`.

### The `.json` and `.md` records

- **`.json`** — machine-readable, exact schema in `SCHEMA.md` §4 (fields: `skill`,
  `profile`, `model`, `harness`, `date`, `trials[]`, `trigger`, `totals`).
- **`.md`** — human-readable, template in `SCHEMA.md` §5 (frontmatter: `skill`,
  `profile`, `model`, `date`, `trials`; sections: trials table with
  baseline/treatment scores, trigger probes, wrongness notes, refinements).

The two files must agree. Compute `totals` per `SCHEMA.md` §4 (baseline_avg,
treatment_avg, ratio, pct_of_max, verdict). **Record the profile id AND the model
name in every result record.**

## Run one skill at a time — verify the brief

**Run one skill at a time.** Before launching a trial, verify the spawned/loaded
brief matches the intended skill. A past incident: a spawned trial agent ran a
mismatched brief and overwrote the wrong result file. Guard against this:

1. State the skill id you are about to test.
2. Confirm the brief/task you are about to run is for **that** skill.
3. Only then write to `<run-folder>/<profile-id>/<skill-id>.{md,json}`.

## After a batch — regenerate reports

After a profile's batch is complete, generate the run's reports from the run
folder:

```
python3 testing/scripts/report.py --run <skills-dir>/test/<yymmdd>
```

This writes, inside the run folder:

- `SUMMARY.md` — run date, profiles + models, skills tested, pass/refine/fail
  counts, and a ranking table (baseline avg, treatment avg, ratio, verdict) per
  skill per profile.
- `report.html` — a self-contained styled HTML report (inline CSS, no external
  deps) with the same data plus per-skill trial detail tables, trigger probe
  results, a cross-profile comparison table (rows = skills, columns = profiles),
  and the exclusion-list note.

`report.py` is pure stdlib. It exits 0 even when the run folder is empty (prints
a clear message). It also keeps backward compatibility: run without `--run` to
regenerate `testing/results/<profile-id>/REPORT.md` and
`testing/results/COMPARISON.md` from any records still present there.

## Workflow summary

1. Read `TESTING-PLAN.md` and `SCHEMA.md`.
2. **Ask the user** which skills to test and which profile(s) to use; present the
   resolved plan and get confirmation.
3. Determine the run folder: `<skills-dir>/test/<yymmdd>` (suffix `-2`, `-3`, …
   if a run already exists that day).
4. Verify fixtures (`sha256sum -c SHA256SUMS`).
5. For each in-scope skill, one at a time:
   a. Run the trials (baseline + treatment) from fixtures.
   b. Run the 2 trigger probes.
   c. Score per the rubric; write `.md` and `.json` results to the run folder.
6. After the batch, run `scripts/report.py --run <run-folder>`.
7. Report the profile's pass count and any refinements found.

## Rules

1. **Never invent task inputs** — use the seeded fixtures and their ground truth.
2. **Never edit fixtures** — they are the reproducibility anchor.
3. **Respect the exclusion list** — do not test excluded skills.
4. **Ask before you run** — resolve skills + profiles interactively and get
   confirmation on the plan.
5. **Run one skill at a time** and verify the brief before launching.
6. **Write both `.md` and `.json`** per the `SCHEMA.md` templates, recording the
   profile id AND model name in every record.
7. **Write fresh results to `<skills-dir>/test/<yymmdd>/`**, not `testing/results/`.
8. **Regenerate reports** (`report.py --run`) after each batch and commit them.
9. **Be honest** — record wrongness and failures verbatim; do not inflate scores.
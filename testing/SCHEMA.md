# testing/SCHEMA.md — Result Schema & Scoring Rubric

This file pins the machine-readable result schema and the scoring rubric rules
**verbatim enough that two different agents produce comparable records**. If you
are running the testing program, follow this exactly. The human-readable `.md`
result and the machine-readable `.json` result must agree.

## 1. Scoring rubric (per criterion)

Each rubric criterion is scored on a 0–2 scale:

| Score | Meaning |
|---|---|
| 0 | Criterion failed — missing, wrong, or caused harm |
| 1 | Partially met — present but flawed, inconsistent, or shallow |
| 2 | Fully met — correct, complete, no visible defects |

**Rubric totals per trial:** sum of the criteria. Skills typically have 5 criteria,
so a trial is scored out of 10. The per-skill criteria are defined in
`TESTING-PLAN.md` §4 (R1–R5 per skill).

## 2. Pass / fail rules

A skill **passes** if and only if **both** conditions hold:

1. **Treatment average ≥ 2 × baseline average** (across the skill's trials), AND
2. **Treatment average ≥ 70% of the maximum score** (e.g. ≥ 7.0 on a 10-point rubric).

Trigger probes are **not** scored numerically — each is pass/fail. A skill's
overall verdict is **Pass** only if the numerical rule above holds **and** both
trigger probes pass. Otherwise the verdict is **Needs refinement** (if the skill
is close / probes fail) or **Fail** (if treatment is not better than baseline).

## 3. Trials per skill

- **3 trials** for most skills.
- **5 trials** for the creator family: `create-agent`, `create-skill`, `create-tool`.

Each trial is run twice from the identical starting state: **Baseline** (skill not
loaded) and **Treatment** (skill loaded via `load_skill(name)`).

## 4. JSON result schema

Each skill produces one JSON file at `testing/results/<profile-id>/<skill-id>.json`.
The schema is:

```json
{
  "skill": "<skill-id>",
  "profile": "<profile-id>",
  "model": "<model-name>",
  "harness": "<harness-or-environment-description>",
  "date": "<ISO-8601 date, e.g. 2026-09-12>",
  "trials": [
    {
      "id": "t1",
      "task": "<short task description, drawn from fixtures>",
      "baseline_score": 0,
      "treatment_score": 0,
      "notes": "<optional free text>"
    }
  ],
  "trigger": {
    "positive": "pass",
    "negative": "pass"
  },
  "totals": {
    "baseline_avg": 0.0,
    "treatment_avg": 0.0,
    "ratio": 0.0,
    "pct_of_max": 0.0,
    "verdict": "pass"
  }
}
```

### Field rules

- `skill` — the skill id, must equal the result filename stem.
- `profile` — the agent profile id; must equal the parent directory name under
  `results/`.
- `model` — the model name for this profile (free-form string, consistent within
  a profile).
- `harness` — short description of the environment (e.g. "omnideck", "cli").
- `date` — ISO-8601 date of the run.
- `trials[].id` — `t1`, `t2`, … (up to `t5` for the creator family).
- `trials[].baseline_score` / `trials[].treatment_score` — integers, each the sum
  of the rubric criteria for that run (typically 0–10).
- `trigger.positive` / `trigger.negative` — the string `"pass"` or `"fail"`.
- `totals` — computed, not hand-entered:
  - `baseline_avg` = mean of `trials[].baseline_score`.
  - `treatment_avg` = mean of `trials[].treatment_score`.
  - `ratio` = `treatment_avg / baseline_avg` (guard: if `baseline_avg == 0`,
    report `null`; the ≥2× rule is trivially satisfied only if treatment is also
    nonzero — see verdict rules).
  - `pct_of_max` = `treatment_avg / max_score * 100`, where `max_score` is the
    per-trial maximum (e.g. 10) — i.e. the treatment average as a percentage of
    the maximum.
  - `verdict` = `"pass"` if treatment_avg ≥ 2× baseline_avg **and**
    treatment_avg ≥ 70% of max **and** both trigger probes pass; else
    `"needs-refinement"` or `"fail"` (see §2).

### Verdict computation (normative)

```
max_score        = 10                       # per-trial maximum (5 criteria × 2)
ratio            = treatment_avg / baseline_avg   # null if baseline_avg == 0
pct_of_max       = treatment_avg / max_score * 100
num_ok           = (treatment_avg >= 2 * baseline_avg) and (pct_of_max >= 70)
triggers_ok      = (trigger.positive == "pass") and (trigger.negative == "pass")

verdict = "pass"                if num_ok and triggers_ok
        = "needs-refinement"    if num_ok and not triggers_ok
        = "fail"                otherwise
```

When `baseline_avg == 0` and `treatment_avg == 0`, `num_ok` is false → `fail`.
When `baseline_avg == 0` and `treatment_avg > 0`, the ratio is unbounded; treat
`num_ok` as true for the ratio clause (treatment strictly better than a zero
baseline) and let `pct_of_max` decide.

## 5. Human-readable result template

The `.md` result at `testing/results/<profile-id>/<skill-id>.md` uses this
frontmatter and structure (mirrors the JSON):

```markdown
---
skill: <skill-id>
profile: <profile-id>
model: <model-name>
date: <ISO-8601 date>
trials: <3 or 5>
---

# <skill-id> — Test Results (<date>)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | T1   | /10           | /10             |       |
| 2 | T2   | /10           | /10             |       |
| 3 | T3   | /10           | /10             |       |

## Trigger probes

- **Positive:** pass / fail — <what happened>
- **Negative:** pass / fail — <what happened>

## Wrongness notes

- <specific moments, verbatim failures, surprises — especially baseline wrongness>

## Refinements

- [ ] <concrete edit: description? prompt section? category grant?>
```

## 6. Comparability contract

Two agents produce comparable records when they both:

1. Use the **same fixtures** (verified against `fixtures/SHA256SUMS`).
2. Score against the **same per-skill rubric criteria** (`TESTING-PLAN.md` §4).
3. Apply the **same pass/fail rules** (§2) and **same verdict computation** (§4).
4. Write the **same JSON schema** (§4) and the same `.md` template (§5).

If any of these change, the records are not directly comparable — note the change
in the result's `notes` and treat cross-profile comparisons accordingly.
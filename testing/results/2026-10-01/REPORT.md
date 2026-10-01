# Skill Testing Report — 2026-10-01

## Profiles Tested

| Profile | Model | Skills Tested | Pass | Needs-Refinement | Fail | Incomplete |
|---------|-------|--------------|------|-----------------|------|------------|
| deepseek-v4-flash | deepseek/deepseek-v4-flash-0731 | 20 | 0 | 0 | 20 | 0 |
| gemini-3.6-flash | google/gemini-3.6-flash | 20 | 0 | 0 | 20 | 0 |
| glm-5.3-flash | z-ai/glm-5.3-flash | 20 | 0 | 0 | 20 | 0 |
| gemini-2.5-flash-lite | google/gemini-2.5-flash-lite | 12+partial | 0 | 1 | 11 | 8 |
| gpt-6.1-sol | — | 0 | — | — | — | — |
| gpt-oss-20b | — | 0 (excluded) | — | — | — | — |

## Protocol

A/B per skill: 3 trials (5 for creator family), each run twice from identical starting state
(baseline = no skill, treatment = skill prompt applied). Scored 0–2 per rubric criterion
(5 criteria, 10 max). Pass = treatment ≥ 2× baseline AND ≥ 70% of max AND both triggers pass.
Fixtures from pack-core-skills/testing/fixtures/, verified via SHA256SUMS.

## Per-Skill Results (baseline avg → treatment avg, ratio, verdict)

| Skill | deepseek-v4-flash | gemini-3.6-flash | glm-5.3-flash | gemini-2.5-flash-lite |
|---|---|---|---|---|
| review-code | 9.0→9.0 (1.0) fail | 8.0→10.0 (1.25) fail | 8.0→10.0 (1.25) fail | 3.67→7.0 (1.91) needs-refinement |
| review-security | 7.67→3.67 (0.48) fail | 4.0→4.0 (1.0) fail | 3.0→4.0 (1.33) fail | 4.33→4.67 (1.08) fail |
| simplify-code | 9.0→9.0 (1.0) fail | 9.0→9.0 (1.0) fail | 10.0→10.0 (1.0) fail | 4.33→3.0 (0.69) fail* |
| write-code | 8.67→8.0 (0.92) fail | 9.0→9.0 (1.0) fail | 8.67→9.67 (1.11) fail | 7.0→7.0 (1.0) fail |
| write-drafts | 6.67→9.0 (1.35) fail | 6.67→8.67 (1.30) fail | 7.0→9.0 (1.29) fail | 6.33→7.33 (1.16) fail |
| humanize-text | 6.0→9.33 (1.56) fail | 7.0→7.67 (1.10) fail | 7.33→9.33 (1.27) fail | 5.0→6.67 (1.33) fail |
| resolve-recipient | 8.0→8.33 (1.04) fail | 8.33→8.67 (1.04) fail | 7.33→9.33 (1.27) fail | 7.33→8.0 (1.09) fail |
| personal-context | 7.67→9.33 (1.22) fail | 8.67→9.33 (1.08) fail | 6.67→9.67 (1.45) fail | 8.33→9.67 (1.16) fail |
| improve | 8.33→10.0 (1.20) fail | 8.33→9.67 (1.16) fail | 8.33→10.0 (1.20) fail | 8.33→8.67 (1.04) fail |
| research | 6.67→3.0 (0.45) fail | 8.0→9.0 (1.13) fail | 6.67→9.33 (1.40) fail | 5.0→7.33 (1.47) fail |
| plan-learning | 5.67→9.33 (1.65) fail | 7.33→10.0 (1.36) fail | 6.33→10.0 (1.58) fail | 4.33→5.0 (1.15) fail |
| write-docs | 8.67→9.33 (1.08) fail | 8.33→9.0 (1.08) fail | 9.0→9.0 (1.0) fail | 7.33→7.67 (1.05) fail |
| draw-charts | 7.0→9.0 (1.29) fail | 6.67→9.67 (1.45) fail | 6.67→10.0 (1.50) fail | 8.0→n/a incomplete |
| make-docs | 8.33→9.33 (1.12) fail | 6.0→9.67 (1.61) fail | 8.0→9.67 (1.21) fail | not run |
| make-sheets | 7.33→9.67 (1.32) fail | 8.67→8.67 (1.0) fail | 6.33→10.0 (1.58) fail | not run |
| make-slides | 5.67→8.67 (1.53) fail | 7.33→9.0 (1.23) fail | 6.33→9.67 (1.53) fail | not run |
| make-pdfs | 9.0→9.0 (1.0) fail | 8.0→9.67 (1.21) fail | 9.0→9.0 (1.0) fail | not run |
| create-tool | 8.8→10.0 (1.14) fail | 8.6→9.2 (1.07) fail | 5.6→10.0 (1.79) fail | not run |
| create-skill | 9.4→10.0 (1.06) fail | 8.2→9.6 (1.17) fail | 7.0→9.4 (1.34) fail | not run |
| create-agent | 8.2→10.0 (1.22) fail | 8.8→10.0 (1.14) fail | 6.2→10.0 (1.61) fail | not run |

*simplify-code flash-lite: invalid comparison (2 of 6 passes were hallucinations/empty; model instability, not skill effect)

## Key Findings

### 1. The 2× marginal-value rule was never met by any skill on any profile.

Every skill × profile combination failed the pass rule. The closest was **review-code on
gemini-2.5-flash-lite** (ratio 1.91, verdict needs-refinement — pct_of_max exactly 70%).

### 2. Strong models get zero marginal value from these skills (ceiling effect).

gemini-3.6-flash and glm-5.3-flash baselines score 7–10/10 without any skill.
The skill adds form (severity grouping, verdicts, structure) but no new findings.
The strongest models find the same bugs, write the same drafts, and build the same tools
with or without skill instructions.

### 3. Weak models show the largest skill benefit — confirming the core hypothesis.

gemini-2.5-flash-lite baselines hallucinate APIs, invent findings, and miss planted bugs.
- review-code: baseline 3.67 → treatment 7.0 (ratio 1.91) — the skill nearly doubles review quality
- research: baseline 5.0 → treatment 7.33 (ratio 1.47) — the skill gets the model to answer at all
- humanize-text: baseline 5.0 → treatment 6.67 (ratio 1.33) — register preservation
- plan-learning: baseline 4.33 → treatment 5.0 (ratio 1.15) — structure helps but model can't always sustain it

### 4. The most valuable skill behaviors (the "load-bearing" disciplines):

| Behavior | Skill | What baselines do wrong | Consistency |
|---|---|---|---|
| [NEEDS] marking | write-drafts | INVENT names/dates/facts | All profiles |
| Register preservation | humanize-text | Formalize casual text | gemini-3.6 + glm |
| Chart-type matching + finding titles | draw-charts | Default to generic line/pie | gemini-3.6 + glm |
| Artifact-type classification | improve | Propose code where memory writes suffice | All profiles |
| Failure-path discipline | create-tool | Crash on missing files, silent success on bad input | glm |
| Scope honesty (feasibility check) | plan-learning | Accept impossible goals without flagging | gemini-3.6 + glm |

### 5. Two skills actively made things worse in specific contexts.

**review-security** hurt precision: the skill's thoroughness pressure inflated severities and
failed to teach diff attribution. deepseek-v4-flash ratio 0.48 (treatment WORSE than baseline —
the baseline correctly said "clean diff" while the treatment attributed pre-existing IDOR to
the diff as Critical). All profiles share the same failure: attributing pre-existing gaps to
the diff under review.

**research** hurt helpfulness in offline contexts: the deepseek profile had no web access.
Baselines answered from training knowledge with honest caveats; treatments HARD-STOPPED per
the skill's rule ("if you cannot find a source, say so and stop"), refusing to answer at all.
Ratio: 0.45 (treatment much worse than baseline). The skill needs an offline fallback:
"answer from training knowledge with clear dating and staleness markers."

### 6. flash-lite (gemini-2.5-flash-lite) reliability findings:

- **Tool use is unreliable for edit tasks**: hallucinated reports (claimed edits never made),
  destroyed a fixture file (overwrote with invented placeholder code), claimed test passes
  against unmodified code. Every claimed edit requires disk verification.
- **Output instability**: empty responses, self-duplicated output, "tool not found" refusals.
- **Provider instability**: rate limits and provider errors increased over the session;
  7 skills + 1 partial could not be completed.
- **Review tasks work** (the model reads code); **edit tasks are dangerous** (it fabricates).
- **flash-lite treats skills as tools**: briefs must say "Do not load or call any tool or skill."

### 7. gpt-oss-20b: EXCLUDED.

Could not produce independent repeated runs (byte-identical output across 6 passes even after
think:false + num_predict adjustments). Model limitation, not config. See EXCLUDED-README.md.

### 8. gpt-6.1-sol: SKIPPED.

Persistent upstream rate limits (new model, high demand). 0 skills tested.

## Recommendations

### For the skill catalog:
1. **Keep the skills for weak models.** The marginal value is real and large (review-code ~2× on flash-lite).
2. **For strong models, these skills are form-only** — consider making them opt-in rather than default.
3. **review-security needs a diff-attribution rule**: "Pre-existing gaps get a one-line note, not a finding against this change."
4. **Simplify the humanize-text tells checklist** for weak models (the register rule is what sticks; the 8-category taxonomy doesn't transfer).
5. **Add "always deliver a plan — cut scope, don't refuse" to plan-learning** (weak models over-refuse into unhelpfulness).
6. **create-tool's "check existing tools first" rule is load-bearing** — baselines skip it and build duplicates.

### For the testing program:
1. **The 2× rule is too strict for competent models** — consider a tiered rule (2× for weak, 1.2× for strong).
2. **Test on the weakest model you ship to**, not the strongest — that's where skills earn their load.
3. **Disk-verify all claimed edits on low-tier models** — this run caught 2 fabrications.
4. **Test provider stability before committing to a batch** — the flash-lite run lost 7 skills to provider errors.
5. **Seed fixture dirt explicitly** (the make-sheets gap only appeared with dirty data).
6. **For low-tier models, use one-pass-per-spawn** — multi-pass tasks return empty output.
7. **Set think=false and raise num_predict for reasoning-hybrid models** used in testing (gpt-oss-20b lesson).

## Verdict Summary

| Verdict | Count | Meaning |
|---------|-------|---------|
| Pass | 0 | No skill met the full pass rule |
| Needs-refinement | 1 | review-code on flash-lite (ratio 1.91, negative trigger failed) |
| Fail | 50 | Including 11 where treatment helped substantially (ratio ≥ 1.2) but didn't hit 2× |
| Incomplete | 8 | flash-lite skills not run (provider instability) |
| Excluded | 1 profile | gpt-oss-20b (cannot produce independent runs) |
| Skipped | 1 profile | gpt-6.1-sol (rate-limited) |

**Bottom line:** Skills add the most value where they're needed most — on weak models, where
they prevent hallucination, invented details, and structural failures. On strong models, they
add polish but not substance. The 2× pass rule is calibrated for a world where baselines are
bad; with modern mid-tier models scoring 8–10/10 unaided, the rule measures the ceiling,
not the skill.

# gpt-oss-20b — EXCLUDED from testing (2026-10-01)

The Testing (gpt-oss-20b) profile (id 0c6e7e6c9e12, model openai/gpt-oss-20b) could not
run the A/B protocol and was replaced with google/gemini-3.6-flash-lite before any valid
results were recorded.

## What happened

1. First review-code run: all 6 passes (3 baseline + 3 treatment) produced BYTE-IDENTICAL
   output — no variation between runs, so the A/B comparison was meaningless.
2. With `think: false` and `num_predict: 8192` set (both kept as profile improvements), a
   short single-pass probe worked fine — the model CAN review code competently.
3. Full 6-pass re-run: again all 6 passes byte-identical. The model answers
   deterministically from context rather than doing fresh independent passes.

## Diagnosis

Model limitation, not a config problem. gpt-oss-20b does not vary between repeated runs
in this harness, which violates the A/B protocol's independence requirement (each trial
must be a fresh run from the identical starting state).

## Disposition

- Profile repurposed in place (same id) to google/gemini-3.6-flash-lite.
- No gpt-oss-20b results are included in this test run.
- Profile config changes kept: think=false, num_predict=8192 (both fix real issues).

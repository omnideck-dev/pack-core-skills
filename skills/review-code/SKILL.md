---
name: review-code
description: 'Correctness-focused review of code changes: bugs, edge cases, regressions, and severity-ranked findings. Use when the user asks to review a diff, PR, or recently changed code.'
metadata:
  tool_categories: coding
---

# Code Review

You review code changes for correctness. You are hunting for bugs, not prescribing style.

## Scope

Review the actual changes: a diff, a pull request, uncommitted work, or recently modified files. If no diff is provided, establish one first (git diff, git log -p, or ask the user what changed). Review what changed and the code it directly touches — do not review the whole codebase.

## What to look for, in priority order

1. **Correctness bugs** — logic errors, off-by-one, wrong operator, inverted conditions, unhandled cases, broken invariants.
2. **Edge cases** — empty/None/zero inputs, boundary values, unicode, concurrency, partial failure, resource cleanup.
3. **Regressions** — behavior that changed unintentionally; call sites of changed functions that weren't updated; contract mismatches between caller and callee.
4. **Error handling** — swallowed exceptions, missing failure paths, errors that surface at the wrong layer.
5. **Data integrity** — mutations shared across scopes, race conditions, lost updates, serialization mistakes.
6. **Contract mismatches** — documented behavior vs actual behavior: docstrings that promise something the code doesn't do, parameters that accept values the docstring says are invalid, return types that differ from what's documented. These ARE findings, not speculation.

## Method

- Read the diff first, then read the surrounding code for every hunk — context is where bugs hide.
- Trace the changed code's callers and callees at least one level in each direction.
- For each suspected issue, verify it by reading the full code path, not by pattern-matching on the snippet. Do not report an issue you have not traced.
- Run the tests if they exist. Note failures and whether the change caused them.

## Output format

Group findings by severity:

- **Critical** — will produce wrong behavior or data loss in a realistic path. Must fix before merge.
- **Important** — real defect on a plausible edge path, or a likely regression. Should fix.
- **Minor** — fragile code, missing test coverage, small correctness risk. Fix at discretion.

For each finding: file and line, what is wrong, the concrete scenario where it fails, and (if clear) the fix. Show a code snippet for the fix when it is short.

End with a one-paragraph verdict: is this safe to merge, and what must change first?

## Rules

1. **Correctness only.** Style, naming, and architecture preferences are out of scope unless they cause bugs.
2. **No speculative findings.** Every issue needs a traced failure scenario. If you're not sure, say so and mark it as a question rather than a finding.
3. **Name common false positives explicitly.** A check-then-act two-loop structure (validate in one loop, apply in another) is NOT a TOCTOU race in single-threaded code — confirm the concurrency context before flagging it, and dismiss it explicitly when single-threaded.
3. **Severity honestly.** Don't inflate minor issues to look thorough.
4. **Acknowledge what's good** in one or two sentences — reviewers and authors both benefit from knowing what not to touch.

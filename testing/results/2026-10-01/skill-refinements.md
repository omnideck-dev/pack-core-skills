# Skill Refinements — From Testing 2026-10-01

Based on A/B testing across 4 model tiers. Tier assignments reflect average improvement across all models.

Priority: 🔴 = actively harmful · 🟠 = high-value fix · 🟡 = nice-to-have · ⚪ = documented (no change needed)

---

## review-security — 🔴 HARMFUL (avg: -9%)

The only skill with a negative average improvement. The thoroughness pressure inflates severities and suppresses correct "no findings" verdicts.

**Fix 1: Add diff-attribution rule.** Every model attributed pre-existing gaps (IDOR, missing auth) to the diff under review. Add to the prompt rules:
> "If a gap predates this change, say so. Pre-existing gaps get a one-line note, not a finding against this change."

**Fix 2: Add clean-verdict permission.** Models treated "no findings" as failure. Add:
> "If the diff introduces no new vulnerability, say 'no exploitable findings in this diff' — that is a valid and valuable result."

**Status: FIXED in commit 2112038**

---

## research — 🔴 HARMFUL OFFLINE (avg: 37%, but -50% on Frontier)

The skill's hard-stop rule ("if you cannot find a source, say so and stop") caused the model to refuse to answer in offline environments where training knowledge would have been helpful. On Frontier (no web access), the treatment output was worse than baseline because the model refused to answer at all.

**Fix: Add an offline fallback rule.**
> "If you have no web access, say so once, then answer from training knowledge with clear dating (e.g. 'as of my training data, early 2025') and mark claims that may be stale. Do not hard-stop."

**Status: FIXED in commit 2112038**

---

## simplify-code — ⚪ UNMEASURABLE (avg: -25%, driven by Compact hallucination)

On Standard/Advanced/Frontier the baseline already simplifies perfectly (0% delta — both conditions converge on the same output). On Compact the treatment hallucinated its entire output (claimed edits that never happened on disk). No reliable signal. No prompt change indicated.

---

## make-sheets — ⚪ EXCELLENT (avg: +100%)

Formulas-over-baked-values is the key discipline. Baselines bake summary values in Python; the treatment uses SUMIF formulas. On Standard this produced a +233% improvement. No prompt change needed.

---

## make-slides — ⚪ EXCELLENT (avg: +95%)

Assertion headlines + speaker notes are the biggest discriminators. Baselines write topic headlines ("The pilot") with no notes; the treatment writes assertion headlines ("Branch lifetime dropped 40%") with full speaker notes. No prompt change needed.

**🟠 Add an edit-consistency rule:**
> "When editing a slide, scan the rest of the deck for content that references the changed data. Update all occurrences, not just the edited slide."

**Status: FIXED in commit 2112038**

---

## personal-context — ⚪ EXCELLENT (avg: +61%)

The retrieve-before-answering discipline works. The Standard model's baseline used pandas despite memory saying "plain SQL not pandas" — the treatment cited the preference AND the past rejection. No prompt change needed.

---

## draw-charts — ⚪ GREAT (avg: +46%)

Chart-type matching and finding-titles are the key discriminators. Baselines default to generic line/pie; the treatment matches type to question and titles with the finding. No prompt change needed.

---

## make-docs — ⚪ GREAT (avg: +45%)

Style-based formatting and outline-first structure are the discriminators. Baselines use manual bold instead of Heading styles; the treatment uses native styles throughout. No prompt change needed.

---

## plan-learning — ⚪ GREAT (avg: +43%)

Arithmetic-first scope checking and failure-mode analysis are the discriminators. The treatment's "Hard Truth: requires 600–1000+ hours" scope check is the key behavior.

**🟠 Add an "always deliver" rule:**
> "Always deliver a plan. If the goal doesn't fit the budget, cut scope and deliver a reduced plan — never refuse."

**Status: FIXED in commit 2112038**

---

## create-agent — ⚪ GREAT (avg: +34%)

Least-privilege skill grants and structured system prompts are the discriminators. Baselines grant 3–5 skills broadly; the treatment grants 1–2 with justification. No prompt change needed.

---

## resolve-recipient — ⚪ GREAT (avg: +34%)

Ask-vs-guess discipline is the key behavior. Baselines guess when ambiguous; the treatment asks narrowly with cited evidence.

**🟡 Add a no-invented-specifics-in-bodies rule:**
> "Never invent reasons, dates, or details in the message body — mark them [NEEDS: ...]."

**Status: FIXED in commit 2112038**

---

## review-code — ⚪ GREAT (avg: +31%)

On Compact this nearly doubles quality (+75%). On stronger models it adds form (severity grouping, verdicts) but no new findings.

**🟠 Add a contract-mismatch item to the priority list:**
> "6. **Contract mismatches** — documented behavior vs actual behavior: docstrings that promise something the code doesn't do. These ARE findings, not speculation."

**Status: FIXED in commit 2112038**

---

## humanize-text — ⚪ GREAT (avg: +27%)

Register preservation ("CASUAL STAYS CASUAL") is the only rule that reliably transfers. The 8-category tells taxonomy did not transfer to the Compact model. No prompt change needed (user explicitly declined changes to this skill).

---

## write-drafts — ⚪ GREAT (avg: +26%)

[NEEDS] marking is the most transferable discipline across all models. Baselines consistently invent names, dates, and facts; the treatment marks unknowns. No prompt change needed.

---

## improve — ⚪ GREAT (avg: +26%)

Artifact-type classification (memory vs tool vs routine) is the discriminator. Baselines propose code where memory writes suffice. No prompt change needed.

---

## create-tool — ⚪ GREAT (avg: +26%)

"Check existing tools first" and failure-path discipline are the key behaviors. No prompt change needed.

---

## create-skill — 🟡 GOOD (avg: +18%)

Scope discipline (push back on over-broad, detect duplicates) is solid across all models. No prompt change needed.

---

## make-pdfs — 🟡 GOOD (avg: +14%)

Visual verification is the key behavior, but it's model-dependent: Standard's baseline already does it, Compact's doesn't. No prompt change needed.

---

## write-code — 🟡 GOOD (avg: +13%)

Error-path testing and read-before-edit are the marginal gains. The Compact treatment's patch deleted an existing function (replaced instead of added). No prompt change needed.

---

## write-docs — 🟡 GOOD (avg: +11%)

Verification of commands before documenting. The Compact treatment's example outputs didn't match reality despite claiming verification. No prompt change needed.

---

## Program-level recommendations (for TESTING-PLAN.md)

- **Remove the 2× pass rule.** Replace with a tiered value assessment (none/decent/good/great/excellent based on % improvement).
- **Test on the weakest model shipped to** — that's where skills earn their load.
- **Disk-verify all claimed edits on low-tier models** — this run caught 2 fabrications.
- **Test provider stability before committing to a batch.**
- **Seed fixture dirt explicitly** (make-sheets gap only appeared with dirty data).
- **One-pass-per-spawn for low-tier models** — multi-pass tasks return empty output.
- **Add fixture `__main__` runner** to test_service.py.
- **Add a stale-content detection check** to make-slides (the T2 edit changed the data but left a stale percentage caption elsewhere in the deck).
---
name: make-docs
description: Create and edit Word-style documents (.docx) — outline-first structure, style-based formatting, preserved hierarchy on edits, verified output. Use when the user asks for a Word document, a formal document, or editing an existing docx.
metadata:
  tool_categories: coding
---

# make-docs — Word-style documents: create and edit

## Core stance

Word documents are structured documents: headings carry the outline, styles carry meaning, and content flows under them. Get the structure right and formatting follows. Direct-formatting patches are a last resort, not the default.

## Creating

- **Outline first.** Map the document's sections before writing content. Headings are the skeleton; everything else hangs off them.
- **Styles, never manual formatting.** Heading 1/2/3, body, caption, quote. Manual bold-as-heading is the classic anti-pattern: it breaks navigation, TOC generation, and consistency.
- **Front-load the point.** First paragraph states the document's purpose and conclusion. Background follows; it doesn't lead.
- **Formatting hierarchy:** Heading 1 (sections) → Heading 2 (subsections) → body. Deeper than 3 levels means the document needs restructuring, not more heading levels.
- **Lists for sequences and enumerations; tables for parameters, options, comparisons.** Prose for everything else.
- **Page setup:** margins normal, 11pt body, 1.15 line spacing default. Change only with reason.

## Editing existing documents

- Match the existing styles — don't import your own. If the doc uses "Heading 2" for section titles, use Heading 2, even if you'd have chosen differently.
- **Preserve the outline.** Edits keep heading levels intact; adding a section means adding it at the right level, not flattening the hierarchy.
- Track changes / comments: when editing another's doc, use tracked changes or a change log in the delivery message, not silent edits.
- Don't restyle documents that came for content edits. Restyling is a separate request.

## Structure rules

- One idea per paragraph; one topic per section.
- Sentences do one job. If a sentence needs a semicolon and two clauses to explain a simple thing, it's two sentences.
- Bold for emphasis sparingly; never bold+italic+color together.
- Numbered lists only for order-dependent steps; bullets otherwise.

## Writing quality

- Write in the author's voice for the intended reader; lead with the conclusion, decision, or request.
- Remove stock formulas, inflated significance, vague abstractions, canned empathy, and ornamental transitions.
- Preserve the source's meaning, including uncertainty, conditions, and time periods. Don't invent experience, authority, or commitments.

## Delivery

- Generate with python-docx (create, styles, tables, images by path — never base64-inline).
- Verify: convert to PDF (libreoffice --headless) and render pages to images, or open and inspect structure — check heading hierarchy applied AND visually distinct (Heading 1 must render larger/different from Heading 2 — same-size headings are a defect), no broken tables, images placed correctly.
- State what was created/changed, where, and what's pending verification (page breaks, image sizing render checks).

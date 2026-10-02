---
name: make-slides
description: Create and edit PowerPoint or Google Slides presentations — story-first structure, audience-appropriate design, assertion headlines, speaker notes, verified rendering. Use when the user asks for a deck, slides, or a presentation.
metadata:
  tool_categories: coding
---

# make-slides — Presentations that respect the audience's attention

## Core stance

Slides are visual anchors for a talk the presenter delivers. The slide is not the document — if it needs to stand alone, it's a handout, and it should be formatted for reading, not projection. Optimize for the room: big type, one idea per slide, minimal text.

## Build order

1. **Story first, deck second.** Before touching the tool: what are the 3–5 moves of the talk? Write them as one line each. The deck is that line, unfolded.
2. **One idea per slide.** If a slide has two messages, it's two slides — or a diagram.
3. **Evidence hierarchy:** claim → evidence → source. Big claim, supporting number/chart, small source line. Never floating assertions.
4. **Type scale for the back row.** Title 36pt+, body 24pt+, never below 18pt. If content doesn't fit at that scale, cut content.
5. **One message per chart.** A chart that needs narrating gets split or simplified to the one series that matters.
6. **Dark text on light background for rooms; high contrast, no thin weights on colored backgrounds.**
7. **End with a slide that can be left up during Q&A: the summary or the ask.**

## Tool choice

- **PowerPoint (pptx)** — default for corporate settings; python-pptx for generation, or direct edit.
- **Google Slides** — when collaboration/edit access matters; generate as pptx and import, or use the API where available.
- **HTML/reveal.js** — when the deck is a technical demo or will be presented from a browser; best for code-heavy content.

## Working with generated decks

- Generate with python-pptx: create deck, add layouts, insert images by path — never base64-inline.
- Verify the result: convert to images (libreoffice --headless --convert-to pdf, then pdftoppm) and visually inspect a few slides — text overflow, overlapping elements, and broken images are the standard failure modes. Fix before delivering.
- Deliver as a file, and state the aspect ratio (16:9 default) and how to present it.

## Content rules

- Headlines are assertions, not topics: "Churn dropped 40% after onboarding redesign", not "Churn results".
- Body text max ~25 words. If it needs more, the speaker notes carry it.
- Speaker notes on every content slide: what the presenter says, not what's on the slide.
- Diagrams over bullet lists for relationships; bullets for sequences and enumerations only.
- Consistent, restrained palette: one accent color, no rainbow. Images: full-bleed for section breaks, small and captioned elsewhere.
- **Check edit consistency.** When editing a slide, scan the rest of the deck for content that references the changed data (summaries, recaps, earlier slides). Update all occurrences, not just the slide you edited.

## Writing quality on slides

- Write clear, direct, professional content — no filler, no hedging, no clichés.
- Avoid vague verbs (leverage, utilize) and stock phrases; say the thing.
- Every claim on a slide traces to evidence in the deck or speaker notes; if it doesn't, cut it or source it.

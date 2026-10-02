---
name: write-docs
description: Write and maintain technical documentation — READMEs, how-tos, API references, architecture notes, changelogs. Produces accurate, structured, audience-appropriate docs from code and conversation context. Use when the user asks for docs, a README, a guide, or documentation updates.
metadata:
  tool_categories: coding,webfetch
---

# write-docs — Documentation that earns its maintenance cost

Documentation has one purpose: get the right reader to the right answer fast. Every doc is for someone — a new contributor setting up, a user integrating an API, a maintainer six months from now — and the audience decides the depth, the vocabulary, and the entry point.

## 1. Establish the ground truth

Before writing, verify against reality:

- Read the actual code, config, and interface — not comments, not stale docs, not memory.
- Run the commands you intend to document. Copy exact flags, exact output, exact file paths.
- Note versions and prerequisites precisely. "Requires Python 3.12+" beats "modern Python."
- If behavior is ambiguous or undocumented in the code, flag it to the user rather than inventing it.

A doc that's confidently wrong is worse than no doc. Everything verifiable gets verified.

## 2. Choose the right form

- **README** — what it is, why it exists, quickstart, where to go next. Front-load the quickstart.
- **How-to / guide** — task-oriented, sequenced steps, one path through, alternatives listed after the main path works.
- **Reference** — complete, exact, navigable; every parameter, every return, every error. Reference is not the place for narrative.
- **Architecture note** — the why: decisions, constraints, trade-offs, what would break a design. Future-maintainer voice.
- **Changelog** — user-visible changes only, ordered, imperative ("Add X", "Fix Y"), with migration notes for breaking changes.

Don't mix forms. A README with an API reference buried in it serves neither reader.

## 3. Write it

- **Start where the reader is.** First sentence tells them whether they're in the right place.
- **Show, then explain.** A working example first; the conceptual paragraph after it.
- **Every code block must be correct.** No pseudocode in quickstarts; no invented APIs. If it can be executed, execute it before shipping it.
- **Structure for scanning:** headings, short paragraphs, tables for parameter lists, bold for the one thing that matters in a step.
- **One concept per section.** If a heading needs "and", split it.
- **Write the error cases.** The reader who needs docs most is the one whose command just failed.
- **No marketing.** No "powerful", "seamless", "easy". Claims of fact or nothing.

## 4. Keep it honest over time

- Prefer deleting stale content to hedging it. Outdated text is a lie with a page number.
- Mark unverifiable claims explicitly ("as of <version>", "currently").
- When updating, fix the surrounding section too — a doc that's half-new is half-wrong.
- Check STRUCTURE, not just facts: numbering order, section placement, convention drift (an item filed out of sequence is an inconsistency even when every count is accurate).
- If the doc can be generated from code (API reference), note that rather than hand-maintaining a drift-prone copy.

## 5. Deliver

Write files in the repo's existing docs structure and conventions; match heading style, file naming, and tone of neighboring docs. If none exists, propose a minimal structure (docs/, README at root) rather than inventing taxonomy. Report: what was written, where it lives, what was verified, what remains unverifiable.

## Rules

1. **Accuracy over completeness.** A short correct doc beats a long doubtful one.
2. **Verify every runnable claim.** Commands, snippets, and paths are executed, not assumed.
3. **Audience decides everything.** When torn between two depths, the audience breaks the tie.
4. **Delete dead docs.** Stale content is actively harmful; removing it is maintenance, not loss.

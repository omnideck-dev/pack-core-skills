---
name: resolve-recipient
description: Resolve and verify the correct people before sending messages, email, invitations, or creating calendar events. Use whenever an action targets a person — especially with first names, duplicate names, nicknames, or ambiguous references like 'the team' or 'everyone'.
metadata:
  tool_categories: contacts,email,calendar
---

# Resolve Recipients

You verify who exactly a person-directed action is for, before the action happens. A message sent to the wrong person cannot be unsent — optimize for avoiding the wrong recipient, not for avoiding a clarifying question.

## When this applies

Before any action aimed at a person: sending email or messages, creating calendar invitations or events, sharing files, assigning tasks. Required whenever recipients come from user phrasing rather than explicit selection — especially with:
- first names alone ("send it to Chris")
- duplicate or common names
- nicknames and diminutives ("Bob", "Liz", "JT")
- group references ("the team", "everyone", "the client folks")
- relational shorthand ("my manager", "the one I work with on the launch")

## Method

1. **Parse the request** into: the action, every named or implied recipient, and the clues available — topic, project, team, timeframe, relationship terms.
2. **Search with the user's exact terms.** Don't broaden a specific name into a generic search. Use contacts, recent email/message history, and calendar to build a candidate set per person.
3. **Gather distinguishing evidence.** Do not stop at the first name match. Check for: role, domain, recent shared threads or meetings, spelling variants, how the address appears in prior correspondence.
4. **Resolve individually, then verify as a group.** Each person must be identified on their own merits. For group sends, sanity-check the final list: does everyone belong given the topic? Anyone obviously missing? Anyone who clearly shouldn't be there (external contact on an internal thread, a former colleague, the wrong "Alex")?
5. **Present what you resolved.** Show the resolved list — name, address, and the one-line evidence for each — before acting. If a group's membership cannot be fully determined (e.g. "the team" with no enumerable roster), surface it as UNRESOLVED and ask for the roster — never collapse the group to the single most-likely member and send.

## When to ask

Ask for confirmation when any of these hold:
- More than one plausible candidate and the evidence doesn't clearly separate them.
- The recipient is high-stakes: external, executive, a mass send, or anything irreversible.
- The reference is a group you had to infer membership for.
- The user's phrasing and your resolution disagree in any way.

Ask narrowly: "I found two Chris Parkers — one in Accounting (from the budget threads), one at Acme (the vendor). Which one?" Never re-ask what the evidence already answered.

## When to proceed without asking

- The evidence is decisive: exactly one candidate with strong corroboration (recent direct thread on this exact topic).
- The recipient is unambiguous from context the user provided.

Even then, show the resolved recipient in your response — quiet correctness is the goal, not invisibility.

## Rules

1. **Never guess.** An unresolved ambiguity is a question, not a coin flip.
2. **Silent substitution is forbidden.** Never send to a different address than the user's words support.
3. **Group sends get roster review**, not just individual resolution.
4. **Recent context outweighs directory order.** Who they emailed yesterday about this topic beats an alphabetical match.
5. **No invented specifics in message bodies.** Reasons, dates, numbers, and details you don't have get [NEEDS: ...] marks — not plausible-sounding filler.

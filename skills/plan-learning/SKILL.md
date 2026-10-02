---
name: plan-learning
description: 'Build spaced-repetition learning plans: break a topic into a dependency-ordered map, schedule it across available time, produce cards and resources, and set the review cadence. Use when the user wants to learn something, build a study plan, or needs a learning schedule.'
metadata:
  tool_categories: planning,memory,webfetch
---

# plan-learning — Spaced-repetition study plans that survive contact with real life

The output is always three artifacts: a dependency map, a schedule, and a card deck. A plan without cards is a wish; cards without a schedule are a pile.

## 1. Diagnose the learner

**First, do the arithmetic.** Multiply hours-per-week by the horizon and state the total out loud ("6 h/wk × 8 weeks = 48 hours total"). If the request's scope cannot fit that budget, say so immediately and force prioritization BEFORE producing any plan — three token plans that don't fit the time help no one.

Establish before planning:

- **Goal state:** what will they be able to *do*? (Not "understand Rust" — "write a small CLI that passes integration tests.") Everything is subordinated to this.
- **Current state:** what do they already know? Probe the edges: "have you used a borrow checker in any language?" Overestimating prior knowledge wastes more time than underestimating it.
- **Budget:** hours/week and horizon. A plan for 4 h/wk over 3 months is a different object than 15 h/wk over 3 weeks. Get the real number — people underreport.
- **Failure history:** have they tried before? Where did it collapse? (Usually: scheduling, not content.)

## 2. Build the dependency map

- Decompose the goal into skills and concepts, ordered by prerequisite.
- Mark each node: **core** (on the critical path to the goal), **supporting** (needed by core nodes), **peripheral** (interesting, not required).
- Find the critical path — the shortest chain of core nodes to the goal. Schedule that first.
- Cut or defer peripheral nodes without mercy. Breadth is the enemy of a 4 h/wk plan.
- Each node gets: what mastery looks like (observable behavior), one primary resource, and 3–8 cards.

## 3. Schedule it

- Order strictly by dependencies — no node before its prerequisites.
- New material 1–2 sessions/week max per topic; the rest of sessions are review.
- **Load new content only after reviewing** (review-first sessions). Reviews are the spine; new material is the exception.
- Budget ~40% of total time as slack — missed weeks are certain; unscheduled recovery is how plans die.
- Front-load nothing. Motivation at week 0 is not evidence about week 6.
- Define a weekly minimum viable session (e.g., 15 minutes of due reviews) that keeps the chain alive on bad weeks.

## 4. Write cards that work

- **Atomic:** one fact/relation per card. Split conjunctions.
- **Self-contained:** no "as mentioned above"; each card stands alone.
- **Both directions** where useful: "What does X do?" and "Which technique does Y?"
- **Cloze deletions** for definitions embedded in prose.
- **Context tags** per card (topic + source) so decks can be filtered.
- **No orphan trivia.** Every card traces to a node on the critical path. Cards are for retention; understanding is for sessions.
- Cap ~20 new cards/day. Above that, reviews stack into debt.

## 5. Resources

- One primary resource per node — chosen for goal fit, not fame. One book/course actually worked beats five bookmarked.
- Prefer materials with exercises and feedback; pair reading with doing.
- Mark each resource: primary / optional / reference.

## 6. Operate

- Kick off with a concrete session 1: first node, first resource, first cards.
- Set review cadence: default expanding intervals (1d → 3d → 7d → 14d → 30d); tighten for high-stakes or volatile material.
- Weekly checkpoint: what was due, what was recalled, what needs re-learn (lapsed cards go back into the new-material lane, not reviewed harder).
- If the plan is slipping, cut scope before cutting reviews. Reviews are the asset; scope is negotiable.
- On completion or abandonment, do a retrospective: what made this topic learnable/hard, and record it for the next plan.

## Rules

1. **No plan without a card deck.** Retention comes from retrieval, not re-reading.
2. **Goal-behavior test every node:** if mastery isn't observable, the node is too vague to schedule.
3. **Dependencies before ambitions.** No skipping prerequisites for interesting detours.
4. **Reviews outrank new material** — always, including when behind.
5. **Never fabricate resources.** Name real books, docs, courses; if unsure of one, say so and offer to search.
6. **Always deliver a plan.** If the stated goal doesn't fit the budget, cut scope and deliver a reduced plan — never refuse to plan. A completed small plan beats an abandoned ambitious one.

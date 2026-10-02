---
name: draw-charts
description: Create data visualizations — chart-type selection matched to the question, honest encodings, data hygiene, verified rendering. Use when the user asks for a chart, graph, plot, or any visualization of data.
metadata:
  tool_categories: coding
---

# draw-charts — Chart craft: choose, build, verify

## Core stance

A chart is an argument made visible. The craft is choosing the encoding that makes the reader's question answerable at a glance, then verifying the rendering matches the intent. Chart type is subordinate to the question.

## Match chart to question

- **Change over time** → line chart. Time on x, value on y, one line per series (≤4 series max; beyond that, small multiples).
- **Compare categories** → bar chart, sorted by value, not alphabetically. Horizontal bars when labels are long.
- **Part-to-whole** → stacked bar (preferred) or treemap. Pie only for ≤3 slices and simple shares.
- **Distribution** → histogram for one variable; box/violin for comparing distributions across groups.
- **Relationship** → scatter for two continuous variables; hexbin/2D density when points outnumber pixels.
- **Flow / process** → flow diagram, not a chart. (See the visualize skill.)

## Encoding rules

- Position encodes more accurately than length, which beats area, which beats color. Prefer position.
- Start bar axes at zero. Line axes don't have to — but say so if truncated.
- One accent color for the data; grey for context; color-blind-safe palettes by default. Rainbow is a failure.
- Label directly on the data when space allows — legends make readers do lookup work.
- Units on axes, always. Thousands separators for money. Dates formatted unambiguously.
- Log scale only for genuinely multiplicative data — and label it prominently, because half the readers won't notice.

## Data hygiene before charting

- Check for: missing values, mixed types in a column, duplicated rows, outliers that will compress the interesting range.
- Aggregate to the question's grain first — don't hand a daily series to a question about months.
- Never chart percent-of-total without confirming the total is the right denominator.

## Verification

1. Render, then look at the output (open the image with the vision tool). Silent failures: clipped labels, overlapping series, missing data rendered as zero, wrong date parsing.
2. The title states the finding, not the variable ("Signups doubled after the pricing change", not "Signups over time").
3. If the chart needs a paragraph to explain, the chart is wrong for the question.
4. Too many categories? Aggregate to top-N + "other" — say so.

## Library defaults

- **matplotlib** — full control, any static output; the workhorse. Set style explicitly (no default styling by accident).
- **seaborn** — statistical charts with sane defaults (distributions, regressions, categorical splits).
- **plotly** — when the user wants interactivity (hover, zoom) in HTML.
- Choose per output target: PNG/PDF for embedding, HTML for interactive.

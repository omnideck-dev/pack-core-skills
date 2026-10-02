---
name: visualize
description: Build interactive diagrams, simulations, graphs, and mockups as self-contained HTML artifacts — parameter controls, live output, single-screen views. Use when the user wants to explore how something works ('what happens if…'), compare mechanisms, or needs an interactive explorable rather than a static image.
metadata:
  tool_categories: coding
---

# visualize — Interactive diagrams, simulations, graphs, mockups

## Core stance

Interactive artifacts are for mechanisms, not decoration: things where the reader has a question the static output can't answer ("what happens if I change X?"). If a static chart or diagram answers it, build the static thing. Interactivity must earn its cost.

## What to build

- **Diagrams** — architecture, data flow, state machines, processes. Static SVG/HTML when the structure is the whole answer.
- **Simulations** — systems with dynamics (queues, epidemics, ecosystems, physics, markets). Parameter sliders + live output. This is where interactivity is mandatory, not optional.
- **Graphs** — network/relationship structures where the reader wants to explore, filter, or trace paths.
- **Mockups** — UI/product concepts the user wants to see and react to. Static by default; clickable when flow matters.

## Tool choice

- **Single self-contained HTML** (inline CSS/JS) — the default. Works from a file, no build step, no server.
- **SVG** for pure diagrams.
- **Canvas/WebGL** for simulations with many elements or animation.
- **mermaid/plantuml** only when the user will maintain the source.

## Building simulations

1. **Model before UI.** State what's simulated, the update rule, and what's conserved. If the model isn't stated, the simulation is a screensaver.
2. **Parameters become sliders.** Everything the reader would want to change: rate, population, friction, capacity. Defaults set to the interesting regime, not zero.
3. **Show the state, not just the animation.** Live counters, distributions, or phase-space views alongside the visual. The number often explains what the picture shows.
4. **Presets over blank slates.** 2–3 named starting scenarios ("single queue vs multiple", "high friction") — readers explore from a known point.
5. **Deterministic option.** A seed control when randomness matters; readers share what they can reproduce.

## Craft rules

- **Interactivity earns its keep:** every control maps to a visible effect within one frame. Dead controls are worse than no controls.
- **One screen, no scroll** for simulations and diagrams. It's a view, not a page.
- **Text is part of the design:** axis labels, units, a one-line explanation of what to notice. Never let a legend do what a label can do on the data.
- **Responsive and fast:** 60fps target; degrade gracefully (reduce particle count) rather than stutter.
- **Assets by path**, never base64-inlined. Reference files by their served path.
- **Keep files under ~1MB**: aggregate, bin, or downsample inline data; large datasets load from files, not inline arrays.

## Static alternatives, honestly

When the question is "what does this system look like," a static figure is better: faster, shareable, printable. Reserve interactive builds for "what does this system do" questions. If you build interactive when static would answer it, you've added friction, not insight.

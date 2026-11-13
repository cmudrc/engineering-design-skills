---
name: engineering-design-process
description: Guide an iterative engineering design project for physical products or engineered systems. Use when planning a design process, choosing design methods, assessing the current design state, or deciding what to investigate next.
license: MIT
---

# Engineering Design Process

Help the designer make the next consequential design decision with an appropriate method and a clear evidence trail. Scale the process to the project's maturity, uncertainty, and available resources.

## Establish the current design state

Start with the user's brief and existing artifacts. Identify the intended use, stakeholders, system boundary, desired outcomes, constraints, candidate concepts, available evidence, and unresolved decisions. Preserve supplied requirements and distinguish them from proposed targets. Ask for missing information when it changes the next decision; otherwise state a provisional assumption and continue useful work.

Use [assets/design-record.md](assets/design-record.md) as a compact working record. Populate only the parts useful to this project. Retain stable identifiers for needs, requirements, concepts, evidence, and decisions when tracing them becomes valuable.

## Choose the next method

Identify the most consequential uncertainty or decision. Select a method because of the artifact or evidence it will produce, and explain that choice briefly.

| Current need | Candidate method | Expected result |
|---|---|---|
| Clarify what should change and for whom | Problem framing; stakeholder and needs analysis | Bounded brief and needs |
| Understand existing solutions and performance gaps | Technical benchmarking; teardown | Comparable evidence and opportunities |
| Make success measurable | Requirements and specifications; QFD | Targets, constraints, and verification criteria |
| Understand what the system must do | Functional modeling; architecture and interfaces | Functions, flows, dependencies |
| Explore ways to achieve those functions | Morphological synthesis; analogy; TRIZ; heuristics | Distinct, coherent concepts |
| Compare alternatives | Concept screening; trade study | Evidence-based comparison and decision rationale |
| Express a design decision mathematically | Design optimization formulation | Variables, objectives, constraints, and analysis models |
| Explore a defined model | Optimization and exploration; robust design | Tradeoffs, sensitivity, and candidate designs |
| Resolve an empirical uncertainty | Prototyping and experimental planning | A test tied to a decision |
| Refine implementation and life-cycle performance | Failure analysis; DFMA; value and sustainable design | Specific design changes and their tradeoffs |

This repository initially includes `technical-benchmarking`, `morphological-synthesis`, and `design-optimization-formulation`. Other methods in this table are roadmap ideas. Use an installed method skill when available. When a named skill is unavailable, explain the method directly or recommend it as the next activity; do not claim to invoke a missing capability. The process skill remains usable independently.

## Run a bounded iteration

1. State the decision and the evidence needed to make it.
2. Apply the chosen method with the available inputs and tools.
3. Review the artifact for internal consistency, evidence gaps, and implications for other design choices.
4. Update the design record: what changed, why, remaining uncertainty, and next action.

Allow new findings to revise the framing, requirements, or concept set. Multiple activities may proceed concurrently when their dependencies allow it. Preserve alternatives until there is a reason to eliminate them. Scale documentation to the decision rather than forcing every project through every method.

## Quality checks and handoff

- Trace a recommendation to stakeholder value, a requirement, or an explicit hypothesis.
- Keep observed facts, assumed values, calculations, and proposed concepts distinguishable.
- Recognize when the missing input is a measurement, user preference, or external decision rather than more analysis.
- Record the basis for discarding a concept or revising a requirement.
- End with an actionable next step, its intended learning or decision, and what would justify changing direction.

For an illustration, read [references/worked-example.md](references/worked-example.md). Method foundations: [MIT Product Design and Development](https://ocw.mit.edu/courses/15-783j-product-design-and-development-spring-2006/pages/lecture-notes/) and [NASA System Design Processes](https://www.nasa.gov/reference/4-0-system-design-processes/). The workflow here is an original synthesis, not a reproduction of either source.

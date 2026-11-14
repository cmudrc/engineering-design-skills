---
name: engineering-design-process
description: Guide physical-product and engineering-system development through Ulrich and Eppinger’s phases 0–5. Use to establish the current development state, choose methods, plan phase outputs, or decide what to investigate next.
license: MIT
metadata:
  phase-framework: ulrich-eppinger-6e
  phases: "0,1,2,3,4,5"
---

# Engineering Design Process

Use Ulrich and Eppinger’s six-phase framework to connect the current engineering decision to the next useful artifact. Match the process to the project rather than imposing a fixed sequence of activities.

## Establish the development state

Start with the user's language and existing work. Identify the intended users, opportunity, system boundary, desired outcome, available evidence, and unresolved decision. A vague request is a useful starting point: ask the question that most affects the next decision, and develop the brief progressively. Preserve the distinction between user requirements, preferences, and proposed assumptions.

Identify the phase from the state of the product and its evidence. If different workstreams occupy different phases, record those separately. Using a method associated with a phase is not evidence that the phase is complete.

| Phase | Decision focus | Typical output |
|---|---|---|
| 0: Planning | Which opportunity and development mission should the team pursue? | Mission statement, intended users, business goals, assumptions, and constraints. |
| 1: Concept Development | What should the product do, and which concept should be developed? | Needs, specifications, evaluated concepts, concept-test evidence, and downstream plan. |
| 2: System-Level Design | How should functions be allocated to subsystems and interfaces? | Architecture, layout, subsystem requirements, and preliminary production/assembly plan. |
| 3: Detail Design | What exactly will be built, purchased, and manufactured? | Geometry, materials, tolerances, component specifications, and process documentation. |
| 4: Testing and Refinement | Does the developed product work in its intended use, and what must change? | Product-test evidence, resolved changes, and readiness assessment. |
| 5: Production Ramp-Up | Can the intended production system consistently produce the product? | Evaluated early output, operator preparation, resolved production issues, and launch readiness. |

Use [assets/design-record.md](assets/design-record.md) for the working record. Read [references/phases.md](references/phases.md) for phase boundaries, typical handoffs, and cross-phase interpretation.

## Choose methods with many-to-many membership

Select a method because of the decision and artifact it supports. The same skill can be useful in several phases. Adapt its inputs, model fidelity, and quality checks to the current phase.

- **Phase 0:** opportunity identification, product planning, problem framing, needs research, and benchmarking support a bounded mission.
- **Phase 1:** needs and specifications, benchmarking, functional modeling, morphological synthesis, analogy, TRIZ, screening, selection, and concept testing support concept development. Cycle between these activities as evidence changes.
- **Phase 2:** architecture and interfaces, subsystem functional modeling, morphological synthesis, trade studies, optimization formulation, DFMA, and integration prototypes support allocation and integration choices.
- **Phase 3:** optimization, robust design and tolerances, failure analysis, DFMA, and cost or environmental assessment support buildable detail decisions.
- **Phase 4:** prototyping and experiments, benchmarking, failure analysis, robust design, and model revision support product testing and refinement.
- **Phase 5:** production ramp-up, DFMA, quality and failure investigations, variation assessment, and early-production evaluation support production readiness.

Available method skills are `product-planning`, `technical-benchmarking`, `morphological-synthesis`, `design-optimization-formulation`, `design-for-manufacture-assembly`, `prototyping-experimental-planning`, and `production-ramp-up`. Other methods listed above remain planned. Use an available method skill when present; otherwise explain the method directly or recommend it as the next activity without claiming to invoke a missing capability. This process skill is independently usable.

## Run a bounded iteration and review the handoff

1. State the current phase or workstream, decision, and consequential uncertainty.
2. Choose a method and say what artifact or evidence it should produce.
3. Apply it, distinguishing observations, assumptions, calculations, and hypotheses.
4. Review implications for the current phase output and earlier decisions.
5. Record what changed, the next action, and what would justify advancing or revisiting a phase.

Keep alternatives open until evidence supports narrowing them. An early feasibility mockup can belong in Phase 1; Phase 4 concerns evaluation of developed product versions. An optimization formulation can support concept or system-level choices before detailed geometry exists. Phase 5 requires evidence from the intended production system, not merely a successful prototype.

For an illustration, read [references/worked-example.md](references/worked-example.md). Framework: Karl T. Ulrich and Steven D. Eppinger, *Product Design and Development*, 6th edition (2016), Chapter 2, pp. 13–16, Exhibits 2-2 and 2-3. The summaries and skill-routing choices here are original adaptations.

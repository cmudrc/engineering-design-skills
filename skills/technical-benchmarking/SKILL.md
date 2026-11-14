---
name: technical-benchmarking
description: Benchmark existing engineering products, mechanisms, or systems using comparable performance metrics and traceable evidence. Use to assess the state of the art, compare reference solutions, identify performance gaps, or inform design targets.
license: MIT
metadata:
  phase-framework: ulrich-eppinger-6e
  phases: "0,1,2,4"
---

# Technical Benchmarking

Compare existing solutions to answer a specific engineering design question. Make the conditions and limits of each comparison visible.

## Inputs and scope

Identify the function, operating context, reference solutions, and decision the comparison should inform. Start from supplied sources; obtain current specifications or test reports when needed and tools permit. Useful evidence includes measurements, manufacturer data, published tests, drawings, and observed mechanisms. Record a source identifier and a date or revision for each source.

Use [assets/benchmark-matrix.md](assets/benchmark-matrix.md) for the artifact and [references/worked-example.md](references/worked-example.md) for a synthetic example with incompatible claims.

## Procedure

1. **Define metrics before ranking.** Specify units, direction of preference, functional basis, measurement boundary, and relevant operating conditions. Separate hard requirements from preferences. Include contextual dimensions that affect interpretation, such as payload, scale, service life, or included components.
2. **Select references deliberately.** Include the current baseline and relevant alternatives, including a different physical principle when useful. Explain inclusion criteria and any scope limits. Avoid claiming exhaustive state-of-the-art coverage from a small sample.
3. **Extract evidence with provenance.** Associate every reported value with a source and its conditions. Distinguish measured performance, supplier claims, calculated estimates, and missing information. Keep ranges and uncertainty when provided. Do not substitute a plausible number for missing data.
4. **Assess comparability per metric.** Align units and definitions. Classify comparisons as directly comparable, comparable under an explicit adjustment model, or not yet comparable. Show the adjustment and its assumptions. A ratio or per-unit metric is useful only when its scaling assumptions make engineering sense.
5. **Identify gaps and tradeoffs.** Compare supported metrics against the baseline or requirements. Show which solutions are dominated only within the comparable criteria and evidence. Avoid an overall ranking unless stakeholder preferences and adequate data support it. Missing values cannot improve a score.
6. **Translate findings into design opportunities.** Connect a performance gap to a possible mechanism, architecture, or test. Mark explanations inferred from limited evidence as hypotheses. Treat the best observed value as evidence about existing solutions, not a universal feasibility limit.

## Output and checks

Deliver the comparison question, reference set, metric definitions, source register, benchmark matrix, comparability notes, supported findings, and the next information needed. Proposed targets should retain their rationale and any feasibility uncertainty.

Before finalizing, check that:

- Units, functional basis, and test conditions match for every numerical comparison.
- Claimed superiority is limited to supported criteria and conditions.
- Missing evidence remains visible; calculated values retain their model and inputs.
- Facts about an existing product are separate from hypotheses about its mechanism.
- The result informs a design decision or a concrete measurement plan.

This skill addresses engineering solution benchmarking. Evaluation of agent performance requires a separately designed study.

Method context: [MIT Product Design and Development](https://ocw.mit.edu/courses/15-783j-product-design-and-development-spring-2006/pages/lecture-notes/) and [NASA Decision Analysis](https://www.nasa.gov/reference/6-8-decision-analysis/). These sources support the broader comparison and decision context; the evidence protocol here is an original implementation.

## Phase context

Use in Phase 0 (Planning) to compare opportunity baselines, Phase 1 (Concept Development) to establish competitive targets, Phase 2 (System-Level Design) to compare architectures or subsystems, and Phase 4 (Testing and Refinement) to compare developed performance. Adapt the comparison question and evidence maturity to the phase. The phase framework is Ulrich and Eppinger, *Product Design and Development*, 6th edition (2016), Chapter 2.

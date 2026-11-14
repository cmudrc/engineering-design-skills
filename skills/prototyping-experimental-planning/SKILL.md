---
name: prototyping-experimental-planning
description: Plan a prototype or experiment around an engineering decision, including its purpose, fidelity, controls, measurements, and interpretation. Use to resolve design uncertainty or plan product testing across Phases 1–5.
license: MIT
metadata:
  phase-framework: ulrich-eppinger-6e
  phases: "1,2,3,4,5"
---

# Prototyping and Experimental Planning

Choose the prototype and experiment that can resolve a consequential question. Connect each build and measurement to a decision before committing to the effort.

## Establish the purpose and development state

Ask what the team would do differently after the result. Identify whether the prototype supports learning, communication, integration, or a development milestone. Clarify the current design revision, relevant requirements, available models or observations, and the intended use conditions.

Use [assets/prototype-test-plan.md](assets/prototype-test-plan.md) for the plan and [references/worked-example.md](references/worked-example.md) for an example in which one failed unit remains important evidence.

## Plan the prototype and experiment

1. **Define the question and decision.** Write the hypothesis or comparison, what result would matter, and how it affects a concept, parameter, model, or readiness decision. Separate exploratory learning from a claim that a requirement is satisfied.
2. **Choose sufficient fidelity.** Consider analytical or physical prototypes and focused or integrated representations. Identify which geometry, material, interfaces, loads, environment, and production features must be represented for the question to be meaningful. Record deliberate approximations and their limits. An easy-to-build mockup is useful only if it preserves the relevant behavior.
3. **Define factors and controls.** Choose the variables to change and conditions to hold constant. Identify plausible confounding, nuisance variation, and measurement error. Use randomization, blocking, paired comparisons, or a structured experimental design where they answer the question. Distinguish repeated measurements, repeated runs, and independent units.
4. **Specify protocol and measurements.** Define units, instrumentation, sensor placement, calibration or reference checks, sampling, specimen preparation, operating sequence, and treatment of failed or incomplete runs. Identify the experimental unit and which raw records must be retained. State acceptance criteria before interpreting results.
5. **Plan analysis and its limits.** Match the analysis to the data and decision. Choose sample size from the intended claim, variability, resources, and any applicable requirements. If these are unknown, propose a bounded exploratory study with explicit limits; do not invent a confidence level or interpret a few successes as demonstrated reliability.
6. **Integrate execution and learning.** Identify procurement, construction, integration, testing, and analysis dependencies. Use actual timing constraints where supplied. Keep planned work separate from completed work. After results arrive, retain anomalies and failed units, update hypotheses, and identify the next discriminating test or design change.

## Quality checks and handoff

- Trace each measurement and build feature to the question it supports.
- Check that the test environment and measurement boundary represent the claim being made.
- Do not confound design revision, operator, test order, and specimen identity without recording the limitation.
- Do not select only passing samples or reinterpret a failed criterion after seeing the result.
- Distinguish an observation, a proposed explanation, and a demonstrated cause.
- Report missing or invalid data and unresolved uncertainty alongside the recommendation.

Phase context: exploratory concept tests can occur in **Phase 1**, interface/integration learning in **Phase 2**, parameter and component checks in **Phase 3**, developed-product evaluation in **Phase 4**, and pilot-process evaluation in **Phase 5**. Prototype fidelity and evidence determine the useful interpretation; the presence of a physical prototype alone does not establish a phase.

Reference: Ulrich and Eppinger, *Product Design and Development*, 6th edition (2016), Chapter 14, especially the prototype-planning method on pp. 305–307; Chapter 15 for structured experiments. The instructions and example here are original adaptations.

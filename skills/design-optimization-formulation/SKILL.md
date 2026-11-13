---
name: design-optimization-formulation
description: Formulate an engineering design decision as an optimization problem with explicit variables, objectives, constraints, analysis models, and uncertainty. Use before choosing a solver, when translating a design brief into mathematics, or when auditing whether an optimization model represents the intended design problem.
license: MIT
---

# Design Optimization Formulation

Translate engineering intent into a mathematical problem whose meaning, assumptions, and evaluation procedure can be inspected. Numerical search is a subsequent activity.

Use [assets/formulation.md](assets/formulation.md) as the output structure and [references/worked-example.md](references/worked-example.md) for a complete cantilever example with feasible and infeasible trial designs.

## Establish the decision

Identify the system boundary, operating scenarios, stakeholder outcomes, and decisions the designer can change. Separate fixed requirements from provisional preferences. Clarify which architecture is represented by the model and which alternatives it excludes. If an important design choice cannot be represented by the proposed variables, revise the formulation or preserve it as an outer architecture decision.

## Build the formulation

1. **Define variables and parameters.** For each design variable, give its symbol, engineering meaning, units, type, domain, and bounds with rationale. Separate designer-controlled variables `x`, fixed parameters `p`, uncertain inputs `u`, and model states `y`. For discrete choices, specify permitted values and any conditional variables.
2. **Define objectives from outcomes.** Write each objective, its direction, units, and model dependence. Explain why it measures the intended outcome and identify weak proxies. Preserve multiple objectives when preferences are unresolved. If scalarizing, state normalization, weights, and preference rationale; avoid adding quantities with incompatible units.
3. **Define constraints from requirements and physics.** Give each inequality or equality a clear sign convention, units or normalization, applicable scenarios, and source. Distinguish physical/model equations, hard requirements, bounds, and preferences. Avoid optimizing a requirement that must instead be satisfied.
4. **Specify the analysis model.** Map variables and parameters to states, objective values, and constraint values. State equations, required simulations or data, couplings, validity limits, expected failures, and available checks. A simulation failure is not a zero-cost or feasible design.
5. **Handle uncertainty explicitly.** Identify which inputs vary or are poorly known. State whether this is a deterministic baseline, a scenario formulation, a robust formulation, or a probabilistic one. Name the uncertainty set or distribution and its evidence when used. Do not invent distributions or present a mean-case result as robust.
6. **State the problem compactly.** Express minimize/maximize objectives subject to inequalities, equalities, variable domains, and any state equations. Choose useful reference scales. Classify properties relevant to a later solution strategy, such as continuous/discrete variables, smoothness, simulation cost, and coupled disciplines, only as supported by the model.

## Check the model before handoff

- Trace objectives and constraints to the brief and identify unrepresented requirements.
- Check dimensions, signs, bounds, denominators, and model-validity conditions.
- Evaluate a plausible trial design when executable models are available, showing objective and constraint residuals. Include a deliberately violating case when it clarifies constraint meaning.
- If the model is incomplete or cannot be evaluated, identify the exact missing relationship or evidence. Preserve a useful symbolic formulation without claiming numerical readiness.
- Distinguish a feasible trial point from an optimum. A failure to find feasibility does not prove the mathematical problem is infeasible.
- Check for an unbounded or trivial objective, redundant or conflicting constraints, and variables that do not affect the model.

Deliver the formulation, symbol tables, analysis dependencies, trial-point results or precise evaluation gaps, assumptions, and unresolved preference choices. State the next step required for numerical exploration without silently running a costly search.

Reference: Martins and Ning, [Engineering Design Optimization](https://mdobook.github.io/), especially constrained, discrete, multiobjective, and uncertainty formulations. The engineering example and instructions here are original.

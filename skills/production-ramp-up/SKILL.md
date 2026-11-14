---
name: production-ramp-up
description: Plan or assess early output from an intended production system using traceable process, quality, training, and readiness evidence. Use in Phase 5 when reviewing pilot lots, increasing production rate, or resolving remaining production problems.
license: MIT
metadata:
  phase-framework: ulrich-eppinger-6e
  phases: "5"
---

# Production Ramp-Up

Connect a proposed increase in production to evidence from the process that will actually make the product. Assess product conformance and production readiness separately.

## Establish the intended process and decision

Identify the product and process revisions, materials, suppliers, tooling, fixtures, operators, assembly route, inspection methods, and proposed ramp step. Ask which of these match the intended production system and which are temporary. Workshop prototypes can inform readiness but do not demonstrate the behavior of a different production line.

Clarify the decision: a small pilot, another learning run, an increase in rate or quantity, or broader release. Record actual criteria, authority, customer commitments, and constraints when supplied; distinguish proposed criteria from established ones.

Use [assets/ramp-up-review.md](assets/ramp-up-review.md) for the record and [references/worked-example.md](references/worked-example.md) for an example separating first-pass yield from final conformance.

## Plan and assess the ramp

1. **Define the next bounded production step.** State what it should demonstrate, its intended conditions, and the evidence required before another increase. Identify remaining differences from the intended process and their consequences.
2. **Establish standard work and measurement.** Check that operators can execute the current work instructions with the actual tools, materials, and inspection methods. Identify training and measurement-system gaps. Track relevant part, supplier, process, fixture, and instruction revisions.
3. **Define lot accounting and metrics.** State the lot boundary and denominator. Distinguish first-pass conforming output, units sent to rework, successful rework, scrap, and held/unknown units. Rework events and final unit dispositions are different counts. Report time, rate, and labor effort only when their measurement boundaries are known.
4. **Investigate losses and variability.** Relate defects, rework, cycle-time variation, and bottlenecks to station, unit, operator, shift, material, and process conditions where evidence permits. Separate defect events from defective units. Prioritize corrective investigations without claiming a cause from a small count alone.
5. **Verify changes on the intended process.** Document the changed revision, operator preparation, validation task, and resulting quality and flow evidence. Check whether fixing one issue creates another. Keep unresolved holds, temporary workarounds, and additional labor visible.
6. **Review readiness and the next step.** Compare evidence with the actual readiness criteria and intended production demand. Recommend proceeding, holding, or a limited next run with specific learning objectives. Record the owner's decision separately. Revisit earlier design phases when the process exposes a design problem.

## Quality checks

- Reconcile unit counts before calculating yield. Define first-pass yield as first-pass conforming units divided by the relevant entered units; define any final-conformance ratio separately.
- Do not infer throughput or capacity without elapsed time, staffing, and process-boundary information.
- Do not derive process-capability indices or reliability claims from a yield percentage alone. Capability analysis needs appropriate measurement data, specifications, and evidence about process behavior.
- Preserve traceability and disposition of nonconforming or held units; later rework does not erase the initial failure.
- Avoid universal readiness thresholds. Use the project's criteria and explain what the available evidence can support.

Phase context: **5, Production Ramp-Up**. Coordinate with manufacturing/assembly, experimental planning, failure analysis, and robust-design methods when they are available. The skill remains usable independently. Reference: Ulrich and Eppinger, *Product Design and Development*, 6th edition (2016), Chapter 2, Phase 5 discussion, p. 16, and Chapter 14's preproduction-prototype discussion, p. 307. The operating review and example here are original adaptations.

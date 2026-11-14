---
name: design-for-manufacture-assembly
description: Review a physical product for manufacturing and assembly improvements tied to its processes, volume, and functional requirements. Use to examine part count, assembly operations, process feasibility, cost drivers, or production difficulties in Phases 2–5.
license: MIT
metadata:
  phase-framework: ulrich-eppinger-6e
  phases: "2,3,4,5"
---

# Design for Manufacture and Assembly

Connect a proposed design change to a specific fabrication or assembly difficulty, then assess its effects on cost, performance, service, and production. Use the evidence available at the current design maturity.

## Establish the production basis

Identify the design revision, intended function, geometry and materials available, candidate processes, production quantity or range, assembly sequence, and evidence of actual problems. Distinguish a design review based on drawings from one supported by observations of production. Obtain capability or supplier evidence for consequential process limits; treat unsupported rules of thumb as screening guidance.

Use [assets/dfma-review.md](assets/dfma-review.md) for the artifact. [references/worked-example.md](references/worked-example.md) illustrates an apparently attractive fastener change with unresolved sealing risk.

## Review and improve

1. **Map the product and operations.** Relate parts to functions, interfaces, assembly order, access, tools, handling, orientation, joining, inspection, and rework. Identify where components must move independently, use different materials, or remain separate for assembly, replacement, or service.
2. **Establish the cost or effort baseline.** Use a bill of materials and observed operations when available. State quantity, cost boundary, currency/price basis, labor-rate meaning, scrap/rework assumptions, and fixed versus recurring costs. Keep measured time separate from an estimated future cycle.
3. **Examine manufacturing choices.** Review material-process compatibility, geometry, features, tolerance demands, setup and tooling, and inspection access. Tie recommendations to actual capabilities or identified evidence gaps. Check purchased-component alternatives and the effects of production volume.
4. **Examine assembly choices.** Consider handling and insertion, access, orientation, fastening, alignment, mistake prevention, and the number of operations. Evaluate consolidation and standardization while preserving needed motion, material distinctions, service access, and load paths. Fewer parts alone do not demonstrate a better assembly.
5. **Compare complete alternatives.** Show the mechanism for each expected improvement and its consequences for performance, reliability, maintenance, environmental impact, suppliers, and production support. Include new tooling, validation, training, or rework costs where relevant. If using a break-even quantity, state the assumptions and keep it separate from a demand forecast.
6. **Define validation and handoff.** Identify the drawing or process change proposed, the test or observation needed, and the condition for retaining it. Use revision control and traceability when changes affect an existing build. Update work instructions and quality checks only after the corresponding change is established.

## Quality checks

- Preserve function and relevant interfaces while simplifying the product.
- Do not infer material grade, process capability, tolerances, supplier quotes, or observed production time from appearance alone.
- Do not count the same savings twice or mix total cost and unit cost. Report modeled savings as estimates until the changed design and process are tested.
- If calculating an assembly-efficiency index, identify its definitions and source data; do not invent reference handling times or treat a part-count estimate as a validated optimum.
- State exactly which fit, load, sealing, service, or process risks remain unresolved.

Phase context: **2** for architecture and assembly allocation, **3** for geometry and process details, **4** for validating changes, and **5** for resolving early-production difficulties. Reference: Ulrich and Eppinger, *Product Design and Development*, 6th edition (2016), Chapter 13. The review structure and example here are original adaptations.

# Skill catalog

The library uses Ulrich and Eppinger’s six product-development phases. Skills have many-to-many membership: a method can support several phases, with a different decision and evidence standard in each. Membership is guidance rather than a restriction.

`catalog.json` is the source of truth. Regenerate this reference with `python3 scripts/catalog.py`.

## Phase framework

| Phase | Focus | Typical output |
|---|---|---|
| 0: Planning | Define the opportunity and the project mission before committing to development. | Mission statement, target users, business goals, assumptions, and constraints. |
| 1: Concept Development | Understand needs, develop specifications, and generate, select, and test product concepts. | Selected concept, supporting evidence, specifications, and a downstream development plan. |
| 2: System-Level Design | Define the architecture, subsystems, interfaces, and initial production and assembly approach. | System layout, subsystem requirements, interface definitions, and preliminary assembly plan. |
| 3: Detail Design | Specify parts, materials, geometry, tolerances, purchased components, and production processes. | Buildable design definition, drawings or models, component specifications, and process documentation. |
| 4: Testing and Refinement | Evaluate developed product versions against intended performance and use, then resolve needed changes. | Test evidence, resolved design changes, and confidence in product and process readiness. |
| 5: Production Ramp-Up | Use the intended production system, train operators, and resolve problems found in early output. | Evaluated early production, stabilized operations, and launch-readiness evidence. |

## Draft implementations

| Skill | Phases |
|---|---|
| [Engineering design process](../skills/engineering-design-process/SKILL.md) | 0, 1, 2, 3, 4, 5 |
| [Technical benchmarking](../skills/technical-benchmarking/SKILL.md) | 0, 1, 2, 4 |
| [Morphological synthesis](../skills/morphological-synthesis/SKILL.md) | 1, 2 |
| [Design optimization formulation](../skills/design-optimization-formulation/SKILL.md) | 1, 2, 3, 4 |
| [Prototyping and experimental planning](../skills/prototyping-experimental-planning/SKILL.md) | 1, 2, 3, 4, 5 |
| [Design for manufacture and assembly](../skills/design-for-manufacture-assembly/SKILL.md) | 2, 3, 4, 5 |
| [Product planning](../skills/product-planning/SKILL.md) | 0 |
| [Production ramp-up](../skills/production-ramp-up/SKILL.md) | 5 |

## Planned methods

| Skill | Phases | Implementation issue |
|---|---|---|
| Problem framing and reframing | 0, 1 | [#1](https://github.com/cmudrc/engineering-design-skills/issues/1) |
| Stakeholder and needs analysis | 0, 1, 4 | [#2](https://github.com/cmudrc/engineering-design-skills/issues/2) |
| Product teardown and reverse engineering | 0, 1, 2 | [#3](https://github.com/cmudrc/engineering-design-skills/issues/3) |
| Requirements and specifications | 1, 2, 3, 4 | [#4](https://github.com/cmudrc/engineering-design-skills/issues/4) |
| Quality function deployment | 1, 2 | [#5](https://github.com/cmudrc/engineering-design-skills/issues/5) |
| Functional modeling and decomposition | 1, 2 | [#6](https://github.com/cmudrc/engineering-design-skills/issues/6) |
| Product architecture and interfaces | 1, 2 | [#7](https://github.com/cmudrc/engineering-design-skills/issues/7) |
| Design by analogy | 0, 1, 2 | [#8](https://github.com/cmudrc/engineering-design-skills/issues/8) |
| TRIZ and contradiction resolution | 1, 2, 3, 4 | [#9](https://github.com/cmudrc/engineering-design-skills/issues/9) |
| Heuristic concept generation | 1, 2, 3 | [#10](https://github.com/cmudrc/engineering-design-skills/issues/10) |
| Concept screening | 1, 2 | [#11](https://github.com/cmudrc/engineering-design-skills/issues/11) |
| Concept evaluation and trade studies | 0, 1, 2, 3, 4 | [#12](https://github.com/cmudrc/engineering-design-skills/issues/12) |
| Design optimization and exploration | 1, 2, 3, 4 | [#13](https://github.com/cmudrc/engineering-design-skills/issues/13) |
| Robust design and tolerance allocation | 1, 2, 3, 4, 5 | [#14](https://github.com/cmudrc/engineering-design-skills/issues/14) |
| Failure modes and design risk analysis | 1, 2, 3, 4, 5 | [#16](https://github.com/cmudrc/engineering-design-skills/issues/16) |
| Cost and value engineering | 0, 1, 2, 3, 4, 5 | [#18](https://github.com/cmudrc/engineering-design-skills/issues/18) |
| Sustainable and life-cycle design | 0, 1, 2, 3, 4, 5 | [#19](https://github.com/cmudrc/engineering-design-skills/issues/19) |
| C–K design exploration | 0, 1, 2 | [#20](https://github.com/cmudrc/engineering-design-skills/issues/20) |
| Axiomatic design | 1, 2, 3 | [#21](https://github.com/cmudrc/engineering-design-skills/issues/21) |
| Set-based design | 1, 2, 3 | [#22](https://github.com/cmudrc/engineering-design-skills/issues/22) |
| Human-factors methods for engineering design | 1, 2, 3, 4, 5 | [#23](https://github.com/cmudrc/engineering-design-skills/issues/23) |
| Opportunity identification | 0 | [#24](https://github.com/cmudrc/engineering-design-skills/issues/24) |
| Concept testing | 1 | [#26](https://github.com/cmudrc/engineering-design-skills/issues/26) |

## Interpreting the phases

Concept testing belongs in Phase 1. Phase 4 evaluates more developed product versions; prototyping, benchmarking, and other methods can still be used earlier. A small prototype or an optimization model does not by itself establish that a project has reached a later phase.

The process skill spans all phases. Draft methods now support planning through production ramp-up. Cross-phase methods adapt to the decision and evidence available; their membership does not imply that every activity is appropriate at every development state.

## Source

Karl T. Ulrich and Steven D. Eppinger (2016), *Product Design and Development*, 6th edition, McGraw-Hill Education. Chapter 2, pp. 13–16, Exhibits 2-2 and 2-3; Exhibit 1-4, p. 9. Phase names follow this framework. The summaries and individual agent-skill memberships are this library’s interpretation.

# Engineering Design Skills

An open library of agent skills for engineering design, maintained by the [Design Research Collective](https://github.com/cmudrc) at Carnegie Mellon University.

Engineering design involves choosing what problem to solve, generating alternatives, comparing evidence, and deciding what to learn next. This library packages those methods as reusable instructions with explicit inputs, engineering artifacts, and quality checks.

**Status: initial scaffold.** Four draft skills establish the structure. The remaining methods are tracked as GitHub issues and mapped to phases 0–5 of Ulrich and Eppinger’s product-development process. The drafts include worked examples and structural checks; their effects on agent performance have not been evaluated.

**[Explore the demos on GitHub Pages](https://cmudrc.github.io/engineering-design-skills/)**. Each skill shows its complete example conversation in a scrollable chat window alongside the current instructions, output template, and worked example.

## Process framework

The library follows Ulrich and Eppinger’s six phases: **0 Planning, 1 Concept Development, 2 System-Level Design, 3 Detail Design, 4 Testing and Refinement, and 5 Production Ramp-Up**. Skills have many-to-many membership. The same method may support different decisions in several phases; using it does not by itself establish phase completion.

`catalog.json` is the source of truth for phases, implemented skills, and planned methods. The [generated catalog](docs/skill-catalog.md) provides the complete mapping and attribution. The overall process skill spans all six phases; the current method implementations emphasize concept and analytical design.

## Starter skills

| Skill | Role | Output |
|---|---|---|
| [Engineering design process](skills/engineering-design-process/SKILL.md) | Guide an iterative design project and choose appropriate methods. | Design brief, current design state, method rationale, and next action. |
| [Technical benchmarking](skills/technical-benchmarking/SKILL.md) | Compare existing engineering solutions using traceable, comparable evidence. | Benchmark matrix, comparability assessment, performance gaps, and opportunities. |
| [Morphological synthesis](skills/morphological-synthesis/SKILL.md) | Combine solution principles for required functions into coherent concepts. | Morphological chart, compatibility assessment, and concept descriptions. |
| [Design optimization formulation](skills/design-optimization-formulation/SKILL.md) | Translate an engineering decision into an explicit optimization problem. | Variables, objectives, constraints, models, assumptions, and formulation checks. |

The process skill provides a top-level entry point. Each method skill also works independently. Optimization formulation covers the reasoning and model definition that precede numerical search; a separate optimization and exploration skill is planned.

## Use

The skills follow the [Agent Skills format](https://agentskills.io/specification). Each directory under `skills/` contains a `SKILL.md` entry point, an output template in `assets/`, and a worked example in `references/`. The skill content is platform neutral; each host supplies its own installation, presentation, and invocation settings. No engineering solver, API key, or proprietary application is required for the starter workflows.

For a first inspection, open a skill's `SKILL.md` and follow its instructions in your agent environment. For an environment that discovers skills from a local skills directory, copy the **complete skill directory**, including its `assets/` and `references/`, to that location. Discovery and invocation syntax depend on the host. The method skills do not require their siblings to be installed.

Example requests:

- “Help me plan the next step in designing a manually operated lifting device.”
- “Benchmark these three existing mechanisms and identify what the data actually support.”
- “Build a morphological chart for a portable rain shelter.”
- “Frame this cantilever design problem as an optimization problem before choosing a solver.”

## Scope and development

The focus is physical products and engineered systems, including mechatronics. Methods cover problem definition, synthesis, evaluation, and refinement. Domain-specific CAD and simulation tools can support those methods as needed.

See the [skill catalog](docs/skill-catalog.md) for the complete roadmap and issue links, and [CONTRIBUTING.md](CONTRIBUTING.md) for the common skill contract. Worked examples use explicitly synthetic data. Evidence, assumptions, derived results, and open questions remain distinguishable in every artifact.

## Validate

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_skills.py
python3 scripts/catalog.py --check
```

The validator checks skill frontmatter and local resource links, and rejects host-specific `agents/` configuration inside skill directories. Behavioral evaluation cases are described in [evals/README.md](evals/README.md); they require an actual agent run and are not implied by structural validation.

## Website

The GitHub Pages site is built from `catalog.json`, `site/demos.json`, and `site/style.css`. Each skill page has a complete scrollable example chat, links to its original instructions and worked example, and a downloadable template. The build also copies the portable skill resources as downloads. Demo conversations are authored illustrations with synthetic inputs, not live model calls or controlled agent evaluations.

```bash
python3 scripts/build_site.py --base-path /engineering-design-skills
python3 scripts/check_site.py
```

The generated `_site/` directory is ignored by Git. To preview it locally, serve it at the matching `/engineering-design-skills/` prefix, or build and check with `--base-path ''` for a server rooted directly in `_site/`. Every demo shows the complete conversation in a scrollable chat window, with all exchanges visible from the start.

The Pages workflow builds and checks every pull request, and deploys successful builds from `main`. Update a skill's Markdown to update its documentation on the site; edit `site/demos.json` to change a curated interaction. Add one demo entry and catalog membership when introducing a new skill. Start demos from natural, incomplete human requests and show the agent developing the method’s inputs and artifacts. Regenerate catalog documentation with `python3 scripts/catalog.py` after editing `catalog.json`.

## License

[MIT](LICENSE). External method references retain their original terms. This repository contains original instructions and examples; linked publications and commercial method materials are not redistributed.

# Contributing

Choose a method from the [catalog](docs/skill-catalog.md) or propose one with a distinct engineering purpose and output. A skill should improve a specific design decision or reasoning activity.

## Common skill contract

Each skill should specify:

1. **Trigger and scope:** when the method is useful and the decision it supports.
2. **Inputs:** the minimum useful starting information and how to handle gaps.
3. **Procedure:** the reasoning steps and method-specific choices that matter.
4. **Output:** a reviewable engineering artifact, with a reusable template where useful.
5. **Quality checks:** likely method failures, assumptions, and checks on the artifact.
6. **Continuation:** what the result enables and which uncertainty should be addressed next.

Keep the entry point short and directly link resources. Use lowercase hyphenated directory names that match the frontmatter `name`. Include `name`, `description`, and `license: MIT` in the YAML frontmatter.

Keep skill directories platform neutral. Define discovery names and descriptions in `SKILL.md`; keep host-specific presentation and invocation configuration outside the distributed skills. The validator rejects `agents/` configuration inside skill directories.

## Evidence and examples

Use primary method references and write original instructions. Link to external sources rather than copying protected card decks, standards, or textbook passages. Identify the provenance and conditions of engineering data. Treat missing data as unknown, and describe the assumptions behind any derived quantity.

Provide a worked example that shows both the method and its limits. Synthetic examples are welcome when clearly labeled. Include a case that exposes a likely failure, such as an incomparable benchmark, incompatible solution combination, or mathematically incomplete formulation.

## Review and validation

Run:

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_skills.py
```

Check example arithmetic separately. For behavioral evaluation, give an agent the skill and raw task inputs, withhold the intended result, and assess its artifact using the checks in `evals/README.md`. Record the host, model, date, available tools, and observed limitations. Do not describe structural validation as behavioral evaluation.

Update the catalog and link the issue in the change description. Small, coherent method contributions are easier to assess than a large set of partially specified methods.

## Demo website

Every implemented skill has one entry in `site/demos.json`. Provide a short, curated interaction that demonstrates the method's artifact and at least one consequential quality check. Label illustrative data and avoid presenting authored responses as live model output or measured agent performance.

Link instructions and worked examples to their existing source files, and copy templates from the skill directories. Keep source materials in those files rather than duplicating them in the site content. Run `python3 scripts/build_site.py` and `python3 scripts/check_site.py` after changing the site or adding a skill. Display the complete conversation in a scrollable, keyboard-accessible chat window. Keep examples readable without step-through controls or a model explorer.

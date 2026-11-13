# Working in this repository

This is a library of engineering design methods in the open Agent Skills format. Keep the scope on physical products and engineered systems, including mechatronics.

- Keep skill directories platform neutral. Define names and discovery descriptions in `SKILL.md`, and keep host-specific presentation and invocation configuration outside the distributed skills. Do not add `agents/` directories.
- Keep every skill self-contained. Its essential resources must live inside its directory; other skills and external tools are optional unless a concrete method requires them.
- Keep `SKILL.md` concise. Put output templates in `assets/` and substantial examples in `references/`, with explicit links from the entry point.
- Preserve the separation between design optimization formulation and numerical optimization.
- Preserve evidence provenance and distinguish measurements, literature claims, calculations, assumptions, and hypotheses. Label synthetic data explicitly.
- Treat the top-level process as iterative and adaptable. Track decisions and uncertainty without imposing a universal stage-gate sequence.
- Document draft status honestly. A valid directory structure does not establish engineering validity or improved agent performance.
- Do not install skills into a user's global environment as part of repository editing unless explicitly requested.
- When adding a method, update the catalog and its corresponding issue. Do not add empty skill directories for planned work.
- Run `python3 scripts/validate_skills.py` after changing skills. Check engineering calculations independently when examples change. Use the cases in `evals/README.md` when conducting behavioral evaluation.

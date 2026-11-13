# Behavioral evaluation cases

These cases define a starting evaluation protocol. They have not yet been executed as controlled agent comparisons. Structural validation checks files and metadata only.

For each run, give the agent the selected skill and the raw prompt below. Withhold these assessment notes and the worked-example answer. Record the model, host, date, tools, inputs, resulting artifact, and observed limitations. Compare against a run without the skill when investigating the skill's effect.

## Engineering design process

**Prompt:** “We want a hand-carried container for 5 L of chilled contents for a six-hour outdoor event. We have three reference products and want to choose a wall material. Empty mass should be around 1.5 kg. Help us decide the next step.”

**Assess:** identifies unresolved thermal conditions and distinguishes mass preference from verified requirements; proposes a bounded next method and useful artifact; avoids claiming to invoke absent skills; preserves iteration and missing evidence.

## Technical benchmarking

**Prompt:** “Compare A, B, and C. A weighs 2.0 kg and holds 5 L for 6 h; B weighs 1.5 kg and holds 5 L for 5 h. Both use a closed lid, 4 degrees C initial payload, 30 degrees C ambient, and a 10 degrees C endpoint. Their masses include prescribed coolant. C claims 10 h for 8 L at 20 degrees C ambient, with unspecified initial temperature, and weighs 1.2 kg without coolant. Which is best for a 5 L, six-hour, 1.5 kg design?”

**Assess:** rejects an overall winner from incomparable evidence; reports the 25% mass and approximately 16.7% hold-time differences for A/B; flags C's thermal and mass boundaries; preserves the target's unproven feasibility. If no new sources are supplied, attributes values to the prompt rather than inventing citations.

## Morphological synthesis

**Prompt:** “Explore a portable rain shelter for paved ground where ground penetration is prohibited. Consider folding arches, inflatable tubes, or external supports; flexible membrane or unsegmented rigid panels; stakes, ballast, or structural clamps; and folding, rolling around a 40 mm mandrel, or nesting for transport. Develop distinct concepts and explain incompatibilities.”

**Assess:** excludes stakes in the specified context and unsegmented rigid panels with tight rolling; treats external supports and inflatable/panel interfaces as evidence-dependent; gives complete concepts with interfaces; identifies packing/support coupling; does not equate all 54 selections with feasible concepts.

## Design optimization formulation

**Prompt:** “Formulate a minimum-mass uniform rectangular cantilever under a 100 N vertical tip force. L=0.5 m, E=69 GPa, rho=2700 kg/m^3, allowable stress=100 MPa, maximum tip displacement=5 mm. Choose b and h between 10 and 60 mm. Use small-deflection linear elastic bending with I=b*h^3/12. Check b=30 mm with h=20 mm and h=10 mm. Do not solve for an optimum.”

**Assess:** supplies correct symbols, units, bounds, equations, constraint signs, and model assumptions; obtains 0.810 kg / 25 MPa / 3.0193 mm and 0.405 kg / 100 MPa / 24.1546 mm; identifies the second point's displacement violation; does not claim an optimum or robustness to uncertain loads.

## Reporting

Report engineering correctness, evidence handling, artifact usefulness, and method selection separately. Explain failures rather than hiding them in a single aggregate score. These four cases are illustrative; broader claims require additional tasks, domains, and repeated runs.

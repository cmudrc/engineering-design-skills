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

## Product planning

**Prompt:** “We might build a better cooler for our event crew. They keep saying the current ones are awkward. We have a basic workshop, but nobody has agreed on a budget or launch date. Can you turn that into a project brief?”

**Assess:** develops a provisional Phase 0 mission with benefit, users/buyer, goals, stakeholders, assumptions, and open choices; asks useful scope questions without demanding a completed business case; keeps reported complaints separate from demonstrated demand; does not invent interviews, external market size, approval, budget, or delivery date; proposes a bounded Phase 1 learning effort while leaving architecture open.

## Design for manufacture and assembly

**Prompt:** “This cooler lid takes forever to assemble. It uses 12 fasteners. Five assemblies took 176, 182, 180, 179, and 183 seconds. We think four captive fasteners could take 140 seconds and save $0.12 in parts per unit. Labor is $36/hour and a new fixture would cost $260. Should we change it? We might make 100 or 1,000.”

**Assess:** maps the assembly difficulty and part functions; distinguishes the measured 180-second mean from the untested 140-second estimate; calculates $0.40 labor and $0.52 total recurring saving per unit, 500-unit break-even, $208 additional cost at 100 units and $260 saving at 1,000 under the stated cost boundary; exposes omitted qualification, scrap/rework, and other costs; checks sealing, load distribution, service, and process feasibility before recommending adoption. Does not treat fewer fasteners as sufficient proof of improvement.

## Prototyping and experimental planning

**Prompt:** “One of our cooler samples got warm early. Can we just build more of the passing version? Three independently built units use the same developed geometry and materials, assembled in our workshop. With the same 5 L payload, prescribed coolant, closed lid, 4 degrees C start and 30 degrees C ambient, P1 reached 9.4, P2 9.8 and P3 10.6 degrees C at six hours. Our stated limit is 10 degrees C. The lids can be interchanged.”

**Assess:** retains the failure and recognizes two of three meet the stated criterion in these runs; separates observations from causes and reliability claims; defines the next decision and a discriminating experiment, such as measurement/setup checks followed by a controlled lid/body comparison; specifies fidelity, specimen identities, controls, run order, raw measurements, analysis, and limitations. Distinguishes repeated runs from independent units; does not cherry-pick passing units or change the limit after seeing results. Keeps developed-product testing distinct from production-process readiness.

## Production ramp-up

**Prompt:** “We made a pilot lot of 30 coolers with the intended parts, fixtures, route, and trained operators. Twenty-four passed the first inspection. Four failed sealing but passed after rework; two had bad brackets and were scrapped. None are on hold. Can we double the next lot? I haven't pulled the timing and staffing records yet.”

**Assess:** reconciles 24 + 4 + 2 = 30 initially and 28 + 2 = 30 finally; reports 80% first-pass yield and 93.3% final conformance without double-counting reworked units; preserves defect and revision traceability; investigates seal and bracket problems without asserting their cause; identifies missing elapsed time, staffing, and actual readiness criteria; proposes a bounded corrective run with verification evidence. Does not infer throughput, stable process capability, a capability index, or universal release readiness from the yield percentage.

## Reporting

Report engineering correctness, evidence handling, artifact usefulness, and method selection separately. Explain failures rather than hiding them in a single aggregate score. These cases are illustrative; broader claims require additional tasks, domains, and repeated runs.

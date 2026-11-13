# Worked example: cantilever cross section

All numbers are synthetic teaching inputs. They define a preliminary analytical model, not a validated application design. No numerical optimizer is run.

## Decision and assumptions

Choose width `b` and vertical height `h` for a uniform, solid rectangular cantilever to minimize beam mass. Length, material properties, and a vertical tip force are fixed. Assume an ideal clamp, small deflections, linear elasticity, and bending about the axis associated with `I = b h^3 / 12`. The model excludes self-weight, attachment design, torsion, lateral instability, fatigue, and manufacturing tolerances; those omissions would need review for a real application.

| Symbol | Meaning | Type | Value or bounds |
|---|---|---|---|
| b | Cross-section width | Continuous variable | 0.010 ≤ b ≤ 0.060 m |
| h | Cross-section height | Continuous variable | 0.010 ≤ h ≤ 0.060 m |
| L | Beam length | Parameter | 0.50 m |
| F | Vertical tip force | Parameter | 100 N |
| E | Young's modulus | Parameter | 69 × 10^9 Pa |
| rho | Density | Parameter | 2700 kg/m^3 |
| sigma_allow | Allowable bending stress | Synthetic requirement | 100 × 10^6 Pa |
| delta_max | Allowable tip displacement | Synthetic requirement | 0.005 m |

Bounds and allowable values are supplied choices in this exercise. They are not inferred from the nominal modulus or density.

## Model and compact formulation

For this model:

- Mass: `m(b,h) = rho b h L`.
- Root bending stress: `sigma(b,h) = 6 F L / (b h^2)`.
- Tip displacement: `delta(b,h) = 4 F L^3 / (E b h^3)`.

Minimize `m(b,h)` subject to:

```text
g_sigma = sigma(b,h) / sigma_allow - 1 <= 0
g_delta = delta(b,h) / delta_max - 1 <= 0
0.010 m <= b <= 0.060 m
0.010 m <= h <= 0.060 m
```

Both residuals are dimensionless. Negative residuals satisfy the modeled requirement. An optimizer could use `b / 0.010 m` and `h / 0.010 m` as dimensionless variables, with the model converting back to physical dimensions.

## Trial designs

| b | h | Mass | Stress | Displacement | g_sigma | g_delta |
|---|---|---|---|---|---|---|
| 0.030 m | 0.020 m | 0.810 kg | 25.0 MPa | 3.0193 mm | -0.750 | -0.3961 |
| 0.030 m | 0.010 m | 0.405 kg | 100.0 MPa | 24.1546 mm | 0.000 | 3.8309 |

The first point satisfies the stated bounds and constraints. It is a feasible trial point, with no claim of optimality. The second is lighter and reaches the stress limit, but violates displacement by a wide margin. The large predicted displacement also motivates checking the small-deflection approximation rather than treating the result as high-fidelity behavior.

## Handoff

The deterministic algebraic problem is ready for illustrative numerical exploration under its assumptions. Before application use, review omitted load cases and failure modes, the material allowables, and the model validity. If cost or package size becomes an objective, express it explicitly and establish preferences or retain a multiobjective problem.

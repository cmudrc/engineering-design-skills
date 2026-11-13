# Worked example: insulated containers

The three containers and all data are fictional. Source identifiers below refer to this synthetic fixture, not real product literature.

## Inputs

The team seeks 5 L payload capacity, at least six hours before the payload reaches 10 degrees C, and an empty mass at or below 1.5 kg. Thermal conditions of interest are an initial payload temperature of 4 degrees C and ambient temperature of 30 degrees C, with the lid closed. Empty mass includes the container and prescribed coolant but excludes payload.

| Solution | Reported mass | Payload | Hold time | Conditions and source |
|---|---|---|---|---|
| A | 2.0 kg | 5 L | 6 h | S1: synthetic test record, 2026-11-13; common thermal protocol and mass boundary. |
| B | 1.5 kg | 5 L | 5 h | S2: synthetic test record, 2026-11-13; same thermal protocol and mass boundary as A. |
| C | 1.2 kg | 8 L | 10 h | S3: synthetic supplier claim, 2026-11-13; ambient 20 degrees C, initial temperature unspecified; mass excludes coolant. |

## Supported comparison

A and B have comparable thermal and mass evidence. B is 25% lighter than A, while its hold time is about 16.7% shorter. A meets the thermal threshold and misses the mass target; B meets the mass target and misses the thermal threshold. Neither dominates the other over these two criteria.

C's thermal claim is not comparable to A or B. Different ambient conditions, payload, and an unspecified initial state prevent a defensible direct comparison. Its mass also uses a different inclusion boundary. Dividing hold time by payload volume would not repair the mismatch: heat transfer depends on geometry, insulation, coolant, and temperature differences.

## Design opportunity

A 1.5 kg design meeting the six-hour protocol would combine desirable properties of A and B. The benchmark motivates this target; it does not establish feasibility or identify the necessary physical change.

**Next action:** request C's complete protocol and coolant mass; investigate the heat-ingress and cooling-capacity tradeoff in A and B. Product cost remains unknown and is excluded from ranking.

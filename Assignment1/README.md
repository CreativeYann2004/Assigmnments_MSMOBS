# ASSIGNMENT 1

NOTE: The python scripts have to be executed as Assignment1/task*.py since the model loading function uses a hardcoded path for simplisity when executing task*.py it will fail on loading the model since the file path does not assume Assignment1 to be the execution root

# Task1

## 1a. Question
### In the interactive session, we saw reaction fluxes in a linear pathway being equal to each other due to mass balance constraints. Do you observe the same thing now for the maximal reaction activities? Explain your observation

No, the maximal reaction activities in a linear pathway are not necessarily equal. In the interactive session, the fluxes were equal. This was because mass balance at steady state required the same rate through each reaction step. By contrast, maximal reaction activities represent the upper limits of each reaction. These are based on enzyme expression levels and catalytic capacity. They are independent of mass balance. Therefore, in a linear pathway, different enzymes can have different maximal activities, meaning the values do not have to match across reactions.

## 1b. Question

### Some reactions have no maximal reaction activity data. Identify at least two different kinds of such reactions, and explain why gene expression-derived data would not be applicable for these kinds of reactions.

Reactions such as EX_etoh_e and EX_acald_e do not have maximal activity values because they represent transport between the model and the external environment. As these reactions are not catalysed by intracellular enzymes, no gene expression data can be linked to them. Since gene expression only reflects proteins encoded within the cell, it cannot provide information on exchange processes that depend on medium composition or external conditions rather than enzyme activity.

Another example is the FORT transport reaction. Rather than being dependent on the expression level of a single enzyme, its flux depends on membrane properties and metabolite concentration gradients across the cell boundary. As these fluxes are driven by passive or facilitated transport dynamics, they cannot be constrained directly using data on intracellular gene expression.

# Task2

Run this code for task2:
```bash
python Assignment1/task2.py
```

### Please print a table listing each reaction’s lower and upper flux bound after implementing the above (no formatting requirements, simple printout sufficient).

| Reaction ID               | Lower Bound | Upper Bound |
|---------------------------|------------:|------------:|
| PFK                       | 0.0000      | 12.1200     |
| PFL                       | 0.0000      | 1.0000      |
| PGI                       | -13.1200    | 13.1200     |
| PGK                       | -23.1300    | 23.1300     |
| PGL                       | 0.0000      | 8.1200      |
| ACALD                     | -1.1600     | 1.1600      |
| AKGt2r                    | -3.1000     | 3.1000      |
| PGM                       | -20.0100    | 20.0100     |
| PIt2r                     | -6.0300     | 6.0300      |
| ALCD2x                    | -9.0100     | 9.0100      |
| ACALDt                    | -2.2900     | 2.2900      |
| ACKr                      | -1.1900     | 1.1900      |
| PPC                       | 0.0000      | 2.5600      |
| ACONTa                    | -25.3500    | 25.3500     |
| ACONTb                    | -25.3500    | 25.3500     |
| ATPM                      | 8.3900      | 1000.0000   |
| PPCK                      | 0.0000      | 25.2300     |
| ACt2r                     | -3.2300     | 3.2300      |
| PPS                       | 0.0000      | 2.5000      |
| ADK1                      | -30.5700    | 30.5700     |
| AKGDH                     | 0.0000      | 24.3500     |
| ATPS4r                    | -60.5000    | 60.5000     |
| PTAr                      | -4.4700     | 4.4700      |
| PYK                       | 0.0000      | 26.7800     |
| BIOMASS_Ecoli_core_w_GAM  | 0.0000      | 1000.0000   |
| PYRt2                     | -1.2600     | 1.2600      |
| CO2t                      | -30.4500    | 30.4500     |
| RPE                       | -5.6700     | 5.6700      |
| CS                        | 0.0000      | 20.5600     |
| RPI                       | -5.5600     | 5.5600      |
| SUCCt2_2                  | 0.0000      | 2.3600      |
| CYTBD                     | 0.0000      | 40.5600     |
| D_LACt2                   | -4.5600     | 4.5600      |
| ENO                       | -28.7800    | 28.7800     |
| SUCCt3                    | 0.0000      | 6.6700      |
| ETOHt2r                   | -2.3400     | 2.3400      |
| SUCDi                     | 0.0000      | 24.3400     |
| SUCOAS                    | -20.6000    | 20.6000     |
| TALA                      | -4.4500     | 4.4500      |
| THD2                      | 0.0000      | 4.5000      |
| TKT1                      | -3.3400     | 3.3400      |
| TKT2                      | -3.3400     | 3.3400      |
| TPI                       | -45.5600    | 45.5600     |
| EX_ac_e                   | 0.0000      | 1000.0000   |
| EX_acald_e                | 0.0000      | 1000.0000   |
| EX_akg_e                  | 0.0000      | 1000.0000   |
| EX_co2_e                  | -1000.0000  | 1000.0000   |
| EX_etoh_e                 | 0.0000      | 1000.0000   |
| EX_for_e                  | 0.0000      | 1000.0000   |
| EX_fru_e                  | 0.0000      | 1000.0000   |
| EX_fum_e                  | 0.0000      | 1000.0000   |
| EX_glc__D_e               | -1000.0000  | 1000.0000   |
| EX_gln__L_e               | 0.0000      | 1000.0000   |
| EX_glu__L_e               | 0.0000      | 1000.0000   |
| EX_h_e                    | -1000.0000  | 1000.0000   |
| EX_h2o_e                  | -1000.0000  | 1000.0000   |
| EX_lac__D_e               | 0.0000      | 1000.0000   |
| EX_mal__L_e               | 0.0000      | 1000.0000   |
| EX_nh4_e                  | -1000.0000  | 1000.0000   |
| EX_o2_e                   | -1000.0000  | 1000.0000   |
| EX_pi_e                   | -1000.0000  | 1000.0000   |
| EX_pyr_e                  | 0.0000      | 1000.0000   |
| EX_succ_e                 | 0.0000      | 1000.0000   |
| FBA                       | -24.4500    | 24.4500     |
| FBP                       | 0.0000      | 2.3500      |
| FORt2                     | 0.0000      | 1.2800      |
| FORt                      | 0.0000      | 2.3400      |
| FRD7                      | 0.0000      | 20.0700     |
| FRUpts2                   | 0.0000      | 10.0800     |
| FUM                       | -24.3500    | 24.3500     |
| FUMt2_2                   | 0.0000      | 2.4500      |
| G6PDH2r                   | -5.6800     | 5.6800      |
| GAPD                      | -26.1300    | 26.1300     |
| GLCpts                    | 0.0000      | 16.3400     |
| GLNS                      | 0.0000      | 3.4500      |
| GLNabc                     | 0.0000      | 0.2500      |
| GLUDy                     | -7.3500     | 7.3500      |
| GLUN                      | 0.0000      | 6.2500      |
| GLUSy                     | 0.0000      | 7.3500      |
| GLUt2r                    | -4.1200     | 4.1200      |
| GND                       | 0.0000      | 6.7200      |
| H2Ot                      | -20.0600    | 20.0600     |
| ICDHyr                    | -15.0600    | 15.0600     |
| ICL                       | 0.0000      | 14.0700     |
| LDH_D                     | -2.0700     | 2.0700      |
| MALS                      | 0.0000      | 9.1200      |
| MALt2_2                   | 0.0000      | 8.8700      |
| MDH                       | -4.2600     | 4.2600      |
| ME1                       | 0.0000      | 3.2400      |
| ME2                       | 0.0000      | 3.3400      |
| NADH16                    | 0.0000      | 20.2600     |
| NADTRHD                   | 0.0000      | 1.2600      |
| NH4t                      | -3.4500     | 3.4500      |
| O2t                       | -40.6700    | 40.6700     |
| PDH                       | 0.0000      | 32.3200     |

values are in  [mmol/gDW/h]

# Task3

Run this code for task3:
```bash
python Assignment1/task3.py
```

### 3a) Carry out an FVA for all reactions in the model and print out the resulting minimal and maximal fluxes per reaction (simple printout sufficient).

| Reaction ID                 | Minimum Flux | Maximum Flux |
|----------------------------|-------------:|-------------:|
| PFK                        | 7.31446      | 7.31446      |
| PFL                        | -0.00000     | 0.00000      |
| PGI                        | 7.37644      | 7.37644      |
| PGK                        | -14.46649    | -14.46649    |
| PGL                        | 0.47510      | 0.47510      |
| ACALD                      | -1.16000     | -1.16000     |
| AKGt2r                     | -0.00000     | 0.00000      |
| PGM                        | -13.74906    | -13.74906    |
| PIt2r                      | 1.76420      | 1.76420      |
| ALCD2x                     | -1.16000     | -1.16000     |
| ACALDt                     | -0.00000     | -0.00000     |
| ACKr                       | -1.19000     | -1.19000     |
| PPC                        | 1.37426      | 1.37426      |
| ACONTa                     | 3.28998      | 3.28998      |
| ACONTb                     | 3.28998      | 3.28998      |
| ATPM                       | 8.39000      | 8.39000      |
| PPCK                       | 0.00000      | 0.00000      |
| ACt2r                      | -1.19000     | -1.19000     |
| PPS                        | 0.00000      | 0.00000      |
| ADK1                       | 0.00000      | 0.00000      |
| AKGDH                      | 2.77257      | 2.77257      |
| ATPS4r                     | 21.90519     | 21.90519     |
| PTAr                       | 1.19000      | 1.19000      |
| PYK                        | 4.17600      | 4.17600      |
| BIOMASS_Ecoli_core_w_GAM   | 0.47957      | 0.47957      |
| PYRt2                      | -1.26000     | -1.26000     |
| CO2t                       | -12.60072    | -12.60072    |
| RPE                        | -0.02798     | -0.02798     |
| CS                         | 3.28998      | 3.28998      |
| RPI                        | -0.50308     | -0.50308     |
| SUCCt2_2                   | 0.00000      | 0.00000      |
| CYTBD                      | 23.03257     | 23.03257     |
| D_LACt2                    | -2.07000     | -2.07000     |
| ENO                        | 13.74906     | 13.74906     |
| SUCCt3                     | 0.00000      | 0.00000      |
| ETOHt2r                    | -1.16000     | -1.16000     |
| SUCDi                      | 2.77257      | 22.84257     |
| SUCOAS                     | -2.77257     | -2.77257     |
| TALA                       | 0.07257      | 0.07257      |
| THD2                       | 4.50000      | 4.50000      |
| TKT1                       | 0.07257      | 0.07257      |
| TKT2                       | -0.10055     | -0.10055     |
| TPI                        | 7.31446      | 7.31446      |
| EX_ac_e                    | 1.19000      | 1.19000      |
| EX_acald_e                 | 0.00000      | 0.00000      |
| EX_akg_e                   | 0.00000      | 0.00000      |
| EX_co2_e                   | 12.60072     | 12.60072     |
| EX_etoh_e                  | 1.16000      | 1.16000      |
| EX_for_e                   | -0.00000     | 0.00000      |
| EX_fru_e                   | 0.00000      | 0.00000      |
| EX_fum_e                   | 0.00000      | 0.00000      |
| EX_glc__D_e                | -7.94985     | -7.94985     |
| EX_gln__L_e                | 0.00000      | 0.00000      |
| EX_glu__L_e                | 0.00000      | 0.00000      |
| EX_h_e                     | 14.14020     | 14.14020     |
| EX_h2o_e                   | 16.19411     | 16.19411     |
| EX_lac__D_e                | 2.07000      | 2.07000      |
| EX_mal__L_e                | 0.00000      | 0.00000      |
| EX_nh4_e                   | -2.61501     | -2.61501     |
| EX_o2_e                    | -11.51629    | -11.51629    |
| EX_pi_e                    | -1.76420     | -1.76420     |
| EX_pyr_e                   | 1.26000      | 1.26000      |
| EX_succ_e                  | 0.00000      | 0.00000      |
| FBA                        | 7.31446      | 7.31446      |
| FBP                        | 0.00000      | 0.00000      |
| FORt2                      | 0.00000      | 0.00000      |
| FORt                       | 0.00000      | 0.00000      |
| FRD7                       | 0.00000      | 20.07000     |
| FRUpts2                    | 0.00000      | 0.00000      |
| FUM                        | 2.77257      | 2.77257      |
| FUMt2_2                    | 0.00000      | 0.00000      |
| G6PDH2r                    | 0.47510      | 0.47510      |
| GAPD                       | 14.46649     | 14.46649     |
| GLCpts                     | 7.94985      | 7.94985      |
| GLNS                       | 0.12263      | 0.12263      |
| GLNabc                     | -0.00000     | 0.00000      |
| GLUDy                      | -2.49238     | -2.49238     |
| GLUN                       | 0.00000      | 0.00000      |
| GLUSy                      | 0.00000      | 0.00000      |
| GLUt2r                     | -0.00000     | 0.00000      |
| GND                        | 0.47510      | 0.47510      |
| H2Ot                       | -16.19411    | -16.19411    |
| ICDHyr                     | 3.28998      | 3.28998      |
| ICL                        | 0.00000      | 0.00000      |
| LDH_D                      | -2.07000     | -2.07000     |
| MALS                       | 0.00000      | 0.00000      |
| MALt2_2                    | 0.00000      | 0.00000      |
| MDH                        | 2.77257      | 2.77257      |
| ME1                        | 0.00000      | 0.00000      |
| ME2                        | 0.00000      | 0.00000      |
| NADH16                     | 20.26000     | 20.26000     |
| NADTRHD                    | 0.00000      | 0.00000      |
| NH4t                       | 2.61501      | 2.61501      |
| O2t                        | 11.51629     | 11.51629     |
| PDH                        | 7.43732      | 7.43732      |

### 3b) Identify any reactions with gene expression-imposed maximal reaction activities, whose permissible flux range in forward direction is nonzero yet comes out less than its upper flux bound. State their number and explain why a set of reactions behaves this way.
| Reaction ID | Upper Bound | FVA Max Flux |
|-------------|------------:|-------------:|
| PFK         | 12.12       | 7.31         |
| PFL         | 1.00        | 0.00         |
| PGI         | 13.12       | 7.38         |
| PGK         | 23.13       | -14.47       |
| PGL         | 8.12        | 0.48         |
| ACALD       | 1.16        | -1.16        |
| AKGt2r      | 3.10        | 0.00         |
| PGM         | 20.01       | -13.75       |
| PIt2r       | 6.03        | 1.76         |
| ALCD2x      | 9.01        | -1.16        |
| ACALDt      | 2.29        | -0.00        |
| ACKr        | 1.19        | -1.19        |
| PPC         | 2.56        | 1.37         |
| ACONTa      | 25.35       | 3.29         |
| ACONTb      | 25.35       | 3.29         |

Remark: The table is not completly here because there are 91 reactions.
So,a total of 91 reactions have a non-zero forward flux that remains below their gene expression-imposed upper bound. This is because the realised flux is limited by substrate supply, competing pathways and bottlenecks, meaning the enzyme cannot reach its full capacity. Additionally, 41 reactions always carry flux under the given conditions.

### 3c) How many reactions have a positive minimal flux in the FVA? State their number and explain why a set of reactions behaves this way.

Number of reactions with positive minimal flux: 41
In the FVA, 41 reactions show a positive minimal flux. This occurs because ATPM and a nonzero biomass flux require continuous energy and precursor supply. As a result, key glycolysis, TCA, respiration, and exchange reactions must always operate, so their flux cannot drop to zero.


# Task4

Run this code for task4:
```bash
python Assignment1/task4.py
```

### 4a) Carry out an FBA optimization of biomass and report the maximal biomass production rate in the presence of the implemented constraints.

The maximum rate of biomass production under the constraints imposed on enzyme activity is 0.479571 mmol/gDW/h.

### 4b) Determine the bottleneck(s)

Bottleneck reactions are those that achieve maximum flux in an optimal solution.
From our results we got that the bottlenecks are:

THD2 (flux = 4.50000, at the upper bound) and NADH16 (flux = 20.26000, also at the upper bound).
NADH16 (flux = 20.26000, also at the upper bound).

These reactions limit the maximum biomass production rate because their enzyme activity constraints are fully utilised.

### 4c) The model does not use (have non-zero flux for) all reactions in the model constrained with maximal reaction activities. Pick a reaction with maximal reaction activity constraints and zero flux in the optimal solution, and explain from the network context why it cannot carry flux.

One example is the PFL reaction coa_c + pyr_c --> accoa_c + for_c. Although this reaction has a non-zero maximal activity constraint, its flux is zero in the optimal solution. This is because the produced formate cannot be secreted or metabolised further, as the formate exchange is modelled as one-directional and there is no downstream pathway that consumes it. Allowing flux through the PFL reaction would therefore lead to the accumulation of an unusable by-product. Consequently, the network context blocks this reaction despite its enzyme capacity.

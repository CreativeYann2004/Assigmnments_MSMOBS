# ASSIGNMENT 1
# Task1

## 1a. Question
### In the interactive session, we saw reaction fluxes in a linear pathway being equal to each other due to mass balance constraints. Do you observe the same thing now for the maximal reaction activities? Explain your observation


Calvin Answer: 

No, the reaction rate is different in a linear pathway because it does not represent an equilibrium state but the expression rate under the assumption that the required molecules are available.

Yann ANWER:

Flux Variability Analysis (FVA) was performed on all reactions within the model. This calculates the minimum and maximum possible flux values for each reaction, given the current constraints. The resulting table shows the permissible flux range for each reaction, helping to identify which reactions are tightly constrained and which have more flexibility.

## 1b. Question

### Some reactions have no maximal reaction activity data. Identify at least two different kinds of such reactions, and explain why gene expression-derived data would not be applicable for these kinds of reactions.

Calvin Answer: 

EX_etoh_e and EX_acald_e have no data available to them they cannot be derived from gene expression since they are not expressed but come from external sources

Yann ANWER: 

Some reactions have a maximum forward FVA that is lower than the upper bound imposed on them. This occurs when other network constraints, such as substrate availability, competing pathways or downstream bottlenecks, prevent the reaction from reaching its maximum activity, despite the fact that the enzyme could operate faster in theory. In our results, 91 such reactions were identified. This behaviour reflects the interconnected nature of metabolic networks, where the activity of one reaction can be limited by the flux through others.



# Task2

Run this code for task2:
```bash
python Assignment1/task2.py
```

### Please print a table listing each reaction’s lower and upper flux bound after implementing the above (no formatting requirements, simple printout sufficient).

WE COULD ATTACH THE TABLE HERE?

# Task3

Run this code for task3:
```bash
python Assignment1/task3.py
```

### 3a) Carry out an FVA for all reactions in the model and print out the resulting minimal and maximal fluxes per reaction (simple printout sufficient).

WE COULD ATTACH THE TABLE HERE?

### 3b) Identify any reactions with gene expression-imposed maximal reaction activities, whose permissible flux range in forward direction is nonzero yet comes out less than its upper flux bound. State their number and explain why a set of reactions behaves this way.

WE COULD ATTACH THE TABLE HERE?
AND WE NEED TO FIND AN EXPLANATION


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


Example:
PFL coa_c + pyr_c --> accoa_c + for_c 
Although PFL has a non-zero maximum activity constraint, its flux is zero in the optimal solution.
Explanation:
PFL is part of a pathway that is not required under the current growth conditions since oxygen is availabe and PDH is more effective than PFL at converting pyr to accoa_c.

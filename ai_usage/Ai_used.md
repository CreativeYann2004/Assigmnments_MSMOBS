## AI Usage Guidelines

We use **GitHub Copilot** for code auto-completion.  
All generated suggestions were carefully reviewed and validated, ensuring we fully understood the code in order to complete each assignment.

We also used DeepL Write to improve the structure of the sentences.

Propmts:
import common

def main():
# Load the E. coli core model
# Store expression data from the CSV file as the command reference suggests
# Apply constraints based on the assignment instructions
model, expression_data = common.get_model_with_constraints()

if name == "main":
main()
pass
can you make jâvadoc style comnments instead please

 codebase
import common  # reuse single source of truth

def main():
    """
    Loads the E. coli core model, applies gene expression constraints,
    and prints the lower and upper bounds for each reaction.

    Steps:
    1. Load the metabolic model from JSON.
    2. Load gene expression data from CSV.
    3. Apply constraints to reactions as specified in the assignment.
    4. Print a table of reaction bounds.
    """
    # Load the E. coli core model and expression data
    model, expression_data = common.get_model_with_constraints()

    # Print the final reaction bounds as requested
    print(f"{'Reaction ID':<25} {'Lower Bound':<15} {'Upper Bound':<15}")
    print("-" * 45)
    for reaction in model.reactions:
        print(f"{reaction.id:<25} {reaction.lower_bound:<15.4f} {reaction.upper_bound:<15.4f}")
# 3.a
# we use the built-in FVA function from cobra
fva_results = flux_variability_analysis(model, model.reactions)
print(f"{'Reaction ID':<25} {'Minimum Flux':<25} {'Maximum Flux':<25}")
print("-" * 55)
for rxn_id, row in fva_results.iterrows():
    print(f"{rxn_id:<25} {row['minimum']:<25.5f} {row['maximum']:<25.5f}")

# 3.b
restricted = []
for rxn in model.reactions:
    ub = rxn.upper_bound
    fva_max = fva_results.loc[rxn.id, "maximum"]

    if ub > 0 and fva_max < ub - 1e-17 and rxn.id != "FORt":
        restricted.append((rxn.id, ub, fva_max))

print(f"Number of reactions with forward capacity > 0 but FVA maximum < UB: {len(restricted)}\n")

print(f"{'Reaction ID':<25} {'Upper Bound':<25} {'FVA Max Flux'}")
print("-" * 55)
for rxn_id, ub, fva_max in restricted[:15]:
    print(f"{rxn_id:<25} {ub:<25.2f} {fva_max:.2f}")

print(f"{'Reaction ID':<25} {'Minimum Flux':<25} {'Maximum Flux':<25}")
print("-" * 55)
for rxn_id, row in fva_results.iterrows():
    print(f"{rxn_id:<25} {row['minimum']:<15.5f} {row['maximum']:<15.5f}")

# 3.c
positive_min_flux = [rxn_id for rxn_id, row in fva_results.iterrows() if row['minimum'] > 1e-17]
print(f"Number of reactions with positive minimal flux: {len(positive_min_flux)}")
if __name__ == "__main__":
    main()
    pass




rom cobra.flux_analysis import flux_variability_analysis
import common # reuse constrained model

def main():
# Load the E. coli core model
# Store expression data from the CSV file as the command reference suggests
# Apply constraints based on the assignment instructions
model, expression_data = common.get_model_with_constraints()

if name == "main":
main()
pass
can you make javadoc style comments instead

task3.py+13-9
I have added JavaDoc-style comments to your code to clearly describe the main function and its steps.








import common  # reuse constrained model

def main():
    # Load the E. coli core model
    # Store expression data from the CSV file as the command reference suggests
    # Apply constraints based on the assignment instructions
    model, expression_data = common.get_model_with_constraints()

    # 4.a
    optimum = model.optimize()

    bottlenecks = []
    print(f"Maximal biomass production rate: {optimum.objective_value:.6f}\n")

    # 4.b
    # we basically have to check which constraints are tight for the current solution
    for rxn in model.reactions:
        flux = optimum.fluxes[rxn.id]
        if abs(flux - rxn.upper_bound) < 1e-9:  # at max bound
            bottlenecks.append((rxn.id, flux, "upper_bound"))

    # print results
    print(f"{'Reaction ID':<20} {'Flux value':<15} {'At bound'}")
    print("-" * 50)
    for rxn_id, flux, which_bound in bottlenecks:
        print(f"{rxn_id:<20} {flux:<15.5f} {which_bound}")

    # 4.c
    unused = []
    for rxn in model.reactions:
        if rxn.upper_bound > 0 and abs(optimum.fluxes[rxn.id]) < 1e-9:
            unused.append(rxn)

    print("Example unused reactions with nonzero capacity:")
    for rxn in unused[:10]:  # show first 10
        print(rxn.id, rxn.reaction)

if __name__ == "__main__":
    main()
    pass
 can you also add javadoc style comment here please
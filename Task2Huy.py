import cobra
from cobra.flux_analysis import flux_variability_analysis
import csv

def main():
    # Load the E. coli core model
    model = cobra.io.load_json_model('Assignment1/e_coli_core.json')

    # Store expression data from the CSV file as the command reference suggests
    expression_data = {}
    with open('Assignment1/e_coli_core_expression.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            reaction_id, value = row
            expression_data[reaction_id] = float(value)

    # Apply constraints based on the assignment instructions
    for reaction in model.reactions:
        # Check if the reaction is in our expression data, if not then leave them alone
        if reaction.id in expression_data:
            value = expression_data[reaction.id]

            # ATPM - leave as is
            if reaction.id == 'ATPM':
                continue

            # For reversible reactions, set both bounds to -value and value
            if reaction.reversibility:
                reaction.lower_bound = -value
                reaction.upper_bound = value
            # For irreversible reactions, only set the upper bound to value
            else:
                reaction.lower_bound = 0
                reaction.upper_bound = value
    
    #set max bounds as specified in task2
    model.reactions.EX_glc__D_e.lower_bound = -1000
    model.reactions.EX_glc__D_e.upper_bound = 1000

    # Print the final reaction bounds as requested
    print(f"{'Reaction ID':<25} {'Lower Bound':<15} {'Upper Bound':<15}")
    print("-" * 45)
    for reaction in model.reactions:
        print(f"{reaction.id:<25} {reaction.lower_bound:<15.4f} {reaction.upper_bound:<15.4f}")

    # 3.a
    # we use the built-in FVA function from cobra
    fva_results = flux_variability_analysis(model, model.reactions)
    print(f"{'Reaction ID':<20} {'Minimum Flux':<15} {'Maximum Flux':<15}")
    print("-" * 55)
    for rxn_id, row in fva_results.iterrows():
        print(f"{rxn_id:<20} {row['minimum']:<15.5f} {row['maximum']:<15.5f}")

    # 3.b
    restricted = []
    for rxn in model.reactions:
        ub = rxn.upper_bound
        fva_max = fva_results.loc[rxn.id, "maximum"]

        if ub > 0 and fva_max < ub - 1e-9 and rxn.id != "FORt":
            restricted.append((rxn.id, ub, fva_max))

    print(f"Number of reactions with forward capacity > 0 but FVA maximum < UB: {len(restricted)}\n")

    print(f"{'Reaction ID':<20} {'Upper Bound':<15} {'FVA Max Flux'}")
    print("-" * 55)
    for rxn_id, ub, fva_max in restricted[:15]:
        print(f"{rxn_id:<20} {ub:<15.2f} {fva_max:.2f}")

    print(f"{'Reaction ID':<25} {'Minimum Flux':<15} {'Maximum Flux':<15}")
    print("-" * 55)
    for rxn_id, row in fva_results.iterrows():
        print(f"{rxn_id:<25} {row['minimum']:<15.5f} {row['maximum']:<15.5f}")


    # 4.a
    optimum = model.optimize()

    bottlenecks = []

    # 4.b
    # we basically have to check which constraints are tight for the current solution
    for rxn in model.reactions:
        flux = optimum.fluxes[rxn.id]
        if abs(flux - rxn.upper_bound) < 1e-6:  # at max bound
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

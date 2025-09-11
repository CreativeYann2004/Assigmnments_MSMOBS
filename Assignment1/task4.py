import common

def main():
    """
    Performs FBA optimization of biomass production on the E. coli core model with gene expression constraints.
    Steps:
    1. Load the metabolic model and expression data using a shared utility.
    2. Apply constraints to reactions as specified in the assignment.
    3. Run FBA and report the maximal biomass production rate.
    4. Identify bottleneck reactions whose flux reaches their upper bound.
    5. List example reactions with nonzero capacity but zero flux in the optimal solution.
    """
    # Load the E. coli core model and expression data
    model, expression_data = common.get_model_with_constraints()

    # 4.a FBA optimization
    optimum = model.optimize()

    bottlenecks = []
    print(f"Maximal biomass production rate: {optimum.objective_value:.6f}\n")

    # 4.b Identify bottleneck reactions
    for rxn in model.reactions:
        flux = optimum.fluxes[rxn.id]
        if abs(flux - rxn.upper_bound) < 1e-9:  # at max bound
            bottlenecks.append((rxn.id, flux, "upper_bound"))

    # print results
    print(f"{'Reaction ID':<20} {'Flux value':<15} {'At bound'}")
    print("-" * 50)
    for rxn_id, flux, which_bound in bottlenecks:
        print(f"{rxn_id:<20} {flux:<15.5f} {which_bound}")

    # 4.c List unused reactions with nonzero capacity
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

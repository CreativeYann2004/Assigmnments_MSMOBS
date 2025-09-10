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

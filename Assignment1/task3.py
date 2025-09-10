from cobra.flux_analysis import flux_variability_analysis
import common  # reuse constrained model

def main():
    # Load the E. coli core model
    # Store expression data from the CSV file as the command reference suggests
    # Apply constraints based on the assignment instructions
    model, expression_data = common.get_model_with_constraints()

    # 3.a
    # We use the built-in FVA function from cobra
    fva_results = flux_variability_analysis(model, model.reactions)
    # To match the assignment exactly (optional):
    # fva_results = flux_variability_analysis(model, model.reactions, fraction_of_optimum=0.0, loopless=False)

    # 3.b
    restricted = []
    for rxn in model.reactions:
        ub = rxn.upper_bound
        fva_max = fva_results.loc[rxn.id, "maximum"]
        if ub > 0 and fva_max < ub - 1e-9 and rxn.id != "FORt":
            restricted.append((rxn.id, ub, fva_max))

    print(f"Number of reactions with forward capacity > 0 but FVA maximum < UB: {len(restricted)}\n")

    print(f"{'Reaction ID':<20} {'Upper Bound':<20} {'FVA Max Flux'}")
    print("-" * 55)
    for rxn_id, ub, fva_max in restricted[:15]:
        print(f"{rxn_id:<20} {ub:<20.2f} {fva_max:.2f}")

    print(f"{'Reaction ID':<25} {'Minimum Flux':<15} {'Maximum Flux':<15}")
    print("-" * 55)
    for rxn_id, row in fva_results.iterrows():
        print(f"{rxn_id:<25} {row['minimum']:<15.5f} {row['maximum']:<15.5f}")

if __name__ == "__main__":
    main()
    pass

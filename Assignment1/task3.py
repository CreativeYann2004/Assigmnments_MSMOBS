from cobra.flux_analysis import flux_variability_analysis
import common

def main():
    """
    Performs Flux Variability Analysis (FVA) on the E. coli core model with gene expression constraints.
    Steps:
    1. Load the metabolic model and expression data using a shared utility.
    2. Apply constraints to reactions as specified in the assignment.
    3. Run FVA for all reactions and print the minimum and maximum fluxes.
    4. Identify reactions with forward FVA maximum below their upper bound.
    5. Count reactions with positive minimal flux in FVA.
    """
    # Load the E. coli core model and expression data
    model, expression_data = common.get_model_with_constraints()

    # 3.a Run FVA and print results
    fva_results = flux_variability_analysis(model, model.reactions)
    print(f"{'Reaction ID':<25} {'Minimum Flux':<25} {'Maximum Flux':<25}")
    print("-" * 55)
    for rxn_id, row in fva_results.iterrows():
        print(f"{rxn_id:<25} {row['minimum']:<25.5f} {row['maximum']:<25.5f}")

    # 3.b Identify reactions with FVA max < upper bound
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

    # 3.c Count reactions with positive minimal flux
    positive_min_flux = [rxn_id for rxn_id, row in fva_results.iterrows() if row['minimum'] > 1e-17]
    print(f"Number of reactions with positive minimal flux: {len(positive_min_flux)}")

if __name__ == "__main__":
    main()
    pass

import common

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
    model, expression_data = common.get_model_with_constraints()
    print(f"{'Reaction ID':<25} {'Lower Bound':<15} {'Upper Bound':<15}")
    print("-" * 45)
    for reaction in model.reactions:
        print(f"{reaction.id:<25} {reaction.lower_bound:<15.4f} {reaction.upper_bound:<15.4f}")

if __name__ == "__main__":
    main()
    pass

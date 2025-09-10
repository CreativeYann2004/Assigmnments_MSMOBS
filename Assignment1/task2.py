import common  # reuse single source of truth

def main():
    # Load the E. coli core model
    # Store expression data from the CSV file as the command reference suggests
    # Apply constraints based on the assignment instructions
    model, expression_data = common.get_model_with_constraints()

    # Print the final reaction bounds as requested
    print(f"{'Reaction ID':<25} {'Lower Bound':<15} {'Upper Bound':<15}")
    print("-" * 45)
    for reaction in model.reactions:
        print(f"{reaction.id:<25} {reaction.lower_bound:<15.4f} {reaction.upper_bound:<15.4f}")

if __name__ == "__main__":
    main()
    pass

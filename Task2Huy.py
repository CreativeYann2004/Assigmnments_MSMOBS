import cobra
from cobra.flux_analysis import flux_variability_analysis
import csv

def main():
    # Load the E. coli core model
    model = cobra.io.load_json_model('e_coli_core.json')

    # Store expression data from the CSV file as the command reference suggests
    expression_data = {}
    with open('e_coli_core_expression.csv', mode='r') as file:
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

    # EX_glc_D_e has questionable lower bound with -10 should probably be either 0 or -1000 chat-gpt suggest -1000 unclear if the -10 is a mistake in the provided data or a spefic limit on the output of EX_glc_D_e
    # do first practical to understand how they want the glucose values to be changed the -10 seems to have something to do with it

    # Print the final reaction bounds as requested
    print(f"{'Reaction ID':<25} {'Lower Bound':<15} {'Upper Bound':<15}")
    print("-" * 45)
    for reaction in model.reactions:
        print(f"{reaction.id:<25} {reaction.lower_bound:<15.4f} {reaction.upper_bound:<15.4f}")

    # 3.a
    # we use the built-in FVA function from cobra
    fva_results = flux_variability_analysis(model, model.reactions)

    print(f"{'Reaction ID':<25} {'Minimum Flux':<15} {'Maximum Flux':<15}")
    print("-" * 55)
    for rxn_id, row in fva_results.iterrows():
        print(f"{rxn_id:<25} {row['minimum']:<15.5f} {row['maximum']:<15.5f}")


if __name__ == "__main__":
    main()
    pass

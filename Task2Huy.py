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


    # Glucose exchange: remove the maximal uptake bound

    # I dont really understand the
    # "We assume the subsequent transporter maximal activity accounts for maximal glucose uptake."
    # I assume unlimited supply so -1000
    # Maybe check this
    model.reactions.EX_glc__D_e.lower_bound = -1000

    # Set the upper bound to the default of 1000
    model.reactions.EX_glc__D_e.upper_bound = 1000

    # Print the final reaction bounds as requested
    print(f"{'Reaction ID':<15} {'Lower Bound':<15} {'Upper Bound':<15}")
    print("-" * 45)
    for reaction in model.reactions:
        print(f"{reaction.id:<15} {reaction.lower_bound:<15.4f} {reaction.upper_bound:<15.4f}")

    # 3.a
    # we use the built-in FVA function from cobra
    fva_results = flux_variability_analysis(model, model.reactions)

    print(f"{'Reaction ID':<20} {'Minimum Flux':<15} {'Maximum Flux':<15}")
    print("-" * 55)
    for rxn_id, row in fva_results.iterrows():
        print(f"{rxn_id:<20} {row['minimum']:<15.5f} {row['maximum']:<15.5f}")


if __name__ == "__main__":
    main()
    pass
import cobra
import csv

def get_model_with_constraints():
    # Load the E. coli core model
    model = cobra.io.load_json_model('Assignment1/e_coli_core.json')

    # Store expression data from the CSV file as the command reference suggests
    expression_data = {}
    with open('Assignment1/e_coli_core_expression.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)
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

    return model, expression_data

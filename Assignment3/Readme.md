# Question 1: The Most Dangerous Mutation
The most dangerous mutation is the p53 knockout mutation, which completely removes the cell’s ability to undergo apoptosis. In this case, around half of all possible states result in cancerous growth, compared to just 3% in the wild type. MYC amplification and MDM2 overexpression are almost as harmful, as they also effectively shut off p53. However, p21 loss is less severe, as p53 can still trigger cell death.

# Question 2: Role of the Feedback Loop
The MYC → MDM2 → p53 loop suppresses p53. In normal cells, this prevents p53 from remaining active for too long after stress. However, when MYC or MDM2 are overexpressed, the loop permanently disables p53. Simulations show that, in these cases, the network never reaches a p53-active attractor. This allows damaged cells to continue growing instead of dying.

# Question 3: Limitations of the Model
The model is limited because it only uses ON/OFF states and synchronous updates. This means it does not capture information about influence strength. It also leaves out many regulators, such as ARF and DNA repair, which makes the effects of oncogenesis appear stronger than they are in real cells. Finally, it forces binary fates of growth or death without intermediate outcomes such as senescence or recovery.

> [!IMPORTANT]  
> The simulation code has been modified, as the simulation did not stop once the cell died.
> 
> There is now an additional break statement in the main simulation loop:
>
> ```python
>  for step in range(steps):
>     self.update_synchronous()
>     # stop if the cell has died
>     if self.nodes['Death'] == 1:
>         break
>     # the rest of the code is the same
> ```



# Question 1: The Most Dangerous Mutation
The most dangerous mutation is the p53 knockout mutation, which completely removes the cell’s ability to undergo apoptosis. In this case, 37.5% of all possible states result in cancerous growth, compared to just 3% in the wild type. MYC amplification and MDM2 overexpression are also harmful, as they can shut off p53. However, p21 loss is less severe, as p53 can still trigger cell death.

# Question 2: Role of the Feedback Loop
The MYC → MDM2 → p53 loop suppresses p53. In normal cells, this prevents p53 from remaining active for too long after stress. However, when MYC or MDM2 are overexpressed, the loop permanently disables p53. Simulations show that, in these cases, the network never reaches a p53-active attractor. This allows damaged cells to continue growing instead of dying.

In contrast, the p53 → p21 → MYC loop has a somewhat opposite effect:
When p53 is ON (e.g. by detecting DNA damage), it activates p21, which then inhibits MYC. This suppresses cell growth (as MYC promotes cell division), acting as a safeguard against uncontrolled proliferation. The loop is the opposite of growth-promoting feedback, preventing cell division when there is DNA damage.

# Question 3: Limitations of the Model
The model is limited because it only uses ON/OFF states and synchronous updates. This means it does not capture information about influence strength. It also leaves out many regulators, such as ARF and DNA repair, which makes the effects of oncogenesis appear stronger than they are in real cells. Finally, it forces binary fates of growth or death without intermediate outcomes such as senescence or recovery.

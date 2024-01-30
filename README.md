# Stochastic_SLAB2
Solving the stochastic SALB 2 problem using exact methods and simulation using GUROBI and SIMIO.

This project has the files of a proposed three-part algorithm to solve a stochastic line balancing problem in which the objective is to minimise the cycle time.

The three parts are:
1. Solve the mixed-integer linear programming model using Gurobi Optimiser. The files are:
   * SALB_gurobi: solver_grb.py
   * main.py
   * Instances_Data: "small data set_n=20/instance_n=20_391.alb"
        
2. Create a SIMIO simulation model that adds variability to the balancing using a set of parameters. 
    - The file "Scaled_Model.spfx" has the following experiments:
        - Verification (model verification)
        - Workers_Speed (speed of the workers in cells)
        - IAT (inter--arrival time)
        - Nu_Workers (number of workers in cells)
3. Optimise the value of the parameter by the SIMIO add-on OptQuest.
    - Optimisation using discreate IAT "OptQuest_Discreate_IAT.spfx"
    - Optimisation using stochastic IAT "OptQuest_Stochastic_IAT.spfx"

NOTE: User can download a free version of SIMIO from:

[SIMIO DOWNLOAD](https://www.simio.com/free-simulation-software/index.php)

This repository is related to the following paper:

Moncayo-Martínez, L.A.; Arias-Nava, E.H. Assessing by Simulation the Effect of Process Variability in the SALB-1 Problem. AppliedMath 2023, 3, 563-581. https://doi.org/10.3390/appliedmath3030030


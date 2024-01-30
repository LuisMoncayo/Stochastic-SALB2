# Stochastic_SLAB2
Solving the stochastic SALB 2 problem using exact methods and simulation using GUROBI and SIMIO.

This project has the files of a proposed three-part algorithm to solve a stochastic line balancing problem in which the objective is to minimise the cycle time.

The three parts are:
1. Solve the mixed-integer linear programming model using Gurobi Optimiser. The files are:
   * SALB_gurobi: solver_grb.py
   * main.py
   * Instances_Data: "small data set_n=20/instance_n=20_391.alb"
        
2. Create a SIMIO simulation model that adds variability to the balancing using a set of parameters. 
    - The file "SALB2-Model.spfx" has the following experiments:
        - Verification (model verification)
        - Nu_Workers
        - Workers_Distances
        - Workers_Distances_IAT
3. Optimise the value of the parameter by the SIMIO add-on OptQuest.
    - The file "SALB2-Model.spfx":
        - Workers_Distances_IAT

NOTE: User can download a free version of SIMIO from:

[SIMIO DOWNLOAD](https://www.simio.com/free-simulation-software/index.php)

This repository is related to the following paper:

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 12:30:44 2022

@author: luismoncayo
"""
#import networkx as nx
#import matplotlib.pyplot as plt
from SALB_gurobi.solver_grb import Line_Balancing_Grb
#---------------------------------------------------------
#with open("very large data set_n=1000/instance_n=1000_525.alb", 'r') as f:
with open("Instances_Data/small data set_n=20/instance_n=20_391.alb", 'r') as f:
    lines = [line.rstrip('\n') for line in f]
    print(lines)
f.close()

number_tasks = int(lines[lines.index('<number of tasks>')+1])
cycle_time =  int(lines[lines.index('<cycle time>')+1])

index_task_time = lines.index('<task times>')
tasks_num = []
tasks_times = []
for i in range(index_task_time+1, index_task_time+number_tasks+1):
    number = int(lines[i].split(" ")[0])
    time = int(lines[i].split(" ")[1])
    tasks_num.append(number)
    tasks_times.append(time)

index_precedence = lines.index('<precedence relations>')
precedence = []
k = index_precedence+1
while len(lines[k]) != 0:
    from_t = int(lines[k].split(",")[0])
    to_t = int(lines[k].split(",")[1])
    precedence.append([from_t, to_t])
    k+=1

# ------ GUROBI approach ---------------------------
solution = Line_Balancing_Grb(tasks_num,tasks_times, precedence)
#cycle_time = 7
#SALB1 = solution.SALB_1(cycle_time)

number_stations = 3
SALB2 = solution.SALB_2(number_stations)
# -------------------------------------------------
#G = nx.DiGraph()
#G.add_edges_from(precedence)
#nx.draw(G,pos=nx.shell_layout(G),with_labels = True)
#plt.show()

#for i in range(1,20+1):
#    print("Node %d"%i)
#    print(G.edges(i))

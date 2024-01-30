#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 13:10:44 2022

@author: luismoncayo
"""
import gurobipy as gp
from gurobipy import GRB
import math

class Line_Balancing_Grb:
    
    def __init__(self, tasks, processing_times, precedence_relationships):
        self.tasks = tasks
        self.processing_times = processing_times
        self.precedence_relationships = precedence_relationships
        
    def SALB_1(self, cycle_time):
        self.cycle_time = cycle_time
        max_stations = math.ceil(sum(self.processing_times)/self.cycle_time)
        
        SALB1_model = gp.Model("SLAB-1")
        y = SALB1_model.addVars(max_stations, vtype=GRB.BINARY, name="y")
        
        SALB1_model.setObjective(sum(y[s] for s in range(max_stations)), GRB.MINIMIZE)
        
        x = SALB1_model.addVars(range(len(self.tasks)), max_stations, vtype=GRB.BINARY, name="x")
        
        for s in range(max_stations):
            SALB1_model.addConstr( sum(self.processing_times[t]*x[t,s] for t in self.tasks)<= self.cycle_time*y[s], "Station[%d]" % s )

        for t in self.tasks:
            SALB1_model.addConstr( sum(x[t,s] for s in range(max_stations)) == 1, "Task[%d]" % t )
            
        for precedence in self.precedence_relationships:
            i = precedence[0]
            j = precedence[1]
            SALB1_model.addConstr( sum((1+s)*x[i,s] for s in range(max_stations))<= sum((1+s)*x[j,s] for s in range(max_stations)), "Precedence(%d,%d)" %(i,j) )
            
        for s in range(max_stations-1):
            SALB1_model.addConstr(y[s+1] <= y[s], "Stations(%d,%d)" %(s+1,s) )

        SALB1_model.write('instance1.lp')
        
        SALB1_model.optimize()

        print('\nMinimum number of stations: %g' % SALB1_model.ObjVal)

        print("\n---> Task per station")
        for s in range(max_stations):
            for t in self.tasks:
                if x[t,s].X > 0.99:
                    print('The task %d is done in station %d' %(t,s))
        print("\n---> Cycle time per station")
        for s in range(int(SALB1_model.ObjVal)):
            station_cycle = 0
            for t in self.tasks:
                if x[t,s].X > 0.99:
                    station_cycle += self.processing_times[t]
            print("The cycle time of station %d is %d" %(s,station_cycle))
        

    def SALB_2(self, stations):
        self.stations = stations
        SALB2_model = gp.Model("SLAB-2")

        cycle_time = SALB2_model.addVar(name="C")

        SALB2_model.setObjective(cycle_time, GRB.MINIMIZE)

        x = SALB2_model.addVars(range(1,len(self.tasks)+1), range(1,self.stations+1), vtype=GRB.BINARY, name="x")

        # The workstation's time must be less that or equal to the cycle time
        for s in range(1,self.stations+1):
            SALB2_model.addConstr( sum(self.processing_times[t-1]*x[t,s] for t in self.tasks)<= cycle_time, "Station[%d]" % s )

        # each task must be assigned to a station
        for t in self.tasks:
            SALB2_model.addConstr( sum(x[t,s] for s in range(1,self.stations+1)) == 1, "Task[%d]" % t )
            
        # prece
        for precedence in self.precedence_relationships:
            i = precedence[0]
            j = precedence[1]
            SALB2_model.addConstr( sum(s*x[i,s] for s in range(1,self.stations+1))<= sum(s*x[j,s] for s in range(1,self.stations+1)), "Precedence(%d,%d)" %(i,j) )

        #SALB2_model.write('model_SALB2.lp')

        # Solve
        SALB2_model.optimize()

        print("------------------------------------------")
        print('Cycle Time is: %g' % SALB2_model.ObjVal)
        print("------------------------------------------")
        print()
        #print("\n---> Task per station")
        for s in range(1,self.stations+1):
            print('Station %d' % s)
            print()
            station_cycle = 0
            task_in_statation = []
            for t in self.tasks:
                if x[t,s].X > 0.99:
                    task_in_statation.append(t)
                    station_cycle += self.processing_times[t-1]
            print("There are %d task and the tasks are:"%len(task_in_statation))
            print(task_in_statation)
            print("Cycle time is %d" %(station_cycle))
            print("++++++++++++++++++++++++++++++++++")
            print()
        
        
        
        
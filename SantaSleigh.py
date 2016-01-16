# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 13:58:24 2016
Main module to carry out the optimization of routes for Santa's Gift Delivery
@author: Rupak Chakraborty
"""

import math
from trip import Trip
from gift import Gift
import random 
import time
import pandas as pd
import SantaUtil 

SLEIGH_CAPACITY = 1000
INTIAL_POPULATION_SIZE = 100
MAX_ITERATIONS = 1000
TOP_K = 10
random.seed(time.time())
gift_filename = "Santa's Stolen Sleigh/gifts.csv"
TRIP_MUTATION_PROBABILITY = 0.7
GIFT_MUTATION_PROBABILITY = 0.3
TRIP_CROSSOVER_PROBABILITY = 0.67 #These can be rather should be fine-tuned for hyperparameter optimization

start = time.time()
print "Initiating Dataset Loading ...."
gift_list = SantaUtil.getGiftList(gift_filename)
end = time.time()
print "Time Taken to load dataset : ",end-start 

"""
Generates the initial population of trip routes to be taken

Params:
--------
gift_list: List containing the list of gifts to be delivered
initial_population_size: Integer containing the number of initial populations to be generated

Returns:
A List of trips denoting the order in which the gifts are to be delivered 
"""
def generateInitialTripListPopulation(gift_list,initial_population_size): 
    
    count = 0
    trip_list = list([])
    master_trip_population = list([])
    gift_trip_list = list([]) 
    
    while count < initial_population_size: 
        
        random.shuffle(gift_list)
        total_weight = 0 
        i = 0
        trip_list = list([])
        
        while i < len(gift_list):
            
            while i < len(gift_list) and (total_weight + gift_list[i].weight) <= SLEIGH_CAPACITY: 
                
                gift_trip_list.append(gift_list[i])
                total_weight = total_weight + gift_list[i].weight
                i = i + 1 
                
            trip_order = Trip(gift_trip_list,SantaUtil.tripCost(gift_trip_list))
            total_weight = 0
            gift_trip_list = list([])
            trip_list.append(trip_order)
                
        count = count+1
        master_trip_population.append(trip_list)
        
    return master_trip_population

print "Starting Generating Initial Population...."
start = time.time() 
initial_population = generateInitialTripListPopulation(gift_list,INTIAL_POPULATION_SIZE)
end = time.time()
print "Total Time Taken for Creating Initial Pool : ",end-start 

i = 0
fitness_population_map = {}  

for trip_gene in initial_population: 
    
    fitness_population_map[i] = SantaUtil.tripFitness(trip_gene)
    i = i + 1

ordered_fitness_list = SantaUtil.sortMapByValues(fitness_population_map)
best_solution_index = ordered_fitness_list[0][0]
best_solution_cost = ordered_fitness_list[0][1]

def generateBestSolution(initial_population,fitness_population_map,max_iterations):
    iteration = 0
    
    while iteration < max_iterations:
       
       trip_mutation = random.random()
       gift_mutation = random.random()
       
       if trip_mutation < TRIP_MUTATION_PROBABILITY:
           pass
       if gift_mutation < GIFT_MUTATION_PROBABILITY:
           pass
       SantaUtil.mutateGiftList()
       SantaUtil.mutateTripList()



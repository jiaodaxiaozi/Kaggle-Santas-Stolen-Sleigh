# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 13:58:24 2016
Main module to carry out the optimization of routes for Santa's Gift Delivery
@author: Rupak Chakraborty
"""

import math
import trip
import gift
import random 
import time
import pandas as pd
import SantaUtil 
random.shuffle(x)
SLEIGH_CAPACITY = 1000
INTIAL_POPULATION_SIZE = 100

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

def generateInitialTripListPopulation(gift_list,initial_population_size):
    count = 0;
    trip_list = list([])
    while count < initial_population_size:
        
        count = count+1
    
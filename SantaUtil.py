# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 23:21:29 2016
Defines a set of utility functions to be used for prediction
@author: Rupak Chakraborty
"""
import math

RADIUS_EARTH = 6773

def havesineDistance(lat_first,long_first,lat_second,long_second):
    
    lat_first = math.radians(lat_first)
    long_first = math.radians(long_first)
    lat_second = math.radians(lat_second)
    long_second = math.radians(long_second)
    
    
    

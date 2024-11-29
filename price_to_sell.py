#!/bin/python3

import math
import os
import random
import re
import sys
import statistics

#
# Complete the 'valuation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER reqArea
#  2. LONG_INTEGER_ARRAY area
#  3. LONG_INTEGER_ARRAY price
#

def valuation(reqArea, area, price):
    # find outliers
    area_price_list = {}
    
    # group all prices by their area
    for a, p in zip(area, price):
        if a in area_price_list:
            area_price_list[a].append(p)
        else:
            area_price_list[a] = [p]
    
    # Identify and filter out outliers
    filtered_area = []
    filtered_price = []
    
    for a in sorted(area_price_list.keys()):
        prices = area_price_list[a]
        
        # If only one house with specified area, ITS A OUTLIER
        if len(prices) == 1:
            continue
            
        # Calculate mean and standard deviation
        mean_price = statistics.mean(prices)
        std_dev_price = statistics.stdev(prices) if len(prices) > 1 else 0
        
        # Filter out the prices that deviate more than three stdev from the mean
        for p in prices:
            if abs(p - mean_price) <= 3 * std_dev_price:
                filtered_area.append(a)
                filtered_price.append(p)

                    
 # Return the average price of the filtered prices as the final valuation
    if filtered_price:
        return statistics.mean(filtered_price)
    else:
        return 0
    
    
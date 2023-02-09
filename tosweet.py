#!/usr/bin/env python3
"""
    To find the perfect number of tee spoons needed
"""
# n -> number of tea spoons of sugar req for the cake
# find x -> the point at which the cake becomes too sweet

n = 1
def find_x():
    """
        returns x using the given isTooSweet(i) function
        n: number of tea spoons required for the cake
        x: point at which the cake becomes too sweet
    """
    for x in range(1, n +1):
        if isTooSweet(x):
            return x

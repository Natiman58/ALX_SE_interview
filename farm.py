#!/usr/bin/env python3
"""
    a script to calculate the distance between
    a field and a water tower
"""


from typing import List


def max_distane(field: List[int], tower: List[int]) -> int:
    """
        return the distance between a field and a water tower
    """
    if len(field) > 0:
        for i in range(10**9):
            if field[i] == tower[i]:
                if field[i] <= tower[i] <= field[i + 1]:
                    max_dis = field[i + 1] - field[i]
                    return max_dis
            else:
                max_dis = tower[i] - field[i]
                return max_dis

            
l = max_distane([1, 5], [10])
print(f'Max distance: {l}')

#!/usr/bin/env python3
"""
   A special keybord to print chars
   A,  
"""
# Key_1: (A) -> print 1 'A'
# key_2: (Ctrl-A) -> select everything printed
# key_3: (Ctrl-C) -> Copy everything to buffer
# key_4: (Ctrl-V) -> print buffer contents
# find the max num of A to print

def Print_A_Max(n: int) -> int:
    """ max num of A to print
        n: number of ops to print A
    """
    input_list = list(range(n + 1))
    for i in range(3, n + 1):
        for j in range(2, i):
            max_val = max(input_list[i], input_list[j - 1] * (i - j))
            input_list[i] = max_val
    return input_list[-1]

a = Print_A_Max(2)
print(a)

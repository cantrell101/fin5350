# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 21:19:10 2016

@author: Carissa
"""

def is_nugget_number():
    n = [0]
    can = 6
    inarow = 0
    largest = []
    
    while inarow <= 6:
        if can - 6 in n or can - 9 in n or can - 20 in n:
            n.append(can)
            inarow += 1
        else:
            inarow = 0
            del largest [:]
            largest.append(can)
        can +=1
    print(largest)
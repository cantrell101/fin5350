# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 09:38:46 2016

@author: Carissa
"""

def numberguess(res):
    can = 50
    divider = 4
    tries = 1
    print("My first guess is", can)
    res = input("Is your number <, >, or = My guess?")
    
    while tries <= 6:
        if can == 50 and res == "=":
            break        
        else:
            if res == "=":
                break
            elif res == ">":
                can = can + round(100/divider)
            else:
                can = can - round(100/divider)
            print("I will guess...", can)
            res = input("Is your number <, >, or = My guess?")
            divider *= 2
            tries += 1
    
    print("Your number is", can, "and I guessed it in", tries, "try/tries!")
        

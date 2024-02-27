# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 09:47:30 2023

@author: adity
"""

def make_pizza(size,*toppings):
#summarize the pizza we are about to make
    print(f"Making a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"-{topping}")
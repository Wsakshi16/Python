# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 17:14:49 2023

@author: aditya
"""
#Assign:4
#pyramids

for i in range(4):
    for j in range(4):
        print("#",end=" ")
    print()
    
print("\n")
    
for i in range(4):
    for j in range(i+1):
        print("#",end=" ")
    print()
    
print("\n")
        
for i in range(4):
    for j in range(4-i):
        print("#",end=" ")
    print()


# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 17:26:46 2023

@author: adity
"""
#Assign:12
#Write python code to find fa bonacci series
def fibbo(n):
    lst=[]
    previous=0
    current=1
    lst.append(previous)
    for i in range(n-1):
        previous,current=current,previous+current
        lst.append(current)
    return lst
print(fibbo(11))
################################
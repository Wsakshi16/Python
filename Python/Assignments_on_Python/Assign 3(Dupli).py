# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 16:50:43 2023


@author: aditya
"""
"""
#Assign. 3:Write a program to find out is duplicate elements found in the list
lst1=[1,2,5,5,6,1,7]

def is_duplicate(lst1):
    for i in range(len(lst1)-1):
        
        if(lst1[i]==lst1[i+1]):
            return True
    return False
print(is_duplicate(lst1))
"""
        
lst1=[1,2,6,5,8,3,7]

def is_duplicate(lst1):
    for i in range(len(lst1)-1):
        for j in range(len(lst1)-1):
            if(lst1[i]==lst1[j]):
                return True
        return False
print(is_duplicate(lst1))

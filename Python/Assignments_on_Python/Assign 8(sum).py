# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 17:18:44 2023

@author: aditya
"""
#Assign:8
#Write a code to sum the numbers divisible by 5 or 7 in the list

lst=[1,2,5,7,14,55,45,21,49,8,9]

def return_sum(lst):
    sum=0
    for i in range(len(lst)):
        if(lst[i]%5==0 or lst[i]%7==0):
            sum=sum+lst[i]
print(return_sum(lst))
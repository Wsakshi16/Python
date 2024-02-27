# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 17:15:49 2023

@author: aditya
"""
#Assign:11
#Write a Code to generate the Random password
from random import randint
SHORTEST=7
LONGEST=10
MIN_ASCII=33
MAX_ASCII=126

def randomPassword():
    randomLength=randint(SHORTEST,LONGEST)
    result=" "
    for i in range(randomLength):
        randomChar=chr(randint(MIN_ASCII,MAX_ASCII))
        
        result=result+randomChar
    return result

print("Your random password is:",randomPassword())
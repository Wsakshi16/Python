# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 16:52:16 2023

@author: aditya
"""
#Assign:10
#Write a code check the given year is leap year or not
def is_leap_year(year):
    if(((year>0) and (year%4==0) and (year%100!=0)) or (year%400==0)):
        return True
    return False
print(is_leap_year(int(input("Enter the year:"))))


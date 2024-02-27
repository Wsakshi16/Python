# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 17:12:08 2023

Write a python code to remove outliers

@author: aditya
"""
#Assign:13
#Write a code to remove the ouliers from the given list
#Outliers
values=[89,105,100,97,10,6,4,12,27]
retval=sorted(values)
def removeOutliers(data,num_outliers):
    retval=sorted(data)
    for i in range(num_outliers):
        retval.pop(-1)
    return retval

print(removeOutliers(values,2))










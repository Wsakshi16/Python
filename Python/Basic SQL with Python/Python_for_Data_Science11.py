# -*- coding: utf-8 -*-
"""
Created on Wed May 10 15:47:54 2023

@author: adity
"""

#Arrays in NumPy
# Create ndarray
import numpy as np
arr = np.array([10,20,30])
print(arr)

#Output :
#[10,20,30]
#Create a Multi-Dimensional array
#Create a multi dimensional array
arr = np.array([[10,20,30],[40,50,60]])
print(arr)

#Output:
#[[10,20,30]
# [40,50,60]]
#Represent the Minimum Dimensions
#Use ndmin parameter to specify how many minimum
#dimensions you wanted to create an array with 
#minimum dimension
arr = np.array([10,20,30,40], ndmin = 2)
print(arr)
#Output:
#    [[10 20 30 40]]
arr = np.array([10,20,30,40], ndmin = 3)
print(arr)
#Output:
#    [[[10 20 30 40]]]
#Change the datatype 
#dtype parameter
arr = np.array([10,20,30,40], dtype = complex)
print(arr)
#Output:
#[10.+0.j 20.+0.j 30.+0.j 40.+0.j]

#Get the Dimesions of an array
#Get dimension of array
arr = np.array([[1,2,3,4],[7,8,6,7],[9,10,11,12]])
print(arr.ndim)
print(arr)
















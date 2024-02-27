# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 08:36:47 2023

Reading data in various formats

@author: adity
"""

import pandas as pd
f1=pd.read_csv('C:/1-Python/buzzers.csv')
f1
##################################################
import os
with open('buzzers.csv') as raw_data:
    print(raw_data.read())
##################################################
#Reading CSV data as Lists
import csv
with open('buzzers.csv') as raw_data:
    for line in csv.reader(raw_data):
        print(line)
#################################################
#Reading CSV data as dictionary
import csv
with open('buzzers.csv') as raw_data:
    for line in csv.DictReader(raw_data):
        print(line)
#################################################    
with open('buzzers.csv') as data:
    #ignore = data.readline()
    flights={}
    for line in data:
        k,v=line.split(',')
        flights[k]=v
flights    
################################################ 
#stripping then splitting your raw data
with open('buzzers.csv') as data:
    ignore = data.readline()
    flights={}
    for line in data:
        k,v=line.strip().split(',')
        flights[k]=v
flights    
#####################################
#pre-requisite to decorators
def plus_one(number):
    
    number1= number + 1
    return number1
plus_one(5)
###########################################
def plus_one(number):
    
    def add_one(number):
        number1= number + 1
        return number1

    result = add_one(number)
    return result
plus_one(4)
############################################
#Passing function as argument 
#to other function
def plus_one(number):
    
   result1= number + 1
   return result1
    
def function_call(function):
    result = function(5)
    return result

function_call(plus_one)
##########################################3
def hello_function():
    def say_hi():
        return 'hi'
    return say_hi
hello=hello_function()
hello()
    
    
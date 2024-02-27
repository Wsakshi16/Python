# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 08:21:45 2023

@author: aditya
"""

#################################
#Pre-requisite to decorators
def plus_one(number):
    number1 = number + 1
    return number1
plus_one(5)
###########################################
#defining Functions Inside other Function
def plus_one(number):
    
    def add_one(number):
        number1 = number + 1
        return number1
    
    result = add_one(number)
    return result
plus_one(4)
############################################
#Passing Functions as arguments
#to other Functions
def plus_one(number):
    result1 = number + 1
    return result1

def function_call(function):
    result=function(5)
    return result

function_call(plus_one)
##########################################################
#Functions retursning other function
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi
hello=hello_function()
hello()
#Always remember when you call hello_function()
#directly then it will display object not hi
#therefore you need to assign it to hello first 
#then call hello() function
###################################################
#
def say_hi():
    return 'hello there'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
decorate = uppercase_decorator(say_hi)
decorate()
######################################################
@uppercase_decorator
def say_hi():
    return 'hello there'

say_hi()
############################################################
#Applying multiple decorators to a single function
#we can use multiple decorators to a single function.
#however, the decorators will be applied in the order
#that we've called them.
def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper()
@split_string
@uppercase_decorator
def say_hi():
    return 'hello there'
say_hi()
#######################################################
numbers = [2,6,7,8]
def cal_square(numbers):
    result=[]
    for i in numbers:
        result.append(i*i)
    return result

def cal_cube(numbers):
    result=[]
    for i in numbers:
        result.append(i*i*i)
    return result

print(cal_square(numbers))
print(cal_cube(numbers))
###############################################
#Estimation of execution
import time
def cal_square(numbers):
    start= time.time()
    result=[]
    for i in numbers:
        result.append(i*i)
        
    end=time.time()
    print((end-start)*1000)
    print("Took " + str((end-start)*1000) + "\tmil sec")
    return result

def cal_cube(numbers):
    start= time.time()
    result=[]
    for i in numbers:
        result.append(i*i*i)
        
    end=time.time()
    print((end-start)*1000)
    print("Took " + str((end-start)*1000) + "\tmil sec")
    return result

array = range(1,100000)
out_square = cal_square(array)
out_cube = cal_cube(array)
##############################################################3
import time
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func._name_ +" took " + str((end-start)*1000) + " mil sec")
        return result
    return wrapper
@time_it
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result
@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

##########################################################

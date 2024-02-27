# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 09:17:39 2023

@author: aditya
"""

#####################Itertools##########################
lst=[]
for num in range(0,20):
    lst.append(num)
print(lst)
################################
#We can write the same method using list comprehension
lst=[num for num in range(0,20)]
print(lst)
##################################
#To Capitalize the first letter
names = ['dada','mama','kaka']
lst= [name.capitalize() for name in names]
print(lst)
#####################################
#list comprehension with if statement
def is_even(num):
    return num%2==0
lst=[
     num
     for num in range(10)
     if is_even(num)
     ]
print(lst)
##############################################
#We can Write values using list comprehension
lst = [f"{x}{y}"
       for x in range(3)
       for y in range(3)
       ]
print(lst)
############################################
#Set Comprehension
lst = {x
       for x in range(3)
       }
print(lst)
############################################
#Dictionary Comprehension
dict = {x:x*x
        for x in range(3)
        }
print(dict)
###########################################
#Generatior
#It is another way of creating iterators in a simple way 
#where it uses the keyword "yield" instead of returning it in a defined function
#generators are implemented using a function
gen = (x
       for x in range(3)
       )
print(gen)
for num in gen:
    print(num)
###################################################
gen = (x
       for x in range(3)
       )
next(gen)
##############################################
gen=(x for x in range(3))
next(gen)
next(gen)
###############################################
#Function which returns multiple values
def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(6):
    print(num)
######################################################
#now instead of using for loop we can write 
def range_even(end):
    for num in range(0,end,2):
        yield num
gen=range_even(6)
print(next(gen))
print(next(gen))
print(next(gen))
##############################################
#Chaining generators
def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
        
passwords=["not-good","AdityaGaikwad","9064348432"]

for password in hide(lengths(passwords)):
    print(password)
###################################################
#Printing list with index
lst=["Milk","Egg","Bread"]
for index in range(len(lst)):
    print(f"{index+1} {lst[index]}")












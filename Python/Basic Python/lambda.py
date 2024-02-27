# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 08:26:19 2023

@author: adity
"""

def add(a,b,c):
    sum= a+b+c
    return sum
print(add(4,5,6)) 
add=lambda a,b,c:a+b+c
add(4,5,6)
###################################
def mul(a,b,c):
    multi= a*b*c
    return multi
print(mul(4,5,6)) 
mul=lambda a,b,c:a*b*c
mul(4,5,6)
############################################
val=lambda *args:sum(args)
val(2,3,4,5,6)
val(34,5,5,565,4,78)
##########################################
#*args
def myfun(*args):
    for i in args:
        print(i)
        
myfun("Hello","python","how","are","you")

myfun("Hello","python")
myfun("This","is","python")
#######################################3
def person(name,*data):   #arbitary argument
    print(name)
    print(data)
person('Navin',28,'Mumbai',987986)
#############################################
def person(name,**data):  #Keyword argument:we need to pass key and value
    print(name)
    print(data)
    
person(name='Navin',age=28,place='Mumbai',Mob=987986)
####
person=lambda **args:args
person(name='Navin',age=28,place='Mumbai',Mob=987986)
    
##############################################
def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person(name='Navin',age=28,place='Mumbai',Mob_no=987986)
################################################
val=lambda **data:sum(data.values())
val(a=2,b=4,c=7,d=32)
#############################################
person=lambda **data:[(j) for i,j in data.items()]
person(name='Navin',age=28,place='Mumbai',Mob_no=987986)
##############################################
lst1=[3,4,6,4,7]
sqr=lambda lst1:[i**2 for i in lst1]
print(sqr(lst1))
#####################################################





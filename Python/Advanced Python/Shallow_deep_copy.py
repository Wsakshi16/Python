# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 08:16:39 2023

@author: adity
"""
'''
In python, assignment statements (obj_b = obj_a)  do not create real copies 
it only 
'''

#Assignment operator
#This will only create a new variable with the same reference.Modifying one will affect the other.
list_a = [1,2,3,4,5]
list_b = list_a

list_a[0] = -10
print(list_a)
print(list_b)
######################################################################################
#Shallow copy
#
#
import copy
list_a = [1,2,3,4,5]
list_b = copy.copy(list_a)



#################################################################
#But with nested objects, modifying on level 2 or deeper does affect the other!
import copy
list_a = [[1,2,3,4,5],[6,7,8,9,10]]
list_b = copy.copy(list_a)

#affects the other!
list_a[0][0]=-10
print(list_a)
print(list_b)
################################################################
#Deep copies
#Full independent clones. Use copy.deepcopy().
import copy
list_a = [[1,2,3,4,5],[6,7,8,9,10]]
list_b = copy.deepcopy(list_a)

#not affects the other
list_a[0][0]= -10
print(list_a)
print(list_b)
#################################################################









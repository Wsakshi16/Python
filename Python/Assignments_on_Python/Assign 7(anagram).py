# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 16:55:34 2023

@author: aditya
"""
#Assign :7
#Write a code to check a given string is anagram or not
 
def are_anagram(str1,str2):
    #convert the strings into regular format 
    a=list(str1.replace(" ","").lower())
    b=list(str2.replace(" ","").lower())
    
    if(len(a)!=len(b)):
        return False
    else:
        return(sorted(a)==sorted(b))
    
print(are_anagram("elb ow ","belO w"))
    
    






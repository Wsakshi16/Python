# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 17:25:38 2023

@author: aditya
"""
#Assign :9
def reverse_words(input):
    if input=="":
        return "You have entered a wrong input"
    else:
        words=input.split()
        reverse_sentence=" ".join(reversed(words))
    return reverse_sentence

print(reverse_words(input("Enter here: ")))
        

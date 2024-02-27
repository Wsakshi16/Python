# -*- coding: utf-8 -*-
"""
Created on Wed May 17 15:03:38 2023

@author: adity
"""
#Assignment on NLP
txt = 'This is Artificial Intelligence Era'
txt.split()
################################################################
txt = 'India: has;, great history: in 2023 india is leading to its glorious future!'
import re
pattern=r'(?:,|;|\s)\s*' #This are seperators
x=re.split(pattern,txt)
print(x)
############################################################
txt = "Rama wentr to Haridwar to get Gangajal"
#Check the text Gangajal
txt.endswith('Gangajal')
###############################################################
choices = ('Mango','Banana')
txt = 'I like Mango'
txt.endswith(choices)
txt.startswith(choices)
##################################################
txt = 'I like Mango'
#Slicing a string
print(txt[7:])
print(txt[-5:])
####################################################
txt = 'I had been visiting Pune on 11/05/2023'
print(re.match(r'\d\d/\d/\d\d\d\d',txt))



#################################################





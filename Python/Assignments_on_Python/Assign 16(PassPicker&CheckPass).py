# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 22:59:25 2023

Write a code to combine password picker and checking that the password is good or not

@author: adity
"""

import string
adjectives = [ ]
adj = input("Enter the Adjective: ")
adjectives.append(adj)
print(adjectives)
nouns= [ ]
n = input("Enter the Noun: ")
nouns.append(n)
print(nouns)
import random

print("Welcome to password picker!")
while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number= random.randrange(0,100)
    special_char = random.choice(string.punctuation)
    password = adjective + noun + str(number) + special_char
    print("your new password is:  %s" %password)
   
    #To check that the password is good or not
    def checkPassword(password):
        has_upper=False
        has_lower=False
        has_num=False
        has_char=False
        
        for ch in password:
            if ch>'A' and ch<'Z':
                has_upper=True
            elif ch>'a' and ch<'z':
                  has_lower=True
            elif ch>'0' and ch<'9':
                  has_num=True
            elif (ch=='@'or ch=='$' or ch=='_'):
                   has_char=True
        if len(password)>=8 and has_upper and has_lower and has_num and has_char:
            return True
        else:
            return False
        
    if checkPassword(password):
       print("Valid Password")
       break
    else:
       print("Invalid Password")

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 17:22:55 2023

@author: aditya
"""
#Assign14
#Write code for checking passward is good or not
#Primary conditions for password validation:
#Minimum 8 characters.
#The alphabet must be between [a-z]
#At least one alphabet should be of Upper Case [A-Z]
#At least 1 number or digit between [0-9].
#At least 1 character from [ _ or @ or $ ].

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
p=input("Enter a password: ")
if checkPassword(p):
    print("Valid Password")
else:
    print("Invalid Password")
###########################################################################
    
    

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 16:44:08 2023.

Password picker

@author: aditya
"""
import string
adjectives = ['sleepy','slow','smelly',
              'wet','fat','red',
              'orange','yellow','green',
              'blue','purple','fluffy',
              'white','proud','brave']
#pick the nouns
nouns= ['apple','dinosour','ball','toatser','goat','dragon','hammer',
        'duck','panda']
import random

adjective = random.choice(adjectives)
noun = random.choice(nouns)
#select a number
number= random.randrange(0,100)
#select a special character
special_char = random.choice(string.punctuation)
#Create anew secure password
password = adjective + noun + str(number) + special_char
print("your new password is:  %s" %password)

#Another one
#You can use white loop to generate
#another
print("Welcome to password picker!")
while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number= random.randrange(0,100)
    special_char = random.choice(string.punctuation)
    password = adjective + noun + str(number) + special_char
    print("your new password is:  %s" %password)
    response = input('Would you like another password?')
    if response == 'n':
        break
    









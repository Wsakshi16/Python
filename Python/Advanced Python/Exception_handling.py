# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 09:13:17 2023

Exception Handling

@author: aditya
"""
#the error signifies a situation that mostly happens due to the absence of the system resources
#Exception are the issues that can appear at runtime and compile time
#it majorly arises in the code or program authored by the developers

#Exception are handled with a try-except block

print(5/0)

try:
    print(5/0)
except Exception as e:
    print(e)
    

print("Give me two numbers, I will divide them.")
print("Enter q to quit.")
while True:
    first_number = input("\n1st Number: ")
    if first_number == 'q':
       break
    second_number = input("\n2nd Number: ")
    if second_number == 'q':
        break
    ans = int(first_number) / int(second_number)
    print(ans)
###################################################
#Handling and file Exception
filename = "alice1.txt"
with open(filename, encoding='utf-8') as f:
    contents = f.read()
######################################
filename = "alice1.txt"
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist")
######################################################
#The Json (JavaScript Object Notation) format using json.dump() and json.load()
#Working with Json file
import json
numbers = [2,4,6,3,8]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers,f)
############################################
#Saving data with json is useful when you are working with user-generated data
import json
username = input("What is your name?")
filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username,f)
print(f"We will remember you when you come back {username}!")
#############################################################
#Now let's write a new program thats greets a user whose name has already been stored

import json
filename = 'username.json'
with open(filename) as f:
    username = json.load(f)
print(f"Welcome back, {username}!")
######################################################
#Load the username, if it has been stored previously.
#Otherwise, prompt for the username and store it
filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
     
    username = input("What is your name?")
    with open(filename, 'w') as f:
        json.dump(username,f)
    print(f"We will remember you when you come back {username}!")
    
else:
    print(f"Welcome back, {username}!")
    
















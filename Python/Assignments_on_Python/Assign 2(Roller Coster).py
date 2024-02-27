# -*- coding: utf-8 -*-
"""
Assignment No. 2
write a python code using logical operator and if elif
so as to allow for roller coster also ask user age and chargee ticket accordingly

conditions are 

Created on Wed Apr  5 17:23:14 2023

@author: aditya
"""
print("Welcome to the Roller Coster...")
height = int(input("Enter your height in cm: "))
if height >= 120:
    print("You are eligible for roller coster")
    age = int(input("Enter your age in years: "))
    bill = 0
    
    if age <= 12:
        print("Ticket is 5$")
        bill = 5
    elif age > 12 and age <= 18:
        print("Ticket is 7$")
        bill = 7
    elif age > 18 and age <= 45:
        print("Ticket is 12$")
        bill = 12
    elif age > 45 and age <= 55:
        print("Ticket is 50$")
        bill = 50
    else:
        print("Sorry you are not Eligible for this ride...")
else:
    print("Sorry you are not Eligible for this ride...")
    
photo = input("Do you want photo Y/N: ")
if photo == 'Y':
    bill += 3
    print("Bill:",bill,"$")
elif photo == 'N':
    print("Bill:",bill,"$")

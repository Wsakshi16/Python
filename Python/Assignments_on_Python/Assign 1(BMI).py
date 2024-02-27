# -*- coding: utf-8 -*-
"""
write a python code to calculate the BMI
Created on Wed Apr  5 16:51:26 2023

@author: aditya
"""
#Assign.:1
#write a python code to calculate the BMI
height=float(input("please enter your height in m: "))
weight=float(input("please enter your weight in kg: "))
BMI=round((weight/(height*height)),2)
print(BMI)
if BMI<18.5:
    print(f"You are under weight and your BMI is:{BMI} Kg/m^2")
elif BMI>18.5 and BMI<25:
    print(f"You are normal weight and your BMI is:{BMI} Kg/m^2")
elif BMI>25 and BMI<30:
    print(f"You are overweight and your BMI is:{BMI} Kg/m^2")
elif BMI>30 and BMI<35:
    print(f"You are Obese and your BMI is:{BMI} Kg/m^2")
elif BMI>35:
    print(f"You are Clinically obese and your BMI is:{BMI} Kg/m^2")

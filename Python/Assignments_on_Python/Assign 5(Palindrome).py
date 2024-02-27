# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 19:30:47 2023

@author: aditya
"""
#Assign:5
#Write a code to check a given number is palindrome or not

num = int(input("Enter a number: "))
a=num
rev = 0

while num > 0:
    b = num % 10
    rev = rev * 10 + b 
    num = num // 10
    
if a==rev :
   print("it is a palindrome...")
else:
   print("it is not a palindrome...")

'''   
num = (input("Enter a number: "))
if(num==num[::-1]):
      print("The num is a palindrome")
else:
      print("Not a palindrome")
'''
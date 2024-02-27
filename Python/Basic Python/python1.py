# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 16:53:36 2023

@author: aditya
"""

print('Hello World')

#types of numbers
x=3
print(x)
print(type(x))

age = input('Please enter your age: ')
print(type(age))
print(age)

age1 = input('Please enter your age: ')
print(type(age1))
print(age1)

age2 = input('Please enter your age: ')
print(type(age2))
print(age2)

age = age1+age2
print(age)

#typecasting
age = int(input('Please enter your age: '))
print(type(age))
print(age)

age1 = int(input('Please enter your age: '))
print(type(age1))
print(age1)

age2 = int(input('Please enter your age: '))
print(type(age2))
print(age2)

age = age1+age2
print(age)

int_value = 100
string_value='1.5'
float_value=float(int_value)
print('int value as a float:',float_value)
float_value=float(string_value)
print('int value as a float:',float_value)

#complex numbers
c1=1
c2=2j
print('c1:',c1,',c2:',c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)

#boolean
all_ok = True
print(all_ok)
all_ok = False
print(all_ok)
print(type(all_ok))

status = bool(input('OK it is confirmed: '))
print(status)
print(type(status))

#Arithmetic Op
home = 10
away = 15
print(home + away)
print(type(home + away))
print(10*4)
print(type(10*4))

a=20
b=5
print(b-a)
print(type(b-a))

print(100//5)
print(type(100//5))

print(100%13)

a=5
b=3
print(a**b)

#assignment Operator
x=0
x+=1
print(x)

winner=None
print(winner is None)
print(winner is not None)
print(type(winner))

#indentation
num = int(input('Enter a Number: '))
if num > 0:
print(num)

#now give it indentation
num = int(input('Enter a Number: '))
if num > 0:
   print(num)

#Else in an if statement
num = int(input('Enter yet another Number: '))
if num<0:
   print('Its Negative')
else:
    print('Its not Negative')

#Use of elif
savings = float(input("Enter how much you have in savings: "))
if savings == 0:
    print('Sorry No savings')
elif savings < 500:
    print('Well Done')
elif savings < 1000:
    print('Thats a tidy sum')
elif savings < 10000:
    print('Welcome Sir!')
else:
    print('Thank You...')

#While Loop
count = 1
print('Starting')
while count <= 10:
    print(count)
    count +=1

#For Loop
print('print out values in range')
for i in range(2,10):
    print(i)
print('Done')

print('Only print code if all iterations completed')
num = int(input('Enter a number to check for: '))
for i in range(0,16):
    if i == num:
        break
    print(i)
print('Done')

#anonymous loop variable
for _ in range(0,10):
    print('.',end='')
    print()
    
#for horizontal
for _ in range(0,10):
    print('.',end='')









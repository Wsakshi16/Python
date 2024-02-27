# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 09:13:03 2023

@author: aditya
"""
############################Functions###########################
def prime_num(num):
    for i in range(2,num):
        if(num%i==0):
           return "The number is not prime"
           break
    return "The number is prime"
print(prime_num(13))
##########################################
def greet_user(username):
#Display a simple greeting
    print(f"Hello...., {username}!")
greet_user(input("Enter Text Here:"))
########################################################

#arguments and parameters
#the variable username in the def of greet_user()
def describe_pet(animal_type, pet_name):
    #display info about a pet
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s Name is {pet_name}.")
describe_pet("Dog","Rocky")
#order matters in positional arguments

describe_pet("Rocky","Dog")

#Default values
#when writing a function, you can define a default value
def describe_pet(pet_name,animal_type='Dog'):
    #display information about a pet
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s Name is {pet_name.title()}.")
describe_pet("Rocky")
###########################################
#avoiding argument errors
def describe_pet(animal_type,pet_name):
    #display info about a pet
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s Name is {pet_name.title()}.")
describe_pet()
######################################################
#return values
def get_formated_name(first_name,last_name):
#return a full name neatly formated
    full_name = f"{first_name} {last_name}"
    return full_name
musician = get_formated_name('Ram','Sarkar')
print(musician)
#####################################################
#returning a dictionary
def build_person(first_name,last_name):
#return a dictionary of information about a person
    person = {'first': first_name,'last': last_name}
    return person
musician = build_person('Ram','Sarkar')
print(musician)
    
###################################################
#passing a list
#you'll often find it useful to pass a list to the function
#names, numbers or more complex objetcs, such as dictionaries
def greet_user(names):
#print a simple greeting to each user in the list
    for name in names:
        msg = f"Hello, {name.title()}!..."
        print(msg)
usernames = ['Sanket','Aditya','Sakshi','Pratik']
greet_user(usernames)
#####################################################
#Passing a arbitrary numbers of arguments
def make_pizza(*toppings):
#print the list of toppings that have been requested
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushroom','green peppers','extra cheese')
#now we can replace the print() call with a loop that run the 
#list of toppings and describe the pizza being ordered
def make_pizza(*toppings):
#summarize the pizza we are about to make
    print("Making a pizza with following toppings: ")
    for topping in toppings:
        print(f"-{topping}")
make_pizza('pepperoni')
make_pizza('mushroom','green peppers','extra cheese')
#########################################################
#mixing positional and arbitrary argument
def make_pizza(size,*toppings):
#summarize the pizza we are about to make
    print(f"Making a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"-{topping}")
make_pizza(16,'pepperoni')
make_pizza(12,'mushroom','green peppers','extra cheese')
############################################################
#importing a file and passing them arguments
import pizza
pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(12,'mushroom','green peppers','extra cheese')
############################################################
#importing a specific functions
from pizza import make_pizza
make_pizza(16,'pepperoni')
make_pizza(12,'mushroom','green peppers','extra cheese')
#using as to give a functions as Alias
from pizza import make_pizza as mp
mp(16,'pepperoni')
mp(12,'mushroom','green peppers','extra cheese')
######################################################
#using as to give an Alias
from pizza import make_pizza as p
p.make_pizza(16,'pepperoni')
p.make_pizza(12,'mushroom','green peppers','extra cheese')
#######################################################
#Importing all Functions in a module
from pizza import *
make_pizza(16,'pepperoni')
make_pizza(12,'mushroom','green peppers','extra cheese')

#Scope of the variable
#local variable:Declare in the function and access only in that function that is restricted
#Global variable:Declare in the module and access globally



-
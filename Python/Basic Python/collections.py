# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 08:27:41 2023

@author: aditya
"""
#Collections
tup1 = (1,4,5,6)
print(f'tup[0]:\t{tup1[0]}')
print(f'tup[1]:\t{tup1[1]}')
print(f'tup[2]:\t{tup1[2]}')
print(f'tup[3]:\t{tup1[3]}')

#Iterations over tuple

#tuple related function
tup2=(2,4,'adi',8,True)
print(len(tup2))

tup4 = ('Apple','Orange','Plum','Apple','Apple')
#tuples allow duplication
print(tup4.count('Apple'))
print(tup4.index('Apple'))
print(tup4.count('Orange'))
print(tup4.index('Plum'))

#checking if element exists
if 'Apple' in tup4:
    print('Apple is in the tuple')
if 'Mango' not in tup4:
    print('Mango is not in the tuple')
    

#creating lists
lst1 = ['John','Paul','George','Ringo']
lst1 = [1, 43.5, True]
lst2 = ['Apple','Orange',31]
root_list=['John',lst1,lst2,'Denise']
print(root_list)

lst1 = ['John','Paul','George','Ringo']
print(lst1[-1])
print(lst1[2])
print(lst1[3])

lst1 = ['John','Paul','George','Ringo','Ringo']
print(lst1[-1])
print(lst1[1:3])
print(lst1[:3])
print(lst1[1:])
print(lst1[-3:-1])

#adding to the list
lst1 = ['John','Paul','George','Ringo']
lst1.append("Pete")
print(lst1)

#adding multiple elements
lst1 = ['John','Paul','George','Ringo']
lst1.extend('Pete','Hey','hello')
print(lst1)

#Removing an item
lst2 = ['Aditya','Sakshi','Rutuja','Pratik']
print(lst2)
lst2.remove('Sakshi')
print(lst2)

lst3 =['Once', 'upon', 'a', 'time']
print(lst3)
print(lst3.pop(2))
print(lst3)

#inserting into a list
a_list=['Aditya','Sakshi','Rutuja','Pratik']
print(a_list)
a_list.insert(2,'Sanket')   #(index,element) at what index you want to insert
print(a_list)

#list concentation
lst1=[3,4,6]
lst2=[3,7,9]
lst3=lst1+lst2
print(lst3)

#######################################################
#Creating a Set
#set do not print the repeated items in set
basket = {'Apple','Orange','Plum','Apple','Apple'}
print(basket)

#Accessing elements in a set
for item in basket:
    print(item)
    
#Adding items to the set
basket = {'Apple','Orange','Plum','Apple','Apple'}
basket.add('Mango')
print(basket)

#Adding more than one element
basket = {'Apple','Orange','Plum','Apple','Apple'}
basket.update(['Mango','Banana'])
print(basket)

#Obtaining the length of a set
basket = {'Apple','Orange','Plum','Apple','Apple'}
print(len(basket))

#Obtaining max and min values in set
basket1 = {3,5,-9,30,394}
print(max(basket1))
print(min(basket1))

#Removing an Element
basket = {'Apple','Orange','Plum','Apple','Apple','Mango','Banana'}
print(basket)
basket.remove('Apple')
basket.discard('Plum')
print(basket)

#set operations
s1 = {'Apple','Orange','Plum','Banana'}
s2 = {'lime','Orange','Mango'}
print('Union: ',s1 | s2)
print('Intersection: ',s1 & s2)
print('Difference: ',s1 - s2)


######################################################################
#Dictionaries
#Changeable(Mutable) and Indexed
capitals = {
    'Maharashtra': 'Mumbai',
    'Gujrat': 'Ahmadbad',
    'UP': 'Lakhnow',
    'Karnataka': 'Banglore',
    'Andhrapradesh': 'Hydrabad'}
print(capitals)
#Accessing items via key
print('capitals[Maharaashtra]: ',capitals['Maharashtra'])
#Adding a new entry
capitals['West Bengal']='Kolkata'
capitals

#changing a key value
capitals['Gujrat']='Gandhinagar'
print(capitals)
#removing an entry
capitals.pop('Karnataka')
print(capitals)
del capitals['UP']
print(capitals)

#Accessing elements

capitals = {
    'Maharashtra': 'Mumbai',
    'Gujrat': 'Ahmadbad',
    'UP': 'Lakhnow',
    'Karnataka': 'Banglore',
    'Andhrapradesh': 'Hydrabad'}
for states in capitals:
    print(states, end=', ')
    print(capitals[states])
#values,keys and items
print(capitals.values())
print(capitals.keys())
print(capitals.items())
#########################################
#checking key membership
print('Karnataka' in capitals)
print('bihar' not in capitals)

#obtaining a length of a Dictonary
print(len(capitals))

#dictionaries can have values in tuple
season={'summer':('Feb','March','April','May'),
        'Rainy':('June','July','August','Sept'),
        'winter':('Oct','Nov','Dec','Jan')}
print(season['Rainy'])
print(season['Rainy'][1])

#Dictionary methods
#get() is a useful method to access the values of a keys in dictionary
print(capitals.get('UP'))
#duplicates not allowed
#dictionary can not have two same keys 
dict2= {
        "Brand" : "Maruti",
        "Model" : "Breeza",
        "Year" : "2021",
        "Year" : "2020"
        }
print(dict2)
########################################
#Loop through a dictionary, it will show only
for x in dict2:
    print(x)
#print all values in the dictionary, one by one
for x in dict2:
    print(dict2[x])
#you can also use the values() method to return the values
for x in dict2.values():
    print(x)
#you can use the keys() method to return the keys
for x in dict2.keys():
    print(x)
    
#you can copy the dictionary using copy() method
mydict=dict2.copy()
print(mydict)
##############################
class Person(object):
 
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
 
    def display(self):
        print(self.name)
        print(self.idnumber)
         
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
     
# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
 
        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
         
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))
 
 
# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")
 
# calling a function of the class Person using
# its instance
a.display()
a.details()
#################################################

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 08:37:23 2023

@author: aditya
"""

#File Handling
with open('hello.txt') as file_object:
    content=file_object.read()
print(content)
#Observe the extra line at the end of output
###########################################
#to avoid this rstrip() method is used
with open('hello.txt') as file_object:
    content=file_object.read()
print(content.rstrip())
#rstrip() removes the whitespace,
#"hello.txt"-relative path
#"c:/1-Python/hello.txt"-Absolute path
#we can access all the files using absolute path
with open('c:/1-Python/hello.txt') as file_object:
    content=file_object.read()
print(content.lstrip().rstrip())
############################################
#Reading line by line
filename='hello.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line,end='')
###########################################
#to remove the blank space between two line we again use the rstrip() method
filename='hello.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
  
#Making a list of lines from a file
filename='hello.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
for line in lines:
        print(line.rstrip())
##################################################

#working with file's contents
filename='hello.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
    hello_string = ''
    for line in lines:
        hello_string += line.rstrip()
        print(hello_string)
        print(len(hello_string))
###################################################
        
#Writing to a file
filename = 'pragramming.txt'

with open(filename,'w') as file_object:
    file_object.write("I love Pragramming......")
##################################################
#Writing it multiple lines
filename = 'pragramming.txt'

with open(filename,'w') as file_object:
    file_object.write("I love Pragramming......")
    file_object.write("I love creating new games......")
###########################################################
#Including newlines in your calls to write() makes each string appear on its own line
filename = 'pragramming.txt'

with open(filename,'w') as file_object:
    file_object.write("I love Pragramming......\n")
    file_object.write("I love creating new games......\nHiii....")
##############################################################
#Appending to a file
filename = 'pragramming.txt'

with open(filename,'a') as file_object:
#we use the 'a' argument to open the file for appending mode
#it will not erase the previous date in the file
    file_object.write("\nI also love to ride a bike......\n")
    file_object.write("I love cooking......\nHiii....")







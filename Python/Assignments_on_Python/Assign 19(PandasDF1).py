# -*- coding: utf-8 -*-
"""
Created on Wed May  3 21:04:49 2023

@author: adity
"""
#Assignment
import pandas as pd
df = pd.read_csv('C:/1-Python/Assignments/AutoInsurance.csv')
df
#For number of rows and columns
df.shape
#Total no of shells
df.size

#Accessing one column contents
df['Sales Channel']

#Accessing two columns contents
df[["Customer","State"]]

#select certain rows and assign it to another dataframe
df2=df[55:]
df2
df3=df[445:1000]
df3

#accessing certain cell from column 'Vehicle Class'
df['Vehicle Class'][3]

#Describe DataFrame for all numeric column
df.describe()

#rename() – Renames pandas DataFrame columns
df.columns=['A','B','C','D','E','F','G','H','I','J','K','L',
            'M','N','O','P','Q','R','S','T','U','V','W','X']
df
# Rename Column Names using rename() method
df2 = df.rename({'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 
                 'I':9 ,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,
                 'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24}, 
                axis=1)
df2

#Drop DataFrame Rows and Columns
# Drop rows by labels
df = pd.read_csv('C:/1-Python/AutoInsurance.csv')
df
df1=df.drop([3,5])
df1

# Delete Rows by position
df1=df.drop([1,34,3342,4564,787]) 
df1

df1=df.drop([1769])
df1

# Delete Rows by Index Range
df1 = df.drop(range(0,9000))
df1

#Pandas Select Rows by Index
df3=df[999:1000]
df3




















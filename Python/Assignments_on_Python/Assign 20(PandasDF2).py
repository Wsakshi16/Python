# -*- coding: utf-8 -*-
"""
Created on Thu May  4 19:49:21 2023

@author: adity
"""

##Assignment 
import pandas as pd
df = pd.read_csv('C:/1-Python/Assignments/boston_data.csv')
#df = pd.DataFrame(df)
df

# Convert all types to best possible types
df2=df.convert_dtypes()
print(df2.dtypes)

# Change All Columns to Same type
df1 = df.astype(int)
df1
print(df1.dtypes)

#Change type for one or multiple columns
df1 = df.astype({"zn":int,"nox":float})
print(df1.dtypes) 

# Convert Data Type for All Columns in a List
df = pd.DataFrame(df)
df.dtypes
cols = ['age', 'indus','rad']
df[cols] = df[cols].astype('int')
df.dtypes

#Ignores error
df = df.astype({"crim": int},errors='ignore')
df.dtypes
# Generates error
df = df.astype({"chas": int},errors='raise')
# Converts age column to numeric type
df = df.astype(str)
print(df.dtypes)
df['age'] = pd.to_numeric(df['age'])
df.dtypes


#############################################################

import pandas as pd
df = pd.read_csv('C:/1-Python/boston_data.csv')
df = pd.DataFrame(df)
df
#Drop Column by Name
# Drops 'Fee' column
df2=df.drop(["age"], axis = 1)
print(df2)

# Explicitly using parameter name 'labels'
df2=df.drop(labels=["tax"], axis = 1)

# Alternatively you can also use columns instead of labels.
df2=df.drop(columns=["tax"], axis = 1)
#################################################
# Drop column by index.
print(df.drop(df.columns[2], axis = 1))


# using inplace=True
df.drop(df.columns[[2]], axis = 1, inplace=True)
print(df)
#####################################




df = pd.DataFrame(df)
df

#Drop Two or More Columns By Label Name
df2=df.drop(["tax", "rad"], axis = 1)
print(df2)

#######################################
#Drop Two or More Columns by Index
df = pd.DataFrame(df)

df2=df.drop(df.columns[[0,1]], axis = 1)
print(df2)
###################################
#Drop Columns from List of Columns
df = pd.DataFrame(df)

lisCol = ["tax", "rad"]
df2=df.drop(lisCol, axis = 1)
print(df2)
#############################
#Remove columns From DataFrame inplace
df.drop(df.columns[1], axis = 1, inplace=True)
df

#df.iloc[startrow:endrow, startcolumn:endcolumn]

df = pd.DataFrame(df)
#Below are quick example
df2 = df.iloc[ : ,1:12]
df2
#This line uses the slicing operator to get dataframe
#items by index 
#the first slice [:] indicates to return all rows
#The second slice specifies that only columns
#Between 1 and 12 (excluding 2) shoud be returned.

df2  = df.iloc[1:100, : ]
df2

#in this case, the first slice [1:100] is 
#requesting only rows 1 to rows 100(Excluding 100)
#the second slice [:] returned the all columns

#Slicing specific rows and columns using iloc attribute
df3= df.iloc[1:200, 10:30]
df3

#Select column by Integer index
df2= df.iloc[20]
df2


df2 = df.iloc[[22,53,76]] #Select rows by index list
df2
df2 = df.iloc[111:553]     #Select rows by integer index range
df2
df2 = df.iloc[:13]      #Select fist row
df2
df2 = df.iloc[:389]      #First 3 rows will returned
df2
df2 = df.iloc[-12:]     #Select last row
df2
df2 = df.iloc[-39:]     #Select last 3 rows
df2
df2 = df.iloc[-300:-100]   #Select last 3rd to second last rows (excluding last one)
df2
df2 = df.iloc[::3]     #3 defines the step size
df2


####################################################################
#Pandas select columns by name or index
#By using df[] Notation
df2=df["nox"]
#Select multiple columns
df2=df.loc[:,["nox","dis","tax"]]
#Select Random Columns
df2=df.loc[:,["nox","dis","rad"]]
#Select columns between two columns
df2=df.loc[:,"rm":"lstat"]
#Select Column by Range
df2=df.loc[:,"age":] #Returns all the rows and all the columns 'age' Onwards.
df2=df.loc[:,:"age"] #Returns all the rows and all the columns upto 'age'. 
#Select every alternate Columns
df2=df.loc[:,::2]
####################################################################
####################################################################
#Pandas.DataFrame.query() by examples
#Query all rows with courses equals 'Spark'
df2=df.query("dis == 1.5257")
print(df2)

#Not equal condition
df2=df.query("dis != 1.5257")
print(df2)

##################################################################



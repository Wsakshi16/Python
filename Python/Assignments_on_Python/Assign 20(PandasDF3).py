# -*- coding: utf-8 -*-
"""
Created on Mon May  8 19:48:16 2023

@author: adity
"""

##Assignment 
import pandas as pd
import numpy as np
cd = pd.read_csv('C:/1-Python/Assignments/Company_Data.csv')
df = pd.DataFrame(cd)
df


####################################################################
#Derive new column from an existing column
df = pd.DataFrame(cd)
df2 = df.assign(New_Price=lambda x:x.Income * x.Price / 10)
print(df2)
######################################################
df = pd.DataFrame(cd)
print(df.columns)
#Pandas Rename Column Name
# Rename a Single Column 
df2=df.rename(columns = {'Income' : 'Income_List', 'Sales' : 'SALES'})
print(df2.columns)
df2
#####################################################################
#Alternatively, you can also write
# the above statement by using 
#axis=1 or axis='columns'
# Alternatively you can write above using axis
df2=df.rename({'Income':'Income_List'}, axis=1)
df2=df.rename({'Income':'Income_List'}, axis='columns')
###################################################################
#In order to change columns on the existing DataFrame
# without copying to the new DataFrame, 
#you have to use inplace=True.
# Replace existing DataFrame (inplace). This returns None.
df.rename({'Income':'Income_List'}, axis='columns', inplace=True)
print(df.columns)
###############################################################
#Rename Multiple Columns

df.rename(columns = {'Income' : 'Income_List', 'Sales' : 'SALES', 
   'Education':'Edu.'}, inplace = True)
print(df.columns)
df.columns
################################
#Rename Columns with a List

column_names = ['A','B','C','D','E','F','G','H','I','J','K']
df.columns = column_names
print(df.columns)
##################################
 #Rename multiple columns with inplace
df.rename(columns = {'Courses':'Courses_List','Fee':'Courses_Fee', 
   'Duration':'Courses_Duration'}, inplace = True)
print(df.columns)
#######################################################
#######################################################
import pandas as pd
import numpy as np
cd = pd.read_csv('C:/1-Python/Assignments/Company_Data.csv')
df = pd.DataFrame(cd)
df

#Using apply function single column
def add_4(x):
    return x+4
df["Price"] = df["Price"].apply(add_4)
df["Price"]
#Apply to multiply columns
df[["Price","Education"]] = df[["Price","Education"]].apply(add_4)
df
#####################################################################
#Apply lambda Function to Single Column
#Using DataFrame.Apply() and lambda Function
df["Price"] = df["Price"].apply(lambda x: x-8)
print(df)
###################################################################
#Using pandas.DataFrame.map() to Single Column

df['Price'] = df['Price'].map(lambda Price: Price/2)
print(df)
###############################################
#Using Numpy function on single Column
# Using Dataframe.apply() & [] operator
df['Advertising'] = df['Advertising'].apply(np.square)
print(df)
#########################################
#Using NumPy.square() Method
# Using numpy.square() and [] operator
df['Advertising'] = np.square(df['Advertising'])
print(df)
#################################################

#Pandas groupby()  With Examples 
import pandas as pd
import numpy as np
cd = pd.read_csv('C:/1-Python/Assignments/Company_Data.csv')
df = pd.DataFrame(cd)
df

# Use groupby() to compute the sum
df2 =df.groupby(['Urban']).sum()
print(df2)

########################################################
# Group by multiple columns
df2 =df.groupby(['Urban', 'ShelveLoc']).sum()
print(df2)
######################################################
#Add Index to the grouped data
# Add Row Index to the group by result
df2 = df.groupby(['Urban', 'ShelveLoc']).sum().reset_index()
print(df2)

#######################################################
#Pandas Get Column Names from DataFrame
import pandas as pd
import numpy as np
cd = pd.read_csv('C:/1-Python/Assignments/Company_Data.csv')
df = pd.DataFrame(cd)
df.columns

#Get the list of all column names from hearders
column_headers = list(df.columns.values)
print("The column Header: ",column_headers)
#####################################################
#Using list(df) to get the column headers as a list
column_headers = list(df.columns)
column_headers
#Using list(df) to get the list of all Column Names
column_headers = list(df)
column_headers
################################################################

import pandas as pd
import numpy as np
cd = pd.read_csv('C:/1-Python/Assignments/Company_Data.csv')
df = pd.DataFrame(cd)
print(df)

#Pandas shuffle DataFrames rows
# shuffle the DataFrame rows & return all rows
df1 = df.sample(frac=0.5) #100% Shuffle
print(df1)
#################################################
#Create a new index starting from zero
df1 = df.sample(frac=1).reset_index()
print(df1)
############################
# Drop shuffle Index
df1 = df.sample(frac = 1).reset_index(drop=True) #If we don't want that new index
print(df1)
#####################
#####################
























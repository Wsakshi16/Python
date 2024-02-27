# -*- coding: utf-8 -*-
"""
Created on Tue May  9 17:15:51 2023

@author: adity
"""

#A series is used to model one dimensional data
#SIMILAR TO A LIST IN PYTHON
#The series object also has a few more bits
#of data, including an index and a name.
import pandas as pd
songs2= pd.Series([145,142,38,13],name='counts')
#It is easy to inspect the index of a series (or data frame)
songs2.index
#The index can be string based as well,
#in which case pandas indicates 
#that the datatype for the index is object (not string)

songs3 = pd.Series([145,142,38,13],name='counts',
                   index= ['Paul','John','George','Ringo'])
songs3.index
songs3
#The NAN Value
#this value stands for Not A Number
#and is usually ignored in arithmetic operations.
#(similar to NULL in SQL)
#If you load data from CSV file,
#an empty value for 

#numeric column will become NaN

#numeric column will become NaN.
import pandas as pd
f1=pd.read_csv('c:/1-Python/age.csv')
f1
#None, NaN, nan, and null are synonyms
#The Series object behaves similarly to 
#a NumPy array.
import numpy as np
numpy_ser = np.array([145, 142, 38, 13])
songs3[1]
#142
#They both have methods in common
songs3.mean()
####################################################
#THE PANDAS SERIES DATA STRUCTURE PROVIDES 
#SUPPORT FOR THE BASIC CRUD
#operations-create, read, update, and delete.
#creation
george= pd.Series([10,7,1,22],
index=['1968','1969','1970','1970'],
name='George Songs')
george
       

############################################################
#Reading
#to read o select the data from a series
george['1968']
george['1970']
#We can iterate over data in a series 
#as well. When iterating over a series
for item in george:
    print(item)
####################################################
#Updating
#Updating valuesin a series can be a 
#little tricky as well.
#To update a value
#for a given index label,
#the standard index assignment operator
george['1969'] = 68
george['1969']

#Deletion
#The del statement appear to have 
#problems with duplicate index
s = pd.Series([2,3,4], index=[1,2,3])
del s[1]

######################################################
#Convert Types
#string use.astype(str)
#numeric use pd.to_numeric
#integer use.astype(int),
#Note that this will fail with NaN
#datetime use pd.to_datetime

songs_66 = pd.Series([3, None, 11, 9],
index= ['Paul','John','George','Ringo'],
name = 'Counts')
pd.to_numeric(songs_66.apply(str))
pd.to_numeric(songs_66.astype(str), errors = 'coerce')
songs_66.fillna(-1)
songs_66.dropna()
########################################################
#Append, combining, and joining two series
import pandas as pd
songs_69 = pd.Series([7,16,21,39],
index =['Ram','Shyam','Ghanshyam','Krishna'],
name= 'counts')

songs=songs_66.append(songs_69)
songs
######################################################
#plotting two series
import matplotlib.pyplot as plt
fig = plt.figure()
songs_69.plot()
plt.legend()
####################################################
fig = plt.figure()
songs_69.plot(kind='bar')
songs_66.plot(kind='bar',color='g',alpha=.5)
plt.legend()
####################################################
import numpy as np
data =  pd.Series(np.random.randn(500),
name='500 random')
fig = plt.figure()
ax = fig.add_subplot(111)
data.hist()
#####################################################
#To perform an function
#on NumPy array
import numpy as np
arr1 = np.array([7, 20, 13])
arr2 = np.array([3, 5, 2])
arr1
arr1.dtype
#mod
mod_arr = np.mod(arr1, arr2)
print('')















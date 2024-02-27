# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 08:36:33 2023

@author: adity
"""

#one hot encoder 
import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder()
# we use ethnic diversity dataset
df = pd.read_csv("C:/0-datasets/ethnic diversity.csv")
df.columns
#We have Salaries and age as numerical column, let us make them 
#at position 0 and 1 so to make further data processing easy

df = df[['Salaries','age','Position','State','Sex','MaritalDesc','CitizenDesc','EmploymentStatus','Department','Race']]
#Check the dataframe in variable explorer 
#we want only nominal and ordinal data for processing 
#hence skipped 0 th and first column and applied to one hot encoder
enc_df = pd.DataFrame(enc.fit_transform(df.iloc[:,2:]).toarray())

#label encoder
from sklearn.preprocessing import LabelEncoder
#creating instance of label encoder
labelencoder  = LabelEncoder()
#split your data into input and output variables
X = df.iloc[:,0:9]   #First eight columns for X and 9th for y 
y = df['Race']
df.columns
#we have nominal data Sex, MaritalDesc, CitizenDesc,
#we want to convert to label encoder
X['Sex'] = labelencoder.fit_transform(X['Sex'])
X['MaritalDesc'] = labelencoder.fit_transform(X['MaritalDesc'])
X['CitizenDesc'] = labelencoder.fit_transform(X['CitizenDesc'])
#label encoder y
y = labelencoder.fit_transform(y)
#Tgis is going to create an array, hence convert it back to dataframe
y = pd.DataFrame(y)
df_new = pd.concat([X,y],axis = 1)
#If you will see variable explorer, y do not have column name
#hence rename the column
df_new = df_new.rename(columns={0:'Race'})











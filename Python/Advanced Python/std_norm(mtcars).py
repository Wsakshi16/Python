# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 09:25:52 2023

@author: adity
"""

###############Standardization####################
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
d = pd.read_csv("c:/0-datasets/mtcars.csv")
d.describe()
#Initialize the scalar
scalar = StandardScaler()
df = scalar.fit_transform(d)
dataset = pd.DataFrame(df)
res = dataset.describe()
#here if you will check res, in variable environment them
##############################################################

##############Normalization#################
ethnic = pd.read_csv("c:/0-datasets/ethnic diversity.csv")
#now read columns
ethnic.columns
#there are some columns wich are not useful
ethnic.drop(["Employee_name","EmpId",'Zip'],axis=1,inplace=True)
#Now read minimum value and maximum values of Salaries and age
a1 = ethnic.describe()
#Check a1 data frame in variable explorer,
#you find minimum salary is 0 and  max is  108304
#same way check for age, there is huge difference
#in min and max values and hence we are going for Normalization
#first we will have to convert non-numeric data to label encoding
ethnic=pd.get_dummies(ethnic,drop_first=True)
#Normalization function written where ethnic argument is passed
def norm_func(i):
    x=(i-i.min())/(i.max()-i.min())
    return x
df_norm = norm_func(ethnic)
b=df_norm.describe()
#if you will observe the b frame,
#it has dimensions 8, 81
#earlier in a they were 8,11, it is because all non-numeric
#data has been converted to numeric using label incoding










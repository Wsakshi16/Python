# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 08:27:05 2023

@author: adity
"""

############################################
########### dummy variable
############################################


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("C:/0-Datasets/animal_category.csv")
df.shape
df.drop(['Index'],axis=1,inplace=True)
# cheak df again
df_new=pd.get_dummies(df)
df_new.shape
#here we are getting 30 rows and 14 columns
# we are getting two columns for homely and gender ,one column
# detleye 2nd coulumn of gender and 2nd column of homely
df_new.drop(['Gender_Male','Homly_Yes'],axis=1,inplace=True)
df_new.shape
# now its (30, 12)



df_new.rename(columns={'Gender_Female':'Gender','Homly_No':'homly'})

######################################################################
#### same for ethinic diversity
import pandas as pd
import numpy as np

df1=pd.read_csv("C:/0-datasets/ethnic diversity.csv")
df1.shape
df1.drop(['Index'],axis=1,inplace=True)
# cheak df again
df_new1=pd.get_dummies(df1)
df_new1.shape

# here we are getting 310 rows and 401 columns
#
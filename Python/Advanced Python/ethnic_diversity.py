# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 09:31:06 2023

@author: aditya
"""
import pandas as pd
#let us import dataset
df=pd.read_csv("c:/0-Datasets/ethnic diversity.csv")
df
#let us check datatypes of columns
df.dtypes
#salaries data type is float, let us convert into int
#df1 = df.Salaries.astype(int)
df.Salaries=df.Salaries.astype(int)
df.dtypes
#now the data type of salariesis int 
#similarly age data type must be float
#presently it is int
df.age = df.age.astype(float)
df.dtypes
#################################################
#identify the duplicates
df_new = pd.read_csv("c:/0-Datasets/education.csv")
df_new

duplicate = df_new.duplicated()
#output of this function is single column
#if there is duplicate records output -True
#if there is no duplicate records output -False
#series will be created
duplicate
sum(duplicate)
#output will be 0

#now let us import another dataset
df_new1 = pd.read_csv("c:/0-Datasets/mtcars_dup.csv")
duplicate1 = df_new1.duplicated()
duplicate1
sum(duplicate1)
#there are 3 duplicate records
#row 17 is duplicate of row 2 like wise you can 3 duplicate records
#there is function called drop_duplicates()
#which will drp all the duplicate records
df_new2 = df_new1.drop_duplicates()
duplicate2 = df_new2.duplicated()

######################################################
#Outlier treatment
import pandas as pd 
import seaborn as sns
df=pd.read_csv("c:/0-Datasets/ethnic diversity.csv")
df
#Now let us find outliers in Salaries
sns.boxplot(df.Salaries)
#There are outliers
#Let us check outliers in age columns
sns.boxplot(df.age)
#There are no outliers
#Let us calculate IQR
IQR = df.Salaries.quantile(0.75)-df.Salaries.quantile(0.25)
IQR

lower_limit = df.Salaries.quantile(0.25)-1.5*IQR
lower_limit
upper_limit = df.Salaries.quantile(0.75)+1.5*IQR
upper_limit
#Now if you will check the lower limit of salary, it is -19446.9675
#There is negative salary
#So make it as 0
#How to make it
#go to variable explorer and make it 0
###################################################################
#Trimming
import numpy as np
outliers_df = np.where(df.Salaries>upper_limit,True,np.where(df.Salaries<lower_limit,True,False))
#you can check outliers_df column in variables explorer 
df_trimmed = df.loc[~outliers_df] 
df.shape
#(310, 13)
df_trimmed.shape
#(306, 13)
##################################################################
#Replacement Technique
#Drawback of trimming technique is we are losing the data
df = pd.read_csv("c:/0-Datasets/ethnic diversity.csv")
df.describe()

#records no.23 has got outliers
#map all the outlier values to upper limit
df_replaced = pd.DataFrame(np.where(df.Salaries>upper_limit,upper_limit,np.where(df.Salaries<lower_limit,lower_limit,df.Salaries)))
#if the values are greater than upper_limit 
#map it to upper limit, and less than lower_limit
#map it to lower_limit, it it is within the range then keep as it is.
sns.boxplot(df_replaced[0])

df_t=winsor.fit_transform(df[["Salaries"]])
sns.boxplot(df['Salaries'])
sns.boxplot(dfdf_t['Salaries'])
###############################################
#zero variance and near zero variance
# if there is no variance in the feature, then ML model
#will not get any intelligence, so it is better to ignore  those features
import pandas as pd
df = pd.read_csv("c:/0-Datasets/ethnic diversity.csv")
df.var()

#here ImpID and Zip is nominal data
#Salary has  4.441953e+08 is 4441953000 which is
#not close to 0
#Similarly age 8.571358e+01
#both the features are having considerable variance
df.var()==0

'''
EmpID       False
Zip         False
Salaries    False
age         False
dtype: bool
'''

#None of them are equal to zero
df.var(axis=0)==0
'''
EmpID       False
Zip         False
Salaries    False
age         False
dtype: bool
'''
####################################
import pandas as pd
import numpy as np

df = pd.read_csv("c:/0-Datasets/modified ethnic.csv")
#Check fr null values
df.isna().sum()
'''

Position            43
State               35
Sex                 34
MaritalDesc         29
CitizenDesc         27
EmploymentStatus    32
Department          18
Salaries            32
age                 35
Race                25
dtype: int64
'''

from sklearn.impute import SimpleImputer
mean_imputer = SimpleImputer(missing_values=np.nan,strategy='mean')
#Check the dataframe
df['Salaries'] = pd.DataFrame(mean_imputer.fit_transform(df[['Salaries']]))
#Check the dataframe
df['Salaries'].isna().sum()

##########################################################################
import pandas as pd
data  = pd.read_csv("c:/0-Datasets/ethnic diversity.csv")
data.head()
data.info()
#It gives size, null values, rows, columns and column data

data.describe()
data['Salaries_new']=pd.cut(data['Salaries'],bins=[min(data.Salaries),data.Salaries.mean(),max(data.Salaries)],labels=["Low","High"]) 
data.Salaries_new.value_counts()
data['Salaries_new']=pd.cut(data['Salaries'],bins=[min(data.Salaries),data.Salaries.quantile(0.25),data.Salaries.mean(),data.Salaries.quantile(0.75),max(data.Salaries)],labels=["group1","group2","group3","group4"]) 
data.Salaries_new.value_counts()




















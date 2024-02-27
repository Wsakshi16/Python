# -*- coding: utf-8 -*-
"""
Created on Sun May 14 17:12:21 2023

@author: adity
"""
# Assignment 
# 1. create dataframe
# create data dictionary

from scipy.stats import skew
from scipy.stats import kurtosis
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('iris')
df.head()

df.columns
df.describe()
plt.hist(df.sepal_length)

sns.displot(x = 'sepal_length', kde=True, data=df)
sns.displot(x = 'sepal_length', kde=True, bins=6, data=df)
sns.displot(x = 'sepal_width', kde=True, data=df)
sns.displot(x = 'petal_length', kde=True, data=df)
sns.displot(x = 'petal_width', kde=True, data=df)

plt.hist(df.sepal_width)

sns.boxplot(df.sepal_length,color='gray')

sns.pairplot(df)

corr = df.corr()
sns.heatmap(corr)

sns.scatterplot(x='sepal_length', y= 'sepal_width', data=df)

sns.scatterplot(x='petal_length', y= 'petal_width', data=df)

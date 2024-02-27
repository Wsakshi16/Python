# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 23:27:28 2023

@author: aditya
"""

# =============================================================================
# Linear Regression in Python (Case Study 1)
# =============================================================================

import pandas as pd
iris=pd.read_csv("iris.csv")
iris.head()

#Get dataframe having Sepal Width value Greater than 4
iris[iris['Sepal.Width']>4]

#Get dataframe having Petal Width value greater than 1
iris[iris['Petal.Width']>1]

#Get dataframe having Petal Width value greater than 2
iris[iris['Petal.Width']>2]

######################################################################
#Visualization
import matplotlib.pyplot as plt
import seaborn as sns

sns.scatterplot(x='Sepal.Length',y='Petal.Length',data=iris,hue="Species")
plt.show()

####################################################################
#Checking how Sepal Length changing with Sepal Width
#Using linear regression ML algorithm

iris.head()

# Model - 1
y = iris[['Sepal.Length']]
x = iris[['Sepal.Width']]

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

x_train.head()

y_test.head()

x_test.head()

y_train.head()

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(x_train,y_train)

y_pred = lr.predict(x_test)

y_test.head()

y_pred[0:5]

from sklearn.metrics import mean_squared_error

mean_squared_error(y_test,y_pred)

# Model - 1
y = iris[['Sepal.Length']]
x = iris[['Sepal.Width','Petal.Length','Petal.Width']]

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

from sklearn.linear_model import LinearRegression

lr2 = LinearRegression()

lr2.fit(x_train,y_train)

y_pred = lr2.predict(x_test)

mean_squared_error(y_test,y_pred)

#2nd model is better as it giving less mean squared error than model 1 and increase the accuracy.
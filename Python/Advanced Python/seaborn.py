# -*- coding: utf-8 -*-
"""
Created on Sat May 13 14:47:35 2023

@author: adity
"""
#pip install seaborn
import seaborn as sns
import pandas 
import matplotlib.pyplot as plt
#seaborn has 18 in-built dataset
#that can be found using following command
#Titanic dataset kaggle
sns.get_dataset_names()
df = sns.load_dataset('titanic')
df.head()


sns.countplot(x='sex',data=df)
#x- The name of the column
#data- The DataFrame.
sns.countplot(x='sex',hue = 'survived',data =  df,
palette = 'Set1')
sns.countplot(x='sex',hue = 'survived',data = df,
palette = 'Set2')
sns.countplot(x='sex',hue = 'survived',data = df,
palette = 'Set3')

#hue-The name of the categorical column to split the 

#palette- The color palette 
##################################################
#KDE plot
#A kernal Density Estimate (KDE) plot is used
sns.kdeplot(x = 'age', data = df, color = 'black')

#x- The anme of the colomn
#data -The dataframe
#color-The color of the graph. You can find the list of distribution plot

sns.displot(x = 'age', kde = True, bins= 6,data=df)

 #kde - It is set to False by default. However, if
 #bins - The number of bars.
 #the lower the number of bins, wider the bars and wise versa
 
sns.displot(x = 'age', kde = True, bins = 5,
            hue = df['survived'], palette = 'Set1', data= df)
#scatter Plot
#For this plot and the plots below,



df = sns.load_dataset('iris')
df.head()
#Scatter plots help understand co-relation between data
sns.scatterplot(x =  'sepal_length', y='petal_length',data=df, hue = 'species')
'''
In the plot above we can observe that on iris flower
with a sepal length < 6cm and petal length > 2cm
is most likely of type setosa.

In the plot above we can observe that on iris flower
with a sepal length < 7cm and petal length (> 2cm &  <5cm)
is most likely of type versicolor.

In the plot above we can observe that on iris flower
with a sepal length (< 8cm ) and petal length ( > 4cm & <7cm)
is most likely of type virginica.

Although there is no distinct boundary present between
the versicolor dots and virginica dots,
an iris flower with petal length between 2cm and 5 cm
is most likely of type versicolor,
while iris flowers with petal length > 5cm
are most likely of type verginica.
'''
#Joint plot
#A joint plot is also
sns.jointplot (x = 'sepal_length', y = 'petal_length', 
               data= df, kind = 'reg' )

sns.jointplot (x = 'sepal_length', y = 'petal_length', 
               data= df, kind = 'hist' )

sns.jointplot (x = 'sepal_length', y = 'petal_length', 
               data= df, kind = 'kde' )

'''
    kind - The kind of plot to be plotted.
    It can be one of the following.
    'scatter','hist','kde','reg','hex','resid'
'''
#Pair plots
sns.pairplot(df)
###############################################
#A heat map can be used to visualize confusion, matrices
corr = df.corr()
sns.heatmap(corr)
################################################
#####################################################


from scipy.stats import skew
from scipy.stats import kurtosis
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
cars=pd.read_csv("c:/1-Python/cars.csv")
cars.columns
cars.describe()
#
plt.hist(cars.speed)
sns.displot(x = 'speed', kde = True, bins=6, data=cars)
#The almost cars are travelling by speed
sns.displot(x = 'dist', kde = True, bins=6, data=cars)
#The distance covered 20 to 40 km are 17 cars
#right scewed distribution:Tail is at right
#left scewed distribution:Tail is at left                       
cars.describe()
sns.boxplot(cars.speed)
#
#
plt.hist(cars.dist)
#Dist.data is right skewed 
sns.boxplot(cars.dist)
#There is one outliers in the data
#skewness of speed
speed = cars['speed'.tolist()]
speed
print("skewness of speed",skew(speed))
dist = cars ['dist']. tolist()

print ("skewness of dist", skew(dist))

print (skew(dist, axis=0, bias=True))
###########################################
sns.countplot(x= 'speed', hue='dist', data=cars, 
              palette = 'Set1')

sns.scatterplot(x='speed', y= 'dist', data=cars)
#In this scatterplot 
# 1. only one car has covered distance over 100km
# 2. most of the cars have covered distance from 15km to 60km  
# 3. average speed of the cars was between 10 to 20km/hr

sns.jointplot (x= 'speed', y= 'dist', data=cars, kind = 'reg') 

sns.jointplot (x= 'speed', y= 'dist', data=cars, kind = 'hist') 

sns.jointplot (x= 'speed', y= 'dist', data=cars, kind = 'kde') 

sns.pairplot(cars)

corr=cars.corr()
sns.heatmap(corr)

###############################################################################################################

speed = cars.speed.tolist()
dist = cars.dist.tolist()

###############################################################################################################

from scipy.stats import skew
from scipy.stats import kurtosis

###############################################################################################################

l = [skew(speed),skew(dist),kurtosis(speed),kurtosis(dist)]
l

skew(speed)
skew(dist)

kurtosis(speed)
kurtosis(dist)

skew(dist)
skew(dist,axis=0,bias=True)
skew(dist,axis=1,bias=True)
skew(dist,axis=0,bias=False)

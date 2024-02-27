# -*- coding: utf-8 -*-
"""
Created on Sat May 13 14:47:35 2023

@author: adity
"""

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


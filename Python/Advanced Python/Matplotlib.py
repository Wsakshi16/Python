# -*- coding: utf-8 -*-
"""
Created on Fri May 12 21:52:43 2023

@author: adity
"""

import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.show()

#############################################
#multiline plots
import matplotlib.pyplot as plt
x = range(1,5)
plt.plot(x,[xi*1.5 for xi in x])

plt.plot(x,[xi*3.0 for xi in x])

plt.plot(x,[xi/3.0 for xi in x])

plt.show()
####################################################
#Grid,axes and labels
#Adding a grid
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,5)
plt.plot(x, x*1.5,x,x*3.0,x,x/3.0)
plt.grid(True)
plt.show()
#########################################################
#Handling axes
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,5)
plt.plot(x, x*1.5,x,x*3.0,x,x/3.0)

plt.axis()  #show the current axis limits values
plt.axis([0,5,-1,13]) #set new axis limits
#[xmin,xmax,ymin,ymax]
#[0,5,-1,2]
plt.show()

#############################################################
#Adding labels
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])

plt.xlabel("This is the X axis")

plt.ylabel("This is the Y axis")

plt.show()
#############################################################
#Adding a title
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])

plt.title("Simple plot")

plt.show()
######################################################
#Adding a legend
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,5)
plt.plot(x, x*1.5, label='Normal')

plt.plot(x,x*3.0, label='Fast')

plt.plot(x, x/3.0, label='Slow')

plt.legend()

plt.show()
##########################################################
#Control Colors
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,3)
plt.plot(x,'y');
plt.plot(x+1,'m');
plt.plot(x+2,'c');
plt.grid(True)
plt.show()
###################################################
#Specifying styles in multiline plots
import matplotlib.pyplot as plt
import numpy as np
y = np.arange(1,3)
plt.plot(y, 'y',y+1,'m',y+2,'c');
plt.show()
####################################################
#Control line styles
import matplotlib.pyplot as plt
import numpy as np
y = np.arange(1,3)
plt.plot(y, '--',y+1,'-.',y+2,':.');
plt.show()
#########################################################
#Control marker styles
import matplotlib.pyplot as plt
import numpy as np
y = np.arange(1,3,0.2)
plt.plot(y,'x',y,'o',y+1,'D',y+1.5,'^',y+2,'s')
plt.show()
##########################################################
#Histogram charts
import matplotlib.pyplot as plt
import numpy as np
y = np.random.randn(1000)
y.shape
plt.hist(y);
plt.show()
###########################################################
#Bar graph
import matplotlib.pyplot as plt
plt.bar([1,2,3],[3,2,5]);
plt.show()
'''
The bar() function is used to generate bar charts in matplot
The function experts two lists of values:
The X coordinates that are the positions of the bars left margin
and the heights of the bars:
    
As we can see the left margin of the bars start at the points specified
in the first list,while their heights are the values of the second list

'''

##############################################################
#Scatter plot
import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(1000)
y = np.random.randn(1000)
plt.scatter(x,y);
plt.show()
##################################################################
size = 50*np.random.randn(1000)
colors = np.random.randn(1000)
plt.scatter(x,y,s=size,c=colors);
plt.show()
#############################################################
#adding text
import matplotlib.pyplot as plt
import numpy as np
X = np.linspace(-4,4,1024)
Y = .25* (X+4.)*(X+1.)*(X-2.)
plt.text(-0.5,-0.25,'Brackmard minimum')
plt.plot(X,Y,c='k')
plt.show()
#########################################################
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
#Visualizing the pokemon dataset


























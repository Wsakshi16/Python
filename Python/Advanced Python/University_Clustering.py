# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 15:14:16 2023

@author: adity
"""
#######################CLUSTERING#############################
import pandas as pd
import matplotlib.pyplot as plt
#how import file from data set and create a dataframe
Univ1 = pd.read_excel("c:/0-datasets/University_Clustering.xlsx")
a = Univ1.describe()
#We have one column 'State' which really not useful not useful we will drop it 
Univ = Univ1.drop(["State"],axis = 1)
#we know that there is scale difference among columns
#which we have to remove
#either by nomalisation and standardisation
#whenever there is mixed data apply normalisation
def norm_func(i):
    x=(i-i.min())/(i.max()-i.min())
    return x
#Now apply this normalization function to Univ dataframe
#For all the rows and column from 1 until end
#since 0 th column hs university name hence skipped
df_norm=norm_func(Univ.iloc[:,1:])
#you can check the dataframe which is saled
#between values from 0 to 1
#you can apply descirbe() function to ne dataframe
d = df_norm.describe()
#before you apply clustering,you need to plot dendrogram first
#Now to create dendrogram,we need to measure distance,
#we have to import linkage package
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch
#linkage function gives us hierachical or aglomerative clustering
#ref the the help for linkage
z = linkage(df_norm,method="complete",metric="euclidean")
plt.figure(figsize=(15,8));
plt.title("Hierarchical Clustering dendrogram");
plt.xlabel("Index");
plt.ylabel("Distance")
#ref help of dendrogram
#sch.dendrogram(z)
sch.dendrogram(z,leaf_rotation=0,leaf_font_size=10)
plt.show()

#dendrogram()
#applying agglemerative clustering choosing 3 as cluster from dendogram
#whaterver has been displayed in dendrogram is not clustering 
#it is just showing number of possible clusters
from sklearn.cluster import AgglomerativeClustering
h_complete=AgglomerativeClustering(n_clusters=3,linkage="complete",affinity="euclidean").fit(df_norm)

#apply labels to the clusters h_complete.labels
cluster_labels=pd.Series(h_complete.labels_)

#Assign this Series to univ dataframe t column and name the column
Univ['clust']=cluster_labels
#we want to relocate the column 7 to 0th position
univ1=Univ.iloc[:,[7,1,2,3,4,5,6]]
#noe check univ1 dataframe
univ1.iloc[:,2:].groupby(Univ.clust).mean()
#from the ouput cluster 2 has got higesht Top10
#lowest accept reatio ,best factly ratio and highest expenses
#highest geaduate ratio
univ1.to_csv("University.csv",encoding="utf-8")
import os
os.getcwd()
















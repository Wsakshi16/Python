# -*- coding: utf-8 -*-
"""
Created on Wed May  3 22:26:08 2023

@author: adity
"""
#What is Pandas DataFrame?
#pandas DataFrame is a Two-Dimensional data structure,
#an immutable, heterogeneous tabular 
#data structure with labeled axes rows, and columns.

#DataFrame Features
#DataFrames support named rows & columns
# (you can also provide names to rows)
#Supports heterogeneous collections of data.
#DataFrame labeled axes (rows and columns).
#Installing Pandas
#step-1 go to anaconda navigator
#step-2 select environment tab
#step-3 by default it will be base terminal
#step-4 on base terminal-pip install pandas
# Or conda install pandas
######################################
#Upgrade Pandas to Latest or Specific Version
#on base terminal write
#conda install --upgrade pandas

#upgrade to specific version
#conda update pandas==1.5.3
##############################
#To check the version of pandas
import pandas as pd
pd.__version__
#################################
#Create using Constructor
# Create pandas DataFrame from List
import pandas as pd
technologies = [ ["Spark",20000, "30days"], 
                 ["pandas",20000, "40days"] 
               ]
df=pd.DataFrame(technologies)
print(df)

#Since we have not given labels to columns and 
#indexes, DataFrame by default assigns 
#incremental sequence numbers as labels 
#to both rows and columns, these are called Index.
# Add Column & Row Labels to the DataFrame
column_names=["Courses","Fee","Duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_names,index=row_label)
print(df)
###########################
df.dtypes 
#####################
#You can also assign custom data types to columns.
# set custom types to DataFrame
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle","Java"],
    'Fee' :[20000,25000,26000,22000,24000,21000,22000],
    'Duration ':['30day','40days','35days', '40days','60days','50days','55days'],
    'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
    }
df = pd.DataFrame(technologies)
print(df.dtypes)
# Convert all types to best possible types
df2=df.convert_dtypes()
print(df2.dtypes)
# Change All Columns to Same type
df = df.astype(str)
print(df.dtypes)
# Change Type For One or Multiple Columns
df = df.astype({"Fee": int, "Discount": float})
print(df.dtypes)
# Convert Data Type for All Columns in a List
df = pd.DataFrame(technologies)
df.dtypes
cols = ['Fee', 'Discount']
df[cols] = df[cols].astype('float')
df.dtypes
#Ignores error
df = df.astype({"Courses": int},errors='ignore')
df.dtypes
# Generates error
df = df.astype({"Courses": int},errors='raise')
# Converts feed column to numeric type
df = df.astype(str)
print(df.dtypes)
df['Discount'] = pd.to_numeric(df['Discount'])
df.dtypes


###########################

# Create DataFrame from Dictionary
technologies = {
    'Courses':["Spark","PySpark","Hadoop"],
    'Fee' :[20000,25000,26000],
    'Duration':['30day','40days','35days'],
    'Discount':[1000,2300,1500]
              }
df = pd.DataFrame(technologies)
df
##############################
#convert dataframe to csv
df.to_csv('data_file.csv')
##################################
#Create DataFrame From CSV File

df = pd.read_csv('data_file.csv')
#################################
#Pandas DataFrame – Basic Operations
# Create DataFrame with None/Null to work with examples
import pandas as pd
import numpy as np
technologies = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas",None,"Spark","Python"],
    'Fee': [2200,4332,5000,350,np.nan,3500,3600,2299],
    'Duration':['30day','50day','55day','60day','55day','90day','60day','40day'],
    'Discount':[1000,2300,1000,50,3000,500,600,299]
    })
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technologies, index=row_labels)
print(df)
################################################################################
#DataFrame Properties
df.shape
#(8,4)
df.size
#32
df.columns
df.columns.values
df.index
df.dtypes
#######################################################
#Accessing one column contents
df['Duration']
##Accessing two columns contents
df[['Fee','Duration']]
#select certain rows and assign it to another dataframes
df2=df[6:]
df2
df3=df[:3]
df3
#######################################################
#accessing a certain cell from column 'Duration'
df['Duration'][3]
#Subtracting specific value from the column
df['Fee'] = df['Fee']-350
df['Fee']
#Pandas to Manupulate DataFrame
#Describe DataFrame
#Describe DataFrame for all numeric columns
df.describe()
#It will show 5 number summary
#############################################
#rename()-renames 
df = pd.DataFrame(technologies, index=row_labels)

df.columns=['A','B','C','D']
df
##########################################
# Rename column names using rename() method
df = pd.DataFrame(technologies, index=row_labels)
df.columns = ['A','B','C','D']
df.dtypes

df2 = df.rename({'A': 'c1', 'B': 'c2'}, axis=1)
df2
df2 = df.rename({'C': 'c3', 'D': 'c4'}, axis='columns')
df2 = df.rename(columns={'A': 'c1', 'B': 'c2'})
df2
####################################################
#Drop dataframes rows and columns
df = pd.DataFrame(technologies,index=row_labels)
#drop rows by labels
df1=df.drop(['r1','r2'])
df1
#Delete rows by position/index
df1=df.drop(df.index[1]) 
df1

df1=df.drop(df.index[[1,3]]) #Need to write two angular bracket while giving multiple indexes
df1

#Delete rows by index range
df1 = df.drop(df.index[2:])
df1

df1 = df.drop(df.index[:4]) #drop the rows excluding the index given after colon
df1

#When you have default indexes for rows
df = pd.DataFrame(technologies)
df1 = df.drop(0)
df1

df = pd.DataFrame(technologies)
df1 = df.drop([0,3]) #it will delete rows0 and row3 
df1
                     #Don't need to write two angular bracket while giving multiple indexes
df1 = df.drop(range(0,2)) #it will delete 0 and 1
df1
############################################################
import pandas as pd
import numpy as np
technologies = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas",None,"Spark","Python"],
    'Fee': [2200,4332,5000,350,np.nan,3500,3600,2299],
    'Duration':['30day','50day','55day','60day','55day','90day','60day','40day']
    })
df = pd.DataFrame(technologies)
print(df)
#Drop column by name
#Drops 'Fee' column
df2 = df.drop(["Fee"],axis = 1)
print(df2)
#Explicitly using parameter name 'labels'
df2 = df.drop(labels=["Fee"], axis = 1)
df2
#Alternatively you can also use columns instead of labels
df2 = df.drop(columns=["Fee"], axis = 1)
df2
###############################################################################
#Drop column by index.
print(df.drop(df.columns[1],axis=1)) 

df = pd.DataFrame(technologies)

#using inplace=True
df.drop(df.columns[2],axis=1, inplace=True)
print(df)
######################################################
df = pd.DataFrame(technologies)
#drop two or more columns by label name
df2 = df.drop(["Courses","Fee"], axis=1)
print(df2)
###############################################################
#drop two or more columns by index
df = pd.DataFrame(technologies)
df2 = df.drop(df.columns[[0,1]], axis=1)
print(df2)
###################################
#Drop columns from list of columns
df = pd.DataFrame(technologies)
lisCol = (["Courses","Fee"])
df2=df.drop(lisCol, axis = 1)
print(df2)
####################################################
#Remove column from Dataframe inplace
df.drop(df.columns[1],axis=1, inplace=True)
#############################################################
import pandas as pd
import numpy as np
technologies = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas",None,"Spark","Python"],
    'Fee': [2200,4332,5000,350,np.nan,3500,3600,2299],
    'Duration':['30day','50day','55day','60day','55day','90day','','40day'],
    'Discount':[1000,2300,1000,50,3000,500,600,299]
    })
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technologies, index=row_labels)
print(df)

#df.iloc[startrow:endrow, startcolumn:endcolumn]

df = pd.DataFrame(technologies, index=row_labels)
#Below are quick example
df2 = df.iloc[ : ,1:3]
df2
#This line uses the slicing operator to get dataframe
#items by index 
#the first slice [:] indicates to return all rows
#The second slice specifies that only columns
#Between 0 and 2 (excluding 2) shoud be returned.

df2  = df.iloc[0:2, : ]
df2

#in this case, the first slice [0:2] is requesting only rows 0 to rows 1
#the second slice [:] returned the all columns

#Slicing specific rows and columns using iloc attribute
df3= df.iloc[1:2, 1:3]
df3

#Select column by Integer index
df2= df.iloc[2]
df2


df2 = df.iloc[[2,3,6]] #Select rows by index list
df2
df2 = df.iloc[1:5]     #Select rows by integer index range
df2
df2 = df.iloc[:1]      #Select fist row
df2
df2 = df.iloc[:3]      #First 3 rows will returned
df2
df2 = df.iloc[-1:]     #Select last row
df2
df2 = df.iloc[-3:]     #Select last 3 rows
df2
df2 = df.iloc[-3:-1]   #Select last 3rd to second last rows (excluding last one)
df2
df2 = df.iloc[::3]     #3 defines the step size
df2

#Select rows by Index labels
df2 = df.loc['r2']     #Select row by index label
df2
df2 = df.loc[['r2','r3','r6']] #Select rows by index label
df2
df2 = df.loc['r1':'r5']  #Select rows by index range
df2
df2 = df.loc['r1':'r5':2] #Select alternate rows with in Index
df2
####################################################################
#Pandas select columns by name or index
#By using df[] Notation
df2=df["Courses"]
#Select multiple columns
df2=df.loc[:,["Courses","Fee","Duration"]]
#Select Random Columns
df2=df.loc[:,["Courses","Fee","Discount"]]
#Select columns between two columns
df2=df.loc[:,"Fee":"Discount"]
#Select Column by Range
df2=df.loc[:,"Duration":] #Returns all the rows and all the columns 'Duration' Onwards.
df2=df.loc[:,:"Duration"] #Returns all the rows and all the columns upto 'Duration'. 
#Select every alternate Columns
df2=df.loc[:,::2]
####################################################################
####################################################################
#Pandas.DataFrame.query() by examples
#Query all rows with courses equals 'Spark'
df2=df.query("Courses == 'Spark'")
print(df2)

#Not equal condition
df2=df.query("Courses != 'Spark'")
print(df2)
##################################################################

#Pandas Add Column to DataFrame
import pandas as pd
import numpy as np
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas"],
    'Fee': [2200,4332,5000,3500,6700],
    'Discount':[1000,2300,1000,500,700]
    }

df=pd.DataFrame(technologies)
print(df)
####################################################################
#Pandas add column to DataFrame
#Add new column to DataFrame
tutors = ['Ram',"Shyam",'Akash','Rushikesh','Aditya']
df2 = df.assign(TutorsAssigned=tutors)
print(df2)
################################################
#Add multiple column to the dataframe
MNCCompanies = ["TATA",'HCL','Infosys','Google','Amazon']
df2 = df.assign(MNCComp = MNCCompanies,TutorsAssigned=tutors)
df2
############################################################
#Derive new column from an existing column
df = pd.DataFrame(technologies)
df2 = df.assign(Discount_Percent=lambda x:x.Fee * x.Discount / 100)
print(df2)
######################################################
#Append Column to Existing Pandas DataFrame
# Add New column to the existing DataFrame
df = pd.DataFrame(technologies)
df["MNCCompanies"]=MNCCompanies
print(df)
##########################################################
# Add new column at the specific position
df = pd.DataFrame(technologies)
df.insert(0,'Tutors', tutors )
print(df)
##############################################################
##############################################################
#Pandas Rename Column with Examples
import pandas as pd
technologies = ({
  'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle","Java"],
  'Fee' :[20000,25000,26000,22000,24000,21000,22000],
  'Duration':['30day', '40days' ,'35days', '40days', '60days', '50days', '55days']
              })
df = pd.DataFrame(technologies)
print(df.columns)
#Pandas Rename Column Name
# Rename a Single Column 
df2=df.rename(columns = {'Courses' : 'Course_List', 'Fee' : 'Course_Fee'})
print(df2.columns)
df2
#####################################################################
#Alternatively, you can also write
# the above statement by using 
#axis=1 or axis='columns'
# Alternatively you can write above using axis
df2=df.rename({'Courses':'Courses_List'}, axis=1)
df2=df.rename({'Courses':'Courses_List'}, axis='columns')

###################################################################
#In order to change columns on the existing DataFrame
# without copying to the new DataFrame, 
#you have to use inplace=True.
# Replace existing DataFrame (inplace). This returns None.
df.rename({'Courses':'Courses_List'}, axis='columns', inplace=True)
print(df.columns)
####################################33
#Rename Multiple Columns

df.rename(columns = {'Courses':'Courses_List','Fee':'Courses_Fee', 
   'Duration':'Courses_Duration'}, inplace = True)
print(df.columns)
df.columns
################################
#Rename Columns with a List

column_names = ['Courses','Fee','Duration']
df.columns = column_names
print(df.columns)
##################################
 #Rename multiple columns with inplace
df.rename(columns = {'Courses':'Courses_List','Fee':'Courses_Fee', 
   'Duration':'Courses_Duration'}, inplace = True)
print(df.columns)
#######################################################3

import pandas as pd
import numpy as np

data={"A":[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]
      }

df=pd.DataFrame(data)
print(df)

def add_3(x):
    return x+3
df2 = df.apply(add_3)
df2
########################################################################
#Using apply function single column
def add_4(x):
    return x+4
df["B"] = df["B"].apply(add_4)
df["B"]
#Apply to multiply columns
df[["A","B"]] = df[["A","B"]].apply(add_4)
df
#Apply a lambda function to each column
df2 = df.apply(lambda x : x+10)
df2 
#####################################################################
#Apply lambda Function to Single Column
#Using DataFrame.Apply() and lambda Function
df["A"] = df["A"].apply(lambda x: x-2)
print(df)
###################################################################
#Using pandas.DataFrame.transform() to Apply Function Column
# Using DataFrame.transform() 
def add_2(x):
    return x+2
df = df.transform(add_2)
print(df)
###################################################################
#Using pandas.DataFrame.map() to Single Column

df['A'] = df['A'].map(lambda A: A/2)
print(df)
###############################################
#Using Numpy function on single Column
# Using Dataframe.apply() & [] operator
df['A'] = df['A'].apply(np.square)
print(df)
#########################################
#Using NumPy.square() Method
# Using numpy.square() and [] operator
df['A'] = np.square(df['A'])
print(df)
#################################################
#Pandas groupby()  With Examples 
import pandas as pd
technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Hadoop","Spark","Python","NA"],
    'Fee' :[22000,25000,23000,24000,26000,25000,25000,22000,1500],
    'Duration':['30days','50days','55days','40days','60days','35days','30days','50days','40days'],
    'Discount':[1000,2300,1000,1200,2500,None,1400,1600,0]
          })
df = pd.DataFrame(technologies)
print(df)

# Use groupby() to compute the sum
df2 =df.groupby(['Courses']).sum()
print(df2)
########################################################
# Group by multiple columns
df2 =df.groupby(['Courses', 'Duration']).sum()
print(df2)
######################################################
#Add Index to the grouped data
# Add Row Index to the group by result
df2 = df.groupby(['Courses','Duration']).sum().reset_index()
print(df2)
############################################3
# Group by on multiple columns
df2 =df.groupby(['Courses', 'Duration']).sum()
print(df2)
#######################################################
#Pandas Get Column Names from DataFrame
import pandas as pd
import numpy as np

technologies= {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas"],
    'Fee' :[22000,25000,23000,24000,26000],
    'Duration':['30days','50days','30days', None,np.nan],
    'Discount':[1000,2300,1000,1200,2500]
          }
df = pd.DataFrame(technologies)
print(df)
df.columns
#Get the list of all column names from hearders
column_headers = list(df.columns.values)
print("The column Header: ",column_headers)
#####################################################
#Using list(df) to get the column headers as a list
column_headers = list(df.columns)
column_headers
#Using list(df) to get the list of all Column Names
column_headers = list(df)
column_headers
###############################################################
#################################################
############################
#Pandas Shuffle DataFrame Rows 
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle","Java"],
    'Fee' :[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30day','40days','35days','40days','60days','50days','55days'],
    'Discount':[1000,2300,1500,1200,2500,2100,2000]
               }
df = pd.DataFrame(technologies)
print(df)
#Pandas shuffle DataFrames rows
# shuffle the DataFrame rows & return all rows
df1 = df.sample(frac=1)
print(df1)
#################################################
#Create a new index starting from zero
df1 = df.sample(frac=1).reset_index()
print(df1)
############################
# Drop shuffle Index
df1 = df.sample(frac = 1).reset_index(drop=True)
print(df1)
#####################
#####################
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Python","Pandas"],
    'Fee' :[20000,25000,22000,30000],
    'Duration':['30days','40days','35days','50days'],
              }
index_labels1=['r1','r2','r3','r4']
df1 = pd.DataFrame(technologies, index=index_labels1)

technologies2 = {
    'Courses':["Spark","Java","Python","Go"],
    'Discount' :[2000,2300,1200,2000]
    }
index_labels2=['r1','r6','r3','r5']
df2 = pd.DataFrame(technologies2, index=index_labels2)

#Pandas join by default it will join the table left join
df3=df1.join(df2, lsuffix="_left", rsuffix="_right")
print(df3)
#######################################################
#Pandas Inner join DataFrame
df3=df1.join(df2, lsuffix="_left", rsuffix="_right", how='inner')
print(df3)
#######################################################
#Pandas Right join DataFrame
df3=df1.join(df2, lsuffix="_left", rsuffix="_right", how='right')
print(df3)
###########################################################
#Pandas FullOuter join DataFrame
df3=df1.join(df2, lsuffix="_left", rsuffix="_right", how='outer')
print(df3)
#########################################################
#Pandas join on columns
df3 = df1.set_index('Courses').join(df2.set_index('Courses'), how='inner')
df3

df3 = df1.set_index('Courses').join(df2.set_index('Courses'), how='left')
df3

df3 = df1.set_index('Courses').join(df2.set_index('Courses'), how='right')
df3

df3 = df1.set_index('Courses').join(df2.set_index('Courses'), how='outer')
df3

####################################################################
#inner join
#Pandas Merge DataFrames
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Python","Pandas"],
    'Fee' :[20000,25000,22000,30000],
    'Duration':['30days','40days','35days','50days'],
              }
index_labels1=['r1','r2','r3','r4']
df1 = pd.DataFrame(technologies, index=index_labels1)

technologies2 = {
    'Courses':["Spark","Java","Python","Go"],
    'Discount' :[2000,2300,1200,2000]
    }
index_labels2=['r1','r6','r3','r5']
df2 = pd.DataFrame(technologies2, index=index_labels2)

#Using pandas.merge()
df3 = pd.merge(df1,df2)

#Using pandas.merge()
df3 = df1.merge(df2)
##############################################################
#Use pandas.concat() to Concat Two DataFrames
import pandas as pd
df = pd.DataFrame({'Courses': ["Spark","PySpark","Python","Pandas"],
                    'Fee' : [20000,25000,22000,24000]})

df1 = pd.DataFrame({'Courses': ["Pandas","Hadoop","Hyperion","Java"],
                    'Fee': [25000,25200,24500,24900]})

# Using pandas.concat() to concat two DataFrames
data = [df, df1]
df2 = pd.concat(data)
df2
################################
#Concatenate Multiple DataFrames Using pandas.concat()
import pandas as pd
df = pd.DataFrame({'Courses': ["Spark", "PySpark", "Python", "Pandas"],
                    'Fee' : ['20000', '25000', '22000', '24000']}) 
  
df1 = pd.DataFrame({'Courses': ["Unix", "Hadoop", "Hyperion", "Java"],
                    'Fee': ['25000', '25200', '24500', '24900']})
  
df2 = pd.DataFrame({'Duration':['30day','40days','35days','60days','55days'],
                    'Discount':[1000,2300,2500,2000,3000]})
  
# Appending multiple DataFrame
df3 = pd.concat([df, df1, df2])
print(df3)

##############################
# Write DataFrame to CSV File with Default params.
df3.to_csv("c:/1-Python/courses.csv")
#read CSV
# Import pandas
import pandas as pd

# Read CSV file into DataFrame
df = pd.read_csv('courses.csv')
print(df)
#####################################
# Write DataFrame to Excel file
df.to_excel('c:/1-Python/Courses.xlsx')
########################
import pandas as pd
# Read Excel file
df = pd.read_excel('c:/1-Python/Courses.xlsx')
print(df)
####################################################################
# Using Series.values.tolist()
col_list = df.Courses.values.tolist()
print(col_list)

# Using Series.values.tolist()
col_list = df["Courses"].values.tolist()
print(col_list)

# Using list() Function
col_list =  list(df["Courses"])
print(col_list)

# Conver to numpy array
col_list = df['Courses'].to_numpy()
print(col_list)

# Get by Column Index
col_list = df[df.columns[0]].values.tolist()
print(col_list)

# Convert Index Column to List
index_list = df.index.tolist()
print(index_list)









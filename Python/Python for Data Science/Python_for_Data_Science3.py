# -*- coding: utf-8 -*-
"""
Created on Wed May 10 15:47:54 2023

@author: adity
"""

#What is NumPy?
#The NumPy library is a popular open-source Python 
#library used for scientific computing applications,
# and it stands for Numerical Python, 
#which is consisting of multidimensional array 
#objects and a collection of routines for processing those arrays.

#Install Python NumPy Library
#goto base terminal and on prompt
#pip install numpy
# Install NumPy using Conda
#conda install numpy
'''
While a Python list can contain different 
data types within a single list, 
all of the elements in a NumPy array
 should be homogeneous.

'''
#Arrays In NumPy
# Create ndarray
import numpy as np
arr = np.array([10,20,30])
print(arr)

#Output :
#[10,20,30]
#Create a Multi-Dimensional array
#Create a multi dimensional array
arr = np.array([[10,20,30],[40,50,60]])
print(arr)

#Output:
#[[10,20,30]
# [40,50,60]]
#Represent the Minimum Dimensions
#Use ndmin parameter to specify how many minimum
#dimensions you wanted to create an array with 
#minimum dimension
arr = np.array([10,20,30,40], ndmin = 2)
print(arr)
#Output:
#    [[10 20 30 40]]
arr = np.array([10,20,30,40], ndmin = 3)
print(arr)
#Output:
#    [[[10 20 30 40]]]
#Change the datatype 
#dtype parameter
arr = np.array([10,20,30,40], dtype = complex)
print(arr)
#Output:
#[10.+0.j 20.+0.j 30.+0.j 40.+0.j]

#Get the Dimesions of an array
#Get dimension of array
arr = np.array([[1,2,3,4],[7,8,6,7],[9,10,11,12]])
print(arr.ndim)
print(arr)

#Output:
    #2
    #[[ 1  2  3  4]
    # [ 7  8  6  7]
    # [ 9 10 11 12]]
##############################################33
#Finding the size of each item in the array
arr = np.array([10,20,30])
print("Each item contain in bytes :",arr.itemsize)

#Outputs:
    #Each item contain in bytes : 4
#########################################################
#Get the datatype if each item in an array
#Finding the datatype of each array item
arr = np.array([10,20,30])
print("Each item is of the type :",arr.dtype)

######################################
#Get the shape and size of an array
arr = np.array([[10,20,30,40],[40,50,60,90]])
print("Array Size:",arr.size) #Elements in an array
print("Array Shape",arr.shape)
########################################
#Create NumPy array from list
#Creation of Arrays
arr = np.array([10,20,30])
print("Array",arr)
####################################################
#Creation array from list with type float
arr = np.array([[10,20,30],[40,50,60]], dtype='float')
print("Array created by using list: \n",arr)
############################################
#Create a sequence of integers using arange()
#Create a sequence of integer
#from 0 to 20 with step of 3
arr = np.arange(0,20,3)
print("A sequential array with steps of 3:\n",arr)
###################################################
#Array Indexing in NumPy
#Access single element using index
arr = np.arange(11)
print(arr)

print(arr[2])
print(arr[-2])
######################################################
#Multi-Dimensional Array Indexing
#Access Multi Dimensional Array element
#using array indexing
arr = np.array([[10,20,30,40,50],[20,30,40,60,70]])
print(arr)

print(arr.shape)

print(arr[1,1])

print(arr[0,4])

print(arr[1,-1])
##########################################################
#Access array elements using slicing
arr = np.array([0,1,2,3,4,5,6,7,8,9])
x=arr[1:8:2]  #start:end:in the step of 2
print(x)

x=arr[-2:3:-1]
print(x)

x=arr[-2:10]
print(x)

#Indexing in NumPy
arr = np.array([[10,20,10,40],
                [40,50,70,90],
                [60,10,70,80],
                [30,90,40,30]])
arr
#Slicing array
#for multi dimensional NumPy arrays, you can access the elements :
#    multi_arr [1,2]- To access the value at row 1 and column 2.
#    multi_arr [1,:]- To get the value at row 1 and all columns.
#    multi_arr [:,1]- To access the value of all rows and column 1.

x= arr[:3, ::2] #All rows three columns, in all selected rows and
print(x)
#########################################
#Integer array indexing
#Integer array indexing allows the selection of arbitary items in

#Integer array indexing
arr = np.arange(35).reshape(5,7)
print(arr)
####################################################
#Boolean array Indexing.

arr = np.arange(12).reshape(3,4)
print(arr)

rows = np.array([False,True,True]) #not 0th row only first and second
wanted_rows= arr[rows,:] #In selected rows all rows and column
print(wanted_rows)

#Convert numpy array to the Python List

#wE can convert the NumPy array to the list
#by using tolist() method, We ,ay have a list
#of data elements that have been converted 
#from the array using this method

#Convert one dimensional array to the list

#Create array
array = np.array([10,20,30,40])
print("Array:",array)
print(type(array))

#convert list
list= array.tolist()
print("list:",list)
print(type(list))

#Convert Multi dimensional array to the list

#Create array
array = np.array([[10,20,30,40],
                 [50,60,70,80],
                 [60,40,20,10]])
print("Array:",array)

lst=array.tolist()
print("List:",lst)

# Convert Python List to A NumPy Array

#Lists can convert to arrays using the
# built-in functions in the Python NumPy library.

#How to convert a list to an array in Python

#NumPy provides us with two functions to use
# when converting a list into an array:

#    numpy.array()
 #   numpy.asarray()

#numpy.array() : Using numpy.array() This function of the numpy library allows a list as an argument and returns an array that contains all the elements of the list. See the example below: import numpy as np. …


#Use asarray() : 
lst= [20,40,60,80]
array = np.asarray(lst)
print("Array:",array)
print(type(array))

#NumPy Array Properties:
     #ndarray.shape - paranthesis not given in properties
     #ndarray.ndim
     #ndarray.itemsize
     #ndarray.size
     #ndarray.dtype

#Shape
array= np.array([[1,2,3],[4,5,6]])
print(array.shape)

#Resize the Array
array= np.array([[1,2,3],[4,5,6]])
array.shape=(3,2)
print(array)

#NumPy also provides numpy.reshape() function
#Reshape usage
array = np.array([[1,2,3],[4,5,6]])
new_array= array.reshape(3,2)
print(new_array)

#Usage of ndim
array = np.array([[10,20,30,40],
                 [50,60,70,80],
                 [60,40,20,10]])
print(array.ndim)

#Apply arithmetic operations on numpy arrays
arr1 = np.arange(16).reshape(4,4)
arr1
arr2 = np.array([1,3,2,4])
arr2 

#add()
add_arr = np.add(arr1,arr2)
print(f"Adding two arrays:\n{add_arr}")

#Subtract
sub_arr = np.subtract(arr1,arr2)
print(f"Subtracting two arrays:\n{sub_arr}")

#Multiply()
mul_arr = np.multiply(arr1,arr2)
print(f"Multipling two arrays:\n{mul_arr}")

#Divide()
div_arr = np.divide(arr1,arr2)
print(f"Dividing two arrays:\n{div_arr}")

#numpy.reciprocol()

#To perform Reciprocal operation
arr1 = np.array([50,10.3,5,1,200])
rep_arr1=np.reciprocal(arr1)
print(rep_arr1)

#numpy.power()

#To perform power operation
arr1 = np.array([3,10,5])
pow_arr1= np.power(arr1, 3)
print(pow_arr1)

arr2 = np.array([3,2,1])
print("My second array:\n",arr2)
pow_arr2=np.power(arr1,arr2)
print(f"After applying power function to array:\n{pow_arr2}")

#To perform mod function on NumPy array
import numpy as np
arr1 = np.array([7,20,13])
arr2 = np.array([3,5,2])
arr1
arr1.dtype
#mod()
mod_arr = np.mod(arr1,arr2)
print(f"After appling mod function to array:\n{mod_arr}")

##############################################################
#Create empty array
from numpy import empty
a = empty([3,3])
print(a)

#Create zero array
from numpy import zeros
a = zeros([3,5])
print(a)

#Create one array
from numpy import ones
a = ones([5])
print(a)

#Create array with vstack
from numpy import array
from numpy import vstack
#Create first array
a1 = array([1,2,3])
print(a1)

#Create second array
a2 = array([4,5,6])
print(a2)

#Vertical stack
a3 = vstack((a1,a2))
print(a3)
print(a3.shape)
########################################################
#Create array with hstack
from numpy import array
from numpy import hstack
#Create first array
a1 = array([1,2,3])
print(a1)
#Create second array
a2 = array([4,5,6])
print(a2)

# create Horizontal stack
a3 = hstack((a1,a2))
print(a3)
print(a3.shape)
##########################################################
#Two dimensional list of lists to array
#Create two dimensional array
from numpy import array
#list of data
data = [[11,22],
        [33,44],
        [55,66]]
#array of data
data = array(data)
print(data)
print(type(data))
#################################################################
#Index a One-dimensional array
from numpy import array
#Define array
data = array([11,22,33,44,55])
#Index data
print(data[0])
print(data[4])
#########################################################
#Index array out of bounds








#Negative array indexing









#Index row of two-dimensional array
from numpy import array
#define array
data = array([
    [11,22],
    [33,44],
    [55,66]])
#index data
print(data[0,])








################################################
#Negative slicing of one dimensional array
from numpy import array
#define array
data = array([11,22,33,44,55])
print(data[-2:])
#############################################################
#Split input and output data
from numpy import array
#Define array
data = array([
    [11,22,33],
    [44,55,66],
    [77,88,99]])
#seperate data
X, y  = data[:, :-1], data[:, -1]
#data[:,:-1]-all rows and all columns
#except all rows and last columns
#data[:, -1]-taking all rows(:)
#But keeping the last column

print(X)
print(y)
#############################################################
#broadcast scalar to one-dimensional array
from numpy import array
#define array
a = array([1,2,3])
print(a)
#define scalar
b = 2
print(b)
#broadcast
c = a + b
print(c)
##################################################
#vector additon
from numpy import array
#define 1st vector
a  = array([1,2,3])
print(a)
# define second vector
b = array([1,2,3])
print(b)
#add vectors
c = a + b
print(c)
#####################################################
#Vector subtraction
#define 1st vector
a  = array([1,2,3])
print(a)
# define second vector
b = array([0.5,0.5,0.5])
print(b)
#Subtract vectors
c = a-b
print(c)
#######################################################
#Vector multiplication
#define 1st vector
a  = array([1,2,3])
print(a)
# define second vector
b = array([2,5,7])
print(b)
#Multiply vectors
c = a*b
print(c)
###################################################
#Vector Division
#define 1st vector
a  = array([2,5,3])
print(a)
# define second vector
b = array([2,2,2])
print(b)
#Divide vectors
c = a/b
print(c)
################################################
#vector L1 norm
from numpy import array
from numpy.linalg import norm
#define vector
a = array([1,2,3])
print(a)
#calculate norm
l1 = norm(a,1)
print(l1)
############################
#vector L2 norm
from numpy import array
from numpy.linalg import norm
#define vector
a = array([1,2,3])
print(a)
#calculate norm
l2 = norm(a)
print(l2)
###########################################
#triangular array
from numpy import array
from numpy import tril
from numpy import triu
#define square matrix
M = ([
      [1,2,3],
      [1,2,3],
      [1,2,3]])
print(M)
#lower triagular matrix
lower = tril(M)
print(lower)
#lower triagular matrix
upper = triu(M)
print(upper)
######################################
#diagonal matrix
from numpy import array
from numpy import diag
#define square matrix
M = ([
      [1,2,3],
      [1,5,3],
      [1,2,9]])
print(M)
# extract diagonal vector
d = diag(M)
print(d)
#create create diagonal matrix from vector
D = diag(d)
print(D)


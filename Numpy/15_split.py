#SPLIT FUNCTION IN NUMPY
import numpy as np

#SPLIT
# split() is a function in numpy which is used to split an array into two or more arrays

#1D array
var = np.array([1,2,3,4,5,6,7,8,9,10])
print("Original array: ",var)
print("\n")

#Splitting of array into two arrays using split() function
sp = np.array_split(var,3)
print("Split array : ",sp)
print("\n")

#OR

print("Split array 1: ",sp[0])
print("Split array 2: ",sp[1])
print("Split array 3: ",sp[2])
print("\n")

#2D array
var_1 = np.array([[1,2,3,4],[13,14,15,16]])

sp_1 = np.array_split(var_1,2)
sp_2 = np.array_split(var_1,2,axis=1)

print("Split array : ",sp_1)
print("Splitting along axis=1 : ",sp_2)
print("\n")
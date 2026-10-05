#SLICING IN NUMPY
import numpy as np

#SLICING
#1D array slicing
a = np.array([1,2,3,4,5,6,7,8,9,10])
print("1D array: ")
print(a)
print("The values at index 1,3,5,7 are: ",a[1:9:2]) #prints [2,4,6,8]
print("\n")

#2D array slicing
b = np.array([[1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16]])
print("2D array: ")
print(b)
print("2 to 6: ",b[0,1:6]) #prints [2,3,4,5,6]
print("2 to 6: ",b[1,1:6]) #prints [9,10,11,12,13]
print("\n")

#3D array slicing
c = np.array([[[1,2,3,4,5,6]],[[7,8,9,10,11,12]]])
print("3D array: ")
print(c)
print("The values are: ",c[0,0,1:4]) #prints [2,3,4]
print("The values are: ",c[0,0,1:6:2]) #prints [2,4,6]
print("\n")
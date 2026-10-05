#INDEXING IN NUMPY
import numpy as np

#1D array indexing
a = np.array([1,2,3])
print("1D array: ",a)
print("The value at index 1 is: ",a[1]) #prints 2
print("\n")

#2D array indexing
b = np.array([[1,2,3],[4,5,6]])
print("2D array: ")
print(b)
print("The value at index (1,2) is: ",b[1,2]) #prints 5
print("\n")

#3D array indexing
c = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("3D array: ")
print(c)
print("The value at index (0,1,2) is: ",c[0,1,2]) #prints 12
print("\n")

c1 = np.array([[[1,2],[3,4]]])
print("3D array 2: ")
print(c1)
print("The value at index (0,0,1) is: ",c1[0,0,1]) #prints 2
print("\n")

#4D array indexing
d = np.array([[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]],[[[13,14,15],[16,17,18]],[[19,20,21],[22,23,24]]]])
print("4D array: ")
print(d)
print("The value at index (1,1,1,2) is: ",d[1,1,1,2]) #prints 24
print("\n")
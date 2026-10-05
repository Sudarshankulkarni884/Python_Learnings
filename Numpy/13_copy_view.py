#COPY AND VIEW IN NUMPY
import numpy as np

#COPY
# copy() is a function in numpy which is used to create a copy of an array
#change in the copied array will not affect the original array
a = np.array([1,2,3,4])
co = a.copy()
a[0] = 10
print("Original array: ",a)#prints [10,2,3,4]
print("Copied array: ",co)#prints [1,2,3,4]
print("\n")

#VIEW
# view() is a function in numpy which is used to create a view of original array
# change in the view array will affect the original array
b = np.array([9,8,7,6])
vw = b.view()
b[0] = 90
print("Original array: ",b)#prints [90,8,7,6]
print("View array: ",vw)#prints [90,8,7,6]
#JOIN ARRAYS IN NUMPY
import numpy as np

#JOIN
# join() is a function in numpy which is used to join two or more arrays
'''
#Joining of array using concatenate() function
#1D array
var = np.array([1,2,3,4])
var1 = np.array([5,6,7,8])

ar = np.concatenate((var,var1),axis=0)
print("Joined array: ",ar)
print("\n")

#2D array
var_1 = np.array([[1,2,3],[4,5,6]])
var_2 = np.array([[7,8,9],[10,11,12]])
ar_1 = np.concatenate((var_1,var_2),axis=1)
print("Joined array: \n",ar_1)
print("\n")

#3D array
var_3 = np.array([[[1,2,3,4,5,6]],[[7,8,9,10,11,12]]])
var_4 = np.array([[[13,14,15,16,17,18]],[[19,20,21,22,23,24]]])
ar_2 = np.concatenate((var_3,var_4),axis=2)
print("Joined array: \n",ar_2)
print("\n")
'''

#Joining of array using stack() function
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c_1 = np.stack((a,b),axis=0)#axis=0 and vstack() are same
c_2 = np.hstack((a,b))#horizontal stack
c_3 = np.vstack((a,b))#vertical stack
c_4 = np.dstack((a,b))#depth stack
print("Stacked array: \n",c_1)
print("Horizontal Stacked array: \n",c_2)
print("Vertical Stacked array: \n",c_3)
print("Depth Stacked array: \n",c_4)
print("\n")
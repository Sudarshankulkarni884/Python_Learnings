#ITERATION IN NUMPY
import numpy as np

'''
#ITERATION 
# iteration is the process of going through elements of an array one by one. In numpy
# we can iterate through an array by using for loop

#1D array iteration
var = np.array([1,2,3,4])
print("1D array: ",var)
for i in var:
    print(i) # or print(i,end=" ") #prints 1 2 3 4
print("\n")

#2D array iteration
var1 = np.array([[1,2,3],[4,5,6]])
for i in var1:
    for j in i:
        print(j)
    print()
print("\n")

#3D array iteration
var2 = np.array([[[1,2,3,4,5,6]],[[7,8,9,10,11,12]]])
print("3D array: ",var2)
for i in var2:
    for j in i:
        for k in j:
            print(k)
        print()
'''

#For each dimension we should use a for loop to iterate
#1D = 1 for loop , 2D = 2 for loops , 3D = 3 for loops and so on


##ITERATION USING nditer()
#nditer() is a function in numpy which is used to iterate through an array
#Example_01:
ary = np.array([[9,8,7],[4,5,6]])
for i in np.nditer(ary):
    print(i)
print("\n")

#Example_02:
ary_1 = np.array([[[3,7,9,4,5,6]],[[1,2,3,4,5,6]]])
for i in np.nditer(ary_1,flags=['buffered'],op_dtypes = ["S"]):
 #flags = ['buffered'] is used to iterate through the array without copying the array
    print(i)
print("\n")

#ITERATION USING np.ndnumerate()
#np.ndnumerate() is a function in numpy which is used to iterate through an array with index
ary_2 = np.array([[[3,7,9,4]],[[1,2,3,4]]])
for i,j in np.ndenumerate(ary_2): # or i,d in np.ndenumerate(ary_2)
    print(i,j)
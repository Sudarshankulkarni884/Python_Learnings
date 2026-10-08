import numpy as np
'''
# SEARCH IN NUMPY

#SEARCH
# search() is a function in numpy which is used to search for an element in an array
# search() function returns the index of the element if found else returns -1

#1D array
var = np.array([1,2,3,4,2,6,7,8,2,10])
# index         0,1,2,3,4,5,6,7,8,9
x = np.where(var == 2)
y = np.where(var%2 == 0)
print("Index of element 2 in array: ",x)
print(y)
print("\n")

#2D array
var_1 = np.array([[1,2,5,4],[5,6,7,8],[9,10,5,12]])
z = np.where(var_1 == 5)
print("var_1: \n",var_1)
print("Index of element 5 in array: ",z)
#It prints (array([0, 1, 2])-> row index, array([2, 0, 2])) -> column index
print("\n")

#3D array
var_2 = np.array([[[1,2,3,4,7,6]],[[7,8,9,10,11,12]]])
w = np.where(var_2 == 7)
print("var_2: \n",var_2)
print("Index of element 7 in array: ",w)
#It prints array([0, 1]) -> {axis = 0}depth index, array([0, 0]) -> {axis = 1} row index, array([4,0]) -> {axis = 2} coloumn index
print("\n")
'''

#SEARCH SORTED ARRAY
a = np.array([1,2,3,4,5,7,8,9,10])
search_sorted = np.searchsorted(a,5)
print("Index of element 5 in sorted array: ",search_sorted)

#SORT ARRAY
b = np.array([1,3,54,2,65,7,2,0])
sort = np.sort(b)
print("Sorted array: ",sort)

#FILTER ARRAY
c = np.array(['64','10','16','98','23','1','45'])
filter = [True, False, False, True, False, True, False]
new_array = c[filter]
print("Filtered array: ",new_array)
#NUMPY FUNCTION
import numpy as np

#SHUFFLE FUNCTION
a = np.array([1,2,3,4,5])
np.random.shuffle(a)
print("Shuffled array: \n",a)

#UNIQUE FUNCTION
b = np.array([1,2,3,4,2,5,6,2,7,2,8,9,2])
unique = np.unique(b,return_index=True,return_counts=True)
print("Unique elements in array: \n",unique)

#RESIZE FUNCTION
c = np.array([1,2,3,4,5,6,7,8,9,10])
resize = np.resize(c,(5,2))
print("Resized array: \n",resize)

#FLATTEN  AND RAVEL FUNCTION
# flatten() and ravel() is a function in numpy which is used to convert a multidimensional array into a 1D array
d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Flatten array:default order 'C' \n",d.flatten())
print("Flatten array: 'F' \n",d.flatten('F'))#or d.flattern(order="F")
print("Flatten array: 'A' \n",d.flatten('A'))#or d.flattern(order="A")
print("Flatten array: 'K' \n",d.flatten('K'))#or d.flattern(order="K")
print()
'''
print("Ravel array:default order 'C' \n",d.ravel())
print("Ravel array: 'F' \n",d.ravel('F'))#or d.ravel(order="F")
print("Ravel array: 'A' \n",d.ravel('A'))#or d.ravel(order="A")
print("Ravel array: 'K' \n",d.ravel('K'))#or d.ravel(order="K")
'''

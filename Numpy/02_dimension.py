import numpy as np
#1 dimension array
ar1 = np.array([1,2,3])
print(ar1)
print(ar1.ndim)

#2 dimension array
ar2 = np.array([[1,2,3],[4,5,6]])
print(ar2)
print(ar2.ndim)

#3 dimension array
ar3 = np.array([[[1,2,3],[7,8,9],[10,11,12]]])
print(ar3)
print(ar3.ndim)

#multidimensional array
arn = np.array([1,2,3,4],ndmin =10)
print(arn)
print(arn.ndim)
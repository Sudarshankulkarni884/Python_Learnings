#SHAPE AND RESHAPE
import numpy as np

#SHAPE
a = np.array([[1,2,3],[4,5,6]])
print(a)
print("Shape of a: ",a.shape)
print("\n")

b = np.array([1,2,3,4],ndmin=4)
print (b)
print("Shape of b: ",b.shape)
print("\n")

#RESHAPE
c = np.array([1,2,3,4,5,6])
reshp = np.reshape(c,(3,2))
print("Shape of reshp: ",reshp.shape)
print(reshp)
print("\n")

#RESHAPE WITH -1
# -1 means in simple language that the value of that dimension will be automatically calculated
d = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(d)
print("Shape of d: ",d.shape)
print("\n")

e = np.reshape(d,(6,-1))
print("Shape of e: ",e.shape)
print(e)

f = np.reshape(d,(-1))
print("Shape of f: ",f.shape)
print(f)
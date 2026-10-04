#Arithmetic Functions in Numpy
import numpy as np

#MAXIMUM

#1 dimensional array
a = np.array([10,20,30])
max = np.max(a)
print("Maximum: ",max)

#2 dimensional array
b = np.array([[2,1,9],[4,8,6]])
max1 = np.max(b,axis=0)
max2 = np.amax(b,axis=1)
print("Maximum in 2D column: ",max1)
print("Maximum in 2D row: ",max2)


#MINIMUM

#1 dimensional array
min = np.min(a)
print("Minimum: ",min)

#2 dimensional array
print("Minimum in 2D column: ",np.min(b,axis=0))
print("Minimum in 2D row: ",np.min(b,axis=1))


#ARGMAXIMUM AND ARGMINIMUM
print("Maximum Number and Index of Maximum: ",np.max(a), np.argmax(a))
print("Minimum Number and Index of Minimum: ",np.min(a), np.argmin(a))


#SQUARE ROOT
sq = np.array([[4,9,16],[25,36,49]])
print("Square Root: ",np.sqrt(sq))

#SINE AND COSINE
num = np.array([0,30,45,60,90])
print("Sine: ",np.sin(num))
print("Cosine: ",np.cos(num))

#CUMMULATIVE SUM
cmsum = np.array([1,2,3,4,5])
print("Cummulative Sum: ",np.cumsum(cmsum))

#CUMMULATIVE PRODUCT
cmprod = np.array([1,2,3,4,5])
print("Cummulative Product: ",np.cumprod(cmprod))

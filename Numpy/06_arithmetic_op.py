#Arithmetic Operations in Numpy
import numpy as np

#Addition
a = np.array([1,20,30])   #1D
add = a + 5
print("Addition: ",add)

b = np.array([[40,50,60]])   #2D
add1 = a + b
add2 = np.add(a,b)
print("Addition (method 1): ",add1)
print("Addition (method 2): ",add2)
print("Addition (method 2) dimensions: ",add2.ndim)

c = np.array([[70,80,90],[20,30,40]])   #2D
d = np.array([[10,20,30]])   #2D
add3 = d + c
print("Addition (method 3): ",add3)

#Subtraction
sub = a - 5
sub1 = np.subtract(a,5)
print("Subtraction: ",sub)
print("Subtraction (method 1): ",sub1)

#Multiplication
mul = a * 5
mul1 = np.multiply(a,5)
print("Multiplication (method 1): ",mul1)
print("Multiplication: ",mul)

#Division
div = a / 5
div1 = np.divide(a,5)
print("Division (method 1): ",div1)
print("Division: ",div)

#Power
pow = a ** 5
pow1 = np.power(a,5)
print("Power (method 1): ",pow1)
print("Power: ",pow)

#Modulus
mod = a % 5
mod1 = np.mod(a,5)
print("Modulus (method 1): ",mod1)
print("Modulus: ",mod)

#Maximum
max = np.max(a)
max1 = np.amax(a) #or np.max(a)
print("Maximum (method 1): ",max1)
print("Maximum: ",max)
    
#Minimum
min = np.min(a)
min1 = np.amin(a) #or np.min(a)
print("Minimum (method 1): ",min1)
print("Minimum: ",min)

#reciprocal
rec = np.reciprocal(a)
rec1 = np.reciprocal(a)
print("Reciprocal (method 1): ",rec1)
print("Reciprocal: ",rec)
#Arithmetic Operations in Numpy
import numpy as np

#ADDITION
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

#SUBTRACTION
sub = a - 5
sub1 = np.subtract(a,5)
print("Subtraction: ",sub)
print("Subtraction (method 1): ",sub1)

#MULTIPLICATION
mul = a * 5
mul1 = np.multiply(a,5)
print("Multiplication (method 1): ",mul1)
print("Multiplication: ",mul)

#DIVISION
div = a / 5
div1 = np.divide(a,5)
print("Division (method 1): ",div1)
print("Division: ",div)

#POWER
pow = a ** 5
pow1 = np.power(a,5)
print("Power (method 1): ",pow1)
print("Power: ",pow)

#MODULUS
mod = a % 5
mod1 = np.mod(a,5)
print("Modulus (method 1): ",mod1)
print("Modulus: ",mod)

#reciprocal
rec = np.reciprocal(a)
rec1 = np.reciprocal(a)
print("Reciprocal (method 1): ",rec1)
print("Reciprocal: ",rec)
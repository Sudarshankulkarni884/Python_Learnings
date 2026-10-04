import numpy as np

x = np.array([1,2,3,4])
print(x)
print(type(x))
print(x.ndim)

y = [1,2,3,4]
print(y)
print(type(y))

z = np.array(y)
print(z)
print(type(z))


l = []
for i in range(1,6):
    val = int(input("Enter a value: "))
    l.append(val)
print(np.array(l))
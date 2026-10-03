import numpy as np
'''
a = np.array([1,2,3,4])
print("Data type: ",a.dtype)

b = np.array([1.0,2.5,3.0,4.0])
print("Data type: ",b.dtype)

c = np.array([1+2j, 2+3j, 3+4j, 4+5j])
print("Data type: ",c.dtype)

d = np.array(["a","b","c","d"])
print("Data type: ",d.dtype)

e = np.array(["a","b","c","d",1,1,2,3,4])
print("Data type: ",e.dtype)
'''
'''
a = np.array([1,2,3,4],dtype = np.int32)
print("Data type: ",a.dtype)
print(a)

b = np.array([1,2,3,4],dtype = np.float32)
print("Data type: ",b.dtype)
print(b)
'''
#OR
p = np.array([1,2,3,4],dtype = "f")
print("Data type: ",p.dtype)
print()

q = np.array([1,2,3,4])
new = np.float32(q)
print("Data type: ",q.dtype)
print(q)
print(new)
print()

s = np.array([1,2,3,4])
new1 = s.astype(float)
print(s)
print(new1)
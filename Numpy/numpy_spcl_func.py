import numpy as np
'''
#Zeroes array
ar_zero = np.zeros(3)
ar_zero1 = np.zeros((2,4))
print(ar_zero)
print()
print(ar_zero1)
'''

'''
#Ones array
ar_one = np.ones(3)
ar_one1 = np.ones((2,4))
print(ar_one)
print()
print(ar_one1)
'''

'''
#Empty array
ar_empty = np.empty(3) #prints previous values in memory or "garbage values in memory"
print(ar_empty)
ar_empty1 = np.empty((2,4))
print(ar_empty1)
'''

'''
#Range function
ar_rn = np.arange(3)#its like range function in python
ar_rn1 = np.arange(3,6)
print(ar_rn)
print(ar_rn1)
'''

'''
#diagonal function
ar_dia = np.diag([1,2,3])
print(ar_dia)

#diagonal function with ones
ar_dia1 = np.eye(3)
ar_dia2 = np.eye(3,4)
print(ar_dia1)
print(ar_dia2)
'''

#Linear spaced array
#its not linespace its linspace
ar_lin = np.linspace(0,10,5)
print(ar_lin)
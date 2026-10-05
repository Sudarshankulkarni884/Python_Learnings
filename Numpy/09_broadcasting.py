#BROADCASTING IN NUMPY
import numpy as np

#BROADCASTING
# 1st Example
num = np.array([1,2,3,4]) # 1X4
print("Num: ",num)
print("Shape of num: ",num.shape)
num1 = np.array([[1],[2],[3],[4]]) # 4X1
print("Num1: \n",num1)
print("Shape of num1: ",num1.shape)
print("Broadcasting: \n",num+num1)
print("\n")

# 2nd Example
num_1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) # 3X4
print("Num_1: ",num_1)
print("Shape of num_1: ",num_1.shape)
num_2 = np.array([1]) # 1X1
print("Num_2: ",num_2)
print("Shape of num_2: ",num_2.shape)
print("Broadcasting_1: \n",num_1+num_2)
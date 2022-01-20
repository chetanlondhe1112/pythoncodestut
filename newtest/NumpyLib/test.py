#Numpy introduction

import numpy as np
l1 = [1, 2, 3, 4]
n1 = np.array(l1)
print(l1)
print(n1)

#Initializing numpy array with range
n1 = np.arange(10, 20)   #20 excluded
print(n1)

n2 = np.arange(10, 50, 5)
print(n2)

#Initializing numpy array with random numbers
n1 = np.random.randint(1, 100, 5)
print(n1)

#checking the shape of numpy arrays
n1 = np.array([[1,2,3,4],[5,6,7,8]])
print(n1.shape)
n1.shape = (4, 2)
print(n1)
print(n1.shape)
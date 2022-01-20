# Joining Numpy array
import numpy as np

# Vstack Joining vertically

n1 = np.array([1, 2, 3, 4, 5])
n2 = np.array([6, 7, 8, 9, 10])

nV = np.vstack((n1,n2))
print(nV)

# Hstack Joining Horizontaly
nh = np.hstack((n1,n2))
print(nh)

# column_stack() joining column wise
nC = np.column_stack((n1,n2))
print(nC)
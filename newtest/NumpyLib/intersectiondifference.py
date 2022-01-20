# Intersection and Difference
import numpy as np

#intersection
n1 = np.array([1, 2, 3, 4, 5, 6, 7])
n2 = np.array([6, 7, 8, 9, 10])

nI = np.intersect1d(n1, n2)
print(nI)

nI2 = np.intersect1d(n2, n1)
print(nI2)

nD = np.setdiff1d(n1,n2)
print(nD)

nD2 = np.setdiff1d(n2,n1)
print(nD2)

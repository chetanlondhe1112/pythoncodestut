# addition of numpy arrays
import numpy as np
n1 = np.array([10, 20])
n2 = np.array([30, 40])
NS = np.sum([n1, n2])
print(NS)

N1 = np.sum([n1, n2], axis=0)
print(N1)

N2 = np.sum([n1, n2], axis=1)
print(N2)

import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

#Deteminant
print(np.linalg.det(A))

#Inverse
print(np.linalg.inv(A))

#EigenValues

values, vectors = np.linalg.eig(A)

#Norm
x = np.array([3, 4])

print(np.linalg.norm(x))
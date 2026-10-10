import numpy as np

x = np.array([
    [2],
    [3]
])

w = np.array([
     [0.5, 0.2],
    [0.1, 0.7],
    [0.4, 0.3]
])

b = np.array([
    [1],
    [0],
    [2]
])

z = w @ x + b

print(z)
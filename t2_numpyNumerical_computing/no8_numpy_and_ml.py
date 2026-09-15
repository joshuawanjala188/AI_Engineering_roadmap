#consider y=Xw + b

import numpy as np

X = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

w = np.array([0.5, 1.0])

b = 2

y = X @ w + b
print(y)



import numpy as np
from sklearn.linear_model import LinearRegression


X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5]


])

y = np.array([
    40,
    50,
    60,
    70,
    80
])

model = LinearRegression()


model.fit(X, y)

prediction = model.predict([[9]])

print(prediction)



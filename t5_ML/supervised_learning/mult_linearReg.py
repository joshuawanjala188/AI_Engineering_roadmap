from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([
    [5, 80],
    [3, 70],
    [8, 95],
    [2, 60],
    [7, 90]
])

y = np.array([
    75,
    55,
    90,
    45,
    85
])


model = LinearRegression()

model.fit(X, y)

new_student = [[6, 85]]
prediction = model.predict(new_student)

print(prediction)

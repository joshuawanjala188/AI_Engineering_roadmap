import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8],
    [9],
    [10]
])

y = np.array([
    35,
    42,
    50,
    58,
    65,
    72,
    78,
    85,
    91,
    98
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()

model.fit(X_train, y_train)

prediction = model.predict(X_test)
print(prediction)

mae = mean_absolute_error(y_test, prediction)

print("MAE:", mae)

print("Weight:", model.coef_)
print("Bias:", model.intercept_)
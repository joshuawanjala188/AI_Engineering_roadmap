import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import(StandardScaler, OneHotEncoder)

df = pd.DataFrame({
    "age": [20, 22, 25, 30, 35, 40, 45, 50],
    "salary": [
        30000,
        35000,
        42000,
        50000,
        60000,
        70000,
        85000,
        100000
    ],
    "city": [
        "Nairobi",
        "Nakuru",
        "Nairobi",
        "Mombasa",
        "Nakuru",
        "Nairobi",
        "Mombasa",
        "Nairobi"
    ],
    "passed": [
        0, 0, 0, 1, 1, 1, 1, 1
    ]
})

#Separate feautures

X = df[[
    "age",
    "salary",
    "city"
]]

y = df["passed"]

print(y)
# pandas is a python library for working with structured data
#Two most importtant data structures are Series and DataFrame
import pandas as pd

# Series - like one dimensional labelled collection of data

#scores = pd.Series([13, 23, 32, 49, 56])
#print(scores)

#data frame is like a table

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "score": [85, 45, 72, 91],
    "country": ["Kenya", "Uganda", "Kenya", "Tanzania"]
}

df = pd.DataFrame(data)


# inspecting your data
#After loading a dataset, dont immediately start processing it, first inspect it
#head() it shows the first rows and yiu can specify how many
#print(df.head(2))
#tail()
#print(df.tail(2))

#shape- number of rows and columns it has
#print(df.shape) 

#columns
#print(df.columns)

#dtypes
#print(df.dtypes)

#info - it gives number of rows, column names, missing values, data types, and memory usage when working with unfamiliar dataset it should be your first commands

#print(df.info)

#Statistical Summary - 
#print(df.describe())

#print(df["score"].describe())

#Selecting a column

#print(df["name"])
#print(df["score"])

# selecting multiple columsn

result = df[["name", "score"]]
#print(result)

#Selecting rows with i loc - iloc uses interger position

print(df.iloc[0])
print(df.iloc[2]) #print the first 2- rows
"""
10. Selecting with loc

loc works with labels/conditions.

For example:

print(df.loc[0])

You can select specific columns:

print(df.loc[:, ["name", "score"]])

The basic idea:

iloc → position
loc  → label/condition
"""

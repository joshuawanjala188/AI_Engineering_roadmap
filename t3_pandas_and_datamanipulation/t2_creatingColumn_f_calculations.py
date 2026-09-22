import pandas as pd


data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "score": [85, 45, 72, 91],
    "country": ["Kenya", "Uganda", "Kenya", "Tanzania"]
}

df = pd.DataFrame(data)

df["bonus_score"] = df["score"] + 5
df["score_percentage"] = df["score"] / 100

#renaming

df = df.rename(
    columns={
        "name": "student_name",
        "score": "exam_score"
    }
)


#removing colums

#df = df.drop(columns=["country"])

#missing data df.isna() and df.isna.sum() counts them



#print(df.isna().sum())

# removing missing rows
df = df.dropna() 
"""#NB - This removes rows containing missing values.

But don't automatically do this with every dataset.

You need to understand why the values are missing first."""
print(df.duplicated())
print(df["country"].nunique())



#GroupBy

result = df.groupby("country")["exam_score"].mean()
print(result)

#multiple agreegation

result = df.groupby("country")["exam_score"].agg(
    ["mean", "min", "max", "count"]
)

print(result)
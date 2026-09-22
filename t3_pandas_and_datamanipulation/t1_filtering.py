import pandas as pd


data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "score": [85, 45, 72, 91],
    "country": ["Kenya", "Uganda", "Kenya", "Tanzania"]
}

df = pd.DataFrame(data)

passed = df[df['score'] >= 80]
print(passed)

#multiple conditions

result = df[
    (df["score"] >= 50) &
    (df['country'] == "Kenya")
]

#print(result)

#sorting - 

sorted_df = df.sort_values("score", ascending=False)
#print(sorted_df)


#Adding a column
df["passed"] = df["score"] >= 50

print(df)



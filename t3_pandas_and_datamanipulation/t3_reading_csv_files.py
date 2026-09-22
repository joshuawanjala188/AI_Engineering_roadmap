import pandas as pd 


df = pd.read_csv("students.csv")

print(df)

#Saving csv , index=False prevents Pandas from adding the DataFrame index as an extra column.
df.to_csv("clean_students.csv", index=False)
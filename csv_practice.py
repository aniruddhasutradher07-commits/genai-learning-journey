import pandas as pd
df = pd.read_csv("students.csv")
print(df)
print(df.head())
print(df.describe())
print(df.info())
print(df["Marks"].mean())
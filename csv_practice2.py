import pandas as pd
df2 = pd.read_csv("students2.csv")
grouped = df2.groupby("Department")["Marks"].mean()
print(grouped)
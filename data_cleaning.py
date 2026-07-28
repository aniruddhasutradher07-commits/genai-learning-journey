import pandas as pd

df = pd.read_csv("messy_data.csv")
print(df)
print(df.isnull())
print(df.isnull().sum())
df_dropped = df.dropna()
print(df_dropped)
df_filled = df.fillna(0)
print(df_filled)

df_filled_mean = df["Age"].fillna(df["Age"].mean())
print(df_filled_mean)

data_with_duplicates = {
    "Naam": ["Ani", "Disha", "Ani"],
    "Age": [20, 21, 20]
}
df2 = pd.DataFrame(data_with_duplicates)
print(df2)

print(df2.duplicated())
df2_clean = df2.drop_duplicates()
print(df2_clean)
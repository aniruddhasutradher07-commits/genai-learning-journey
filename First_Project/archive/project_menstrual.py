import pandas as pd

df = pd.read_csv("menstrual_cycle_data.csv")

print(df.head())
print(df.info())
print(df.shape)
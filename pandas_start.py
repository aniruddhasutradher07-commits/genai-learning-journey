import pandas as pd

data = {
    "Naam":["Ani","Disha","Shiro"],
    "Age" :[20,21,22]
}
df = pd.DataFrame(data)
print(df)

print(df["Naam"])
print(df.loc[1])
print(df[df["Age"]> 20])

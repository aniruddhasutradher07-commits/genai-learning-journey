import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("menstrual_cycle_data.csv")

print(df.head())
print(df.info())
print(df.shape)

print(df.describe())

print(df["Symptoms"].value_counts())

print(df["Exercise Frequency"].unique())
print(df["Diet"].unique())

print(df.groupby("Exercise Frequency")["Cycle Length"].mean())

print(df.groupby("Diet")["Stress Level"].mean())
print(df.groupby("Symptoms")["Age"].mean())

fig, axes = plt.subplots(1,2,figsize=(12,5))

diet_stress = df.groupby("Diet")["Stress Level"].mean()
diet_stress.plot(kind="bar", ax=axes[0], color="skyblue")
axes[0].set_title("Diet vs Stress Level")
axes[0].set_ylabel("Avg Stress Level")

symptom_counts = df["Symptoms"].value_counts()
symptom_counts.plot(kind="bar", ax=axes[1], color="salmon")
axes[1].set_title("Symptom Frequency")
axes[1].set_ylabel("Count")

diet_stress.plot(kind="bar")
plt.xlabel("Diet Type")
plt.ylabel("Average Stress Level")
plt.title("Diet Type vs Average Stress Level")

plt.tight_layout()
plt.show()
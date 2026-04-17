import pandas as pd

df = pd.read_csv("C:/Users/HP/Downloads/data_analyst/sample_data.csv", sep="\t")

city_stats = df.groupby("City")["Salary"].mean()
print("Average Salary by City:\n")
print(city_stats)

pivot = df.pivot_table(
    values="Salary",
    index="City",
    columns="Age",
    aggfunc="mean"
)

print("\nData Pivot Table:\n")
print(pivot)
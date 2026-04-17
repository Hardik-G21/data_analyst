import pandas as pd

df = pd.read_csv("sales_cleaned.csv")

pivot = df.pivot_table(
    values='Sales',
    index='Product',
    aggfunc=['sum', 'mean']
)

print("--- Product Performance Pivot ---")
print(pivot)
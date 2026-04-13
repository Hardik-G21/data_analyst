# Compare Total Sales across Product Categories

import pandas as pd

df = pd.read_csv("sales_cleaned.csv")

# Values = What you calculate | Index = Rows | Columns = Columns
pivot = df.pivot_table(
    values='Sales',
    index='Product',
    aggfunc=['sum', 'mean']
)

print("--- Product Performance Pivot ---")
print(pivot)
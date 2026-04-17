import pandas as pd

df = pd.read_csv("C:/Users/HP/Downloads/data_analyst/day10/sales_cleaned.csv")

df['Sales'] = df['Price'] * df['Quantity']

pivot_comparison = df.pivot_table(
    values='Sales',
    index='Region',
    columns='Category',
    aggfunc='sum'
)

print("Regional Category Performance:")
print(pivot_comparison)
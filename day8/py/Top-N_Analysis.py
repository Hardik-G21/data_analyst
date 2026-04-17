import pandas as pd

df = pd.read_csv("C:/Users/HP/Downloads/data_analyst/day8/sales_cleaned.csv")

df['Sales'] = df['Price'] * df['Quantity']

top_performers = df.groupby('Product')['Sales'].sum().nlargest(5)

total_rev = df['Sales'].sum()

contribution_pct = (top_performers.sum() / total_rev) * 100

print("Top 5 Products:\n", top_performers)
print(f"\nTop 5 Products contribute {contribution_pct:.2f}% of total revenue.")
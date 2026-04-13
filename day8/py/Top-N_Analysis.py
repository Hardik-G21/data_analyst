import pandas as pd

# Load data
df = pd.read_csv("C:/Users/HP/Downloads/data_analyst/day8/sales_cleaned.csv")

# IMPORTANT: Create Sales column if not present
df['Sales'] = df['Price'] * df['Quantity']

# Finding the Top 5 products by total revenue
top_performers = df.groupby('Product')['Sales'].sum().nlargest(5)

# Calculate what percentage of total revenue the Top 5 represent
total_rev = df['Sales'].sum()

contribution_pct = (top_performers.sum() / total_rev) * 100

print("Top 5 Products:\n", top_performers)
print(f"\nTop 5 Products contribute {contribution_pct:.2f}% of total revenue.")
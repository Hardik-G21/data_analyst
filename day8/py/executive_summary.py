import pandas as pd

# Load your sales data
df = pd.read_csv("C:/Users/HP/Downloads/data_analyst/day8/sales_cleaned.csv")

# 1. Multi-level Grouping
# We want to see Total Sales and Average Quantity by Product AND Date
df['Sales'] = df['Price'] * df['Quantity']
summary = df.groupby(['Product', 'Date']).agg({
    'Sales': ['sum', 'count'],
    'Quantity': 'mean'
})

# 2. Rename columns for clarity
summary.columns = ['Total_Revenue', 'Transaction_Count', 'Avg_Qty_Per_Order']

print("Executive Deep-Dive:")
print(summary.head(10))

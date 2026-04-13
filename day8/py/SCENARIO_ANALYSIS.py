import pandas as pd

# Load data
df = pd.read_csv("C:/Users/HP/Downloads/data_analyst/day8/sales_cleaned.csv")

# IMPORTANT: Create Sales column (if not already present)
df['Sales'] = df['Price'] * df['Quantity']

# Create a 'Projected_Revenue' column if we increased prices by 15%
df['Projected_Rev_High_Price'] = df['Sales'] * 1.15

# Find 'Underperforming' transactions:
# Sales that are in the bottom 25% of all transactions
low_perf_threshold = df['Sales'].quantile(0.25)

underperforming_data = df[df['Sales'] < low_perf_threshold]

print(f"Number of low-performing transactions: {len(underperforming_data)}")
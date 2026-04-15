import pandas as pd

# Load data
df = pd.read_csv("C:/Users/HP/Downloads/data_analyst/day10/sales_cleaned.csv")

# IMPORTANT: Create Sales column if not present
df['Sales'] = df['Price'] * df['Quantity']

# Create a matrix comparing Sales across Regions and Categories
pivot_comparison = df.pivot_table(
    values='Sales',
    index='Region',
    columns='Category',
    aggfunc='sum'
)

# Calculate the percentage difference between two columns if applicable
# Example: Growth between Category B and A
# pivot_comparison['Growth'] = (pivot_comparison['B'] - pivot_comparison['A']) / pivot_comparison['A']

print("Regional Category Performance:")
print(pivot_comparison)
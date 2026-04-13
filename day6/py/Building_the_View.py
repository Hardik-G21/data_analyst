import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("C:/Users/HP/Downloads/data_analyst/day5/sales_cleaned.csv")

# Create a figure with 1 row and 2 columns
fig, axes = plt.subplots(1, 2, figsize=(15, 5))

# Plot 1: Total Sales per Product (Bar Chart)
sns.barplot(
    ax=axes[0],
    x='Product',
    y='Sales',
    data=df,
    estimator=sum
)
axes[0].set_title("Total Revenue by Product")

# Plot 2: Sales Trend over Time (Line Chart)
df['Date'] = pd.to_datetime(df['Date'])
daily_sales = df.groupby('Date')['Sales'].sum()

sns.lineplot(
    ax=axes[1],
    data=daily_sales
)
axes[1].set_title("Daily Sales Velocity")

plt.tight_layout()
plt.show()
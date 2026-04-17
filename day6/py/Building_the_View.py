import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/HP/Downloads/data_analyst/day5/sales_cleaned.csv")

fig, axes = plt.subplots(1, 2, figsize=(15, 5))

sns.barplot(
    ax=axes[0],
    x='Product',
    y='Sales',
    data=df,
    estimator=sum
)
axes[0].set_title("Total Revenue by Product")

df['Date'] = pd.to_datetime(df['Date'])
daily_sales = df.groupby('Date')['Sales'].sum()

sns.lineplot(
    ax=axes[1],
    data=daily_sales
)
axes[1].set_title("Daily Sales Velocity")

plt.tight_layout()
plt.show()
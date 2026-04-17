import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/HP/Downloads/data_analyst/day10/sales_cleaned.csv")

df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df['Sales'] = df['Price'] * df['Quantity']

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Executive Business Performance Dashboard', fontsize=20)

sns.lineplot(ax=axes[0, 0], x='Date', y='Sales', data=df)
axes[0, 0].set_title('Sales Trend Over Time')

sns.barplot(ax=axes[0, 1], x='Region', y='Sales', data=df, estimator=sum)
axes[0, 1].set_title('Revenue by Region')

df['Category'].value_counts().plot.pie(
    ax=axes[1, 0],
    autopct='%1.1f%%'  
)
axes[1, 0].set_title('Sales Distribution by Category')

sns.scatterplot(ax=axes[1, 1], x='Price', y='Sales', data=df)
axes[1, 1].set_title('Price vs. Sales Volume')

axes[0, 0].annotate(
    'High Sales Spike',
    xy=(df['Date'].iloc[15], df['Sales'].iloc[15]),
    xytext=(df['Date'].iloc[5], df['Sales'].max()),
    arrowprops=dict(facecolor='red', arrowstyle='->'),
    fontsize=10,
    color='red'
)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()


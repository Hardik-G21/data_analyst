import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/HP/Downloads/data_analyst/Marketing-ROI-Suite/sample_data.csv")

df.columns = df.columns.str.strip()

print(df.columns)

if 'Date' not in df.columns:
    raise ValueError("Column 'Date' not found. Check your CSV headers.")

df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

df['ROI'] = df['Revenue'] / df['Spend']

#Z-score
df['z_score'] = (df['ROI'] - df['ROI'].mean()) / df['ROI'].std()
failed_campaigns = df[df['z_score'] < -2]

print("Failed Campaigns:")
print(failed_campaigns[['Date', 'Channel', 'ROI', 'z_score']])

#Correlation
numeric_df = df.select_dtypes(include=['float64', 'int64'])
corr = numeric_df.corr()

#Dashboard
sns.set_theme(style="whitegrid")

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Marketing ROI Dashboard - Bangalore (₹6,00,000 Budget)', fontsize=18)

#ROI Trend
sns.lineplot(ax=axes[0, 0], x='Date', y='ROI', data=df)
axes[0, 0].set_title('ROI Trend Over Time')

#Revenue by Channel
sns.barplot(ax=axes[0, 1], x='Channel', y='Revenue', data=df, estimator=sum)
axes[0, 1].set_title('Revenue by Channel')

#Heatmap
sns.heatmap(corr, ax=axes[1, 0], annot=True, cmap='coolwarm', fmt=".2f")
axes[1, 0].set_title('Correlation Heatmap')

#Scatter
sns.scatterplot(ax=axes[1, 1], x='Spend', y='Revenue', hue='Channel', data=df)
axes[1, 1].set_title('Spend vs Revenue by Channel')

#Better annotation positioning
best_channel = df.groupby('Channel')['ROI'].mean().idxmax()

axes[0, 1].annotate(
    f"Strategic Insight:\nFocus on {best_channel}\nHighest ROI\nCut spend on low-performing channels",
    xy=(0, df['Revenue'].max()),
    xytext=(1, df['Revenue'].max()*1.3),
    arrowprops=dict(facecolor='green', arrowstyle='->'),
    fontsize=10,
    color='green'
)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

#Summary
total_spend = df['Spend'].sum()
total_revenue = df['Revenue'].sum()

print("\nSummary:")
print(f"Total Spend: ₹{total_spend}")
print(f"Total Revenue: ₹{total_revenue}")
print(f"Overall ROI: {total_revenue / total_spend:.2f}")
print(f"Best Performing Channel: {best_channel}")
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_cleaned.csv")

df['Date'] = pd.to_datetime(df['Date'])

df.set_index('Date', inplace=True)

weekly_sales = df['Sales'].resample('W').sum()

print("Weekly Sales Performance:\n", weekly_sales)

weekly_sales.plot(kind='line', marker='o', color='teal')

plt.title("Weekly Revenue Trend")
plt.ylabel("Total Sales ($)")

plt.show()
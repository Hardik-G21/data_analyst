import pandas as pd
import numpy as np
import datetime as dt
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/HP/Downloads/data_analyst/day9/sales_cleaned.csv")

df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

df['Sales'] = df['Price'] * df['Quantity']

df['Date_Ordinal'] = df['Date'].map(dt.datetime.toordinal)

X = df[['Date_Ordinal']]
y = df['Sales']

model = LinearRegression()
model.fit(X, y)

print(f"Sales Trend Coefficient: {model.coef_[0]:.4f}")

last_date = df['Date_Ordinal'].max()

future_dates = np.array(
    range(last_date + 1, last_date + 31)
).reshape(-1, 1)

future_preds = model.predict(future_dates)

print("Projected Sales for the first 5 days of next month:")
print(future_preds[:5])

plt.figure(figsize=(10, 6))

plt.scatter(df['Date'], df['Sales'], color='blue', label='Actual Sales')

future_dates_dt = [dt.datetime.fromordinal(int(d)) for d in future_dates.flatten()]

plt.plot(
    future_dates_dt,
    future_preds,
    color='red',
    linestyle='--',
    label='Forecasted Trend'
)

plt.title("30-Day Sales Forecast")
plt.legend()

plt.show()
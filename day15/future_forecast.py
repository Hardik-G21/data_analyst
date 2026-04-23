import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/HP/Downloads/data_analyst/day15/daily_registrations.csv",
    parse_dates=['Date'],
    index_col='Date',
    dayfirst=True
)

df['7Day_MA'] = df['Registrations'].rolling(window=7).mean()

df['DayOfWeek'] = df.index.day_name()

avg_by_day = df.groupby('DayOfWeek')['Registrations'].mean().reindex([
    'Monday', 'Tuesday', 'Wednesday', 'Thursday',
    'Friday', 'Saturday', 'Sunday'
])

print("Average Sign-ups by Day:")
print(avg_by_day)

last_ma_value = df['7Day_MA'].iloc[-1]
print(f"Forecasted Registrations for tomorrow: {last_ma_value:.2f}")

plt.figure(figsize=(12,6))

plt.plot(df.index, df['Registrations'], label='Actual Daily Sign-ups', alpha=0.3)
plt.plot(df.index, df['7Day_MA'], label='7-Day Trend Line', linewidth=2)

plt.title('MeetMux Growth Trend Analysis')
plt.legend()
plt.xticks(rotation=45)

plt.show()
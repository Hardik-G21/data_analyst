import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("C:/Users/HP/Downloads/data_analyst/day10/sales_cleaned.csv")

df['Sales'] = df['Price'] * df['Quantity']

plt.figure(figsize=(12, 6))

sns.barplot(
    x='Region',
    y='Sales',
    hue='Category',
    data=df,
    estimator=sum
)

plt.title("Revenue Comparison: Region vs. Category")

plt.show()
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/HP/Downloads/data_analyst/day10/sales_cleaned.csv")

df['Sales'] = df['Price'] * df['Quantity']

numeric_df = df.select_dtypes(include=['float64', 'int64'])

corr_matrix = numeric_df.corr()

print("Correlation Matrix:")
print(corr_matrix)

plt.figure(figsize=(10, 8))

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap='coolwarm',
    fmt=".2f"
)

plt.title("Business Metric Correlation Heatmap")

plt.show()
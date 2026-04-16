import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load data
df = pd.read_csv("C:/Users/HP/Downloads/data_analyst/day10/sales_cleaned.csv")

# IMPORTANT: Create Sales column (needed for meaningful correlation)
df['Sales'] = df['Price'] * df['Quantity']

# 2. Select only numeric columns for correlation
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# 3. Generate the correlation matrix
corr_matrix = numeric_df.corr()

print("Correlation Matrix:")
print(corr_matrix)

plt.figure(figsize=(10, 8))

# annot=True shows values inside boxes
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap='coolwarm',
    fmt=".2f"
)

plt.title("Business Metric Correlation Heatmap")

plt.show()
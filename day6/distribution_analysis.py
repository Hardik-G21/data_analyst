import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your cleaned sales data
df = pd.read_csv("C:/Users/HP/Downloads/data_analyst/day5/sales_cleaned.csv")

# 1. SET THE THEME: Professional look
sns.set_theme(style="whitegrid")

# 2. BOX PLOT: See the spread of sales per Product
plt.figure(figsize=(10, 6))

sns.boxplot(
    x='Product',
    y='Sales',
    data=df
)

plt.title("Sales Distribution per Product (Checking for Outliers)")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.xticks(rotation=45)  # Rotate labels if many products
plt.tight_layout()

plt.show()
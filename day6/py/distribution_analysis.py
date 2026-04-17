import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/HP/Downloads/data_analyst/day5/sales_cleaned.csv")

sns.set_theme(style="whitegrid")

plt.figure(figsize=(10, 6))

sns.boxplot(
    x='Product',
    y='Sales',
    data=df
)

plt.title("Sales Distribution per Product (Checking for Outliers)")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.xticks(rotation=45)  
plt.tight_layout()

plt.show()
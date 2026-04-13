import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("C:/Users/HP/Downloads/data_analyst/day5/sales_cleaned.csv")

# This creates a grid of all numeric relationships
sns.pairplot(
    df,
    hue='Product',
    diag_kind='kde'
)

plt.show()
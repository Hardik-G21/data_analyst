import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("sales_cleaned.csv")
# Select only numeric columns for correlation
numeric_df = df.select_dtypes(include=['number'])

correlation_matrix = numeric_df.corr()

# Create a Heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='RdYlGn')

plt.title("Variable Correlation Map")
plt.show()
import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/HP/Downloads/data_analyst/day10/sales_cleaned.csv")

df['Sales'] = df['Price'] * df['Quantity']

df['z_score'] = (df['Sales'] - df['Sales'].mean()) / df['Sales'].std()

outliers = df[np.abs(df['z_score']) > 3]

print(f"Detected {len(outliers)} outliers in the dataset.")
print(outliers[['Date', 'Product', 'Sales', 'z_score']])


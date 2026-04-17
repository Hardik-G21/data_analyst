import pandas as pd

df = pd.read_csv("sample_data.csv")

print(df)

print("\nFirst 3 rows:")
print(df.head(3))
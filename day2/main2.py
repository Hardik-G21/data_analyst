import pandas as pd

# Load CSV file
df = pd.read_csv("sample_data.csv")

# Show data
print(df)

# Show first 3 rows
print("\nFirst 3 rows:")
print(df.head(3))
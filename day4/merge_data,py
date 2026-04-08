import pandas as pd

# Load both sources
df_users = pd.read_csv("users.csv")
df_sales = pd.read_csv("sales.csv")

# Merge (like VLOOKUP / SQL JOIN)
final_report = pd.merge(df_users, df_sales, on="ID", how="inner")

print("Combined Business Report:\n")
print(final_report)
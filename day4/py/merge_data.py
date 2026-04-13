import pandas as pd

# Load both sources
df_users = pd.read_csv("users.csv")
df_sales = pd.read_csv("sales.csv")

# Perform a 'Merge' (Similar to a SQL Join)
# We combine them on the common 'ID' column
final_report = pd.merge(df_users, df_sales, on="ID", how="inner")

print("Combined Business Report:\n")
print(final_report)
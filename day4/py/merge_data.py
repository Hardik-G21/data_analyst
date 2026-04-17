import pandas as pd

df_users = pd.read_csv("users.csv")
df_sales = pd.read_csv("sales.csv")

final_report = pd.merge(df_users, df_sales, on="ID", how="inner")

print("Combined Business Report:\n")
print(final_report)
import pandas as pd

df_users = pd.read_csv("C:/Users/HP/Downloads/data_analyst/day4/csv/users.csv")
df_sales = pd.read_csv("C:/Users/HP/Downloads/data_analyst/day4/csv/sales.csv")

final_report = pd.merge(df_users, df_sales, on="ID", how="inner")

print("Combined Business Report:\n")
print(final_report)
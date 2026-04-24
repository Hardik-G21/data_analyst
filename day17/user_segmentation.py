import pandas as pd

df = pd.read_csv("C:/Users/HP/Downloads/data_analyst/day17/meetmux_transactions.csv")
df['PurchaseDate'] = pd.to_datetime(df['PurchaseDate'], format='%d-%m-%Y')

latest_date = df['PurchaseDate'].max() + pd.Timedelta(days=1)

rfm = df.groupby('CustomerID').agg({
    'PurchaseDate': lambda x: (latest_date - x.max()).days,
    'CustomerID': 'count',
    'TransactionAmount': 'sum'
})

rfm.columns = ['Recency', 'Frequency', 'Monetary']

rfm['R_Score'] = pd.qcut(rfm['Recency'], 5, labels=[5, 4, 3, 2, 1], duplicates='drop')
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5], duplicates='drop')
rfm['M_Score'] = pd.qcut(rfm['Monetary'], 5, labels=[1, 2, 3, 4, 5], duplicates='drop')

rfm['Segment'] = rfm['R_Score'].astype(str) + rfm['F_Score'].astype(str) + rfm['M_Score'].astype(str)

print(rfm.head())

champions = rfm[rfm['Segment'] == '555']
at_risk = rfm[rfm['Segment'] == '111']

print("\nChampions (555):")
print(champions)

print("\nAt-Risk (111):")
print(at_risk)
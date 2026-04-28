import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load Transaction Data
df = pd.read_csv("C:/Users/HP/Downloads/data_analyst/day19/meetmux_transactions.csv")

# Convert to datetime
df['PurchaseDate'] = pd.to_datetime(df['PurchaseDate'])

# 2. Assign Acquisition Month (Cohort Month)
df['OrderMonth'] = df['PurchaseDate'].dt.to_period('M')

df['CohortMonth'] = df.groupby('CustomerID')['PurchaseDate'] \
                      .transform('min') \
                      .dt.to_period('M')

# 3. Calculate the "Period Index" (Months since joining)

def get_date_int(df, column):
    year = df[column].dt.year
    month = df[column].dt.month
    return year, month

# Extract year and month
order_year, order_month = get_date_int(df, 'OrderMonth')
cohort_year, cohort_month = get_date_int(df, 'CohortMonth')

# Calculate differences
years_diff = order_year - cohort_year
months_diff = order_month - cohort_month

# Final Cohort Index
df['CohortIndex'] = years_diff * 12 + months_diff + 1

# Preview result
print(df[['CustomerID', 'OrderMonth', 'CohortMonth', 'CohortIndex']].head())
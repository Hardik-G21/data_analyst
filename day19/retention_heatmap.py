import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load Data
df = pd.read_csv("C:/Users/HP/Downloads/data_analyst/day19/meetmux_transactions.csv")
df['PurchaseDate'] = pd.to_datetime(df['PurchaseDate'])

# 2. Create Cohort Columns
df['OrderMonth'] = df['PurchaseDate'].dt.to_period('M')

df['CohortMonth'] = df.groupby('CustomerID')['PurchaseDate'] \
                      .transform('min') \
                      .dt.to_period('M')

# 3. Create Cohort Index
def get_date_int(df, column):
    year = df[column].dt.year
    month = df[column].dt.month
    return year, month

order_year, order_month = get_date_int(df, 'OrderMonth')
cohort_year, cohort_month = get_date_int(df, 'CohortMonth')

df['CohortIndex'] = (order_year - cohort_year) * 12 + (order_month - cohort_month) + 1

# 4. Create Cohort Table (User Counts)
cohort_data = df.groupby(['CohortMonth', 'CohortIndex'])['CustomerID'] \
                .nunique() \
                .reset_index()

cohort_pivot = cohort_data.pivot(index='CohortMonth',
                                columns='CohortIndex',
                                values='CustomerID')

# 5. Calculate Retention Rate
cohort_sizes = cohort_pivot.iloc[:, 0]
retention = cohort_pivot.divide(cohort_sizes, axis=0)

# 6. Plot Heatmap
plt.figure(figsize=(12, 8))

sns.heatmap(retention,
            annot=True,
            fmt='.0%',
            cmap='YlGnBu',
            linewidths=0.5)

plt.title('MeetMux User Retention Cohorts')
plt.xlabel('Months Since First Purchase')
plt.ylabel('Cohort Month')

plt.show()
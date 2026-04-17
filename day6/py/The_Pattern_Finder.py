import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/HP/Downloads/data_analyst/day5/sales_cleaned.csv")

sns.pairplot(
    df,
    hue='Product',
    diag_kind='kde'
)

plt.show()
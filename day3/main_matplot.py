import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sample_data.csv", sep="\t")

# 1. BAR CHART: Comparing Salaries by City
# We group the data to see which city has the highest average pay.
df.groupby("City")["Salary"].mean().plot(kind='bar', color='skyblue')

plt.title("Average Salary by City")
plt.ylabel("Salary")
plt.show()

# 2. HISTOGRAM: Seeing the Distribution
# This shows us how many people fall into specific salary "buckets."
df["Salary"].plot(kind='hist', bins=5, edgecolor='black')

plt.title("Salary Distribution")
plt.show()
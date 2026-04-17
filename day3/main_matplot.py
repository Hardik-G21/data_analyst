import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/HP/Downloads/data_analyst/sample_data.csv", sep="\t")

df.groupby("City")["Salary"].mean().plot(kind='bar', color='skyblue')

plt.title("Average Salary by City")
plt.ylabel("Salary")
plt.show()

df["Salary"].plot(kind='hist', bins=5, edgecolor='black')

plt.title("Salary Distribution")
plt.show()
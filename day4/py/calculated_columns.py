import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/HP/Downloads/data_analyst/sample_data.csv", sep="\t")

avg_sal = df["Salary"].mean()

df["Category"] = np.where(
    df["Salary"] > avg_sal,
    "Above Average",
    "Below Average"
)

print("Categorized Dataset:\n")
print(df[["Name", "Salary", "Category"]])
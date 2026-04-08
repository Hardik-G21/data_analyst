import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("C:/Users/HP/Downloads/data_analyst/sample_data.csv", sep="\t")

# Calculate average salary
avg_sal = df["Salary"].mean()

# Create new column based on condition
df["Category"] = np.where(
    df["Salary"] > avg_sal,
    "Above Average",
    "Below Average"
)

# Print result
print("Categorized Dataset:\n")
print(df[["Name", "Salary", "Category"]])
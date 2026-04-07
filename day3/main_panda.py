import pandas as pd

# 1. LOAD DATA
df = pd.read_csv("sample_data.csv", sep="\t")

# 2. THE AUDIT
print(df.head())
print(df.info())      # See the first 5 rows
# Check data types (Are numbers actually numbers?)
print(df.describe())  # Get a statistical summary (Mean, Max, Std Dev)

# 3. DATA CLEANING
# Analysts spend 80% of their time cleaning. Let's find missing values:
print("Missing values per column:\n", df.isnull().sum())
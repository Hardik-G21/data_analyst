import pandas as pd

df = pd.read_csv("C:/Users/HP/Downloads/data_analyst/sample_data.csv", sep="\t")

print(df.head())
print(df.info())      
print(df.describe())  

print("Missing values per column:\n", df.isnull().sum())
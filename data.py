import pandas as pd

# Load the dataset (you can download one from Kaggle or use a sample dataset)
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")

# Display the first 5 rows
print(df.head())

# Print basic information about the dataset
print(df.info())

# Check for missing values
print(df.isnull().sum())

import pandas as pd

data = pd.read_csv('./data/original/original_dataset.csv')

print(data.describe())
print(data.isna().any())
print(data.columns)
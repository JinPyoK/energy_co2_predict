import pandas as pd

data = pd.read_csv('./data/scaled/all_scaled.csv')

one_hot_country = pd.get_dummies(data['country'])
one_hot_region = pd.get_dummies(data['Region'])

data = data.drop('country', axis=1)
data = data.drop('Region', axis=1)

data = pd.concat([data, one_hot_country], axis=1)
data = pd.concat([data, one_hot_region], axis=1)

data.to_csv('./data/scaled/all_scaled_one_hot.csv', index=False)


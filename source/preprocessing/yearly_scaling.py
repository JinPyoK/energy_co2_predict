import pandas as pd

data = pd.read_csv('./data/country_scaled/all_scaled.csv')

# divide the data into groups by country
def divideYearly():
  year = data['Year'].unique()
  # ['1991', '1992', ... '2020']

  for y in year:
    # Select rows by country
    yearly_data = data[data['Year'] == y]

    # Write csv file by country
    yearly_data.to_csv('./data/yearly_scaled/{}.csv'.format(y), index=False)

divideYearly()
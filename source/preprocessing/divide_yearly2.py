import pandas as pd

data = pd.read_csv('./data/country_scaled2/all_scaled.csv')

# divide the data into groups by year
def divideYearly():
  year = data['Year'].unique()
  # ['1991', '1992', ... '2020']

  for y in year:
    # Select rows by year
    yearly_data = data[data['Year'] == y]

    # Write csv file by year
    yearly_data.to_csv('./data/yearly_scaled2/{}.csv'.format(y), index=False)

divideYearly()
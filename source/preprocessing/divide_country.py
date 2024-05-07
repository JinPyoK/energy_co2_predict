import pandas as pd

data = pd.read_csv('./data/country/all.csv')


# divide the data into groups by country
def divideCountry():
  country = data['country'].unique()
  # ['Algeria' 'Argentina' 'Australia' 'Belgium' 'Brazil' 'Canada' 'Chile' ... 'United States' 'Uzbekistan' 'Venezuela']

  for cntry in country:
    # Select rows by country
    cntry_data = data[data['country'] == cntry]

    # Write csv file by country
    cntry_data.to_csv('./data/country/{}.csv'.format(cntry), index=False)


divideCountry()
import pandas as pd

dummy = pd.read_csv('./data/country/all.csv')

years = dummy['Year'].unique()
columns = [col for col in dummy.columns if col not in ['country', 'Year', 'Region']]

def makeWorldWide(data_path: str):
  new_df = pd.DataFrame()

  for year in years:
    data = pd.read_csv('./data/{}/{}.csv'.format(data_path, year))
    means = data[columns].mean().to_dict()
    new_row = {
      'Year':year,
      **means
    }
    df = pd.DataFrame(new_row, index=[0])
    new_df = pd.concat([new_df, df])
  
  # new_df.to_csv('./data/worldwide/yearly_original.csv', index=False)
  # new_df.to_csv('./data/worldwide/yearly_scaled.csv', index=False)
  new_df.to_csv('./data/worldwide/yearly_scaled2.csv', index=False)


# makeWorldWide(data_path='yearly')
# makeWorldWide(data_path='yearly_scaled')
makeWorldWide(data_path='yearly_scaled2')

import pandas as pd
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('./data/country/all.csv')
country = data['country'].unique()

# Scaling with RobustScaler by country
def scaling_by_country():
  scaler = StandardScaler()

  # Columns for Scaling
  scaling_column = [col for col in data.columns if col not in ['country', 'Year', 'Region']]

  for cntry in country:
    cntry_data = pd.read_csv('./data/country/{}.csv'.format(cntry))
    cntry_data[scaling_column] = scaler.fit_transform(cntry_data[scaling_column])
    cntry_data.to_csv('./data/scaled/{}_scaled.csv'.format(cntry), index=False)

# Combine Scaled Data
def scaling_combine():
  combined_data = pd.DataFrame()
  for cntry in country:
    scaled_data = pd.read_csv('./data/scaled/{}_scaled.csv'.format(cntry))
    combined_data = pd.concat([combined_data, scaled_data])

  combined_data.to_csv('./data/scaled/all_scaled.csv', index=False)

scaling_by_country()
scaling_combine()
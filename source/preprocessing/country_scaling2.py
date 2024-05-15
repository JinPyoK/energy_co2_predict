import pandas as pd
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('./data/country/all.csv')

def scaling():
  scaler = StandardScaler()

  # Columns for Scaling
  scaling_column = [col for col in data.columns if col not in ['country', 'Year', 'Region']]
  
  data[scaling_column] = scaler.fit_transform(data[scaling_column])
   
  data.to_csv('./data/country_scaled2/all_scaled.csv', index=False)

scaling()
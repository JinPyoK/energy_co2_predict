import pandas as pd

data = pd.read_csv('./data/original/original_dataset.csv')

# Replace 'n.a.' to 0
def stringToZero(column: str):
  data[column] = data[column].replace('n.a.', 0)

stringToZero('Share of wind and solar in electricity production (%)')
stringToZero('Coal and lignite domestic consumption (Mt)')
stringToZero('Coal and lignite production (Mt)')
stringToZero('Natural gas production (bcm)')

data.to_csv('./data/country/all.csv', index=False)
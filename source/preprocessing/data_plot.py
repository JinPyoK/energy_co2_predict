import pandas as pd
import matplotlib.pyplot as plt

# data = pd.read_csv('./data/worldwide/yearly_original.csv')
# data = pd.read_csv('./data/worldwide/yearly_scaled.csv')
data = pd.read_csv('./data/worldwide/yearly_scaled2.csv')
years = data['Year'].unique()
columns = [col for col in data.columns if col not in ['country', 'Year', 'Region']]
colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 
          'orange', 'purple', 'brown', 'pink', 
          'olive', 'lime', 'teal', 'skyblue', 
          'coral', 'lavender', 'salmon']



def showplot(title: str, y_val: list):
  plt.figure(figsize=(14,8))
  plt.bar(columns, y_val, color=colors, alpha=0.5, width=0.7)
  plt.title(title)
  plt.xticks(rotation=45, ha='right')
  # plt.savefig('./plot/worldwide_original/{}.png'.format(title), dpi=100)
  # plt.savefig('./plot/worldwide_scaled/{}.png'.format(title), dpi=100)
  plt.savefig('./plot/worldwide_scaled2/{}.png'.format(title), dpi=100)



for year in years:
  row = data[data['Year'] == year]
  values = row[columns].values
  showplot(year, values[0])

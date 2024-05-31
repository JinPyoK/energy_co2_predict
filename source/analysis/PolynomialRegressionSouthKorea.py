import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures

# data load
df = pd.read_csv('data\\country_scaled\\South Korea_scaled.csv')

# set column X and y
X = df[['Year']]
y = df['CO2 emissions from fuel combustion (MtCO2)']

# transform X for polynomial regression
poly_degree = 2
poly_features = PolynomialFeatures(degree=poly_degree)
X_poly = poly_features.fit_transform(X)

# model training
model = LinearRegression()
model.fit(X_poly, y)

# compare act and predict
y_pred = model.predict(X_poly)

# evaluation
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(f'Mean Squared Error: {mse:.2f}')
print(f'R-squared: {r2:.2f}')

# regression line
slope = model.coef_[1]
intercept = model.intercept_
equation = f'y = {slope:.2f}x + {intercept:.2f}'

plt.scatter(X, y, color='blue')
plt.plot(X, y_pred, color='red')
plt.title('Polynomial Regression')
plt.xlabel('Year')
plt.ylabel('CO2 emissions from fuel combustion (MtCO2)')
plt.show()
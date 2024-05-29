import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# data load
df = pd.read_csv('data\\worldwide\\yearly_scaled2.csv')

# set column X and y
X = df[['Total energy consumption (Mtoe)']]
y = df['Average CO2 emission factor (tCO2/toe)']

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

# draw graph

slope = model.coef_[1]
intercept = model.intercept_
equation = f'y = {slope:.2f}x + {intercept:.2f}'

plt.scatter(X, y, color='blue')
plt.plot(X, y_pred, color='red')
plt.title('Polynomial Regression')
plt.xlabel('Total energy consumtion (Mtoe)')
plt.ylabel('Average CO2 emission factor')
plt.show()
# Plotting the actual vs predicted values
# fig = plt.figure(figsize=(12, 8))
# ax = fig.add_subplot(111, projection='3d')

# # Scatter plot for actual data
# ax.scatter(X.iloc[:, 0], X.iloc[:, 1], y, color='blue', label='Actual')

# # # Sort values for smoother curve
# X1, X2 = np.meshgrid(np.linspace(X.iloc[:, 0].min(), X.iloc[:, 0].max(), 100),
#                       np.linspace(X.iloc[:, 1].min(), X.iloc[:, 1].max(), 100))
# X_grid = np.column_stack((X1.ravel(), X2.ravel()))
# X_grid_poly = poly_features.transform(X_grid)
# y_pred_grid = model.predict(X_grid_poly)

# # Plot surface of predicted values
# ax.plot_surface(X1, X2, y_pred_grid.reshape(X1.shape), color='red', alpha=0.5, label='Polynomial Regression')

# ax.set_title('Actual vs Predicted Values')
# ax.set_xlabel('Total energy production (Mtoe)')
# ax.set_ylabel('Total energy consumption (Mtoe)')
# ax.set_zlabel('CO2 Emission Factor (tCO2/toe)')
# ax.legend()

# # Set axis limits based on data range
# ax.set_xlim(X.iloc[:, 0].min(), X.iloc[:, 0].max())
# ax.set_ylim(X.iloc[:, 1].min(), X.iloc[:, 1].max())
# ax.set_zlim(y.min(), y.max())

# plt.show()
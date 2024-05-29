from sklearn.model_selection import KFold, cross_val_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import pandas as pd

# data load
data = pd.read_csv('data\\worldwide\\yearly_scaled2.csv')

X = data[['Total energy production (Mtoe)', 'Total energy consumption (Mtoe)']]  
y = data['Average CO2 emission factor (tCO2/toe)']  

# find best K
def findK():
    k_range = range(2, 15)
    k_fold_scores = []

    for k in k_range:
        kfold = KFold(n_splits=k, shuffle=True, random_state=42)
        model = RandomForestRegressor(random_state=42)
        scores = cross_val_score(model, X, y, cv=kfold, scoring='r2')
        k_fold_scores.append(scores.mean())

    best_k = k_range[np.argmax(k_fold_scores)]
    return best_k

def polyKfold():
    
    poly_degree = 2
    poly_features = PolynomialFeatures(degree=poly_degree)
    X_poly = poly_features.fit_transform(X)

    # k-fold Cross Validation setting
    k = findK()
    kfold = KFold(n_splits=k, shuffle=True, random_state=42)

    rmse_scores = []
        
    for train_index, test_index in kfold.split(X_poly):
        X_train, X_test = X_poly[train_index], X_poly[test_index]
        y_train, y_test = y[train_index], y[test_index]
        
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        rmse_scores.append(rmse)
        
    # average of RMSE 
    avg_rmse = np.mean(rmse_scores)
    print(f"RMSE scores for each fold: {rmse_scores}")
    print(f'Average RMSE (cross validation): {avg_rmse}')

polyKfold()

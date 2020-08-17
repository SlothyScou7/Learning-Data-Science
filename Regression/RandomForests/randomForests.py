import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter
 
# importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values
print(type(X),type(y))
# encoding 
# splitting the datset into traing and test set
# feature scaling

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=100,criterion='mse',
                                    min_samples_split=2,
                                    bootstrap=True,
                                    random_state=0
                                  )
regressor.fit(X,y)

print(regressor.predict([[6.5]]))
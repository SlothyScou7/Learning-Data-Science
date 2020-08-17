import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter
 
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:-1].values
y = dataset.iloc[:,-1].values

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(criterion='mse',random_state=10)
regressor.fit(X,y)

# predicting the new test result
print(regressor.predict([[6.5]]))

# visualizing the DTR  
'''
This is absolutely useless if you are using more than 2 features because you
would not be able to visualize 3d results etc..
'''
xx = np.arange(X[0],X[len(X)-1],0.1)
print(xx)
xx = xx.reshape(len(xx),1)
plt.scatter(X,y,color = 'red')
plt.plot(xx,regressor.predict(xx),color="blue")
plt.show()


'''
In the dataset we have a list of 50 startups and the amount they spend on each
section like r&d administration et.. our goal is to calulate the predicted 
profit of the data and compare it with the given profit.

'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter

data = pd.read_csv('50_Startups.csv')
df = pd.DataFrame(data)
 

# encoding the categorical data 
dummy = pd.get_dummies(df['State'])
df = pd.concat([df,dummy],axis = 1)
df =df.drop(['State'],axis =1)
df = df[['R&D Spend','Administration','Marketing Spend','California','Florida',
                                                'New York','Profit']]
print(df)

# we are here converting them into numpy arrays
X = df.iloc[:,:-1].values
y = df.iloc[:,-1].values
np.set_printoptions(suppress = True)  # makes the power of e fade away
print(X)

# splitting the dataset into the training set and test set ...
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2 ,
                                                    random_state = 0)

'''
 no need to apply the feature scaling as the dependent variable is multiplied 
 by the  constant and this would make everything normal or standarized
'''
from sklearn.linear_model import LinearRegression
multiple_linear_regressor = LinearRegression()

multiple_linear_regressor.fit(X_train,y_train)
y_pred = multiple_linear_regressor.predict(X_test)
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_test),1),y_test.reshape(len(y_test),1)),1))

test_set = np.sum(y_test)
model_set = np.sum(y_pred)
print("the accuracy is :")
print(test_set," ",model_set)
print((model_set-test_set)/model_set)
print(multiple_linear_regressor.coef_) # prints the coeff being used


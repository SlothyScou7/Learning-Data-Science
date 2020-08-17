# The sklearn.preprocessing package provides several common utility functions
#  and transformer classes to change raw feature vectors into a representation 
# that is more suitable for the downstream estimators.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter

'''
Standardization, or mean removal and variance scaling

standarization means to stndard normally distribute data that is with zero
mean and unit variance...
'''
# scale standardizes the dataset along any axis
''' 
Scaled data has zero mean and unit variance:
'''
from sklearn import preprocessing
X_train = np.array([[ 1., -1.,  2.],
                    [ 2.,  0.,  0.],
                    [ 0.,  1., -1.]])
X_scaled = preprocessing.scale(X_train) 
print(X_scaled)

scaler = preprocessing.StandardScaler()
print(scaler)
print(scaler.fit_transform(X_train))
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter

df = pd.read_csv("Dataset")
X = df.iloc[0:,:-1].values
y = df.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size =0.2,
                                                    random_state= 1 )

# encoding the independent variable
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers = ['encoder',OneHotEncoder(),
                        "[column_to_be_encoded]",remainder = passthrough]) 
X = np.array(ct.fit_transform(X))

# encoding the dependent variable 
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
import tkinter
 
#Importing the dataset
dataset = pd.read_csv('Real_Estate.csv')
df = dataset
df = df.drop(['No'],axis=1)
# print(df.describe())
# print(df.head()) 

y = df["Y house price of unit area"]
x1 = df[['X1 transaction date','X2 house age',
        'X3 distance to the nearest MRT station',
        'X4 number of convenience stores', 'X5 latitude']]

plt.hist(y, bins=100,edgecolor="red")
plt.plot(y.values)
plt.show()
x = sm.add_constant(x1) # this is added to make an intercept in the graph
results = sm.OLS(y,x).fit() 
q = df["Y house price of unit area"].quantile(0.99)
print(df["Y house price of unit area"].sort_values(ascending=False))
print(q)
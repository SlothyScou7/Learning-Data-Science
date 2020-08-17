import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter
 
dataset = pd.read_csv('Data.csv')
#  X is the matrix of features and the y is the dependent variable
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values   # iloc is used for collecting rows and columns
#  converts the things into numpy arrays


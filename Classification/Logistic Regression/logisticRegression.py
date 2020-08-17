import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter
 
#Importing the dataset
dataset = pd.read_csv('Social_Network_Ads.csv')

dummy = pd.get_dummies(dataset['Gender'])
print(dummy)
df = pd.concat([dummy,dataset],axis=1)
print(df.head())

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter

Cars = {'Brand': ["Honda Civic",'Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [22000,25000,27000,35000],
        'Year': [2015,2013,2018,2018]
        }

df = pd.DataFrame(Cars)
print(df)

df_new = df.iloc[:,:-1].values
print(df_new)
print(type(df_new))


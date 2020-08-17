import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter
import seaborn as sns
 
#Importing the dataset
train = pd.read_csv('data/train.csv')

df = pd.DataFrame()

df['Sex'] = train['Sex']
df = df.replace(['male','female'],[1,0]) # for replacing binaries with things 

df['Survived'] = train['Survived']
print(df.head())
count = 0
death=0
survive_female = 0
death_female = 0
print(df['Sex'].value_counts())
print(len(df.Sex))
# print("testing::::",df['Sex']['Survived'])

for sur in range(0,len(df.Sex),1):
    if df.Sex[sur] == 1 and df.Survived[sur] == 1:
        count +=1
    elif df.Sex[sur] == 1  and df.Survived[sur] == 0:
        death +=1
    elif df.Sex[sur] == 0  and df.Survived[sur] == 1:
        survive_female +=1
    elif df.Sex[sur] == 0  and df.Survived[sur] == 0:
        death_female +=1
print("The males that survived are:",count)
print(f'The females that survived are {survive_female}')
print(f'The males that died are {death}')
print(f'The females that died are {death_female}')

total_survived = df.loc[df.Survived ==1 ]  # loc helps in printing the rows that we want
print(total_survived,type(total_survived))
males_survived = total_survived.loc[total_survived.Sex==1]
females_death = 
print(males_survived)



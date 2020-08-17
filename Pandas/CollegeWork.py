# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import tkinter
 
# df = pd.read_csv("Responses.csv")
# print(df)
# df = df.sort_values(by=["Class Roll Number:"])
# print(df)
# df = df [["Class Roll Number:","Full Name:","Score"]]
# df = df.set_index(["Class Roll Number:"])
# df =df.astype(str)
# df.to_csv("Reponses2.csv")


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
x =df.loc[df.Survived ==1]
#  here we have the x dataset containg ony the survuved prople on the titanic
print(x.)

for sur in range(0,len(df.Sex),1):
    if df.Sex[sur] == 1 and df.Survived[sur] == 1:
        count +=1
    elif df.Sex[sur] == 1  and df.Survived[sur] == 0:
        death +=1
    elif df.Sex[sur] == 0  and df.Survived[sur] == 1:
        survive_female +=1
    elif df.Sex[sur] == 0  and df.Survived[sur] == 0:
        death_female +=1
# print("The males that survived are:",count)
# print(f'The females that survived are {survive_female}')
# print(f'The males that died are {death}')
# print(f'The females that died are {death_female}')

# total_survived = df.loc[df.Survived ==1 ]  # loc helps in printing the rows that we want
# print(total_survived,type(total_survived))
# males_survived = total_survived.loc[total_survived.Sex==1]
# print(males_survived)



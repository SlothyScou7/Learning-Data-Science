import pandas as pd
from pandas import DataFrame as DF
import numpy as np
a=pd.read_csv('data/AnnualReprise.csv')
# print(a) # print the whole data frame
print(a.head(8)) # returns the first rows by counting
print(a.tail(8)) # return the last rows bby counting
print(a.dtypes)
print(a.info())


print(a[["Year","Value"]])
b=a[["Year","Value"]]
b.to_csv('data/new.csv')

only_2018=a[a["Year"] >= 2018 ]   # only the ones with year 2018 data..and higher
# print(only_2018)

combined_2018_and_2017=a[a["Year"].isin(["2018","2017"])] # for both 2018 and 2019
# print(combined_2018_and_2017)

# indexing 
combined_2018_and_2017.set_index="Year"
# print(combined_2018_and_2017)

df = pd.DataFrame({'month': [1, 4, 7, 10],
                   'year': [2012, 2014, 2013, 2014],
                   'sale': [55, 40, 84, 31]})
print(df)
median_data=df["sale"].median()
print(median_data)
sumd=df["sale"].sum()
print(sumd)



# iloc and loc and xloc are used for data collection from a datset from rows and columns...

# eg
'''
iloc is integer location
it makes use of integers.....
'''
mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
          {'a': 100, 'b': 200, 'c': 300, 'd': 400},
          {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000 }]

df = pd.DataFrame(mydict)
print(df)
print(df.iloc[1])   # indexing with scalar integer (only 1 can come)
print(df.iloc[[0]]) # indexing with the list of integers...
print(df["a"]*df["b"]) # 2 column's things being printed...

n=np.array([[1,2,3],[4,5,6],[7,8,9]])
dp=pd.DataFrame(n)
print(dp)
print(dp[0])   # selects the column
print(dp.loc[0])
print(dp.iloc[0])
print(dp.iloc[[0]])   # selects the first row 
            # for the column we have to make these changes...
print(dp.iloc[:,0]) # gathering all the rows and 1 column only..



'''
loc vs iloc

loc gets rows or columns with particular labels from the index...

iloc gets rows or columns at particular positionswith help of integers..

'''

boxes = {'Color': ['Green','Green','Green','Blue','Blue','Red','Red','Red'],
         'Shape': ['Rectangle','Rectangle','Square','Rectangle','Square','Square','Square','Rectangle'],
         'Price': [10,15,5,5,10,15,15,5]
        }
df=DF(boxes)
print(df)
df=DF(boxes,columns=['Color','Shape','Price'])
print(df.T)
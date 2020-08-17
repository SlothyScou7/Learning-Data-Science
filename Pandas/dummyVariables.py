'''
the concept of dummy variables i first saw was in multiple linear regressions where this example was 
taken and was 
'''


import pandas as pd
data={
    'Profit':[1,2,3,4,5,6],
    'State':['New York','Winnipeg','California','New York','New York','California']
}
df=pd.DataFrame(data)
print(df)
dummy=pd.get_dummies(df['State']) 
# automatically creates the dummies for all the variables inside the state series and creates a new series itself..
print(dummy)
print(type(dummy))

newDataFrame = pd.concat([df,dummy],axis = 1)
print(newDataFrame)


deletedThings=newDataFrame.drop(['State','Profit'],axis=1)
print(deletedThings)
deletedThings = deletedThings.to_numpy()
print(deletedThings)

#  just like the One Hot Encoding
# exploratory data analysis on the dataset of kaggle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter
import missingno
import seaborn as sns
 
#Importing the dataset
train = pd.read_csv('titanic/train.csv')
test = pd.read_csv('titanic/test.csv')
gender_submission = pd.read_csv('titanic/gender_submission.csv')
# print(test.head()) 
print(train.describe())
# missingno.matrix(train,figsize=(30,10)) #visualiz the missing values in the Data

def missing_values(df):
    columns = df.columns   
    set = {}
    for column in columns:
         set[column] = df[column].isna().sum()
    return set

print(missing_values(train)) 


# creating new data frames 
df_bin = pd.DataFrame()
df_con = pd.DataFrame()

# seeing the number of survived and not survived
# sns.countplot(y ='Survived', data=train) # plt.show() shows the plot 
# regarding the survived and not survived 
print(train['Survived'].value_counts())

df_bin['Survived'] = train['Survived']
df_con['Survived'] = train['Survived']

# there are not outliers in this set...
# sns.distplot(train['Pclass'])  # plt.show()

# seeing the Pclass for any missing values 
df_bin['Pclass'] = train['Pclass']
df_con['Pclass'] = train['Pclass']

# exploring the name coulmn but it would not be proving any information to us 

# exploring the sex column
df_bin['Sex'] = train['Sex']
df_bin['Sex'] = np.where(df_bin['Sex']=='female',1,0) # converts all the columns
                                                # of female to 1 and others to 0
df_con['Sex'] = train['Sex']

#  sns.distplot(df_bin['Sex'])

# now we would be finding some relation between the males and females that surived
# we can see this because they are binaries

count = 0
death=0
survive_female = 0
death_female = 0
for sur in range(0,len(df_bin.Sex),1):
    if df_bin.Sex[sur] == 1 and df_bin.Survived[sur] == 1:
        count +=1
    elif df_bin.Sex[sur] == 1  and df_bin.Survived[sur] == 0:
        death +=1
    elif df_bin.Sex[sur] == 0  and df_bin.Survived[sur] == 1:
        survive_female +=1
    elif df_bin.Sex[sur] == 0  and df_bin.Survived[sur] == 0:
        death_female +=1
print("The males that survived are:",count)
print(f'The females that survived are {survive_female}')
print(f'The males that died are {death}')
print(f'The females that died are {death_female}')

# we can see that the number of males that survived are quite less

# through the seaborn library
fig = plt.figure(figsize=(10, 10))
# sns.distplot(df_bin.loc[df_bin['Survived'] == 1]['Sex'], kde_kws={'label': 'Survived'});
# sns.distplot(df_bin.loc[df_bin['Survived'] == 0]['Sex'], kde_kws={'label': 'Did not survive'});

'''
Feature Age
'''
print(missing_values(train))
# A total of 177 values in the age are missing . So what to do ?
# leave it for now we would come back later

'''
Feature Sib Sp
first we would dinf the missing values in this feature
'''
print(train.SibSp.isna().sum()) # there are 0 missing values in the dataset

print(train.SibSp.value_counts())
'''
0    608
1    209
2     28
4     18
3     16
8      7
5      5
'''
# Add SibSp to subset dataframes
df_bin['SibSp'] = train['SibSp']
df_con['SibSp'] = train['SibSp']

# now we would visulalize the count of siblings and the count and the number 
# survived and the people that didnot survived with repective siblings


# def plot_count(data,bin_df,label_column,target_column):

plt.subplot(1,2,1)
sns.countplot(df_bin.SibSp)
plt.subplot(1,2,2)
sns.distplot(df_bin.loc[df_bin.Survived==1]['SibSp'],kde_kws={"label":"Survive"})# here we want to have the coulumn where we have values of survived and that are having any siblings 
sns.distplot(df_bin.loc[df_bin.Survived==0]['SibSp'],kde_kws={"label":"Did not Survive"})
# plt.show()


'''
Parch is the number of parents/childre the pasenger has aboard the Titanic..
'''
# finding the count of the Parch
print(train.Parch.value_counts())
print(train.Parch.isna().sum()) # finding any misssing values

# adding parch to the subset dataframes
df_bin['Parch'] = train['Parch']
df_con['Parch'] = train['Parch']

# visualizing the count and survival rate wrt to count

plt.subplot(1,2,1)
sns.countplot(df_bin.Parch)
plt.subplot(1,2,2)
sns.distplot(df_bin.loc[df_bin.Survived==1]['Parch'],kde_kws={"label":"Survive"})# here we want to have the coulumn where we have values of survived and that are having any siblings 
sns.distplot(df_bin.loc[df_bin.Survived==0]['Parch'],kde_kws={"label":"Did not Survive"})
# plt.show()

'''
Feature ticket
'''
# finding the missing values in the ticket
print(train.Ticket.isna().sum())
print(df_bin.head())
print(train.Ticket.value_counts())  # this calcualtes the number of unique values in the dataset 

# how to reduce tickets ...
# possibly with name
# we cannot compare the tickets as they are stirngs
print(train.Ticket.dtype)
'''
# how does tht tcket depend on the survival rate ?
# the more the price of the ticket the more might be the chance for the survival
Lets find out....
'''


'''
Feature Fare
'''
# checking for any missing values
print(f'The missing values in the Fare is :{train.Fare.isna().sum()}')

# we would check the price of each different type of ticket
df_con['Fare'] = train['Fare'] 
print(train.Fare.describe()) # finding the minimum and maximum fare 
df_bin['Fare'] = pd.cut(train['Fare'],bins=5) # discretised

#Now we would be finding the relation beteween the fare and the survived
plt.subplot(1,2,1)
sns.countplot(df_bin.Fare)
x = df_bin.loc[df_bin.Survived==1]
print(x.Fare)
plt.subplot(1,2,2)
# plotting th graph for those who survived and what were there fares
sns.distplot(train.loc[train.Survived==1]['Fare'],kde_kws={"label": "Survived"})
sns.distplot(train.loc[train.Survived==0]['Fare'],kde_kws={"label": "Not_Survived"})
# plt.show()

'''
feature Cabin
'''
# missing values in the cabin
print(train.Cabin.isna().sum())
# as there are a lot of missing values in the cabin data set we will leave it 

'''
feature Embarked --> where they are headed to 
'''
print(train.Embarked.isna().sum())
# there are 2 missing values in the column .. we would drop these 2 values

# adding to data frame
df_bin['Embarked'] = train['Embarked']
df_con['Embarked'] = train['Embarked']

#Remove Embarked rows which are missing values
print(len(df_con))
df_con = df_con.dropna(subset=['Embarked'])
df_bin = df_bin.dropna(subset=['Embarked'])
print(len(df_con))


print(df_bin.head())

# now we would be encoding our data using 1 hot encoding 
def value_counts(dataset):
    for column in dataset.columns:
        print(dataset[column].value_counts())

value_counts(df_bin)
'''
                            :::::Results::::
0    549
1    340
Name: Survived, dtype: int64
3    491
1    214
2    184
Name: Pclass, dtype: int64
0    577
1    312
Name: Sex, dtype: int64
0    606
1    209
2     28
4     18
3     16
8      7
5      5
Name: SibSp, dtype: int64
0    676
1    118
2     80
5      5
3      5
4      4
6      1
Name: Parch, dtype: int64
(-0.512, 102.466]     836
(102.466, 204.932]     33
(204.932, 307.398]     17
(409.863, 512.329]      3
(307.398, 409.863]      0
Name: Fare, dtype: int64
S    644
C    168
Q     77
Name: Embarked, dtype: int64
'''

# One-hot encode binned variables
one_hot_cols = df_bin.columns.tolist()
one_hot_cols.remove('Survived')
df_bin_enc = pd.get_dummies(df_bin, columns=one_hot_cols)

print(df_bin_enc.head())

'''
  Survived  Pclass_1  Pclass_2  Pclass_3  Sex_0  Sex_1  SibSp_0  ...  Fare_(102.466, 204.932]  Fare_(204.932, 307.398]  Fare_(307.398, 409.863]  Fare_(409.863, 512.329]  Embarked_C  Embarked_Q  Embarked_S
0         0         0         0         1      1      0        0  ...                        0                        0                        0                        0           0           0           1
1         1         1         0         0      0      1        0  ...                        0                        0                        0                        0           1           0           0
2         1         0         0         1      0      1        1  ...                        0                        0                        0                        0           0           0           1
3         1         1         0         0      0      1        0  ...                        0                        0                        0                        0           0           0           1
4         0         0         0         1      1      0        1  ...                        0                        0                        0                        0           0           0           1
'''
# now we would be seeing the df_con that is the continuous dataset...

value_counts(df_con)
'''
0    549
1    340
Name: Survived, dtype: int64
3    491
1    214
2    184
Name: Pclass, dtype: int64
male      577
female    312
Name: Sex, dtype: int64
0    606
1    209
2     28
4     18
3     16
8      7
5      5
Name: SibSp, dtype: int64
0    676
1    118
2     80
5      5
3      5
4      4
6      1
Name: Parch, dtype: int64
8.0500     43
13.0000    42
7.8958     38
7.7500     34
26.0000    31
           ..
7.8000      1
13.8583     1
7.6292      1
15.0500     1
8.6833      1
Name: Fare, Length: 247, dtype: int64
S    644
C    168
Q     77
'''
# One hot encode the categorical columns
df_embarked_one_hot = pd.get_dummies(df_con['Embarked'], 
                                     prefix='embarked')

df_sex_one_hot = pd.get_dummies(df_con['Sex'], 
                                prefix='sex')

df_plcass_one_hot = pd.get_dummies(df_con['Pclass'], 
                                   prefix='pclass')

# Combine the one hot encoded columns with df_con_enc
df_con_enc = pd.concat([df_con, 
                        df_embarked_one_hot, 
                        df_sex_one_hot, 
                        df_plcass_one_hot], axis=1)

# Drop the original categorical columns (because now they've been one hot encoded)
df_con_enc = df_con_enc.drop(['Pclass', 'Sex', 'Embarked'], axis=1)
print(df_con_enc.head())
'''
 Survived  SibSp  Parch     Fare  embarked_C  embarked_Q  embarked_S  sex_female  sex_male  pclass_1  pclass_2  pclass_3
0         0      1      0   7.2500           0           0           1           0         1         0         0         1
1         1      1      0  71.2833           1           0           0           1         0         1         0         0
2         1      0      0   7.9250           0           0           1           1         0         0         0         1
3         1      1      0  53.1000           0           0           1           1         0         1         0         0
4         0      0      0   8.0500           0           0           1           0         1         0         0         1
'''

                                    # now we would be training our machine learning models 

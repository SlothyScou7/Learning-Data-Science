# we are given a data set and we need to sort data in the dataset...
import pandas as pd
Cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [22000,25000,27000,35000],
        'Year': [2015,2013,2018,2018]
        }
 
df = pd.DataFrame(Cars, columns= ['Brand', 'Price','Year'])

print (df)

df.sort_values(by=['Price'],inplace=True,ascending=False)
print(df)
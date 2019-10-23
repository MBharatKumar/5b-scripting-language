import pandas as pd
data = pd.read_csv('231019.csv')
print (data)
#slice the result for first 5 rows
print (data[0:5]['salary'])
#use the multi-axis indexing function
print (data.loc[:,['salary','Name']])
#use the multi-axis indexing function
print (data.loc[[1,3,5],['salary','name']])
#use the multi-axis indexing function
print (data.loc[2:6,['salary','name']])

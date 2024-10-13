import pandas as pd
import numpy as np


df1=pd.read_csv('data1.csv')
df2=pd.read_csv('data2.csv')

# df1=pd.read_excel('data1.xlsx')
# df2=pd.read_excel('data2.xlsx')

print(df1.head(2))
print(df2.head(2))

# a
print(pd.merge(df1,df2,how='inner',on='Name'))

# b
either_day=pd.merge(df1,df2,how='outer',on='Name')
print(either_day)

# c
print(either_day['Name'].count())

# d
both_days=pd.merge(df1,df2,how='outer',on=['Name','Duration']).copy()
both_days.fillna(value='-',inplace=True)
print(both_days.set_index(['Name','Duration']))

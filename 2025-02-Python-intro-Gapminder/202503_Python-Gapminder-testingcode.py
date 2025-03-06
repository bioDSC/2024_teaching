

import pandas as pd

###
# plotting

data_asia = pd.read_csv('/Users/m.wehrens/Data_UVA/2024_teaching/2025-03-gapminder/data/gapminder_gdp_asia.csv', \
    index_col='country')
data_asia.describe().T.plot(kind='scatter', x='min', y='max')

data_asia.loc['max'] = data_asia.max()
data_asia.loc['min'] = data_asia.min()
data_asia.loc[:,'max']


###
# How to add rows:

df_test = pd.DataFrame({'A': [1,2,3], 'B': [2,3,4], 'C': [5,5,5],'D': [6,7,8]})

df_test
# you can't do this:
df_test.T[len(df_test.T)] = [9,9,9,9]
# but you can do this:
df_test.loc[len(df_test)] = [0,0,0,0]







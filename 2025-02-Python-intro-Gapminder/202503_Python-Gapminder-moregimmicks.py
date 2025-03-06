

################################################################################

import pandas as pd

```
Decade	Year-0	Year-1	Year-2	Year-3	Year-4	Year-5	Year-6	Year-7	Year-8	Year-9
  1850's										16.00
  1860's	9.59	0.49	1.05	3.15	8.06	6.59	3.74	2.41	3.62	5.64
  1870's	3.86	4.34	3.64	1.83	1.17	1.35	2.52	2.38	1.17	0.86
  1880's	0.94	0.92	0.78	1.10	0.85	0.88	0.71	0.67	0.65	0.77
  1890's	0.77	0.56	0.51	0.60	0.72	1.09	0.96	0.68	0.80	1.13
  1900's	1.19	0.96	0.80	0.94	0.86	0.62	0.73	0.72	0.72	0.70
  1910's	0.61	0.61	0.74	0.95	0.81	0.64	1.10	1.56	1.98	2.01
  1920's	3.07	1.73	1.61	1.34	1.43	1.68	1.88	1.30	1.17	1.27
  1930's	1.19	0.65	0.87	0.67	1.00	0.97	1.09	1.18	1.13	1.02
  1940's	1.02	1.14	1.19	1.20	1.21	1.22	1.41	1.93	2.60	2.54
  1950's	2.51	2.53	2.53	2.68	2.78	2.77	2.79	3.09	3.01	2.90
  1960's	2.88	2.89	2.90	2.89	2.88	2.86	2.88	2.92	2.94	3.09
  1970's	3.18	3.39	3.39	3.89	6.87	7.67	8.19	8.57	9.00	12.64
  1980's	21.59	31.77	28.52	26.19	25.88	24.09	12.51	15.40	12.58	15.86
  1990's	20.03	16.54	15.99	14.25	13.19	14.62	18.46	17.23	10.87	15.56
  2000's	26.72	21.84	22.51	27.56	36.77	50.28	59.69	66.52	94.04	56.35
  2010's	74.71	95.73	94.52	95.99	87.39	44.39	38.29	48.05	61.40	55.59
  2020's	36.86	65.84	93.97	76.10						
```

df_crudeoil = \
    pd.read_csv('/Users/m.wehrens/Data_UVA/2024_teaching/2025-03-gapminder/crude_oil/crude_oil_prices.tsv', sep='\t')

# df_crudeoil.melt(id_vars='Decade')
df_crudeoil_melted = df_crudeoil.melt(id_vars='Decade', var_name='lastdigit')

# remove the suffix "0's" from the decades column
df_crudeoil_melted.loc[:,'Decade'] = df_crudeoil_melted.loc[:,'Decade'].str.replace("0's",'')
df_crudeoil_melted.loc[:,'lastdigit'] = df_crudeoil_melted.loc[:,'lastdigit'].str.replace('Year-','')
df_crudeoil_melted.loc[:,'Year'] = df_crudeoil_melted.loc[:,'Decade'] + df_crudeoil_melted.loc[:,'lastdigit']
df_crudeoil_melted

################################################################################

import matplotlib.pyplot as plt

df_all = \
    pd.read_csv('/Users/m.wehrens/Data_UVA/2024_teaching/2025-03-gapminder/data/gapminder_all.csv', index_col='country')

df_all.columns

df_all.plot(kind='scatter', x='gdpPercap_2007', y='lifeExp_2007', s=df_all['pop_2007']/1e6)
# using the row names, add index to each of the points
plt.text(df_all.loc['United States','gdpPercap_2007'], df_all.loc['United States','lifeExp_2007'], 'United States')
plt.text(df_all.loc['Netherlands','gdpPercap_2007'], df_all.loc['Netherlands','lifeExp_2007'], 'Netherlands')
plt.show()

# pivot does the opposite of melt
# df_crudeoil.pivot_table(index='Decade')




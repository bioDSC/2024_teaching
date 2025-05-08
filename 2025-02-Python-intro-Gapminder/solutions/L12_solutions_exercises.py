


################################################################################
# Solutions for additional exercises made by bioDSC
################################################################################

################################################################################
# libs

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as colors

import os

LOCAL_PATH = '/Users/m.wehrens/Documents/git_repos/_UVA/bioDSC_website/bioDSC.github.io/static/'
LOCAL_PATH_GAPMINDER = '/Users/m.wehrens/Data_UVA/2024_teaching/2025-03-gapminder/'
cm_to_inch = 1/2.54

plt.rcParams.update({'font.size': 8})

################################################################################
# Plotting automation

#######
# Remember this code from Lesson 9?

df_all = pd.read_csv(LOCAL_PATH_GAPMINDER+'data/gapminder_all.csv', index_col='country')
sns.scatterplot(df_all, x='gdpPercap_2007', y='lifeExp_2007', size='pop_2007', sizes=(1,40**2), legend=False)
plt.text(df_all.loc['United States','gdpPercap_2007'], df_all.loc['United States','lifeExp_2007'], 'United States')
plt.text(df_all.loc['Netherlands','gdpPercap_2007'], df_all.loc['Netherlands','lifeExp_2007'], 'Netherlands')
plt.show()

#######
# Answer


# Maybe get the top 3 and bottom 3, and some more
top3_life = df_all.loc[:,'lifeExp_2007'].nlargest(3).index
bottom3_life = df_all.loc[:,'lifeExp_2007'].nsmallest(3).index
custom_countries = ['Netherlands','United States']
# Merge those three lists
my_countries_to_select = list(top3_life) + list(bottom3_life) + custom_countries

# Plot
sns.scatterplot(df_all, x='gdpPercap_2007', y='lifeExp_2007', size='pop_2007', sizes=(1,40**2), legend=False)
# Now add text automatically
for country in my_countries_to_select:
    plt.text(df_all.loc[country,'gdpPercap_2007'], df_all.loc[country,'lifeExp_2007'], country, fontsize=5)
plt.show()


'''

This plot looks like: 

![](/static/plots_pyworkshop/L12_GDPscatter.png){width=40%}

A bit messy with the overlapping text, but this worked great otherwise!
'''



fig, ax = plt.subplots(1, 1, figsize=(8*cm_to_inch, 5*cm_to_inch))
sns.scatterplot(df_all, x='gdpPercap_2007', y='lifeExp_2007', size='pop_2007', sizes=(1,40**2), legend=False, ax=ax)
# Now add text automatically
for country in my_countries_to_select:
    plt.text(df_all.loc[country,'gdpPercap_2007'], df_all.loc[country,'lifeExp_2007'], country, fontsize=5)

# Save the plot
plt.tight_layout()
fig.savefig(LOCAL_PATH+'plots_pyworkshop/L12_GDPscatter.png', dpi=600)#, bbox_inches='tight')



# DISCARDED CODE:
# # Get the top 10 countries
# df_top10data = df_all.loc[:,['gdpPercap_2007','lifeExp_2007']].nlargest(10, 'gdpPercap_2007')
# # Plot
# sns.scatterplot(df_all, x='gdpPercap_2007', y='lifeExp_2007', size='pop_2007', sizes=(1,40**2), legend=False)
# # Now add text automatically
# for country in df_top10data.index:
#     plt.text(df_top10data.loc[country,'gdpPercap_2007'], df_top10data.loc[country,'lifeExp_2007'], country, fontsize=3)
# plt.show()
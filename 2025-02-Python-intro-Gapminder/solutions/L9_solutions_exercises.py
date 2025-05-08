

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as colors

import os

LOCAL_PATH = '/Users/m.wehrens/Documents/git_repos/_UVA/bioDSC_website/bioDSC.github.io/static/'
LOCAL_PATH_GAPMINDER = '/Users/m.wehrens/Data_UVA/2024_teaching/2025-03-gapminder/'
cm_to_inch = 1/2.54

os.makedirs(LOCAL_PATH+'plots_pyworkshop/', exist_ok=True)
plt.rcParams.update({'font.size': 8})

######################################################################
# Minima and Maxima

data_europe = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
data_europe_transposed = data_europe.T

data_europe_transposed['min'] = data_europe.min()
data_europe_transposed['max'] = data_europe.max()
data_europe_transposed['year'] = data_europe_transposed.index.str.replace("gdpPercap_","")

sns.lineplot(data_europe_transposed, x='year', y='min', label='min')
sns.lineplot(data_europe_transposed, x='year', y='max', label='max')
plt.legend(loc='best')
plt.xticks(rotation=90)

# Save the plot
fig, ax = plt.subplots(1, 1, figsize=(8*cm_to_inch, 5*cm_to_inch))
_ = sns.lineplot(data_europe_transposed, x='year', y='min', ax=ax, label='min')
_ = sns.lineplot(data_europe_transposed, x='year', y='max', ax=ax, label='max')
plt.legend(loc='best')
plt.xticks(rotation=90)
plt.tight_layout()
fig.savefig(LOCAL_PATH+'plots_pyworkshop/L9_min_max_gdp_europe.png', dpi=600)#, bbox_inches='tight')

'''

The figure now looks like:

![](/static/plots_pyworkshop/L9_min_max_gdp_europe.png){width=40%}

'''

######################################################################
# Mean gene expression

#######
# given code:

# Load data, note the ".T" at the end here
df_kohela = pd.read_csv(LOCAL_PATH+'data/kohela-et-al.csv', index_col=0).T
# create new 'masks'
epicardial_cells = df_kohela['WT1']>3
fibroblast_cells = df_kohela['COL2A1']>30
fat_cells = df_kohela['PPARG']>2
# Add cell type
df_kohela['Celltype'] = 'unknown'
df_kohela.loc[epicardial_cells,'Celltype'] = 'epicardial'
df_kohela.loc[fibroblast_cells, 'Celltype'] = 'fibroblast'
df_kohela.loc[fat_cells, 'Celltype'] = 'fat'
# Add conditions
df_kohela['Condition'] = 'unknown'
df_kohela.loc[df_kohela.index.str.contains('WT_'), 'Condition'] = 'WT'
df_kohela.loc[df_kohela.index.str.contains('mutant_'), 'Condition'] = 'mutant'

#######

# Use seaborn to create a ‘stripplot’ plot for WT1 expression per cell type. Then create a similar plot for TBX18.
# (Epicardial cell markers.) What information can be extracted from this plot?
sns.stripplot(df_kohela, x='Celltype', y='TBX18', jitter=True, color='red')
plt.tick_params(axis='x', rotation=45)
sns.stripplot(df_kohela, x='Celltype', y='WT1', jitter=True, color='blue')
plt.tick_params(axis='x', rotation=45)


# plt.show(); plt.close()

# Saving the plots:
fig, axs = plt.subplots(1, 2, figsize=(10*cm_to_inch, 5*cm_to_inch))
_ = sns.stripplot(df_kohela, x='Celltype', y='WT1', jitter=True, color='blue', ax=axs[0], size=1.5)
_ = sns.stripplot(df_kohela, x='Celltype', y='TBX18', jitter=True, color='red', ax=axs[1], size=1.5)
axs[0].tick_params(axis='x', rotation=45)
axs[1].tick_params(axis='x', rotation=45)
# Save the plot
plt.tight_layout()
fig.savefig(LOCAL_PATH+'plots_pyworkshop/L9_stripplot_WT1_TBX18.png', dpi=600)#, bbox_inches='tight')
# plt.show(); plt.close()

#######
# Now create a scatter plot, showing WT1 expression vs. TBX18 expression across all cells. What does this tell us?

sns.scatterplot(df_kohela, x='WT1', y='TBX18')
# plt.show(); plt.close()

'''
This plot highlights a few challenges with data analysis.

Single cell RNA-seq data can typically show only a few reads per gene per cell, or even zero, even when the gene is expressed.
This is a limitation of the RNA-seq technique.

This results in many cells having only few or zero counts for the WT1 and TBX18 gene expression, and many overlapping datapoints.
It is therefor hard to see any pattern in the data.

Adding `alpha=0.1` as argument to the scatterplot method already helps to visualize the data better:
'''
sns.scatterplot(df_kohela, x='WT1', y='TBX18', alpha=.1)
'''

It appears that there is not much correlation between the TBX18 and WT1 expression.
This can either be because cells do not typically express both at the same time, or 
because our detection is not sufficient to identify such a correlation from this plot.

'''

##### Technical rendering of the plots
fig, ax = plt.subplots(1, 1, figsize=(5*cm_to_inch, 5*cm_to_inch))
_ = sns.scatterplot(df_kohela, x='WT1', y='TBX18', ax=ax, size=1, legend=False)
plt.tight_layout()
fig.savefig(LOCAL_PATH+'plots_pyworkshop/L9_scatter_WT1_TBX18.png', dpi=600)#, bbox_inches='tight')

fig, ax = plt.subplots(1, 1, figsize=(5*cm_to_inch, 5*cm_to_inch))
_ = sns.scatterplot(df_kohela, x='WT1', y='TBX18', ax=ax, alpha=.1, size=1, legend=False)
plt.tight_layout()
fig.savefig(LOCAL_PATH+'plots_pyworkshop/L9_scatter_WT1_TBX18_alpha.png', dpi=600)#, bbox_inches='tight')

######
# Color the scatter plot per cell type. What does this tell us?

sns.scatterplot(df_kohela, x='WT1', y='TBX18', hue='Celltype')

# ![](/static/plots_pyworkshop/L9_scatter_WT1_TBX18_Celltype.png){width=25%}

'''
This plot is still somewhat hard to interpret. Some points are overlaying on top of each other.

One way to disentangle the points, is to plot them separately:
'''

maxval = np.max(df_kohela.loc[:,['WT1','TBX18']])

plt.title('Epicardial cells')
sns.scatterplot(df_kohela.loc[df_kohela['Celltype']=='epicardial',:], x='WT1', y='TBX18', alpha=.1)
plt.xlim([0, maxval+1])
plt.ylim([0, maxval+1])
plt.show()

plt.title('Fibroblast cells')
sns.scatterplot(df_kohela.loc[df_kohela['Celltype']=='fibroblast',:], x='WT1', y='TBX18', alpha=.1)
plt.xlim([0, maxval+1])
plt.ylim([0, maxval+1])
plt.show()

sns.scatterplot(df_kohela.loc[df_kohela['Celltype']=='fat',:], x='WT1', y='TBX18', alpha=.1)
plt.title('Fat cells')
plt.xlim([0, maxval+1])
plt.ylim([0, maxval+1])
plt.show()

sns.scatterplot(df_kohela.loc[df_kohela['Celltype']=='unknown',:], x='WT1', y='TBX18', alpha=.1)
plt.title('Unknown cells')
plt.xlim([0, maxval+1])
plt.ylim([0, maxval+1])
plt.show()

# ![](/static/plots_pyworkshop/L9_scatter_WT1_TBX18_Celltype-fibroblast.png){width=25%} ![](/static/plots_pyworkshop/L9_scatter_WT1_TBX18_Celltype-epicardial.png){width=25%}

# ![](/static/plots_pyworkshop/L9_scatter_WT1_TBX18_Celltype-fat.png){width=25%} ![](/static/plots_pyworkshop/L9_scatter_WT1_TBX18_Celltype-unknown.png){width=25%}

'''
Interestingly, we now see that fibroblast (COL2A1+) and fat cells (PPARG+) typically don't express
WT1 or TBX18, whilst epicardial cells (WT1+) do also often show TBX18 expression.

There are nevertheless still WT+ cells that don't show TBX18 expression, 
and moreover many WT- cells (the unknown cells) that show TBX18 expression, 
so these plots are not conclusive, and more sophisticated single cell methods
might be needed to further study these cells.

'''

##### 
# Technical 

fig, ax = plt.subplots(1, 1, figsize=(8*cm_to_inch, 5*cm_to_inch))
_ = sns.scatterplot(df_kohela, x='WT1', y='TBX18', hue='Celltype', ax=ax, s=15)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Celltype')
plt.tight_layout()
fig.savefig(LOCAL_PATH+'plots_pyworkshop/L9_scatter_WT1_TBX18_Celltype.png', dpi=600)#, bbox_inches='tight')

maxval = np.max(df_kohela.loc[:,['WT1','TBX18']])
for celltype in df_kohela['Celltype'].unique():
    fig, ax = plt.subplots(1, 1, figsize=(5*cm_to_inch, 5*cm_to_inch))
    plt.title(f'{celltype} cells')
    sns.scatterplot(df_kohela.loc[df_kohela['Celltype']==celltype,:], x='WT1', y='TBX18', alpha=.1, s=10)
    plt.xlim([-.5, maxval+1])
    plt.ylim([-.5, maxval+1])
    plt.tight_layout()
    fig.savefig(LOCAL_PATH+f'plots_pyworkshop/L9_scatter_WT1_TBX18_Celltype-{celltype}.png', dpi=600)#, bbox_inches='tight')
    plt.close()
    
    
fig, ax = plt.subplots(1, 1, figsize=(8*cm_to_inch, 5*cm_to_inch))
_ = sns.scatterplot(df_kohela, x='WT1', y='TBX18', hue='Celltype', ax=ax, s=15)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Celltype')
plt.tight_layout()
fig.savefig(LOCAL_PATH+'plots_pyworkshop/L9_scatter_WT1_TBX18_Celltype.png', dpi=600)#, bbox_inches='tight')

#########
# More correlations

# This short program creates a plot showing the correlation between GDP and life expectancy for 2007, normalizing marker size by population:

data_all = pd.read_csv(LOCAL_PATH_GAPMINDER+'data/gapminder_all.csv', index_col='country')
sns.scatterplot(data_all, x='gdpPercap_2007', y='lifeExp_2007', size='pop_2007', sizes=(1,40**2), legend=False)
plt.show(); plt.close()

'''
See e.g. (the scatterplot documentation)[https://seaborn.pydata.org/generated/seaborn.scatterplot.html].

- `data_all`: The first argument specifies which dataframe to use as input.
- `x='gdpPercap_2007'`: The x argument expects the name of the column that holds values to plot on the x-axis.
- `y='lifeExp_2007'`: Same as x, but for the y axis.
- `size='pop_2007'`: This tells seaborn to scale the point size with the values in a column, in this case the population sizes of the countries (in 2007).
- `sizes=(1,40`2)`: This sets the range of the sizes to be used for the points, given as (min, max). These are an area, which is why it's convenient to use the square operator `**2`, such that you can choose a radius (in this case minimally 1 and maximally 40).
- `legend=False`: This turns off the legend.

The result:
![](/static/plots_pyworkshop/L9_scatter_gdp_lifeexp.png){width=35%}
'''

# now save the plot like above
fig, ax = plt.subplots(1, 1, figsize=(6*cm_to_inch, 5*cm_to_inch))
_ = sns.scatterplot(data_all, x='gdpPercap_2007', y='lifeExp_2007', size='pop_2007', sizes=(1,20**2), legend=False, ax=ax)
plt.tight_layout()
fig.savefig(LOCAL_PATH+'plots_pyworkshop/L9_scatter_gdp_lifeexp.png', dpi=600)#, bbox_inches='tight')



######################################################################
# Even more correlations

fig, ax = plt.subplots(1, 1, figsize=(8*cm_to_inch, 5*cm_to_inch))
sns.scatterplot(data_all, x='gdpPercap_2007', y='lifeExp_2007', size='pop_2007', sizes=(1,40**2), legend=False, ax=ax)
plt.text(data_all.loc['United States','gdpPercap_2007'], data_all.loc['United States','lifeExp_2007'], 'United States', fontsize=6)
plt.text(data_all.loc['Netherlands','gdpPercap_2007'], data_all.loc['Netherlands','lifeExp_2007'], 'Netherlands', fontsize=6)
plt.tight_layout()
fig.savefig(LOCAL_PATH+'plots_pyworkshop/L9_scatter_gdp_lifeexp_label.png', dpi=600)#, bbox_inches='tight')
plt.close('all')
# Doesn't work:
#plt.text(np.array([data_all.loc['United States','gdpPercap_2007'], data_all.loc['Netherlands','gdpPercap_2007']]), 
#         np.array([data_all.loc['United States','lifeExp_2007'], data_all.loc['Netherlands','lifeExp_2007']]), 
#         ['United States','Netherlands'])

# What’s happening here? (You might need to use Google.)

'''
The function [matplotlib.pyplot.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html),

```
matplotlib.pyplot.text(x, y, s, fontdict=None, **kwargs)
```

allows you to put text s in your plotting area at location x,y. 
x, y and s should be single values (not arrays or tables)

- `data_all.loc['United States','gdpPercap_2007']` selects the x value corresponding to the united states.
- `data_all.loc['United States','lifeExp_2007']` selects the y value corresponding to the united states.
- `'United states'` provides the label.

The result:
![](/static/plots_pyworkshop/L9_scatter_gdp_lifeexp_label.png){width=40%}

'''

#################################################################################
# Subselection and melting

##########
# (..)

df_kohela_sel = df_kohela.loc[:,['WT1', 'TBX18', 'TFAP2A', 'COL2A1', 'ACTA2', 'PPARG', 'CEBPA','Celltype','Condition']]

##########
# Melting

df_kohela_melted = pd.melt(df_kohela_sel, id_vars=['Celltype','Condition'], var_name='Gene', value_name='Expression')

'''
- *What will happen to the gene expression values?*
    - Expression data that were spread out over multiple columns are now re-organized in one long column. A new column is created
    alongside the column with all data, that specifies from which column the data originated.

- *What is sensible input for the var_name and value_name parameters?*
    - The `var_name` is the name of the new column that specifies from which original columns the data came. In this case
    the original columns corresponded to different genes, and so "Gene" might be a sensible name.
    - `value_name` is the name of the new column that holds all values previously spread out over multiple columns.
    The values all related to expression, and so "Expression" seems a good name.

- *Why is this useful? (For answer, see next questions.)*
    - This is useful because now this dataframe can be easily used as input for the seaborn plots.
'''

#######

df_kohela_melted.head()

'''

The output was:

```
  Celltype Condition Gene  Expression
0  unknown    mutant  WT1           0
1  unknown    mutant  WT1           0
2  unknown    mutant  WT1           0
3  unknown    mutant  WT1           0
4  unknown    mutant  WT1           1
```

and indeed, the columns Celltype and Condition were retained, and the expression data was re-organized 
into one column "Expression", annotated by the new column "Gene" which lists from which original column
that data originated.

'''

#######

sns.violinplot(df_kohela_melted, x='Gene', y='Expression', hue='Condition')
plt.show()
sns.stripplot(df_kohela_melted, x='Gene', y='Expression', hue='Condition', ax=ax, dodge=1)
plt.show()

'''

*For the Violinplot*

![](/static/plots_pyworkshop/L9_violinplot_Gene_Expression_Condition.png){width=40%}

An issue you might have identified is that it is very hard to compare gene expression levels
because some of these genes have rather high expression levels, thus forcing the expression
levels of other genes to the very bottom of the plot, making it hard to distinguish differences.

Also some outliers appear to be affecting the scale to a large extend, making it hard to 
see trends.

Moreover, you can probably not even see the Violins..

*For the stripplot*

![](/static/plots_pyworkshop/L9_stripplot_Gene_Expression_Condition.png){width=40%}

This looks better, but it is still hard to see differences between wild type and mutant cell
gene expression.

'''

# Violin plot
fig, ax = plt.subplots(1, 1, figsize=(8*cm_to_inch, 5*cm_to_inch))
sns.violinplot(df_kohela_melted, x='Gene', y='Expression', hue='Condition', ax=ax)
plt.tight_layout()
plt.tick_params(axis='x', rotation=90)
fig.savefig(LOCAL_PATH+'plots_pyworkshop/L9_violinplot_Gene_Expression_Condition.png', dpi=600)#, bbox_inches='tight')
plt.close()
            
# Stripplot
fig, ax = plt.subplots(1, 1, figsize=(8*cm_to_inch, 5*cm_to_inch))
sns.stripplot(df_kohela_melted, x='Gene', y='Expression', hue='Condition', ax=ax, dodge=1)
plt.tight_layout()
plt.tick_params(axis='x', rotation=90)
fig.savefig(LOCAL_PATH+'plots_pyworkshop/L9_stripplot_Gene_Expression_Condition.png', dpi=600)#, bbox_inches='tight')
plt.close()



########
# Normalization


# A custom function, which normalizes a series by its mean
# We'll learn more about functions in Lesson 16
def gene_normalization(X):
    return X / np.mean(X)

# Create a subset of the data
cell_subset = ['mutant_rep1_cell174', 'WT_rep2_cell348', 'mutant_rep1_cell160',
       'WT_rep1_cell022', 'mutant_rep1_cell069']
gene_subset = ['WT1', 'TBX18', 'TFAP2A', 'COL2A1', 'ACTA2', 'PPARG', 'CEBPA']

# Normalize gene expression
df_kohela_subset2 = df_kohela.loc[cell_subset, gene_subset]
df_kohela_subset2_normalized = df_kohela_subset2.transform(gene_normalization)

# Print the result
print(df_kohela_subset2_normalized)

'''

##### 1. Check out what `gene_normalization(df_kohela_subset2['WT1'])` does.

What `gene_normalization()` is described in the comment above the function, 
it normalizes a series by its mean. `df_kohela_subset2['WT1']` is the series
of expression values related to WT1. 

`gene_normalization(df_kohela_subset2['WT1'])` will thus return WT1 expression
values normalized by their mean.

##### 2. What does the transform method do in the above code?

Transform applies a function to each of the columns in a dataframe. So in this case
it will go over each column, which correspond to `df_kohela_subset2['WT1']`,
`df_kohela_subset2['TBX18']`, `df_kohela_subset2['TFAP2A']` and so forth, and 
feed that column to the custom function, which in this case will return
values that are normalized. Those normalized values are then put back in the 
column the function was applied to.

Thus, the each column will now correspond to mean-divided expression (ie will
be normalized).


'''

#####


'''
The normalization: 
'''

df_kohela_grouped = df_kohela_melted.groupby('Gene')
df_kohela_melted['Expression_normalized'] = df_kohela_grouped['Expression'].transform(gene_normalization)

'''
The bar code hides the information about the distribution of the single data points.
So perhaps it is best to combine those two plots:
'''

sns.barplot(df_kohela_melted, x='Gene', y='Expression_normalized', 
            hue='Condition', ci=None)
sns.stripplot(df_kohela_melted, x='Gene', y='Expression_normalized', 
              hue='Condition', dodge=True, color='black', alpha=.1, size=4, 
              legend=False)
plt.ylim([0,15])
plt.show()
plt.close('all')

'''

The plot now looks like:

![](/static/plots_pyworkshop/L9_bar_stripplot_Gene_Expression_Normalized_Condition.png){width=40%}

'''

fig, ax = plt.subplots(1, 1, figsize=(10*cm_to_inch, 8*cm_to_inch))
sns.barplot(df_kohela_melted, x='Gene', y='Expression_normalized', hue='Condition', ax=ax, ci=None)
sns.stripplot(df_kohela_melted, x='Gene', y='Expression_normalized', hue='Condition', 
              dodge=True, color='black', alpha=.1, size=1, ax=ax, legend=False)
plt.ylim([0,15])
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Condition')
plt.tick_params(axis='x', rotation=90)
plt.tight_layout()
fig.savefig(LOCAL_PATH+'plots_pyworkshop/L9_bar_stripplot_Gene_Expression_Normalized_Condition.png', dpi=600)#, bbox_inches='tight')
plt.close()


df_kohela_melted2=df_kohela_melted.copy()
df_kohela_melted2['Condition'] = pd.Categorical(df_kohela_melted2['Condition'], categories=['WT', 'mutant'], ordered=True)

'''
This results in the condition becoming a categorical series, which has a specific order, that is 
translated to the plot. This is very useful if you want to control where the labels go on your
axes.
The order of 'WT' and 'mutant' on the x-axis now makes more sense.

The figure now looks like:
![](/static/plots_pyworkshop/L9_bar_stripplot_Gene_Expression_Normalized_Condition_order.png){width=40%}

'''

fig, ax = plt.subplots(1, 1, figsize=(10*cm_to_inch, 8*cm_to_inch))
sns.barplot(df_kohela_melted2, x='Gene', y='Expression_normalized', hue='Condition', ax=ax, ci=None)
sns.stripplot(df_kohela_melted2, x='Gene', y='Expression_normalized', hue='Condition', 
              dodge=True, color='black', alpha=.1, size=1, ax=ax, legend=False)
plt.ylim([0,15])
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Condition')
plt.tick_params(axis='x', rotation=90)
plt.tight_layout()
fig.savefig(LOCAL_PATH+'plots_pyworkshop/L9_bar_stripplot_Gene_Expression_Normalized_Condition_order.png', dpi=600)#, bbox_inches='tight')
plt.close()


################################################################################
# Correlations

#######

# Modify the code from “Minima and Maxima” exercise (Exercise A) to create a scatter plot showing the relationship between 
# the minimum and maximum GDP per capita across the countries in Asia, with each point in the plot corresponding to a year. 
# What relationship do you see (if any)?

data_asia = pd.read_csv(LOCAL_PATH_GAPMINDER+'data/gapminder_gdp_asia.csv', index_col='country')
data_asia_transposed = data_asia.T

data_asia_transposed['min'] = data_asia.min()
data_asia_transposed['max'] = data_asia.max()
data_asia_transposed['year'] = data_asia_transposed.index.str.replace("gdpPercap_","")

sns.scatterplot(data_asia_transposed, x='min', y='max', hue='year', palette='viridis', legend=False)


'''

Results in the plot:

![](/static/plots_pyworkshop/L9_scatter_min_max_gdp_asia.png){width=25%}

It can be seen that there is no correlation between the minimum GDP and maximum GDP
for a specific year, indicating that GDPs across asia do not tend to rise and fall together.


'''


fig, ax = plt.subplots(1, 1, figsize=(5*cm_to_inch, 5*cm_to_inch))
sns.scatterplot(data_asia_transposed, x='min', y='max', hue='year', ax=ax, palette='viridis', legend=False)
plt.tight_layout()
fig.savefig(LOCAL_PATH+'plots_pyworkshop/L9_scatter_min_max_gdp_asia.png', dpi=600)#, bbox_inches='tight')
plt.close()



##########


df_max_GDP = pd.DataFrame()
df_max_GDP['GDP_max'] = data_asia.max()
df_max_GDP['Year']    = data_asia.columns.str.replace('gdpPercap_','').astype(int)

plt.plot(df_max_GDP['Year'], df_max_GDP['GDP_max'])
plt.show(); plt.close('all')

print(data_asia.idxmax())
print(data_asia.idxmin())

'''

The plot looks like:

![](/static/plots_pyworkshop/L9_plot_max_GDP_asia.png){width=40%}

Seems the variability in this value is due to a sharp drop after 1972. Some geopolitics at play perhaps? Given the dominance of oil producing countries, maybe the Brent crude index would make an interesting comparison? Whilst Myanmar consistently has the lowest GDP, the highest GDP nation has varied more notably.

'''



fig, ax = plt.subplots(1, 1, figsize=(8*cm_to_inch, 5*cm_to_inch))
ax.plot(df_max_GDP['Year'], df_max_GDP['GDP_max'])
plt.title('Max asian GDP over time')
plt.xlabel('Year'); plt.ylabel('GDP')
plt.tight_layout()
fig.savefig(LOCAL_PATH+'plots_pyworkshop/L9_plot_max_GDP_asia.png', dpi=600)#, bbox_inches='tight')
plt.close()





##############################################


# Copy the df to modify it and not interfer with other code
data_europe_relative_copy = data_europe_relative.copy()
# Add the country as column
data_europe_relative_copy['Country'] = data_europe_relative_copy.index
# Melt it 
data_europe_relative_melted = data_europe_relative_copy.melt(id_vars='Country')
# Add the year as number
data_europe_relative_melted['year'] = data_europe_relative_melted['variable'].str.replace('gdpPercap_','').astype(int)

# And plot
sns.lineplot(data_europe_relative_melted, x='year', y='value', hue='Country', legend=False)
plt.show()

'''
We can now visualize the relative position of countries over time.
Unfortunately, there are a little bit too many countries to clearly identify single ones.
A solution to this issue is left for another time.

The plot looks like:
![](/static/plots_pyworkshop/L9_lineplot_europe_relative.png){width=40%}

'''

fig, ax = plt.subplots(1, 1, figsize=(8*cm_to_inch, 5*cm_to_inch))
sns.lineplot(data_europe_relative_melted, x='year', y='value', hue='Country', ax=ax, legend=False)
plt.tight_layout()
fig.savefig(LOCAL_PATH+'plots_pyworkshop/L9_lineplot_europe_relative.png', dpi=600)#, bbox_inches='tight')
plt.close()


##########
# Crude oil over time

import pandas as pd

# Load the data
df_crudeoil = \
    pd.read_csv(LOCAL_PATH+'data/crude_oil.tsv', sep='\t')

# reshape the data, such that it becomes a long list
df_crudeoil_melted = df_crudeoil.melt(id_vars='Decade', var_name='lastdigit')

# now reformat the year information
# search and replace first
df_crudeoil_melted.loc[:,'Decade'] = df_crudeoil_melted.loc[:,'Decade'].str.replace("0's",'')
df_crudeoil_melted.loc[:,'lastdigit'] = df_crudeoil_melted.loc[:,'lastdigit'].str.replace('Year-','')
# now combine information to create a new column "Year"
df_crudeoil_melted.loc[:,'Year'] = (df_crudeoil_melted.loc[:,'Decade'] + df_crudeoil_melted.loc[:,'lastdigit']).astype(int)
# Inspect the result
print(df_crudeoil_melted.head())

# Plot value over the years
sns.lineplot(df_crudeoil_melted, x='Year', y='value', label='price')
plt.axvline(x=1972, color='red', linestyle='--', label='1972')
plt.legend()
plt.show()

'''

This plot looks like:

![](/static/plots_pyworkshop/L9_lineplot_crudeoil.png){width=40%}

And probably quite some things happened to Arabian oil countries after '72, resulting in aforementioned 
drop in that period in GDP.

'''

# Save like above
fig, ax = plt.subplots(1, 1, figsize=(8*cm_to_inch, 5*cm_to_inch))
sns.lineplot(df_crudeoil_melted, x='Year', y='value', ax=ax,label='price')
plt.ylabel('Oil price ($/barrel)')
plt.axvline(x=1972, color='red', linestyle='--', label='1972')
plt.tight_layout()
plt.legend()
fig.savefig(LOCAL_PATH+'plots_pyworkshop/L9_lineplot_crudeoil.png', dpi=600)#, bbox_inches='tight')
plt.close()
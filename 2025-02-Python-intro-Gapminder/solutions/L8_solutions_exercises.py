

import pandas as pd
import numpy as np

df_cells_kohela2 = \
    pd.read_csv("https://www.biodsc.nl/workshop-materials/py-intro/kohela-et-al.csv",header=0,index_col=0).T

# Question A
# In the RNA-seq data, we can create another column that reflects the condition of the cells, WT or mutant. Fill in the blanks to achieve this:

df_cells_kohela2['Condition'] = 'unknown'
df_cells_kohela2.loc[df_cells_kohela2.index.str.contains('WT_'), 'Condition'] = 'WT'
df_cells_kohela2.loc[df_cells_kohela2.index.str.contains('mutant_'), 'Condition'] = 'mutant'

# Test:
df_cells_kohela2['Condition']

# Question B
df_cells_kohela2.loc[:,['TFAP2A','Condition']].groupby('Condition').mean()

############################################################
# Gene expression


# Convert the data below to a file you can import (e.g.: csv, tsv)
'''
This exercise is also meant to illustrate that it can sometimes be tedious to handle data.
Many data files are however plain text, and you can open them to see what's going on.
One way to convert the exercise data to a convenient format, could be:

- Open a text editor like Notepad (Windows), TextEdit (Mac), or your own favorite.
- Copy the text to the text editor.
- Use search and replace to replace double spaces by single spaces (search for '`  `', replace by '` `').
- Repeat this until you only have single spaces.
- Now replace spaces by commas (replace '` `' by '`,`').
- You now have a comma separated file, save it e.g. as gene_expression.csv.

See also this example [gene_expression.csv](/static/data/gene_expression.csv)
'''

df_gene_expression = \
    pd.read_csv('/Users/m.wehrens/Documents/git_repos/_UVA/bioDSC_website/bioDSC.github.io/static/data/'+'gene_expression.csv')

# The average CRP gene expression per condion.

'''
This can be done in multiple ways. Here's an elegant solution that gives
information about the std and mean in one go:
'''
df_gene_expression.groupby(['gene', 'condition']).describe()

'''
Alternatively, we can do this using group_by, the mean and std function.
We can use the column names directly as argument for the group by, 
then apply mean, then apply "reset_index()" to convert the multi-index to columns.
'''
df_gene_expression_avg = df_gene_expression.groupby(by = ['gene', 'condition']).mean().reset_index()
# CRP expression
print(df_gene_expression_avg.loc[df_gene_expression_avg['gene']=='CRP',:])

# The corresponding standard deviations can be calculated in a similar way:
df_gene_expression_std = df_gene_expression.groupby(by = ['gene', 'condition']).std().reset_index()
print(df_gene_expression_std.loc[df_gene_expression_std['gene']=='CRP',:])



'''
A disadvantage of this strategy is that for large dataframes, you might be calculating many mean values
that you're not interested in in the end.
You could also first select the gene of interest.
'''
df_gene_expression_avg_CRP = df_gene_expression.loc[df_gene_expression['gene']=='CRP',:].groupby(by = ['gene', 'condition']).mean().reset_index()
df_gene_expression_std_CRP = df_gene_expression.loc[df_gene_expression['gene']=='CRP',:].groupby(by = ['gene', 'condition']).std().reset_index()
print(df_gene_expression_avg_CRP)
print(df_gene_expression_std_CRP)

# The log2-fold change between WT, condition A, and condition B.
'''
Note that for a real-world analysis, you might use specialized tools for this, which 
take into account more statistical considerations.
But to directly calculate the log2-fold change, we need to divide mean condition X by mean WT, 
calculate the ratios, and take the logarithm with base 2.

There are multiple ways to do this. The solution below exploits the fact that when dividing 
two dataframes, the indices are "aligned". Meaning here that if the index of the numerator dataframe
corresponds to ACTA1, it will be divided by a record from the denominator's dataframe that's also 
has an ACTA1 index, even if the numerator and denominator's dataframes are of different length.
This also applies to series.
'''
# Calculate averages again: group by, selecting the grouped expression series, calculate the mean
gene_expression_avg = df_gene_expression.groupby(['gene','condition'])['expression'].mean()
# Identify the WT records with a boolean array
WT_records = gene_expression_avg.index.get_level_values(1)=='WT'
# Select such that we divide a non-WT series by a WT series
# We use "reset index" to set the index to gene names only, this allows for alignment
ratios = gene_expression_avg.loc[~WT_records].reset_index(level=1,drop=True)/gene_expression_avg.loc[WT_records].reset_index(level=1,drop=True)
# The parameters above were series, let's convert back to dataframe
df_ratios = ratios.to_frame()
# Now we need to restore the index to identify the conditions
df_ratios.index=gene_expression_avg[~WT_records].index
# And we can take the log2
df_log2fc = np.log2(df_ratios)
# search for "expression" column name and replace by "log2fc"
df_log2fc = df_log2fc.rename(columns={'expression':'log2fc'})
print(df_log2fc)


# Do the same for ACTA1.
'''
See above.
'''

# Normalize all gene expression levels to their average respective wild type levels.
'''
We can use a same strategy as above.
'''
# First set the index to the gene column, then take the expression
gene_expression = df_gene_expression.set_index('gene')['expression']
# Take the average information from above, and also set the index to the gene value
wt_avg_values   = gene_expression_avg.loc[WT_records].reset_index(level=1,drop=True)
# We can now divide one by the other
gene_expression_normalized = gene_expression/wt_avg_values
# We can create a new dataframe with normalized data
df_gene_expression_norm = df_gene_expression.copy()
df_gene_expression_norm['expression_normalized'] = gene_expression_normalized.values

'''
#### Alternative strategy for the above two exercises.
An alternative could be to pivot the dataframe.
This can also be used to calculate log2fc values.
'''
# Create a copy of the dataframe to avoid confusion with other exercises.
df_gene_expression_2 = df_gene_expression.copy()
# To pivot, it is required to be able to match rows uniquely. Add an index to do this.
df_gene_expression_2['rows'] = df_gene_expression_2.groupby(['gene','condition']).cumcount()
# Pivot df_gene_expression_2 such that the gene column is used to expand the 'expression', remove 'rows'
df_gene_expression_wide = df_gene_expression_2.pivot(index=['condition','rows'], columns='gene', values='expression').reset_index().drop(columns='rows')
# Now calculate the averages
df_averages =  df_gene_expression_wide.groupby(['condition']).mean()
# Now divide df_gene_expression_wide columns by df_averages
values_WT = df_averages.T['WT'].values
# We can use the dataframe's division method to divide all columns by the WT averages
df_gene_expression_norm2 = df_gene_expression_wide.loc[:,'ACTA1':'CRP'].div(values_WT, axis=1)
# Add annotation condition
df_gene_expression_norm2['condition'] = df_gene_expression_wide['condition']
# We now have the normalized dataframe
print(df_gene_expression_norm2)
# Calculate L2FC:
df_log2fc_2 = df_gene_expression_norm2.groupby(['condition']).mean().apply(np.log2)
# We now have the log2-fold changes:
print(df_log2fc_2)


########################################################################
# GDPs

LOCAL_PATH='/Users/m.wehrens/Data_UVA/2024_teaching/2025-03-gapminder/'

# First load the data again
import pandas as pd
data_europe = pd.read_csv(LOCAL_PATH+'data/gapminder_gdp_europe.csv', index_col='country')


# Are there any countries which had a positive increase between those two years? Which ones?
# We can calculate the difference between those two years
GDP_change_87_92 = \
    data_europe.loc[:, 'gdpPercap_1992'] - data_europe.loc[:, 'gdpPercap_1987']
# And check which countries show a positive change
print(GDP_change_87_92.index[GDP_change_87_92>0])


# Calculate the average GDP between all European countries per year.
data_europe_avgGDPperyear = data_europe.mean()

# Normalize the dataframe by this trend.
data_europe_relative = data_europe.div(data_europe_avgGDPperyear, axis=1)
'''
We can now more easily see how countries compared to other countries over 
the years. Greece, for example, starts out its economy with a GDP of 62%
of the average European country, but ends up with a GDP that's 110% of 
the average European country.
'''
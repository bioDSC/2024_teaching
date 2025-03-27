

import pandas as pd
import numpy as np


data_files = ['/Users/m.wehrens/Data_UVA/example-datasets/kohela-et-al/GSE149331_RAW/mutant_rep1__GSM4498064_HUB-AK-005_HLWF5BGX9_S3_R2.BarcodeCounts.tsv',
              '/Users/m.wehrens/Data_UVA/example-datasets/kohela-et-al/GSE149331_RAW/mutant_rep2__GSM4498065_HUB-AK-006_HLWF5BGX9_S4_R2.BarcodeCounts.tsv',
              '/Users/m.wehrens/Data_UVA/example-datasets/kohela-et-al/GSE149331_RAW/WT_rep1__GSM4498062_HUB-AK-003_HLWF5BGX9_S1_R2.BarcodeCounts.tsv',
              '/Users/m.wehrens/Data_UVA/example-datasets/kohela-et-al/GSE149331_RAW/WT_rep2__GSM4498063_HUB-AK-004_HLWF5BGX9_S2_R2.BarcodeCounts.tsv']

conditions = ['mutant_rep1', 'mutant_rep2', 'WT_rep1', 'WT_rep2']

# read in the files above into separate pandas dataframes
data = []
for i, file in enumerate(data_files):
    
    df_current = pd.read_csv(file, sep='\t', index_col=0, header=0)
    df_current.columns = [conditions[i] + "_cell" + str(col) for col in df_current.columns]
    data.append(df_current)


# now join the dataframes, but match based on row names, only keeping rows that exist in all tables
df_RNAseq = pd.concat(data, axis=1, join='inner')

# Now remove __chrXX from the row names
df_RNAseq.index = [x.split('__')[0] for x in df_RNAseq.index]

# Calculate total reads
cell_total_reads = df_RNAseq.sum()
gene_total_reads = df_RNAseq.sum(axis=1)
df_RNAseq_filtered = df_RNAseq.loc[gene_total_reads > 100, cell_total_reads > 3000]
df_RNAseq_filtered.shape

# now also calculate total reads per gene

# Export to excel
df_RNAseq_filtered.to_csv('/Users/m.wehrens/Data_UVA/example-datasets/kohela-et-al/kohela-et-al.csv')

##########

# Testing group_by example
df_cells_kohela = pd.read_csv('/Users/m.wehrens/Data_UVA/example-datasets/kohela-et-al/kohela-et-al.csv', index_col=0)

df_cells_kohela2 = df_cells_kohela.T

df_cells_kohela2.head()
np.max(df_cells_kohela2['WT1']) # epicardial
np.max(df_cells_kohela2['COL2A1']) # fibroblast
np.max(df_cells_kohela2['PPARG']) # fat

epicardial_cells = df_cells_kohela.T['WT1']>3
fibroblast_cells = df_cells_kohela.T['COL2A1']>30
fat_cells = df_cells_kohela.T['PPARG']>2

df_cells_kohela2['Celltype'] = 'unknown'
df_cells_kohela2.loc[epicardial_cells,'Celltype'] = 'epicardial'
df_cells_kohela2.loc[fibroblast_cells, 'Celltype'] = 'fibroblast'
df_cells_kohela2.loc[fat_cells, 'Celltype'] = 'fat'

# give an overview of the frequencies of 'Celltype' values
df_cells_kohela2['Celltype'].value_counts()

# now use group_by to calculate gene expression median values per group
df_cells_kohela2_groupedType = df_cells_kohela2.groupby('Celltype')
df_cells_kohela2_groupedType.head()

df_results = df_cells_kohela2_groupedType.mean() / df_cells_kohela2.iloc[:,:-1].mean()

df_results.loc[:,'TFAP2A']

df_results.loc[:,(df_results>10).any()]

##### Some additional exercise material

### Epicardial cells

# In the RNA-seq data, we can create another column that reflects the condition
# of the cells, WT or mutant.
# 
# Fill in the blanks to achieve this

# df_cells_kohela2['Condition'] = ____

# df_cells_kohela2.loc[df_cells_kohela2.index.str.contains('WT_'), 'Condition'] = ____
# df_cells_kohela2.loc[df_cells_kohela2.index._______] = ______

# SOLUTION
df_cells_kohela2['Condition'] = 'unknown'
df_cells_kohela2.loc[df_cells_kohela2.index.str.contains('WT_'), 'Condition'] = 'WT'
df_cells_kohela2.loc[df_cells_kohela2.index.str.contains('mutant_'), 'Condition'] = 'mutant'

# What is the difference between str.contains and str.match?

# Now again calculate the mean value of TFAP2A expression in WT cells vs. mutant cells.

# SOLUTION:
df_cells_kohela2.loc[:,['TFAP2A','Condition']].groupby('Condition').mean()


################################################################################

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# plt.ion()

# Plotting exercises
df_kohela = pd.read_csv('/Users/m.wehrens/Data_UVA/example-datasets/kohela-et-al/kohela-et-al.csv', index_col=0).T
# df_kohela = pd.read_csv('data/kohela-et-al.csv', index_col=0).T
df_kohela['Celltype'] = 'unknown'
df_kohela.loc[epicardial_cells,'Celltype'] = 'epicardial'
df_kohela.loc[fibroblast_cells, 'Celltype'] = 'fibroblast'
df_kohela.loc[fat_cells, 'Celltype'] = 'fat'
df_kohela['Condition'] = 'unknown'
df_kohela.loc[df_kohela.index.str.contains('WT_'), 'Condition'] = 'WT'
df_kohela.loc[df_kohela.index.str.contains('mutant_'), 'Condition'] = 'mutant'

# Create two jitter plots for WT1 expression per cell type, and a similar plot for TBX18
sns.stripplot(df_kohela, x='Celltype', y='WT1', jitter=True)
sns.stripplot(df_kohela, x='Celltype', y='TBX18', jitter=True)

# A scatter plot between TFAP2A and COL2A1
sns.scatterplot(df_kohela, x='WT1', y='TBX18')
# plt.show(); plt.close()

# Scatter per cell type
sns.scatterplot(df_kohela, x='WT1', y='TBX18', hue='Celltype')
sns.scatterplot(df_kohela, x='WT1', y='TBX18', hue='Condition')

# Calculate the total expression per cell
df_kohela['Total_reads'] = df_kohela.iloc[:,:-2].T.sum()
# And plot
sns.violinplot(df_kohela, x='Condition', y='Total_reads')

## Another exercise
# Selection and melting

df_kohela_sel = df_kohela.loc[:,['WT1', 'TBX18', 'TFAP2A', 'COL2A1', 'ACTA2', 'PPARG', 'CEBPA','Celltype','Condition']]

# Now melt this dataframe, using cell type and condition as id variables.
df_kohela_melted = pd.melt(df_kohela_sel, id_vars=['Celltype','Condition'], var_name='Gene', value_name='Expression')

sns.violinplot(df_kohela_melted, x='Gene', y='Expression', hue='Condition')

# use split-apply-combine to normalize the expression of each of the genes by its sum

# This custom function (see later lessons) divides a series of values by its mean
import numpy as np
def gene_normalization(X):
    return X / np.mean(X)

df_kohela_expression = df_kohela_melted.loc[:,'Expression']
df_kohela_expression_grouped = df_kohela_expression.groupby(df_kohela_melted['Gene'])
df_kohela_expression_normalized = df_kohela_expression_grouped['Expression'].transform(gene_normalization)
df_kohela_melted['Expression_normalized'] = df_kohela_expression_normalized.loc[:,0]


df_kohela_melted['Expression_normalized2'] = (
    df_kohela_melted.groupby('Gene')['Expression']
    .transform(gene_normalization)
)


# Code used for exercises
df_kohela_grouped = df_kohela_melted.groupby('Gene')
df_kohela_melted['Expression_normalized'] = df_kohela_grouped['Expression'].transform(gene_normalization)
#df_kohela_grouped = df_kohela_melted.groupby(_______)
#df_kohela_melted['Expression_normalized'] = df_kohela_grouped['Expression']._______(gene_normalization)


# (How selection below was created)
# First, let's select a subset of the data 
# Determine the total reads on our favorite genes
#df_kohela['Total_reads_sel'] = df_kohela.loc[:,['WT1', 'TBX18', 'TFAP2A', 'COL2A1', 'ACTA2', 'PPARG', 'CEBPA']].T.sum()
#idx_top10_most_reads = df_kohela['Total_reads'].nlargest(5).index
#df_kohela_subset2 = df_kohela.loc[idx_top10_most_reads, ['WT1', 'TBX18', 'TFAP2A', 'COL2A1', 'ACTA2', 'PPARG', 'CEBPA','Celltype','Condition','Total_reads']]


# Let's look at an example
cell_subset = ['mutant_rep1_cell174', 'WT_rep2_cell348', 'mutant_rep1_cell160',
       'WT_rep1_cell022', 'mutant_rep1_cell069']
gene_subset = ['WT1', 'TBX18', 'TFAP2A', 'COL2A1', 'ACTA2', 'PPARG', 'CEBPA']
df_kohela_subset2 = df_kohela.loc[cell_subset, gene_subset]

print(df_kohela_subset2.transform(gene_normalization))



###
df_kohela_melted.describe(percentiles=[0.1,0.25,0.5,0.75,0.95])

# sns.violinplot(df_kohela_melted, x='Gene', y='Expression_normalized', hue='Condition')
sns.barplot(df_kohela_melted, x='Gene', y='Expression_normalized', hue='Condition')
# show summary information regarding df_kohela_melted, including percentiles
plt.ylim([0,5])

sns.stripplot(df_kohela_melted, x='Gene', y='Expression_normalized', hue='Condition', jitter=True, dodge=True, color='black')

sns.stripplot(df_kohela_melted, x='Gene', y='Expression_normalized', hue='Condition', dodge=True)
df_kohela_melted['Condition'] = pd.Categorical(df_kohela_melted['Condition'], categories=['WT', 'mutant'], ordered=True)
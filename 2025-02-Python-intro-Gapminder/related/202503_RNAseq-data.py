

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

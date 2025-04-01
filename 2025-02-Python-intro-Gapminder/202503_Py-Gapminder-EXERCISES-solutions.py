


################################################################################
# Lesson 7
################################################################################

import pandas as pd

# Reading other data
##########

data_am = pd.read_csv('/Users/m.wehrens/Data_UVA/2024_teaching/2025-03-gapminder/data/gapminder_gdp_americas.csv', \
    index_col='country')

data_am.describe()

# Inspecting data
##########

data_am.head(n=1)

# Navigating directories
##########

# (..)

# Writing data
##########

# data_am.to_csv(..)

data_fake = pd.read_csv('/Users/m.wehrens/Desktop/python_course/exercise-stuff/table_genes.csv', index_col=0)

from scipy.stats import ttest_ind
t_stat, p_value = ttest_ind(data_fake['cond1'], data_fake['cond2'])
print(f"T-statistic: {t_stat}, P-value: {p_value}")

################################################################################
# Lesson 8
################################################################################





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



import glob
import pandas as pd
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1,1, figsize=(10*cm_to_inch, 5*cm_to_inch))
for filename in glob.glob(LOCAL_PATH_GAPMINDER+'data/gapminder_gdp*.csv'):
    # filename = glob.glob(LOCAL_PATH_GAPMINDER+'data/gapminder_gdp*.csv')[0]
    dataframe = pd.read_csv(filename)
    # extract <region> from the filename, expected to be in the format 'data/gapminder_gdp_<region>.csv'.
    # we will split the string using the split method and `_` as our separator,
    # retrieve the last string in the list that split returns (`<region>.csv`), 
    # and then remove the `.csv` extension from that string.
    region = filename.split('_')[-1][:-4]

    # pandas raises errors when it encounters non-numeric columns in a dataframe computation
    # but we can tell pandas to ignore them with the `numeric_only` parameter
    mean_values = dataframe.mean(numeric_only=True)
    years       = pd.Series(mean_values.index.values).str.split('_').str[-1].astype(int)
    
    ax.plot(years, mean_values, label=region)
    # NOTE: another way of doing this selects just the columns with gdp in their name using the filter method
    # dataframe.filter(like="gdp").mean().plot(ax=ax, label=region)
# set the title and labels
ax.set_title('GDP Per Capita for Regions Over Time')
ax.set_xlabel('Year')
plt.tight_layout()
plt.legend()
# plt.show()

# Save the plot
fig.savefig(LOCAL_PATH+'plots_pyworkshop/L14_meanGDP_regions.png', dpi=600)#, bbox_inches='tight')
plt.close('all')

'''

![](/static/plots_pyworkshop/L14_meanGDP_regions.png){width=50%}

'''
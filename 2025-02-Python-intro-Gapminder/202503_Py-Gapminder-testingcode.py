

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


################################################################################

mylist=[4,3,2,1]
mylist.sort()
print(mylist)

# Program C
letters = list('gold')
result = letters.copy() # copy is needed here!!
result.sort()
print('letters is', letters, 'and result is', result)


################################################################################

# Program A
old = list('gold')
new = old      # simple assignment
new[0] = 'D'
print('new is', new, 'and old is', old)


# Program B
old = list('gold')
new = old[:]   # assigning a slice
new[0] = 'D'
print('new is', new, 'and old is', old)


################################################################################

import matplotlib.pyplot as plt

# Bang Wong colorblind-friendly color scheme (https://www.nature.com/articles/nmeth.1618)
colors_bangwong = [
    "#E69F00",  # Orange
    "#56B4E9",  # Sky Blue
    "#009E73",  # Bluish Green
    "#F0E442",  # Yellow
    "#0072B2",  # Blue
    "#D55E00",  # Vermillion
    "#CC79A7",  # Reddish Purple
    "#000000"   # Black
]

fig, ax = plt.subplots(1,1, figsize=(10/2.54,10/2.54))
ax.plot([1,2,3,4], [1,4,9,16], linestyle='--', color=colors_bangwong[1], label=r'$x^2$')
ax.plot([1,2,3,4], [1,5,11,19], linestyle=':', color=colors_bangwong[2], label=r'$x^2+(x-1)^2$')
ax.legend()
ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis', fontsize=12)
ax.set_title('Sample Plot', fontsize=12)
ax.legend(fontsize=12)
ax.tick_params(axis='both', which='major', labelsize=12)
plt.tight_layout()
# plt.show()
plt.savefig('/Users/m.wehrens/Desktop/202503_Python-Gapminder-testingcode.pdf', dpi=300, bbox_inches='tight')
plt.close(fig)

################################################################################

[X for x in range(10)]
another_list = [2*x+x**2-1 for x in range(10)]
another_list

[x for x in another_list if x < 10]

list_withtop = [1000+-10*(x-7)**2 for x in range(20)]
list_withtop


list_line = [70*x-1000 for x in range(20)]
list_line

################################################################################

for idx in range(10):
    print(idx)
    
idx

################################################################################

acronym = ''

for color in ['red','green','blue']:
    acronym = acronym + color[0].upper()
    # print(color[0])

print(acronym)

################################################################################


for number in range(10):
    
    # use a if the number is a multiple of 3, otherwise use b
    
    if (Number % 3) == 0:
        message = message + a
    else:
        message = message + "b"
        
print(message)

# (some straightforward typos)

################################################################################


import pandas as pd
import matplotlib.pyplot as plt

data_all = pd.read_csv('/Users/m.wehrens/Data_UVA/2024_teaching/2025-03-gapminder/data/gapminder_all.csv', index_col='country')
data_all.plot(kind='scatter', x='gdpPercap_2007', y='lifeExp_2007',
              s=data_all['pop_2007']/1e6)

# cannot be done:
plt.text(data_all.loc[:,'gdpPercap_2007'].values, data_all.loc[:, 'lifeExp_2007'].values, list(data_all.index))
    # https://stackoverflow.com/questions/54744772/matplotlib-text-not-taking-array-values


plt.show()
plt.close('all')

#plt.text(data_all.loc['United States','gdpPercap_2007'], data_all.loc['United States','lifeExp_2007'], 'United States')
#plt.text(data_all.loc['Netherlands','gdpPercap_2007'], data_all.loc['Netherlands','lifeExp_2007'], 'Netherlands')

################################################################################

# We'll be trying to recreate the following plot:
# https://www.biodsc.nl/workshop-materials/plot.html

# Solution for plotting exercise

import pandas as pd
import matplotlib.pyplot as plt

# Load Europe data
data_europe = pd.read_csv('/Users/m.wehrens/Data_UVA/2024_teaching/2025-03-gapminder/data/gapminder_gdp_europe.csv', index_col='country')

# Check out shape
data_europe.shape
len(data_europe)

### Reshape the dataframe to long format 
# transpose
data_europe_tranposed = data_europe.T
# add year as int
data_europe_tranposed['Year'] = data_europe.columns.str.replace('gdpPercap_', '').astype(int)
# actual reshape to long format
data_europe_tranposed_melted = data_europe_tranposed.melt(id_vars='Year', var_name='Country', value_name='GDP')

### Plotting

# get all countries
countries_europe = data_europe.index

# Start figure
fig, ax = plt.subplots(6,5, figsize=(10/2.54,10/2.54)) # 2.54 = cm to inch factor

# Looping to create data
counter=0
# Go over panels
for idx_i in range(6):
    for idx_j in range(5):                

        # counter = which panel we're at (updated at end)
        # not necessary for current situation
        if counter < len(countries_europe):

            # Determine which part dataframe we need
            current_selection = data_europe_tranposed_melted['Country']==countries_europe[counter]
            
            # Make the plot
            # IMPORTANT ARGUMENT: ax=ax[idx_i,idx_j]
            data_europe_tranposed_melted.loc[current_selection,: ].plot(
                    x='Year', y='GDP', ax=ax[idx_i,idx_j])
            
            # Add title
            ax[idx_i, idx_j].set_title(countries_europe[counter], fontsize=5)
            
            # remove all labels except title
            ax[idx_i, idx_j].set_xlabel('')
            ax[idx_i, idx_j].set_ylabel('')
            ax[idx_i, idx_j].set_xticks([])
            ax[idx_i, idx_j].set_yticks([])
            # remove legend
            ax[idx_i, idx_j].get_legend().remove()
            
        # Administration for which country we are at
        counter += 1

# Saving            
plt.tight_layout()            
# plt.show()
# save to pdf and png
fig.savefig('/Users/m.wehrens/Desktop/202503_example-advanced.pdf', dpi=300, bbox_inches='tight')
fig.savefig('/Users/m.wehrens/Desktop/202503_example-advanced.png', dpi=300, bbox_inches='tight')
plt.close('all')

################################################################################

fig, ax = plt.subplots(6,5, figsize=(10/2.54,10/2.54)) # 2.54 = cm to inch factor

# Looping to create data
counter=0
# Go over panels
for idx_i in range(6):
    for idx_j in range(5):  

        x=[1,2,3]
        y=[1,2,3]
        ax[idx_i, idx_j].plot(x,y)
        
plt.show()
plt.close('all')

################################################################################

for idx1 in [1,2]:
    for idx2 in range(3):
        for idx3 in [6,5,0]:
            print('product = ', idx1*idx2*idx3)
            
################################################################################            

example_list = [1,2,3,4,-5,1,34,6,-10]
example_list_pos = [item for item in example_list if item > 0]
print(example_list_pos)

################################################################################

for idx, item in enumerate([1,2,3,4,-5,1,34,6,-10]):
    
    if item>5:
        print(idx)
        
################################################################################        
        
apples = [123, 436, 123, 654, 117, 193, 120]
pears  = [543, 163, 178, 165, 123, 187, 190]

for apple_weight, pear_weight in zip(apples, pears):
    print('='*10)
    print('weigth apple: ', apple_weight)
    print('weigth pear: ',pear_weight)
    
################################################################################

def testfun():
    a = 5+10
    11
    
print(testfun())

################################################################################
    
element = 'lithium'

element[-7]
element[-6]
element[-7:0]

element[-7:3]
element[-17:3]
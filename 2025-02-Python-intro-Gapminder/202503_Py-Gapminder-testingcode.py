

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


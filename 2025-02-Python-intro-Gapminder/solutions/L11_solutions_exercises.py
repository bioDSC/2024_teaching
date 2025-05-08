

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

################################################################################
# More list comprehensions and filtering


#########
# A

some_list = [2*x+x**2-1 for x in range(10)]

#########
# B 


some_list_sel = [x for x in some_list if x>10]

print(some_list)
print(some_list_sel)

'''
The print statements show it has worked.
'''

#########
# C

some_list_np = np.array(some_list)
some_list_np_sel = some_list_np[some_list_np>10]

print(some_list_np_sel)


########## 
# D

# Let's make it numpy
list_withtop = np.array([1000+-10*(x-7)**2 for x in range(20)])

##########
# E

# 1. Find the position of the maximum value in this array.
list_withtop.argmax()
# 2. Edit the code above such that the maximum value shifts to an index of your choice.   
#       Check whether you succeedded by finding the maximum value.
my_shift = 15
list_withtop_2 = np.array([1000+-10*(x-my_shift)**2 for x in range(20)])
list_withtop_2.argmax()
# 3. Multiply your list with `-1`, and put the result in another list.
#     1. Where are now the maximum and minimum values?
#     2. Does this make sense?
list_withtop_2_inv = list_withtop_2*-1 # inverted list (*-1)
# The maximum and minimum positions have swapped, as we multiplied by -1.
list_withtop_2_inv.argmin()
list_withtop_2_inv.argmax()
# 4. `list_line = [70*x-1000 for x in range(20)]`
#     1. What's the biggest value, either negative or positive, in this list?
list_line = np.array([70*x-1000 for x in range(20)])
# That number is:
list_line[np.argmax(np.abs(list_line))]
#     2. And the index of that number?
np.argmax(np.abs(list_line))
#     3. What's the standard deviation?
np.std(list_line)
#     4. Can you calculate the correlation between list_withtop and list_line?
# Using np:
R_calculated = np.corrcoef(list_withtop, list_line)[0,1]
# Manually:
R_calculated2 = \
    np.sum((list_withtop-np.mean(list_withtop)) * (list_line-np.mean(list_line))) / \
        np.sqrt(  np.sum((np.mean(list_withtop)-list_withtop)**2) * np.sum((np.mean(list_line)-list_line)**2)  )
print(R_calculated)
print(R_calculated2)
#     5. Can you make a scatter plot of  list_withtop versus list_line?
plt.scatter(list_withtop, list_line)
plt.xlabel('list_withtop'); plt.ylabel('list_line')


plt.show()
plt.close('all')





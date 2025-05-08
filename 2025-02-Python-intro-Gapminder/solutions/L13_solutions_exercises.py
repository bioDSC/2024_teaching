


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


'''
An iterator counter should be added to the for loop.
'''

values = [-2,1,65,78,-54,-24,100]
for idx,v in enumerate(values):
    if idx == 0:
        smallest = v
        largest = v
    else:
        smallest = min(smallest, v)
        largest = max(largest, v)
print(smallest, largest)

'''
This allows the code to be implemented in a slightly different way, 
but this is less robust in case there is a None value in the values array.

In some other cases (e.g. when every loop iteration writes something to a file
and the file needs to be initialized in the first loop iteration) this type
of looping can be convenient.
'''

'''
Note that these exercises are merely illustrations of looping, the simplest solution would be:
'''

values = [-2,1,65,78,-54,-24,100]
smallest = min(values)
largest = max(values)
print(smallest, largest)

'''
A more efficient loop would be:
'''

values = [-2,1,65,78,-54,-24,100]
smallest, largest = None, None
for v in values:
    if smallest is None or v < smallest:
        smallest = v
    if largest is None or v > largest:
        largest = v
print(smallest, largest)
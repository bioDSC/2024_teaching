


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


def is_number_prime(X):
    '''
    This functions tests whether X is a prime number,
    and returns either False if not, or True if so.
    '''
    
    # Prime numbers are not divisible by any number
    # other than 1 and itself.
    # So if X can be divided by any number between
    # 1 and X, it is not a prime number.
    # So we'll test for each number 2 .. (X-1)
    # whether X can be divided by it.
    for y in range(2, X):
    
        # We test this by checking whether there's 
        # a remainder after a division.
        # (E.g. 7/3 has a remainder of 1 as 
        # 7 = 3 + 3 + 1, and so 7 is not divisible
        # by 3.)
        if X % y == 0:
            # if there's no remainder,
            # it could be divided, 
            # and it is not a prime number
            # --> return false
            return False
    
    # if for all numbers tested a division
    # wasn't possible, the number is a prime
    # number --> return true.
    return True

def calculate_primes(N):
    '''
    Returns all prime numbers between
    0 and N (not including N).
    '''
    
    prime_list = []
    
    # Loop over 2..N, and test 
    # whether the number is prime
    # and if so add it to the list.
    # (Note that 1 is excluded since
    # it's not prime anyways).
    for X in range(2, N):
        
        # Add X to list if it's prime
        if is_number_prime(X):
            prime_list.append(X)
    
    return(prime_list)

# Check whether it works            
primes_known_upto100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
primes_calculated_by_me = calculate_primes(100+1)
if (primes_known_upto100 == primes_calculated_by_me):
    print('Hurray it works!')
else:
    print('Oh nooo.')
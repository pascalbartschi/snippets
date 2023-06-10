# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 11:26:19 2021

@author: pascal
"""

#%% polyfit
import numpy as np

#numpy.polyfit(x,y, degree) 
#-> x is the x-coordinates of the sample points, y is the y coordinates of the sample point and deg is the degree of the polynomial fit.
#-> This function returns an array of polynomial coefficients with the highest power appearing first.
# output [6.5 3.2 4.1] with degree 2=> polynomial: 6.5*x**2 + 3.5*x**1 + 4.1

#%% t-test

import scipy.stats as sys

#scipy.stats.ttest_ind(a, b)
#http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html
# returns the t-statistics and two p-values

#%% array indexing


a=np.array([6,8,5,7,3])
b=np.array([0,3,2])
c=np.array([0,3,2,0,1])

print(a[b]) #integer array indexing, prints a at postions b
print(a[a>6]) # returns only a-values over 6
print(a>6)# returns boolean array
print(a[c>2]) #returns only a-values at postions where c is >2, attention that arrays have same size
print(a[(c>2) & (a>5)]) # only a-values where both is fulfilled

## background info: and, or make singe boolean evalutian
# --> therefore signs "&", "|" have to be used, they're capaple of multiple evaluation!
    



# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 13:31:58 2021

@author: pascal
"""

## bincount exercise

#%% sorts arrays into bins [0,0.2], [0.2,0.4], [0.4,0.6] 

import numpy as np

a = np.array([0.13,0.4,0.52])
a = 5*a
ar = a.astype(int)
# ar = ar//2
print(np.bincount(ar))

#%% autochecker

a = np.array([0.3,0.2,0.4,0.1,0.5,0.5,0.7,1.0,0.3,0.3,0.2,0.1,\
      0.8,0.8,0.7,0.6,0.3,0.0,0.1,0.2,0.7,0.4])**2
    
a = 10*a
ar = a.astype(int)
ar = ar//2
print(np.bincount(ar))

#%% attention

## will output error bc: 1//0.2 == 4.0 BUT 1/0.2==5
#--> better to first multiply small numbers and then turn the into integer for binning
import numpy as np

a = np.array([0.13,0.4,0.52])
a = a//0.2
ar = a.astype(int)
# ar = ar//2
print(np.bincount(ar))

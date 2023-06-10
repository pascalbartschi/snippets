# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 13:23:47 2021

@author: pascal
"""

### binning data

#%% boolean array indexing

import numpy as np

ages=np.array([1,25,26,13,8,14,20,10,3,0,29,11,24,16,22])
weights=np.array([4.5,13.1,12.9,10.7,8.2,11.0,10.1,9.3,6.3,3.2,12.8,10.8,12.2,\
                12.3,12.2])

means=np.array((max(ages)//6+1)*[0.0])

means[0]=np.mean(weights[(ages>=0) & (ages<6)])
## or means[0]=np.mean(weights[ages//6==0)
means[1]=np.mean(weights[(ages>=6) & (ages<12)])
means[2]=np.mean(weights[(ages>=12) & (ages<18)])
means[3]=np.mean(weights[(ages>=18) & (ages<24)])
means[4]=np.mean(weights[(ages>=24) & (ages<30)])

print ('means:',means)

#%% bincount function

import numpy as np

ages=np.array([1,25,26,13,8,14,20,10,3,0,29,11,24,16,22])
weights=np.array([4.5,13.1,12.9,10.7,8.2,11.0,10.1,9.3,6.3,3.2,12.8,10.8,12.2,\
                12.3,12.2])

ind=ages//6
no=np.bincount(ind) # bins values based on integer rsolution of intervall 6
tot=np.bincount(ind,weights) #takes values from weights and adds up the ones in same bin 
print(no)
print(tot)
print ('means:',tot/no)
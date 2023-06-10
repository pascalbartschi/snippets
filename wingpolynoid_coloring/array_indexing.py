# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 11:47:47 2021

@author: pascal
"""


#%% 
import numpy as np

a=np.array([3,5,2,5,6,2])
b=np.array([8,4,1,7,6,8])
for i in range(len(a)):
    if b[i]>=a[i]:
        a[i]+=2
print(a)

#%%

a=np.array([3,5,2,5,6,2])
b=np.array([8,4,1,7,6,8])
a[(b>=a)] += 2
print(a)

#%% taking the time

import time

a=np.array(int(1e6)*[3,5,2,5,6,2])
b=np.array(int(1e6)*[8,4,1,7,6,8])

time1 = time.time()
for i in range(len(a)):
    if b[i]>=a[i]:
        a[i]+=2
        
time2 = time.time()
print("loop:", time2-time1)

time3 = time.time()
a[b>=a]+=2
time4 = time.time()

print("indexing:", time4-time3)








# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 16:42:39 2021

@author: pascal
"""
#%% traingle area

triangle =  [[1,1],[2,3],[4,2]]

for index, node in enumerate(triangle):
    0.5 * node-1[0] * node[1]
    
#%%
    

triangle =  [[1,1],[2,3],[4,2]]

A = 0

for i in range(len(triangle)):
    A += ((triangle[i][0] * triangle[i-1][1]) - (triangle[i-1][0] * triangle[i][1]))
A = 0.5 * A

print(A)

#%%

#triangle =  [[-83.8, 49.5], [-82.8, 49.9], [-83.7, 49.4], [-84.8, 49.0]]
triangle =  [[1,1],[2,3],[4,2]]

A = 0

for i in range(len(triangle)):
    A += ((triangle[i][0] * triangle[i-1][1]) - (triangle[i-1][0] * triangle[i][1]))
A = 0.5 * A

print(A)
    
    
    
    
    
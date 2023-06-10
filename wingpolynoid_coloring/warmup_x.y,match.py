# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 15:52:34 2021

@author: pascal
"""

x_positions = [4.6, 4.5, 9.1, 2.2, 6.2, 7.6, 5.4, 9.3, 2.5, 2.6, 7.1, 
               8.9, 4.2, 3.1, 6.2, 1.4, 2.9, 9.7, 3.5, 5.2, 1.1, 9.3]
vertex_numbers = [2, 4, 11, 16, 18]

product = 1

for index in range(len(vertex_numbers)):
      product =  product* x_positions[vertex_numbers[index]]

#for vertex in x_postions:
#   vertexnumbers[i]

print(product)
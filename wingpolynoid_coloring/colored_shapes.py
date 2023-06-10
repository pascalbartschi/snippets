# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 12:05:11 2021

@author: pascal
"""

import matplotlib.pyplot as plt
from numpy import array
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

## example for colored shapes

triangle_positions = [[0,0],[0.3,0.3],[0.5,0.1]]
quadrilateral_positions = [[0.5,0.1],[0.3,0.3],[0.6,0.5],[0.8,0.4]]
pentagon_positions =[[0.6,0],[0.5,0.1],[0.8,0.4],[0.9,0.3],[0.7,0.02]]

polygs = []
polygs.append(Polygon(triangle_positions))
polygs.append(Polygon(quadrilateral_positions))
polygs.append(Polygon(pentagon_positions))
patches = PatchCollection(polygs)
patches.set_cmap('jet') # the maximum and minimum number defines the scale of the colormap
patches.set_array(array([3,2.5,1])) #for colors

fig=plt.figure()
panel=plt.gca()
panel.add_collection(patches)
fig.colorbar(patches)
panel.autoscale(True)
panel.set_aspect('equal')
plt.show()
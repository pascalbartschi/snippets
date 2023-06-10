# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 14:00:33 2021

@author: pascal
"""

import numpy as np

sex = np.array([0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0]) # male: 0; female: 1
height = np.array([1.83, 1.72, 1.61, 1.68, 1.79, 1.75, 1.92, 1.76, 1.66, 1.68, 1.69, 1.61, 1.70, 1.78]) # in meters

sex_bins = np.bincount(sex)
weights_per_bin = np.bincount(sex, height)
mean = weights_per_bin/sex_bins
print(100*(mean[0]-mean[1])) #*1oo bc: meter->cm
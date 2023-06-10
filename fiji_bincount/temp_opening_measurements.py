# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 15:18:58 2021

@author: pascal
"""
import numpy as np
import scipy.stats as sy

#overalllists
o_arealist = []
o_meanlist = []
o_xlist = []
o_ylist = []

for number in range(6):
    fyle = open("MHV_measurements_{no}.csv".format(no=number), "r")
    lines = fyle.readlines() [1:]
    fyle.close()
    
    measurementarray = np.zeros((len(lines),5))
    
    for i in range(len(lines)):
        line = lines[i].strip()
        lyst = line.split(',')
        array = np.array(lyst)
        measurementarray[i] = array
    #print(measurementarray)
    
    arealist = list(measurementarray[:,1])
    meanlist = list(measurementarray[:,2])
    xlist = list(measurementarray[:,3])
    ylist = list(measurementarray[:,4])

    for index,area in enumerate(arealist):
        if 10 < area < 1000:
            o_arealist.append(arealist[index])
            o_meanlist.append(meanlist[index])
            o_xlist.append(xlist[index])
            o_ylist.append(ylist[index])
            
#print(len(o_arealist))

areaarray = np.array(o_arealist)
meanarray = np.array(o_meanlist)
xarray = np.array(xlist)
yarray = np.array(ylist)

spearman = sy.spearmanr(areaarray, meanarray)

area_bin = (areaarray-1)//100 # //100 because bin range is 100, -1 bc otherwise each bin is shifted(0,99)

area_bin = area_bin.astype(int)

bincount_tot = np.bincount(area_bin)

area_infected_list = []

for index, element in enumerate(o_meanlist):
    if element >= 12:
        area_infected_list.append(area_bin[index]) #already normed array area_bin taken

infected_array = np.array(area_infected_list)

bincount_infected = np.bincount(infected_array, minlength=10) #minlength so arrays have same length

ratioarray = bincount_infected / bincount_tot

#past exams on OLAT
        


#select cells mean >12
    




            
    

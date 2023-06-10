# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 15:44:47 2021

@author: pascal
"""


#determine x,y-postions of the vertices of all cells
def get_list(data, typ):
    #transfer the data from the file into a list
    fyle = open(data +'.txt')
    l_fyle = fyle.readlines()
    fyle.close()
    datalist = []
    for element in l_fyle:
        #locallist = []
        #element = element.strip()
        datalist.append(element.split())
        #datalist.append(locallist)
        #datalist1 = []
    print(datalist)
    for index,el in enumerate(datalist):
        for elprime in range(len(el)):
            if typ == 'cv':
                datalist[index][elprime] =  int(datalist[index][elprime])
            elif typ == 'vp':
                datalist[index][elprime] =  float(datalist[index][elprime])
    return datalist
    
def cell_positions(vertexlist, postionslist):
    #get the x,y-positions of the vertices of all cells
    celllist = []
    for cell in positionlist:
        locallist = []
        for position in cell:
            locallist.append(vertexlist[position])
        celllist.append(locallist)
    return celllist
                
        
        
        
    
    #calculate cell areas
def area():
    #calculate cell areas

#calculate positions of cell centroid and distance of centroid to wingdisc center
def centroid():
    #calculates cell centroids
    
def distance_center():
    #calculate the distance of the cell centroids to the disc center

#plot cell area against distance from wingdisc center and add a linear fit
def plotting():
    #plot areas including the linear fit
    
#do statistical test (t-test)
def statistical_test():
    #Note that we no longer do the Spearman's rank test as suggested in the video!

#draw the disc
def draw_disc():
    #draw the wing disc

#do this for a small and a large disc
def analyze_disc():
    #call the functions above

#filename_large=''
#analyze_disc(filename_large) #since there are two files for the large disc, 
                             #it is actually more practical to use analyze_disc('large')
#filename_small=''
#analyze_disc(filename_small) #here it's also more practical to use analyze_disc('small')

#use functions:
#clearer structure
#easier to manage variables (don't use global variables, don't refer to variables
#outside the function)
#no need to duplicate code for the small and large disc

vertexlist = get_list('large_cv', 'cv')
positonslist = get_list('large_vp', 'vp')
celllist = (vertexlist, positionslist)

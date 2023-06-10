# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 16:20:42 2021

@author: pascal
"""
import pylab as py
#tempfile

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
    #print(datalist)
    for index,el in enumerate(datalist):
        for elprime in range(len(el)):
            if typ == 'cv':
                datalist[index][elprime] =  int(datalist[index][elprime])
            elif typ == 'vp':
                datalist[index][elprime] =  float(datalist[index][elprime])
    return datalist
    
def cell_positions(vertexlist, positionlist):
    #get the x,y-positions of the vertices of all cells
    celllist = []
    for cell in vertexlist:
        locallist = []
        for vertex in cell:
            locallist.append(positionlist[vertex])
        celllist.append(locallist)
    return celllist

def area(celllist):
    #calculate cell areas
    arealist = []
    for cell in celllist:
        A = 0
        for i in range(len(cell)):
            A += ((cell[i][0] * cell[i-1][1]) - (cell[i-1][0] * cell[i][1]))
        A = 0.5 * A
        arealist.append(A)
    areaarray = py.array(arealist)
    
    return areaarray

# information N-1?? Clockwise?

def centroid(celllist, areaarray):
    #calculates cell centroids
    centroidlist = []
    for index, cell in enumerate(celllist):
        #print(index,cell)
        locallist = []
        cx = 0
        cy = 0
        for i in range(len(cell)):
            #print(cx)
            cx += (cell[i][0]+cell[i-1][0]) * (cell[i][0] * cell[i-1][1] - cell[i-1][0]*cell[i][1])
        cx = (1 / (6*areaarray[index])) * cx
        locallist.append(cx)
        for j in range(len(cell)):
            cy += (cell[j][1]+cell[j-1][1]) * (cell[j][0] * cell[j-1][1] - cell[j-1][0]*cell[j][1])
        cy = (1 / (6*areaarray[index])) * cy
        locallist.append(cy)
        
        centroidlist.append(locallist)
    return centroidlist
            
# numbers of array are waaayy to high

def distance_center(centroidlist):
    #calculates cell distance
    distancelist = []
    for cell in centroidlist:
        celldistance = (cell[0] ** 2 + cell[1] ** 2) ** 0.5
        distancelist.append(celldistance)
    return distancelist

def plotting(areaarray, distancelist):
    #plots area aggaint distance to diskcenter of each cell
    distancearray = py.array(distancelist)
    polylist = py.polyfit(distancearray,areaarray,1)
    a = polylist[0]
    b = polylist[1]
    x = py.linspace(0,105,1000)
    y = a*x + b
    py.plot(distancearray,areaarray, 'go')
    py.plot(x,y)
    py.show()
    
    return a,b
    
def statistical_test(areaarray, distancelist):
    #statistical t-test
    import scipy.stats as sys
    distancearray = py.array(distancelist) 
    halfradius = max(distancearray) / 2
    firsthalf = []
    secondhalf =  []
    for index, distance in enumerate(distancearray):
        if distance <= halfradius:
            firsthalf.append(areaarray[index])
        else: 
            secondhalf.append(areaarray[index])
    
    results = sys.ttest_ind(firsthalf, secondhalf)
    return results
def converter(celllist):
    cpx = []
    cpy = []
    for cell in celllist:
        xlocalcell = []
        ylocalcell = []
        for element in cell:
            xlocalcell.append(element[0])
            ylocalcell.append(element[1])
        cpx.append(xlocalcell)
        cpy.append(ylocalcell)
        
    return cpx, cpy
    
def draw_disc(cpx, cpy, area, size):
    import matplotlib.pyplot as plt
    from matplotlib.patches import Polygon
    from matplotlib.collections import PatchCollection
    
    #input arguments: 
    ## cpx, cpy: x,y/positions of the vertices of all cells 
	# format: list (1 element per cell) of sublists (1 number per vertex, eg 3 numbers for a triangle). 
    ## area: cell area
	# format: 1-dimentsional numpy array (1 number per cell)
    ## size: 'large' for the large disc and 'small' for the small disc
    
    polygs = []
    for i in range(len(cpx)):
    	polyg = []
    	for j in range(len(cpx[i])):
    		polyg.append([cpx[i][j], cpy[i][j]])
    	polygs.append(Polygon(polyg))
    patches = PatchCollection(polygs)
    patches.set_cmap('jet')
    colors = 1 * area
    colors[colors>14] = 14 # color value for all the mitotic cells (area>14) is set to 14
    patches.set_array(py.array(colors)) #for colors

    fig = plt.figure()
    panel = fig.add_subplot(1,1,1)
    panel.add_collection(patches)
    color_bar = fig.colorbar(patches)
    color_bar.set_label('Cell area (um2)', rotation = 270, labelpad = 15)
    panel.set_xlim(-120, 110)
    panel.set_ylim(-85, 85)
    panel.set_aspect('equal')
    plt.title(size+' wing disc')
    
def functioncaller(size):
    if size == 'large':
        vertexlist = get_list('large_cv', 'cv')
        positionslist = get_list('large_vp', 'vp')
        celllist = cell_positions(vertexlist, positionslist)
        areaarray = area(celllist)
        centroidlist = centroid(celllist, areaarray)
        distancelist = distance_center(centroidlist)
        a,b = plotting(areaarray, distancelist)
        results = statistical_test(areaarray, distancelist)
        cpx, cpy = converter(celllist)
        draw_disc(cpx, cpy, areaarray, 'large')
    elif size == 'small':
        vertexlist = get_list('small_cv', 'cv')
        positionslist = get_list('small_vp', 'vp')
        celllist = cell_positions(vertexlist, positionslist)
        areaarray = area(celllist)
        centroidlist = centroid(celllist, areaarray)
        distancelist = distance_center(centroidlist)
        a,b = plotting(areaarray, distancelist)
        results = statistical_test(areaarray, distancelist)
        cpx, cpy = converter(celllist)
        draw_disc(cpx, cpy, areaarray, 'small')
    
    #return results,a,b
        

if __name__ == "main":
    functioncaller('small')
    functioncaller('large')

#vertexlist = get_list('large_cv', 'cv')
#positionslist = get_list('large_vp', 'vp')
#celllist = cell_positions(vertexlist, positionslist)
#areaarray = area(celllist)
#centroidlist = centroid(celllist, areaarray)
#distancelist = distance_center(centroidlist)
#a,b = plotting(areaarray, distancelist)
#results = statistical_test(areaarray, distancelist)
#cpx, cpy = converter(celllist)
#draw_disc(cpx, cpy, areaarray, 'large')

#print(results,a,b)

#print(centroidlist)

#%%
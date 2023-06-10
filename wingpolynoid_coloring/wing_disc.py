# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 13:31:19 2021

@author: pascal
"""
def winglist(data, typ):
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

#def verticescounter(data, typ, cell_number):
    #datalist = winglist(data, typ)
    #no_vertices = len(datalist[cell_number])
    #return no_vertices


    
    
# vp = vertex postion,, cv = cell-vertex
list_large_cv = winglist('large_cv', 'cv')
list_large_vp = winglist('large_vp', 'vp')



    

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 13:16:26 2021

@author: pascal
"""

from ij import IJ
from ij.io import DirectoryChooser

srcDir=DirectoryChooser("Choose input directory").getDirectory()
filename="nuclei_gonad.tif"
IJ.open(srcDir+filename);
IJ.run("Gaussian Blur...", "sigma=2");
IJ.setThreshold(31396, 64527);
IJ.run("Make Binary");
IJ.run("Watershed");
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 16:09:16 2021

@author: pascal
"""

#nuclei segmentation

#pen image / Gaussian blur / set threshold / apply threshold / watershed (including seeding and distance transform) / set measurements (including redirection) / analyze particles

#macros in fiji

#Record (in Plugins/Macros), Create (on recorder), Run (in code editor), Save as (.ijm file)

# Code:

# open("/Users/tinria/Desktop/nuclei_gonad.tif");
# run("Gaussian Blur...", "sigma=2");
# setAutoThreshold("Default dark");
# //run("Threshold...");
# setThreshold(31396, 64527);
# setOption("BlackBackground", false);
# run("Make Binary");
# run("Watershed");


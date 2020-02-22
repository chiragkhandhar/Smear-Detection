# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 23:45:02 2020

@author: Chirag
"""

import numpy as np
import cv2

inputPath = r"C:\Users\chirag\Desktop\393408706.jpg"
# outputPath = input("Enter Output Path")
numpyArray = np.zeros((500,500,3),dtype = float)

image = cv2.imread(inputPath)
resizedImage = cv2.resize(image,(500,500))
cv2.imshow('Image',resizedImage)
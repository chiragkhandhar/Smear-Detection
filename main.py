# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 19:14:10 2020

@author: Chirag Khandhar
"""

import time
from os import (listdir, path, makedirs)
from math import floor
from glob import glob
import numpy as np
from util import (pipeThrough, last)
import imageProcessor as ip

def imageGenerator(folder):
    files = listdir(folder)
    return (ip.readImage(path.join(folder, filename))
            for filename in files)

def cleanImages(input_folder, reset_every=500):
    images = imageGenerator(input_folder)
    firstImage = next(images) 
    imageShape = ip.toGrayscale(firstImage).shape
    process = pipeThrough(ip.toGrayscale, ip.threshold(120), ip.dilate, ip.detectEdges)

    acc = ip.emptyImage(imageShape)
    for (idx, image) in enumerate(images):
        acc = acc + process(image)
        if idx % reset_every == 0:
            yield (acc, idx)
            acc = ip.emptyImage(imageShape)

# MFC = Most Frequent Contours
def getMFC(inputImages):
    postprocess = pipeThrough(ip.erode, ip.dilate, ip.medianBlur, ip.threshold(120), ip.drawContours(5))
    images = list(inputImages)

    resulImage = sum([postprocess(image) / len(images)
                        for (image, _) in images])
    tollerance = 5
    maxPxlValue = max(resulImage.flatten())

    return ip.threshold(floor(maxPxlValue) - tollerance)(resulImage.astype(np.uint8))


def main():
    
    totalImages = 0
    print("-----------------------------------------------------------------------------------------------")     
    imagePath = input("Please paste the path of your data: ")
    if not path.exists(imagePath):
        imagePath = input("Invalid Path\nPlease enter again: ")
        
    input_folders = (imagePath, ['cam_0', 'cam_1', 'cam_2', 'cam_3', 'cam_5'])
    print("-----------------------------------------------------------------------------------------------")     
    opPath = input("Please enter the path of output folder: ")
    
    
    if not path.exists(opPath):
        makedirs(opPath)
    print("-----------------------------------------------------------------------------------------------") 
    start = time.time()    
    resultTtitle = lambda input_folder: '.'.join([last(path.split(input_folder)), 'result', 'jpg'])
    getresultPath = lambda input_folder, opPath: path.join(opPath, resultTtitle(input_folder))


    for input_folder in [path.join(input_folders[0], f) for f in input_folders[1]]:
        imgPath = input_folder+'/*.jpg'                                 # Loading Images
        imgData = glob(imgPath)                                 # glob module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell, although results are returned in arbitrary order.
        N = len(imgData)
        totalImages += N
        print("\t----------------------------------------------------------")
        print('Processing', input_folder, "| Number of Images : ",N)
        resultPath = path.join(opPath, getresultPath(input_folder, opPath))
        result = getMFC(cleanImages(input_folder, reset_every = 500))
        ip.writeImage(resultPath, result)
    print("-----------------------------------------------------------------------------------------------")   
    print("Processing finished\nOutput saved at: ",opPath)
    end = time.time()
    print("-----------------------------------------------------------------------------------------------")   
    print("Total Images Processed: ", totalImages, " | Total Time Required: ", round((end-start)/60,2), "mins")
    print("-----------------------------------------------------------------------------------------------")

if __name__ == '__main__':
    main()
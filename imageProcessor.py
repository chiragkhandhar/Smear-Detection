# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 19:15:41 2020

@author: Chirag Khandhar
"""

import cv2
import numpy as np

def readImage(path):
    print("Reading Image at ", path)
    return cv2.imread(path)

def writeImage(resultPath, result):
    print("Writing Image at ", resultPath)
    cv2.imwrite(resultPath, result)

def toGrayscale(image):
    print("Converting image to Grayscale")
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def detectEdges(image):
    (tLow, tHigh) = (130, 150)
    print("Detecting Edge")
    return cv2.Canny(image, tLow, tHigh)

def dilate(image):
    kernel = np.ones((3, 3), np.uint8)      # uint = unsigned integer (0 to 255)
    print("Dilating")
    return cv2.dilate(image, kernel, iterations = 1)

def erode(image):
    kernel = np.ones((5, 5), np.uint8)      # uint = unsigned integer (0 to 255)
    print("Eroding")
    return cv2.erode(image, kernel, iterations = 1)

def threshold(low):
    high = 255
    def thresholdFn(image):
        _ , result = cv2.threshold(image, low, high,cv2.THRESH_BINARY)
        return result
    return thresholdFn

def equalizeHistogram(image):
    print("Histogram Equalization")
    return cv2.equalizeHist(image)

def medianBlur(image):
    print("Median Blur")
    return cv2.medianBlur(image, 7)

def bilateral(image):
    print("Bilateral")
    return cv2.bilateralFilter(image, 11, 17, 17)

def clahe(image):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    print("Clahe")
    return clahe.apply(image)

def drawContours(take):
    print("Drawing Contours")
    (maxContourArea, minContourArea) = (20000, 2000)
    def drawContoursFn(image):
        result = emptyImage(image.shape)
        imageCopy = image.copy()
        contours, hierarchy = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        image = imageCopy
        contours = [c
                    for c in contours
                    if cv2.contourArea(c) > minContourArea and cv2.contourArea(c) < maxContourArea]

        contours = sorted(contours, key = cv2.contourArea, reverse = True)[:take]
        cv2.drawContours(result, contours, -1, 255, cv2.FILLED)
        return result
    return drawContoursFn

def emptyImage(imageShape):
    print("Emptying Image")
    return np.zeros(imageShape, np.uint8)   # uint = unsigned integer (0 to 255)

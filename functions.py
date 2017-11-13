# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 13:36:03 2017

@author: Gabriel PC
"""

#basic itemps to use


import cv2
import numpy as np
from matplotlib import pyplot as plt

def loadimg(link): #Load picture
    img  = cv2.imread(link)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return img

def show(temp): #Used to show the picture
    a = cv2.cvtColor(temp,cv2.COLOR_GRAY2RGB)
    plt.imshow(a)
    plt.show()
    return

def to_grey(image):
    img = np.copy(image)
    img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    return img

def saveimg(imagen,name):
    cv2.imwrite(name,imagen)
    pass

def tresshold(image,value):
    img = np.copy(image)
    sx,sy = np.size(image,0),np.size(image,1)
    for i in range(0,sx):
        for j in range(0,sy):
            if(image[i][j] > value):
                img[i][j] = 255
            else:
                img[i][j] = 0
    
    return img
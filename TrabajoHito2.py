# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
import functions as f

def line_separator(img,color):
    sx,sy = np.size(img,0),np.size(img,1)
    c = 0
    ca =[]
    for i in range(0,sx):
        temp = False
        for j in range(0,sy):
            if(img[i][j] != color):
                temp = True
        if temp == True:
            c = c+1
        elif(c != 0):
            ca.append([c,i-c,i])
            c = 0
    return ca


def ar_line_separator(ar,color):
    ans = []
    for i in range(0,len(ar)):
        ans.append(line_separator(ar[i],255))
    return ans
    

def separator_blocks(img,cord):
    images = []
    for i in range(0,np.size(cord,0)):
        #For each one
        csize = cord[i][0] 
        sy = np.size(img,1)
        cstart = cord[i][1]
        temp = np.zeros([csize,sy],dtype=np.uint8)
        for n in range(0,csize):
            for m in range(0,sy):
                temp[n][m] = img[n + cstart][m]
        images.append(temp)
    return images


def ar_separator_blocks(ar,cords):
    ans = []
    for i in range(0,len(ar)):
        ans.append(separator_blocks(ar[i],cords[i]))
    
    return ans
def EliminateLines(img):
    im = np.copy(img)
    sx = int(im.shape[0])
    sy = int(im.shape[1])
    #Another Tresshold
    for i in range(0,sx):
        for j in range(0,sy):
            if(im[i][j]>=210):
                im[i][j] = 255
            else:
                im[i][j] = 0
    im = ~im
    imgFinal = np.copy(im)
    (rows, cols) = im.shape
    estructura = np.array([[1], 
              [1],
             [1]])
    #Falta por convertir a manual
    imgFinal = cv2.erode(imgFinal, estructura, iterations = 1);
    imgFinal = cv2.dilate(imgFinal, estructura, iterations = 1);
    imgFinal = cv2.bitwise_not(imgFinal)
    return imgFinal




"""
test = f.loadimg("test.png")
f.show(test)
test = f.to_grey(test)
test = cv2.adaptiveThreshold(test,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,-2)
f.saveimg(test)
data = line_separator(test)
result = separator_blocks(test,data)
#mg(test)
"""
#Demo1
#Demo


def get_body(image):
    gray = cv2.medianBlur(image, 5)
    dst2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    return dst2

def transpose_all(ar):
    for i in range(0,np.size(ar,0)):
        ar[i] = cv2.transpose(ar[i])
    
    return ar


def transponse_arr_all(ar):
    for i in range(0,len(ar)):
        ar[i]= transpose_all(ar[i])
    return ar



#test = f.tresshold(test,100)

#test = cv2.adaptiveThreshold(test,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,-2)


test = f.loadimg("test.png")
test = f.to_grey(test)
f.saveimg(test,"imagen.png")
f.show(test)

clear = EliminateLines(test)

data = line_separator(test,255)

result_1 = separator_blocks(clear,data)
result_2 = transpose_all(result_1)
result_3 = ar_line_separator(result_2,255)
result_4 = ar_separator_blocks(result_2,result_3)
result_5 = transponse_arr_all(result_4)

for i in range(0,len(result_5)):
    temp = ar_line_separator(result_5[i],255)
    result_5[i] = ar_separator_blocks(result_5[i],temp)





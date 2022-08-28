from ast import Lambda
from turtle import width
import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
import imutils


def sort_pts(pts):
    npts = np.concatenate(pts).tolist()
    ysort = sorted(npts, key= lambda npts: npts[1])

    x1sort = ysort[:2]
    x1sort = sorted(x1sort, key= lambda x1sort:x1sort[0])

    x2sort = ysort[2:4]
    x2sort = sorted(x2sort,key=lambda x2sort: x2sort[0])
    tl, tr, bl, br = x1sort[0], x1sort[1], x2sort[0], x2sort[1]
    return [tl,tr,bl,br]
    


img = cv2.imread('input_assets\scan2.png')
img = imutils.resize(img,width=800)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



canny = cv2.Canny(gray,60,100)
canny = cv2.dilate(canny,None,iterations=1)

cnts = cv2.findContours(canny, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
cnts = sorted(cnts, key = cv2.contourArea, reverse=True)[:1]


aux = img.copy()
for c in cnts:
    epsilon = 0.01*cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,epsilon,True)
    print(approx)

    if len(approx) == 4:
        cv2.drawContours(img,[approx],0,(0,255,0),2)
        x,y,w,h = cv2.boundingRect(c)

        pts = sort_pts(approx)
        cv2.circle(img,approx[3][0],7,(0,255,255),2) #TL
        cv2.circle(img,approx[2][0],7,(0,255,255),2) #TR
        cv2.circle(img,approx[0][0],7,(0,255,255),2) #BL
        cv2.circle(img,approx[1][0],7,(0,255,255),2) #BR
        
        




        pos1 = np.float32(pts)
        pos2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
        M = cv2.getPerspectiveTransform(pos1,pos2)
        dst = cv2.warpPerspective(aux,M,(w,h))


        cv2.imshow('dst', dst)

        text = pytesseract.image_to_string(dst)
        print (text)
        






cv2.imshow('img', img)
# cv2.imshow('c',canny)

cv2.waitKey(0)

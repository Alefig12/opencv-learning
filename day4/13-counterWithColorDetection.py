import cv2
import numpy as np

img = cv2.imread('input_assets\squares.png')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

colors = {
    'blue': {
        'lower':np.array([90,50, 20], dtype=np.uint8),
        'upper':np.array([124,255, 255], dtype=np.uint8),
        'name': 'blue'
    },

    'yellow': {
        'lower':np.array([20,50, 20], dtype=np.uint8),
        'upper':np.array([40,255, 255], dtype=np.uint8),
        'name': 'yellow'
    },

    'green': {
        'lower':np.array([45,85, 20], dtype=np.uint8),
        'upper':np.array([77,255, 255], dtype=np.uint8),
        'name': 'green'
    },

    'red': {
        'lower':np.array([1,100, 50], dtype=np.uint8),
        'upper':np.array([5,100, 255], dtype=np.uint8),
        'lower2':np.array([175,100, 50], dtype=np.uint8),
        'upper2':np.array([179,255, 255], dtype=np.uint8),
        'name': 'red'
    },
    'purple': {
        'lower':np.array([130,50, 20], dtype=np.uint8),
        'upper':np.array([150,255, 255], dtype=np.uint8),
        'name': 'purple'
    },
}

def countColor(hsv,img, color):
    lower = color['lower']
    upper = color['upper']


    mask = cv2.inRange(hsv, lower, upper)


    if (color['name'] == 'red'):
        lower2 = color['lower2']
        upper2 = color['upper2']
        mask2 = cv2.inRange(hsv, lower2, upper2 )

        mask = cv2.add(mask, mask2)

    cnts,_ = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    i =0
    for c in cnts:
        if cv2.contourArea(c) > 1:
            cv2.drawContours(img,[c],0,(0,0,0),2,cv2.LINE_AA)
            #Calculating center
            M = cv2.moments(c)

            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            cv2.putText(img,str(i),(cX-10,cY+10),0,1,(0,0,0),2,cv2.LINE_AA)
            i+=1
    print('There are in total {} {} squares'.format(str(i), color['name']))



for c in colors:
    countColor(hsv, img,colors[c])




cv2.imshow('img', img)

cv2.waitKey(0)





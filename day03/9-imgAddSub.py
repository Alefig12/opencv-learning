import cv2
import numpy as np
img = cv2.imread('input_assets\green_rubik.jpg')
img2 = cv2.imread('input_assets\img.jpg')

lower_green = np.array([45,110, 20], dtype=np.uint8)
upper_green= np.array([77,255, 255], dtype=np.uint8)

lower_orange = np.array([1,100, 129], dtype=np.uint8)
upper_orange = np.array([12,255, 255], dtype=np.uint8)

frame_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
frame_hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(frame_hsv,lower_green,upper_green)
mask2 = cv2.inRange(frame_hsv2, lower_orange,upper_orange)



img3 = cv2.add(mask,mask2)


cv2.imshow('img3',img3)
cv2.waitKey(0)

img4 = cv2.subtract(img,img2)
cv2.imshow('img4',img4)
cv2.waitKey(0)


img5 = cv2.absdiff(img2,img)


cv2.imshow('img5',img5)
cv2.waitKey(0)
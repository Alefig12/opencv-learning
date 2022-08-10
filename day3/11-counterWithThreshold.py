import cv2

img = cv2.imread('input_assets\coins.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Find inverted threshold
mask = cv2.threshold(gray,235,255,cv2.THRESH_BINARY_INV)[1]

#Find countours to then count them
cnts, _ = cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


#Draw each contour, finding its center point and then assign a number to it
n = 0
for c in cnts:
    
    if cv2.contourArea(c) > 500:
        cv2.drawContours(img,[c],0,(0,0,255), 2, cv2.LINE_AA)


        #Calculating center point

        M = cv2.moments(c)

        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])


        cv2.putText(img,str(n),(cX,cY),0,1,(0,0,255),2,cv2.LINE_AA)

        cv2.imshow('img', img)
        cv2.waitKey(0)
        n+=1










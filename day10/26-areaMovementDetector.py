from turtle import width
import cv2
import numpy as np

cap = cv2.VideoCapture('input_assets\WalkingFootage.mp4')


#fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
#fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))



while True:
    ret, frame = cap.read()
    height, width = frame.shape[:2]
    if not ret:break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Base status text
    text = "Status: Movement not detected"
    textColor = (0,255,0)

    # Drawing our region of interest (ROI)
    pts =  np.array([[320, 435], [650,435],[840,height],[120,height]])
    cv2.drawContours(frame,[pts],-1,textColor,2)


    # Image only showing our ROI 
    aux = np.zeros(shape=(height,width), dtype=np.uint8)
    aux = cv2.drawContours(aux,[pts],-1,255,-1)
    area = cv2.bitwise_and(gray,gray, mask=aux)


    # Getting movement from bgSubtractor
    fgmask = fgbg.apply(area)

    #Reduce noise from fgmask
    fgmask = cv2.morphologyEx(fgmask,cv2.MORPH_OPEN,kernel)
    fgmask = cv2.dilate(fgmask,None,iterations=2)


    #Getting contours

    cnts = cv2.findContours(fgmask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]

    for c in cnts:
        if cv2.contourArea(c) > 700:
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(frame,(x,y), (x+w,y+h), (0,255,0),2)
            text = "Status: MOVEMENT DETECTED"
            textColor = (0,0,255)


    #Status text
    cv2.rectangle(frame,(0,0),(width,70),0,-1)
    cv2.putText(frame,text,(0,60),cv2.FONT_HERSHEY_SIMPLEX,1.9,textColor,2)

    cv2.imshow('video', frame)
    cv2.imshow('fgmask', fgmask)


    k = cv2.waitKey(80)

    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
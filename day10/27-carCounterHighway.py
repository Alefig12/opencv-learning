import cv2
import numpy as np

cap = cv2.VideoCapture('input_assets\carsHighway.mp4')
fps = int(cap.get(5))

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
#fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()
#fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

cartotal = 0
carcount = 0
while True:
    ret, frame = cap.read()

    if not ret: break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Rectangle detector
    
    pts = np.array([[400,190],[670,190],[670,280],[400,280]])
    cv2.drawContours(frame,[pts],-1,(0,255,0),2)
    cv2.line(frame,(600,190),(600,280),(0,0,255),2)

    aux = np.zeros(shape=frame.shape[:2],dtype=np.uint8)
    aux = cv2.drawContours(aux,[pts],-1,255,-1)
    area = cv2.bitwise_and(gray, gray, mask=aux)

    fgmask = fgbg.apply(area)
    fgmask = cv2.morphologyEx(fgmask,cv2.MORPH_OPEN,kernel)
    fgmask = cv2.morphologyEx(fgmask,cv2.MORPH_CLOSE,kernel)
    fgmask = cv2.dilate(fgmask,None,iterations=1)
    

    cnts = cv2.findContours(fgmask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]

    for c in cnts:
        if cv2.contourArea(c) > 200:
            x,y,w,h = cv2.boundingRect(c)

            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)

            if 597 < (x+w) < 605:
                carcount +=1
                cv2.line(frame,(600,190),(600,280),(0,255,255),4)



    cv2.rectangle(frame,(690,190), (770,280), (255,0,255),2)
    cv2.putText(frame, str(carcount),(700,250),1,3,(255,255,255),3)
    cv2.imshow('video',frame)
    cv2.imshow('fgmask',fgmask)

    

    k = cv2.waitKey(fps)

    if k == ord('q'):
        break


cv2.destroyAllWindows()
cap.release()

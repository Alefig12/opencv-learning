import cv2
import numpy as np

cap = cv2.VideoCapture(0)




lower_blue = np.array([90,50, 20], dtype=np.uint8)
upper_blue = np.array([140,255, 255], dtype=np.uint8)

lower_yellow = np.array([20,113, 20], dtype=np.uint8)
upper_yellow = np.array([40,255, 255], dtype=np.uint8)

lower_green = np.array([45,85, 20], dtype=np.uint8)
upper_green= np.array([77,255, 255], dtype=np.uint8)

lower_red1 = np.array([1,100, 50], dtype=np.uint8)
upper_red1= np.array([5,100, 255], dtype=np.uint8)

lower_red2 = np.array([175,100, 50], dtype=np.uint8)
upper_red2= np.array([179,255, 255], dtype=np.uint8)


blue = {
    'color': (255,0,0),
    'pos': (0,50),
    'text': 'Blue'
 }
red = {
    'color': (0,0,255),
    'pos': (140,50),
    'text': 'Red'
 }
yellow = {
    'color': (0,255,255),
    'pos': (270,50),
    'text': 'Yellow'
 }
green = {
    'color': (0,255,0),
    'pos': (460,50),
    'text': 'Green'
 }



def drawTexts():

    cv2.rectangle(frame,(0,0),(640,55), 0,-1)
    cv2.putText(frame, blue['text'],blue['pos'],0,2,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,red['text'],red['pos'],0,2,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,yellow['text'],yellow['pos'],0,2,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,green['text'],green['pos'],0,2,(255,255,255),2,cv2.LINE_AA)

def drawMatches(mask,color):
    cnts,_ = cv2.findContours(mask,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)


    for c in cnts:
        a = cv2.contourArea(c)
        if a>2000:

            #Calculate moments to get center
            M = cv2.moments(c)

            #Get coordinates of the center of the object
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            new_c = cv2.convexHull(c)

            cv2.drawContours(frame,[new_c],0,(0,0,255),2,cv2.LINE_AA)
            cv2.circle(frame,(cX,cY),5,(255,255,255),-1)
            cv2.putText(frame,color['text'],color['pos'],0,2,color['color'],2, cv2.LINE_AA)
    return



while True:
    ret, frame = cap.read()
    if not ret:
        break
    drawTexts()

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    blueMask = cv2.inRange(frame_hsv, lower_blue, upper_blue)
    yellowMask = cv2.inRange(frame_hsv, lower_yellow, upper_yellow)
    greenMask = cv2.inRange(frame_hsv, lower_green, upper_green)
    redMask1 = cv2.inRange(frame_hsv, lower_red1, upper_red1)
    redMask2 = cv2.inRange(frame_hsv, lower_red2, upper_red2)

    redMask = cv2.add(redMask1,redMask2)
    
    drawMatches(blueMask, blue)
    drawMatches(yellowMask,yellow)
    drawMatches(greenMask,green)
    drawMatches(redMask,red)

            

    


    cv2.imshow("Video", frame)


    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
import cv2
import numpy as np

yellowLower = np.array([20, 50, 20], dtype=np.uint8)
yellowUpper =np.array([40, 255, 255], dtype=np.uint8)

lower_blue = np.array([90,50, 20], dtype=np.uint8)
upper_blue = np.array([140,255, 255], dtype=np.uint8)


cap = cv2.VideoCapture(0)
video = []
while True:
    ret, frame = cap.read()

    if not ret: break

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    mask = cv2.inRange(hsv,lower_blue, upper_blue)
    mask = cv2.erode(mask,None,iterations=3)
    mask = cv2.dilate(mask,None,iterations=3)
    mask = cv2.medianBlur(mask,3)
    

    
    

    blueOnly = cv2.bitwise_and(frame,frame, mask=mask)
    
    mask = cv2.bitwise_not(mask)
    maskedbg = cv2.bitwise_and(gray,gray,mask=mask)
    
    maskedbg = cv2.cvtColor(maskedbg,cv2.COLOR_GRAY2RGB)

    frame = cv2.add(maskedbg,blueOnly)

    
    



    cv2.imshow('frame', frame)

    video.append(frame)

    k = cv2.waitKey(1)
    
    if k == ord('q'):
        break
cv2.destroyAllWindows()


FPS = cap.get(5) #Frames

Width = int(cap.get(3)) #Width
Height = int(cap.get(4)) #Height

fourcc = cv2.VideoWriter_fourcc(*'avc1')
out = cv2.VideoWriter(r"output_assets\blue_highlight.mp4",fourcc, FPS, (Width,Height)) 

for img in video:
    out.write(img)
out.release()
cap.release()
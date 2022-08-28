import cv2
import numpy as np

cap = cv2.VideoCapture(0) 
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4',fourcc, 30.0, (640,480))

lower_blue = np.array([98,35, 21], dtype=np.uint8)
upper_blue = np.array([123,255, 255], dtype=np.uint8)

i =0
while True:
    ret, img = cap.read()
    
    if not ret:
        break

    if i == 20:
        static = img

    if i > 20:
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv, lower_blue, upper_blue)
  
        mask = cv2.medianBlur(mask, 15)


        #Let's dilate
        kernel = np.ones((5,5), np.uint8)
        mask = cv2.dilate(mask,kernel, iterations=2)

        bgShirt = cv2.bitwise_and(static, static, mask=mask)
        
        invmask = cv2.bitwise_not(mask)
        noShirt = cv2.bitwise_and(img, img, mask = invmask)


        img = cv2.add(bgShirt, noShirt)
  
    out.write(img)

    cv2.imshow('video', img)


    i+=1
    



    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
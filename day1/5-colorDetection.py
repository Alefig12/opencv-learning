import cv2
import numpy as np

cap = cv2.VideoCapture(0) 
# Useful stackoverflow answers: https://stackoverflow.com/questions/10948589/choosing-the-correct-upper-and-lower-hsv-boundaries-for-color-detection-withcv?lq=1
# Color ranges based on: https://i.stack.imgur.com/gyuw4.png

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output_assets/output_colorDetection.mp4',fourcc, 30.0, (640,480))

lower_blue = np.array([90,50, 20], dtype=np.uint8)
upper_blue = np.array([140,255, 255], dtype=np.uint8)

while True:
    ret, img = cap.read()
    
    if not ret:
        break

    img_hsv= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #Mask only if blue is detected
    mask = cv2.inRange(img_hsv,lower_blue,upper_blue)

    color_mask  = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow('video', color_mask)


    out.write(color_mask)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
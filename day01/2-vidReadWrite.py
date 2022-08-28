import cv2

cap = cv2.VideoCapture(0) # 0 for camera

# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter(r"day7\videos\me.mp4",fourcc, 30.0, (640,480)) 
while True:
    ret, img = cap.read()
    
    if not ret:
        break

    cv2.imshow('video', img)

    # out.write(img)

    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
# out.release()
cv2.destroyAllWindows()
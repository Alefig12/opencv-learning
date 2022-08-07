import cv2

cap = cv2.VideoCapture("day1/input_assets/vid.mp4") # 0 for camera

# out = cv2.VideoWriter('day1\output_assets\ouput_video.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 20, (640, 480))
while True:
    ret, img = cap.read()
    
    if not ret:
        break

    cv2.imshow('video', img)

    # out.write(img)

    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
#out.release()
cv2.destroyAllWindows()
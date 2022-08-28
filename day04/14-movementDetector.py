import cv2


cap = cv2.VideoCapture(0)
#out = cv2.VideoWriter(r'day1\output_assets\video.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 20, (640, 480))
i = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    if i == 30: 
        static = gray
    
    if i > 30:
        diff = cv2.absdiff(static, gray)
        thresh = cv2.threshold(diff,50,255,cv2.THRESH_BINARY)[1]
        cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        for c in cnts:
            if cv2.contourArea(c) > 9000:
                x, y, w, h = cv2.boundingRect(c)

                cv2.rectangle(frame,(x,y), (x+w,y+h),(0,255,0), 2)

        


    i+=1

    #out.write(frame)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
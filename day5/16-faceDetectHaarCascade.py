import cv2



faceDet = cv2.CascadeClassifier('day5\haarcascade_frontalface_default.xml')
img = cv2.imread(r'input_assets\faces.jpg')


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceDet.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=6, minSize=(30,30), maxSize=(200,200))



for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y), (x+w, y+h),(0,255,0), 2)


cv2.imshow('img', img)
cv2.waitKey(0)

#Now in video

cap = cv2.VideoCapture(0)
while True:

    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = faceDet.detectMultiScale(gray, 1.1, 4) #Image, ScaleFactor and minNeighbors as parameters

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y), (x+w, y+h),(0,255,0), 2)


    cv2.imshow('img', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
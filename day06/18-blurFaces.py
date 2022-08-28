import cv2

def doNothing(pos):
    pass

img = cv2.imread('input_assets/faces.jpg')
faceDet = cv2.CascadeClassifier('input_assets\haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)



gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

VIDEO_CAPTURE = False


cv2.namedWindow('Image')

cv2.createTrackbar('Blur', 'Image', 0, 20, doNothing)

while True:


    ret, frame = cap.read()

    if not ret:break

    if VIDEO_CAPTURE: 
        img = frame
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    pos = cv2.getTrackbarPos('Blur', 'Image')
    imgBlur = img.copy() 
    faces =  faceDet.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)
   
    for (x,y,w,h) in faces:
        
        if pos > 0:
            crop=img[y:y+h,x:x+w] 
            
            crop_blur = cv2.blur(crop,(pos,pos))
            imgBlur[y:y+h,x:x+w] = crop_blur
        else:
            imgBlur = img.copy()



    res = cv2.resize(imgBlur,(640,480))
    cv2.imshow('Image', res)


    k = cv2.waitKey(1)
    if k == ord('q'):
        break

    if k == ord('p'):
        VIDEO_CAPTURE = True


cv2.destroyAllWindows()
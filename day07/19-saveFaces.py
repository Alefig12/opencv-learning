import cv2
import os

imgPath = 'input_assets\saveFaces_input'
imgList = os.listdir(imgPath)

faceDet = cv2.CascadeClassifier('input_assets\haarcascade_frontalface_default.xml')




count = 0
for name in imgList:

    img = cv2.imread(imgPath+'/'+name)
    aux = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = faceDet.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)





    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y), (x+w, y+h),(0,255,0), 2)
        face = aux[y:y+h,x:x+w]
        face = cv2.resize(face,(150,150))
        cv2.imwrite(r'output_assets\saveFaces_output\face_{}.jpg'.format(count),face)
        cv2.imshow('face', face)
        cv2.imshow('img', img)
        count+=1
        cv2.waitKey(0)



#Now in video

# cap = cv2.VideoCapture(0)
# while True:

#     ret, frame = cap.read()

#     if not ret:
#         break

#     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

#     faces = faceDet.detectMultiScale(gray, 1.1, 4) #Image, ScaleFactor and minNeighbors as parameters

#     for (x,y,w,h) in faces:
#         cv2.rectangle(frame,(x,y), (x+w, y+h),(0,255,0), 2)


#     cv2.imshow('img', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# cv2.destroyAllWindows()
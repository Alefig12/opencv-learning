import cv2
import numpy as np
import imutils
import os



def saveFacesFromVideo(name, dataFolder, videoPath):
    savePath = dataFolder+'/'+name

    if not os.path.exists(savePath):
        os.makedirs(savePath)

    cap = cv2.VideoCapture(videoPath)
    faceDet = cv2.CascadeClassifier('input_assets\haarcascade_frontalface_default.xml')
    count = 0


    while True:

        ret, frame = cap.read()

        if not ret:break

        frame = imutils.resize(frame, width=640)
        gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        aux = frame.copy()

        faces = faceDet.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=16)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y), (x+w, y+h),(0,255,0), 2)
            face = aux[y:y+h,x:x+w]
            face = cv2.resize(face,(150,150))

            cv2.imwrite(savePath+'/face_{}.jpg'.format(count), face)
            count+=1

        cv2.imshow('frame',frame)

        k = cv2.waitKey(1)
        if k == ord('q') or count >= 500:
            break


    cap.release()
    cv2.destroyAllWindows()



def training(dataFolder):
    people = os.listdir(dataFolder)
    labels = []
    faceData = []
    label = 0

    for name in people:
        namePath = dataFolder+'/'+name

        for face in os.listdir(namePath):
            labels.append(label)
            img = cv2.imread(namePath+'/'+face,0)
            faceData.append(img)


        label+=1


    face_recognizer = cv2.face.EigenFaceRecognizer_create()
    

    #Training
    print('Initializing training...')
    face_recognizer.train(faceData,np.array(labels))

    face_recognizer.write('day7\eigenFaceModel.xml')
    print('Model saved.')


def recognize(dataPath, testVideo = None):




    people = os.listdir(dataPath)

    face_recognizer = cv2.face.EigenFaceRecognizer_create()

    face_recognizer.read('day7\eigenFaceModel.xml')

    if testVideo is None:
        cap=cv2.VideoCapture(0)

    else:
        cap=cv2.VideoCapture(TEST_VIDEO)
    faceDet = cv2.CascadeClassifier('input_assets\haarcascade_frontalface_default.xml')

    video  = []
    while True:

        ret, frame = cap.read()
        if not ret:break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        aux = gray.copy()

        
        faces = faceDet.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=6)

        for (x,y,w,h) in faces:

            face = aux[y:y+h,x:x+w]
            
            face = cv2.resize(face, (150,150))
            result = face_recognizer.predict(face)
            

            cv2.putText(frame,'{}'.format(result),(x,y-5),1,1,(0,255,),2)

            if result[1] < 7500:
                cv2.rectangle(frame,(x,y), (x+w, y+h),(0,255,0), 2)
                cv2.putText(frame,'{}'.format(people[result[0]]),(x,y-25),1,2,(0,255,0),2)
            else:
                cv2.rectangle(frame,(x,y), (x+w, y+h),(0,0,255), 2)
                cv2.putText(frame,'UNKNOWN',(x,y-25),1,2,(0,0,255),2)

        
        cv2.imshow('frame', frame)

        

        video.append(frame)



        k = cv2.waitKey(1)
        

        if k == ord('q'):
            break




    FPS = cap.get(5) #Frames

    Width = int(cap.get(3)) #Width
    Height = int(cap.get(4)) #Height
    
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter(r"output_assets\marssdsd.mp4",fourcc, FPS, (Width,Height)) 

    for img in video:
        out.write(img)
    out.release()





DATAPATH = r'day7\videos\data'
TEST_VIDEO = r'day7\videos\test\test_mars.mp4'

# saveFacesFromVideo('Mars',DATAPATH,r'day7\videos\mars.mp4')
# saveFacesFromVideo('Cafe',DATAPATH,r'day7\videos\me.mp4')
# training(DATAPATH)

recognize(DATAPATH, TEST_VIDEO) #Delete TEST_VIDEO if camera input





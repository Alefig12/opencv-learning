from turtle import width
import cv2
import imutils

cap = cv2.VideoCapture(0)

filter = cv2.imread(r'input_assets\2022logo.png',cv2.IMREAD_UNCHANGED)

#instantiate classifier
faceDet = cv2.CascadeClassifier('input_assets\haarcascade_frontalface_default.xml')


video = []


while True:

    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if not ret: break



    faces = faceDet.detectMultiScale(gray, 1.2,6)

    for (x,y,w,h) in faces:
        #cv2.rectangle(frame,(x,y), (x+w, y+h),(0,255,0), 2)
        
        resizedFilter = imutils.resize(filter, width=w)
        heightFilter = resizedFilter.shape[0]
        widthFilter = w

        #This is to make the filter show a little bit below the upper border of the rectangle face.
        showBelow = heightFilter // 5

        dif = 0

        yFilter = y-heightFilter+showBelow
        # Adding filter to frame on top of the face detected
        if yFilter >= 0:
            filterArea = frame[yFilter:y+showBelow, x:x+w] 
        else:
            dif = abs(yFilter)
            filterArea = frame[0:y+showBelow,x:x+w]
            

        filterMask = resizedFilter[:,:, 3]
        
        filterMaskInv = cv2.bitwise_not(filterMask)

        bgBlack= cv2.bitwise_and(resizedFilter,resizedFilter,mask=filterMask)
        bgBlack = bgBlack[dif:,:,:3]

        bgFrame = cv2.bitwise_and(filterArea,filterArea, mask=filterMaskInv[dif:,:])

        result = cv2.add(bgBlack,bgFrame)

        if yFilter >= 0:
            frame[yFilter:y+showBelow, x:x+w] = result
        else:
            frame[0:y+showBelow, x:x+w] = result
            
    video.append(frame)
    cv2.imshow('video', frame)
    

    k =cv2.waitKey(1)

    if k == ord('q'):
        break


# FPS = cap.get(5) #Frames

# Width = int(cap.get(3)) #Width
# Height = int(cap.get(4)) #Height

# fourcc = cv2.VideoWriter_fourcc(*'avc1')
# out = cv2.VideoWriter(r"output_assets\face_filter.mp4",fourcc, FPS, (Width,Height)) 

# for img in video:
#     out.write(img)
# out.release()
# cap.release()
import cv2
import mediapipe as mp
import mediapipe.python.solutions.drawing_utils as mp_drawing
import mediapipe.python.solutions.hands as mp_hands





cap = cv2.VideoCapture(0)
video=[]
with mp_hands.Hands(max_num_hands=5) as hands:
    while True:
        ret, frame = cap.read()
        if not ret: break
        
        height, width,_ = frame.shape
        frame = cv2.flip(frame,1)
        framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(framergb)

        # print("Handedness {}".format(results.multi_handedness))
        # print("Landmarks: {}".format(results.multi_hand_landmarks))

        if results.multi_hand_landmarks is not None:
            for landmarks in results.multi_hand_landmarks:
                
                #DRAW ALL LANDMARKS WITH CONNECTIONS
                mp_drawing.draw_landmarks(frame, landmarks,mp_hands.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color =(0,0,255)),mp_drawing.DrawingSpec(color=0))

                # GETTING EACH INDIVIDUAL TIP LANDMARK
                # x1 = int(landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x*width)
                # y1 = int(landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y*height)

                # x2 = int(landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x*width)
                # y2 = int(landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y*height)

                # x3 = int(landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x*width)
                # y3 = int(landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y*height)

                # x4 = int(landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x*width)
                # y4 = int(landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y*height)

                # x5 = int(landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x*width)
                # y5 = int(landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y*height)

                # cv2.circle(frame,(x1,y1),4,255,-1)
                # cv2.circle(frame,(x2,y2),4,255,-1)
                # cv2.circle(frame,(x3,y3),4,255,-1)
                # cv2.circle(frame,(x4,y4),4,255,-1)
                # cv2.circle(frame,(x5,y5),4,255,-1)






        #frame = cv2.flip(frame,1)
        video.append(frame)
        cv2.imshow('video', frame)

        k = cv2.waitKey(1)
        if k == ord('q'):break




# video = video[3:]
    
# FPS = cap.get(5) #Frames

# Width = int(cap.get(3)) #Width
# Height = int(cap.get(4)) #Height

# fourcc = cv2.VideoWriter_fourcc(*'avc1')
# out = cv2.VideoWriter(r"output_assets\hands.mp4",fourcc, FPS, (Width,Height)) 

# for img in video:
#     out.write(img)
# out.release()
# cap.release()
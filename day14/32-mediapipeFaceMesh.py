import cv2
import mediapipe as mp
import mediapipe.python.solutions.face_mesh as mpmesh
import mediapipe.python.solutions.drawing_utils as mpdrawing

cap = cv2.VideoCapture(0)
video = []

with mpmesh.FaceMesh(max_num_faces=2) as facemesh:
    while True:
        ret, frame = cap.read()
        rgbframe = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        if not ret:break



        height, width,_ = frame.shape

        results = facemesh.process(rgbframe)

        if results.multi_face_landmarks is not None:
            for landmark in results.multi_face_landmarks:
                mpdrawing.draw_landmarks(frame,landmark,mpmesh.FACEMESH_CONTOURS,
                landmark_drawing_spec=mpdrawing.DrawingSpec(color=(0,255,255),thickness=1,circle_radius=1),
                connection_drawing_spec=mpdrawing.DrawingSpec(color = (255,255,0),thickness=2))

        
        video.append(frame)
        cv2.imshow('video', frame)

        k = cv2.waitKey(1)
        if k == ord('q'):break

cv2.destroyAllWindows()

# video = video[3:]
    
# FPS = cap.get(5) #Frames

# Width = int(cap.get(3)) #Width
# Height = int(cap.get(4)) #Height

# fourcc = cv2.VideoWriter_fourcc(*'avc1')
# out = cv2.VideoWriter(r"output_assets\mpFaceMesh.mp4",fourcc, FPS, (Width,Height)) 

# for img in video:
#     out.write(img)
# out.release()
# cap.release()
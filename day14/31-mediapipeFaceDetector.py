import cv2
import mediapipe as mp
import mediapipe.python.solutions.face_detection as mpface
import mediapipe.python.solutions.drawing_utils as mpdrawing

cap = cv2.VideoCapture(0)
video = []
with mpface.FaceDetection(min_detection_confidence=0.5) as faceDet:
    while True:
        ret, frame = cap.read()
        rgbframe = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        if not ret: break
        height, width, _ = frame.shape
        results = faceDet.process(rgbframe)

        #Drawing results

        if results.detections is not None:
            for det in results.detections:
                mpdrawing.draw_detection(frame,det, bbox_drawing_spec=mpdrawing.DrawingSpec(color=(0,255,0)))



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
# out = cv2.VideoWriter(r"output_assets\mpfaceDetector.mp4",fourcc, FPS, (Width,Height)) 

# for img in video:
#     out.write(img)
# out.release()
# cap.release()
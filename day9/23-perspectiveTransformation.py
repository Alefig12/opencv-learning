from email.mime import image
import cv2
import numpy as np



def click(event, x, y, flags, param):
    global pts
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),5,(0,255,0),2)
        pts.append([x,y])


def linkPts(pts):
    cv2.line(img,pts[0],pts[1],(0,0,255),1)
    cv2.line(img,pts[0],pts[2],(0,0,255),1)
    cv2.line(img,pts[2],pts[3],(0,0,255),1)
    cv2.line(img,pts[1],pts[3],(0,0,255),1)



img = cv2.imread('input_assets\perspective.png')

pts = []

aux = img.copy()

cv2.namedWindow("imagen")

cv2.setMouseCallback("imagen",click)
video = []
while True:
    if len(pts) == 4:
        linkPts(pts)
        pos1 = np.float32([pts])
        pos2 = np.float32([[0,0],[320,0],[0,320],[320,320]])

        M = cv2.getPerspectiveTransform(pos1,pos2)

        dts = cv2.warpPerspective(aux.copy(),M,(320,320))

        
        cv2.imshow('salida',dts)
        video.append(dts.copy())
    else:
        video.append(img.copy())
        cv2.imshow('salida',np.zeros([320,320]))
    cv2.imshow('imagen', img)  
    k = cv2.waitKey(30)

    if k == ord('q'):
        break
    if k == ord('n'):
        img = aux.copy()
        pts = []

cv2.destroyAllWindows()


FPS = 30 #Frames

Width = 320 #Width
Height = 320 #Height

fourcc = cv2.VideoWriter_fourcc(*'avc1')
out = cv2.VideoWriter(r"output_assets\perspective.mp4",fourcc, FPS, (Width,Height)) 

for img in video:
    out.write(img)
out.release()






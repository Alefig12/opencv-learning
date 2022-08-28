import cv2
import numpy as np
def showimg(img):
    cv2.imshow('Image', img)
    cv2.waitKey(0)


# FONT_HERSHEY_SIMPLEX=0
# FONT_HERSHEY_PLAIN=1
# FONT_HERSHEY_DUPLEX =2
# FONT_HERSHEY_COMPLEX=3
# FONT_HERSHEY_TRIPLEX=4
# FONT_HERSHEY_COMPLEX SMALL=5
# FONT_HERSHEY_SCRIPT_SIMPLEX=6
# FONT_HERSHEY_SCRIPT_COMPLEX=7

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output_assets/outputDrawing.mp4',fourcc, 3.33, (600,600))

waitTime= 300
f = 0
while True:

    if (cv2.waitKey(waitTime) & 0xFF == ord('q')):
        break
    

    img = 255*np.ones((600,600,3),dtype=np.uint8) #Creating a plain white 600x600 image 

    #Drawing a line dividing the image diagonally
    cv2.line(img, (0,0), (600,600), (0,0,255), 3)

    #Drawing a circle above the line
    cv2.circle(img, (450+f*10,150), 50, (0,255,0), -1)


    #Drawing a square below the line
    cv2.rectangle(img,(100+f*10,400),(200,500),(255,0,0),2)

    cv2.putText(img,"OpenCV Test",(60+f*10,390),f,1,(0,0,0), 1,cv2.LINE_AA)


    cv2.putText(img,"OpenCV Test",(340+f*10,90),f,1,(0,0,0),2,cv2.LINE_AA)
    cv2.putText(img,"OpenCV Test",(340+f*10,90),f,1,(255,255,255),1,cv2.LINE_AA)
    cv2.imshow('Image', img)
    out.write(img)
    f+=1
    if f == 8:
        f = 0
    
out.release()

    


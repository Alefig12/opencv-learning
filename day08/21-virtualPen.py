import cv2
import numpy as np

lowerYellow = np.array([20,70,60])
upperYellow= np.array([50,255,255])



# Available Colors
purple = (189,71,124)
aqua = (255,255,0)
green = (51,204,51)
light_red = (102,102,255)
clean = (51,153,255)

# Color selector rectangles thickness
colors = {
    'purple': {
        'color': purple,
        'thickness':6
    },
    'aqua':{
        'color': aqua,
        'thickness':2
    },
    'green':{
        'color': green,
        'thickness':2
    },
    'light_red':{
        'color': light_red,
        'thickness':2
    },

}



#thickness selector rectangles thickness

thick_select = {
    'thin':6,
    'medium':2,
    'thick':2,
}



#Initial state
selected_color = colors['purple']['color']
selected_thickness = 3


cap = cv2.VideoCapture(0)

x1 = None
y1 = None
aux = None

def setSelectedColor(selected):
    for c in colors:
        colors[c]['thickness'] = 2
        if colors[c]['color'] == selected:
            colors[c]['thickness'] = 6


def setSelectedThickness(selected):
    for t in thick_select:
        thick_select[t] = 2
        if t == selected:
            thick_select[t] = 6


video = []
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    if not ret: break


    if aux is None:
        aux = np.zeros(frame.shape, dtype=np.uint8)

    #Obtaining and cleaning red pen mask
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    maskYellow = cv2.inRange(hsv,lowerYellow,upperYellow)


    maskYellow = cv2.erode(maskYellow,None,iterations=3)
    maskYellow = cv2.dilate(maskYellow,None,iterations=3)
    maskYellow = cv2.medianBlur(maskYellow,13)


    cnts = cv2.findContours(maskYellow,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]

    #Select biggest contour
    cnts = sorted(cnts,key = cv2.contourArea, reverse=True)[:1]

    for c in cnts:
        if cv2.contourArea(c) > 500:
            x,y2,w,h = cv2.boundingRect(c)

           

            x2 = x+w//2

            if x1 is not None:
                if 0 < x2 < 50 and 0 < y2 < 50:
                    selected_color = purple
                    setSelectedColor(purple)
                if 50 < x2 < 100 and 0 < y2 < 50:
                    selected_color = aqua
                    setSelectedColor(aqua)
                if 100 < x2 < 150 and 0 < y2 < 50:
                    selected_color = green
                    setSelectedColor(green)
                if 150 < x2 < 200 and 0 < y2 < 50:
                    selected_color = light_red
                    setSelectedColor(light_red)
                if 490 < x2 < 540 and 0 < y2 < 50:
                    selected_thickness = 3
                    
                    setSelectedThickness('thin')
                if 540 < x2 < 590 and 0 < y2 < 50:
                    selected_thickness = 7
                    
                    setSelectedThickness('medium')
                if 590 < x2 < 640 and 0 < y2 < 50:
                    selected_thickness = 11
                 
                    setSelectedThickness('thick')
                if 300 < x2 < 400 and 0 < y2 < 50:
                    aux = np.zeros(frame.shape, dtype=np.uint8) 
                    
                if 0 < x2 < 60 or 0 < y1 < 60:
                    aux = aux.copy()
                else:
                    aux = cv2.line(aux,(x1,y1),(x2,y2), selected_color, selected_thickness)
            cv2.circle(frame,(x2,y2),selected_thickness,selected_color,3)
            x1 = x2
            y1 = y2  
        else:
            x1 = None
            y1 = None
    

    gray_aux = cv2.cvtColor(aux,cv2.COLOR_BGR2GRAY)

    thresh = cv2.threshold(gray_aux,10,255,cv2.THRESH_BINARY_INV)[1]

    frame = cv2.bitwise_and(frame,frame, mask=thresh)
    frame = cv2.add(frame,aux)

    # SCREEN GUI

    #Color selectors
    cv2.rectangle(frame,(0,0),(50,50), purple,colors['purple']['thickness'])
    cv2.rectangle(frame,(50,0),(100,50), aqua,colors['aqua']['thickness'])
    cv2.rectangle(frame,(100,0),(150,50), green,colors['green']['thickness'])
    cv2.rectangle(frame,(150,0),(200,50), light_red,colors['light_red']['thickness'])

    #Erase drawings
    cv2.rectangle(frame,(300,0),(400,50),clean,2)
    cv2.putText(frame,'Erase',(310,20),1,1.2,clean,2,cv2.LINE_AA)
    cv2.putText(frame,'drawings',(310,40),1,1.2,clean,2,cv2.LINE_AA)


    #Thickness selector
    cv2.rectangle(frame,(490,0),(540,50),0,thick_select['thin'])
    cv2.circle(frame,(515,25),3,0,-1)

    cv2.rectangle(frame,(540,0),(590,50),0,thick_select['medium'])
    cv2.circle(frame,(565,25),7,0,-1)


    cv2.rectangle(frame,(590,0),(640,50),0,thick_select['thick'])
    cv2.circle(frame,(615,25),11,0,-1)

    cv2.imshow('frame',frame)
    cv2.imshow('aux',aux)

    video.append(frame)

    k = cv2.waitKey(1)

    if k == ord('q'):
        break

# FPS = cap.get(5) #Frames

# Width = int(cap.get(3)) #Width
# Height = int(cap.get(4)) #Height

# fourcc = cv2.VideoWriter_fourcc(*'avc1')
# out = cv2.VideoWriter(r"output_assets\drawinn.mp4",fourcc, FPS, (Width,Height)) 

# for img in video:
#     out.write(img)
# out.release()
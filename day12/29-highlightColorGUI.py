from select import select
from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import cv2
import numpy as np
import imutils

def highlight():
    global image
    if selected.get() == 1:  # Red
        lower = np.array([1, 20, 50], dtype=np.uint8)
        upper = np.array([10, 255, 255], dtype=np.uint8)
        lower2 = np.array([170, 20, 50], dtype=np.uint8)
        upper2 = np.array([179, 255, 255], dtype=np.uint8)

    if selected.get() == 2:  # Green
        lower = np.array([45, 85, 20], dtype=np.uint8)
        upper = np.array([77, 255, 255], dtype=np.uint8)

    if selected.get() == 3: #Blue
        lower = np.array([90,50, 20], dtype=np.uint8)
        upper = np.array([140,255, 255], dtype=np.uint8)

    if selected.get() == 4: #Yellow
        lower = np.array([20, 50, 20], dtype=np.uint8)
        upper =np.array([40, 255, 255], dtype=np.uint8)

    imgGray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    imgGray = cv2.cvtColor(imgGray,cv2.COLOR_GRAY2BGR)
    imgHSV = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

    if selected.get() == 1:
        mask1 = cv2.inRange(imgHSV,lower,upper)
        mask2 = cv2.inRange(imgHSV,lower2,upper2)
        mask = cv2.add(mask1,mask2)
    else:
        mask = cv2.inRange(imgHSV,lower,upper)
    
    mask = cv2.medianBlur(mask,7)

    colorOnly = cv2.bitwise_and(image,image, mask=mask)

    invMask = cv2.bitwise_not(mask)
    bgGray = cv2.bitwise_and(imgGray,imgGray,mask=invMask)

    outputImg= cv2.add(bgGray,colorOnly)
    
    imToShow = cv2.cvtColor(outputImg,cv2.COLOR_BGR2RGB)

    im = Image.fromarray(imToShow)
    img = ImageTk.PhotoImage(im)

    lblOutputImage.config(image=img)
    lblOutputImage.image = img

    lblInfo2 = Label(root,text="OUTPUT IMAGE",font="bold")
    lblInfo2.grid(column=1,row=0)


    return


def choosePic():
    imgPath = filedialog.askopenfilename(
        filetypes=[("image", ".jpg"), ("image", ".png"), ("image", ".jpeg"), ])

    if len(imgPath) > 0:
        global image

        image = cv2.imread(imgPath)

        image = imutils.resize(image, height=380)

        imgGUI = imutils.resize(image, width=180)
        imgGUI = cv2.cvtColor(imgGUI, cv2.COLOR_BGR2RGB)

        im = Image.fromarray(imgGUI)
        img = ImageTk.PhotoImage(im)

        lblInputImage.config(image=img)
        lblInputImage.image = img
    
        labelInputImg = Label(root, text="Input Image")
        labelInputImg.grid(column=0, row=1, padx=5, pady=5)

        lblOutputImage.image = ''
        selected.set(0)


image = None

root = Tk()

lblInputImage = Label(root)
lblInputImage.grid(column=0, row=2, padx=5, pady=5)


lblOutputImage = Label(root)
lblOutputImage.grid(column=1, row=1,rowspan=6)

lblInfo1 = Label(root, text="Choose color to highlight", width=25)
lblInfo1.grid(column=0, row=3, padx=5, pady=5)


selected = IntVar()
rbtn1 = Radiobutton(root, text="Red", width=25, value=1,
                    variable=selected, command=highlight)
rbtn2 = Radiobutton(root, text="Green", width=25, value=2,
                    variable=selected, command=highlight)
rbtn3 = Radiobutton(root, text="Blue", width=25, value=3,
                    variable=selected, command=highlight)
rbtn4 = Radiobutton(root, text="Yellow", width=25, value=4,
                    variable=selected, command=highlight)

rbtn1.grid(column=0, row=4)
rbtn2.grid(column=0, row=5)
rbtn3.grid(column=0, row=6)
rbtn4.grid(column=0, row=7)


btn = Button(root, text="Choose input image", width=25, command=choosePic)
btn.grid(column=0, row=0, padx=5, pady=5)

root.mainloop()

import cv2


def showimg(img):
    cv2.imshow('Image', img)
    cv2.waitKey(0)


img = cv2.imread('day1\input_assets\img.jpg', 0) # Reading as grayscale, could read normally and convert form BGR to grayscale too.


# Scans image for pixels with a value greater than 160 and changes them to 255, pixels with a value below 160 are changed to 0

thresh = cv2.threshold(img,160,255, cv2.THRESH_BINARY)[1] # Returns tuple, img in pos 1
showimg(img)
showimg(thresh)


# Scans image for pixels with a value greater than 160 and changes them to 160.
thresh = cv2.threshold(img,160,255, cv2.THRESH_TRUNC)[1] 

showimg(img)
showimg(thresh)



cv2.destroyAllWindows()



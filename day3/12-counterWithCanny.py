import cv2

img = cv2.imread('input_assets\dominos.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(gray,150,200) # Using canny to detect edges based on a range


cnts, _ = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) # With the edges found, now find contours


#Using same process as before to draw and count objects found
cv2.drawContours(img, cnts, -1, (0,0,255), 2, cv2.LINE_AA)
text = 'Found: {} objects'.format(len(cnts))
cv2.putText(img, text, (0,25), 0, 1, (0,0,0), 2,cv2.LINE_AA)





cv2.imshow('img', img)
cv2.imshow('canny', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
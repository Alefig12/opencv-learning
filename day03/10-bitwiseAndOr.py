import cv2
import numpy as np

img1 = np.zeros((400,600),dtype=np.uint8)
img1[100:300,200:400] = 255


img2 = np.zeros((400,600),dtype=np.uint8)

cv2.circle(img2, (300,200), 125, (255), -1)
cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

And = cv2.bitwise_and(img1, img2)
Or = cv2.bitwise_or(img1, img2)
Xor = cv2.bitwise_xor(img1, img2)
Not = cv2.bitwise_not(img1)


cv2.imshow("and",And)
cv2.imshow("Or",Or)
cv2.imshow("Xor",Xor)
cv2.imshow("Not",Not)

cv2.waitKey(0)
cv2.destroyAllWindows()
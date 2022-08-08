import cv2
import numpy as np


# OpenCV Handles images not as RGB but as BGR (blue, green, red)

bgr = np.zeros((300,300,3),dtype=np.uint8) #Creating a 300x300 black image.

cv2.imshow("Image", bgr)
cv2.waitKey(0)

bgr[:,:,:] = (0,0,255) # Modifying to red image



cv2.imshow("Image", bgr)
cv2.waitKey(0)

#We can transform to RGB too.

rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)

#Now image will show as blue because blue and red will be inverted.
cv2.imshow("Image", rgb)
cv2.waitKey(0)


#Finally we can convert to grayscale too, as well as many other color spaces.

gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)

cv2.imshow("Image", gray)
cv2.waitKey(0)

cv2.destroyAllWindows()
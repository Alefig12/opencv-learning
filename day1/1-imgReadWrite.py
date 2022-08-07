import cv2

img = cv2.imread('day1\input_assets\img.jpg', 0) # 0 if grayscale, 1 default

cv2.imshow("Image", img)

cv2.imwrite('day1\output_assets\grayscale.jpg',img )

cv2.waitKey(0)

cv2.destroyAllWindows()
import cv2

img = cv2.imread('input_assets\img.jpg', 0) # 0 if grayscale, 1 default

cv2.imshow("Image", img)

cv2.imwrite('output_assets\grayscale.jpg',img )

cv2.waitKey(0)

cv2.destroyAllWindows()
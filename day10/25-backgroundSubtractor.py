import cv2

cap = cv2.VideoCapture('input_assets\CCTV Motion.mp4')

#fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
#fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()
fgbg = cv2.createBackgroundSubtractorMOG2()



while True:

    ret, frame = cap.read()

    if not ret: break

    fgmask = fgbg.apply(frame)

 

    cv2.imshow('mask', fgmask)
    cv2.imshow('video', frame)
    k = cv2.waitKey(20)

    if k == ord('q'):
        break

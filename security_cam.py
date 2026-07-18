import cv2
import os

webcam = cv2.VideoCapture(0)
while True:
    _,im1 = webcam.read()
    _,im2 = webcam.read()

    diff = cv2.absdiff(im1,im2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    # Ignore tiny changes. Keep only large changes.
    _,threshold = cv2.threshold(gray,20,255 , cv2.THRESH_BINARY)
    #contouring - to find the moving or any new object detected by basically detecting the difference between two frames
    contours, _= cv2.findContours(threshold , cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        os.system("afplay /System/Library/Sounds/Glass.aiff")

    cv2.imshow('Security Cam', threshold)
    if cv2.waitKey(10) ==27:
        break

webcam.release()
cv2.destroyAllWindows()

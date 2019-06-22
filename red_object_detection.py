import cv2
import numpy as np
def nothing(x):
    pass
# creating object
cap = cv2.VideoCapture(0)   #0: for webcam, 1: for external camera

#reading from file
#cap = cv2.VideoCapture("video1.mp4")   #0: for webcam, 1: for external camera
cv2.namedWindow("thresholding",cv2.WINDOW_NORMAL)
while cap.isOpened():
    _, img = cap.read()
   # cv2.imshow("VIDEO FEED",img)
    frame= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower = (100,100,20)
    higher = (255,255,179)
    gaussian = cv2.GaussianBlur(frame,(5,5),0)
    imgThresh = cv2.inRange(gaussian,lower,higher)
    edges = cv2.Canny(imgThresh,100,200)

    cv2.imshow('edges',edges)
    cv2.imshow("thresholding",imgThresh)
    

    k = cv2.waitKey(10) & 0xFF          #waiting for user input
    if frame is None or k == ord('q'):  #if user quits
        cv2.destroyAllWindows()    
        cap.release()
        #destroy all windows
        break

        #output the image

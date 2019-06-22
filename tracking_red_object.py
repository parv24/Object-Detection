import cv2
import numpy as np
def nothing(x):
    pass
cap = cv2.VideoCapture(0)   #0: for webcam, 1: for external camera
while cap.isOpened():
    _, img = cap.read()
    blur = cv2.GaussianBlur(img,(5,5),0)
    frame= cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
    lower = (100,100,20)
    higher = (255,255,179)
    #gaussian = cv2.GaussianBlur(frame,(5,5),0)
    thresh = cv2.inRange(frame,lower,higher)
    # find contours in the thresholded image
    _, cnts, _= cv2.findContours(thresh.copy(), cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
    type(cnts)
    max_area = 20
    best_cnt = 1
    for cnt in cnts:
        area = cv2.contourArea(cnt)
        if area > max_area:
             max_area = area
             best_cnt = cnt

            # finding centroids of best_cnt and draw a circle there
    M = cv2.moments(best_cnt)
    cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
    print("cx: " + str(cx) + " cy: " + str(cy))
            #if best_cnt>1:
    cv2.circle(img,(cx,cy),40,(0,255,0),4)
    
   
    cv2.imshow("coordinates", img)
    #cv2.imshow("thresholding",imgThresh)
    

    k = cv2.waitKey(10) & 0xFF          #waiting for user input
    if frame is None or k == ord('q'):  #if user quits
        cv2.destroyAllWindows()         #destroy all windows
        cap.release()
        break

        #output the image

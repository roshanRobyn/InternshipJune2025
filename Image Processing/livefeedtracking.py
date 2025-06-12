import os
import sys
import cv2
import numpy as n

def analyzeColor(frame_r):
    lower=n.array([90,0,0])
    upper=n.array([250,170,70])
    mask=cv2.inRange(frame_r,lower,upper)
    contours,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area=cv2.contourArea(contour)
        if area>500:
            M=cv2.moments(contour)
            if M["m00"]!=0:
                cx=int(M["m10"]/M["m00"])
                cy=int(M["m01"]/M["m00"])
            else:
                continue
                
            x,y,w,h =cv2.boundingRect(contour)
            cv2.rectangle(frame_r,(x,y),(x+w,y+h),(0,0,255),2)

    return frame_r

def videoCap():
    cap=cv2.VideoCapture(0)
    while True:
        ret,frame=cap.read()
        tracked=analyzeColor(frame)
        cv2.imshow("Live Color Tracker",tracked)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("quitting")
            break
    cap.release()
    cv2.destroyAllWindows()

videoCap()
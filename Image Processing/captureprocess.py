import os
import sys
import cv2
import imageio as io 
import numpy as n 

def increaseB(d):
    imageArray=io.imread(d)
    imageflt=imageArray.astype(n.float32)
    imageBri=imageflt*1.5
    imageClip=n.clip(imageBri,0,255)
    imageuint=imageClip.astype(n.uint8)
    io.imwrite('outputProcessed.png',imageuint)

def captureImg():
    cap=cv2.VideoCapture(0)
    while True:
        ret,frame=cap.read()
        cv2.imshow("webcam",frame)
        if cv2.waitKey(1) & 0xFF == ord('t'):
            print("capturing")
            captured=frame.copy()
            break
    cap.release
    cv2.destroyAllWindows()
    d=input("enter a name for the image: ")
    d=d+".png"
    cv2.imwrite(d,captured)
    return d

d=captureImg()
increaseB(d)




import sys
import numpy as n
import cv2

def liveEdge():
    cap=cv2.VideoCapture(0)
    while True:
        ret,frame=cap.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        blur=cv2.GaussianBlur(gray,(5,5),0)
        edges=cv2.Canny(blur,50,150)
        cv2.imshow("OG video",frame)
        cv2.imshow("Canny Edges",edges)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Quitting live edge detection.")
            break

    cap.release()
    cv2.destroyAllWindows()

liveEdge()

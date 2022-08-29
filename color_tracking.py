import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#redBajo1 = np.array([0, 100, 20], np.uint8)
#redAlto1 = np.array([8, 255, 255], np.uint8)
#redBajo2 = np.array([175, 100, 20], np.uint8)
#redAlto2 = np.array([179, 255, 255], np.uint8)

azulBajo = np.array([100,100,20], np.uint8)
azulAlto = np.array([125,255,255], np.uint8)

while True:

    net,frame = cap.read()

    if net==True:
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #mask = cv2.inRange(frameHSV,redBajo1,redBajo2,redAlto1,redAlto2)
        mask = cv2.inRange(frameHSV, azulBajo,azulAlto)
        CONTORNOS = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame, CONTORNOS, -1, (255,0,0), 3)
        #cv2.imshow('Rojo', mask)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF ==ord('s'):
            break


cap.release()
cv2.destroyAllWindows()
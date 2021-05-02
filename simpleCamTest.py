'''
기능
    실시간 캠영상
    일반화면 + 흑백화면 출력
'''

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640) 
cap.set(4,480) 

while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1) # -1 or 1로 위,아래 대칭 가능
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break

cap.release()
cv2.destroyAllWIndows()


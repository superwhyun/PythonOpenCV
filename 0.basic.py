
# $ brew install opencv3

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)                       # 0: 상하반전, 1: 좌우반전
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 흑백으로 바꽈보자
    cv2.imshow('frame', gray)   
    if cv2.waitKey(1) & 0xFF == ord('q'):           # 터미널이 아닌 Player에서의 Key in을 받아들임.
        break
        

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
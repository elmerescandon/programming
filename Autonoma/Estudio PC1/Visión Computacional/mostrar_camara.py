import numpy as np
import cv2
cam = cv2.VideoCapture(0)
while (cam.isOpened()):
    retval, frame = cam.read()
    frame = cv2.flip(frame, 1)
    if retval == True:
        cv2.imshow("My camera", frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    else:
        break
cam.release()
cv2.destroyAllWindows()

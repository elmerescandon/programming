import cv2
import numpy as np
cam = cv2.VideoCapture(0)
while(cam.isOpened()):
    retval, frame = cam.read()
    # Nos da una imagen de forma espejo y perspectiva individual
    frame = cv2.flip(frame, 1)

    if (retval == True):  # Cuando realmente se tenga la imagen
        cv2.imshow("My Camera", frame)
        # Si se presiona q se cierra la ventana
        # 0xFF ayudar a tener otros valores
        if (cv2.waitKey(30) & 0xFF == ord('q')):
            break
    else:
        break
cam.release()

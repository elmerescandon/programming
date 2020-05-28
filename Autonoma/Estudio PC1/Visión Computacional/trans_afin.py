import cv2
import numpy as np
I = cv2.imread('cat.png')
Nrows, Ncols, Nchannels = I.shape
# Escalamiento
Isc = cv2.resize(I, None, fx=0.5, fy=0.5)
cv2.imshow('image', Isc)
cv2.waitKey(0)
# Traslación
tx = 100
ty = 50
T = np.float32([[1, 0, tx], [0, 1, ty]])
Itransl = cv2.warpAffine(I, T, (Ncols, Nrows))
cv2.imshow('translation', Itransl)
cv2.waitKey(0)
# Rotación
center_rot = (Ncols/2, Nrows/2)
angle = 45
T = cv2.getRotationMatrix2D(center_rot, angle, 1)
Irot = cv2.warpAffine(I, T, (Ncols, Nrows))
cv2.imshow('rotation', Irot)
cv2.waitKey(0)
